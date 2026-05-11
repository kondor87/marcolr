#!/usr/bin/env python3
"""
Google Search Console Checker — versione OAuth2 (account personale Google)
Usa il token generato da gsc_auth.py

Usage:
    python gsc_checker_oauth.py https://laroccadigitale.it/ --days 28 --json
    python gsc_checker_oauth.py https://laroccadigitale.it/ --inspect https://laroccadigitale.it/blog/ai-automazione-ristorante/
"""

import argparse
import json
import sys
import os
from datetime import datetime, timedelta

TOKEN_PATH = os.path.join(os.path.dirname(__file__), "gsc-token.json")

try:
    from google.oauth2.credentials import Credentials
    from google.auth.transport.requests import Request
    from googleapiclient.discovery import build
    HAS_DEPS = True
except ImportError:
    HAS_DEPS = False


SCOPES = ["https://www.googleapis.com/auth/webmasters.readonly"]


def build_service():
    if not HAS_DEPS:
        print("Errore: installa le dipendenze con:")
        print("  pip install google-api-python-client google-auth-oauthlib google-auth-httplib2")
        sys.exit(1)

    if not os.path.exists(TOKEN_PATH):
        print(f"Errore: token non trovato in {TOKEN_PATH}")
        print("Esegui prima: python gsc_auth.py --client-secret <client_secret.json>")
        sys.exit(1)

    creds = Credentials.from_authorized_user_file(TOKEN_PATH, SCOPES)
    if creds.expired and creds.refresh_token:
        creds.refresh(Request())
        with open(TOKEN_PATH, "w") as f:
            f.write(creds.to_json())

    return build("searchconsole", "v1", credentials=creds)


def get_performance_data(service, site_url, days=28, row_limit=25):
    end_date = datetime.now().strftime("%Y-%m-%d")
    start_date = (datetime.now() - timedelta(days=days)).strftime("%Y-%m-%d")
    body = {
        "startDate": start_date,
        "endDate": end_date,
        "dimensions": ["query", "page"],
        "rowLimit": row_limit,
    }
    try:
        resp = service.searchanalytics().query(siteUrl=site_url, body=body).execute()
        rows = resp.get("rows", [])
        return {
            "period": f"{start_date} to {end_date}",
            "total_rows": len(rows),
            "data": [
                {
                    "query": r["keys"][0],
                    "page": r["keys"][1],
                    "clicks": r.get("clicks", 0),
                    "impressions": r.get("impressions", 0),
                    "ctr": round(r.get("ctr", 0) * 100, 2),
                    "position": round(r.get("position", 0), 1),
                }
                for r in rows
            ],
        }
    except Exception as exc:
        return {"error": str(exc), "period": f"{start_date} to {end_date}"}


def get_top_pages(service, site_url, days=28, limit=20):
    end_date = datetime.now().strftime("%Y-%m-%d")
    start_date = (datetime.now() - timedelta(days=days)).strftime("%Y-%m-%d")
    body = {"startDate": start_date, "endDate": end_date, "dimensions": ["page"], "rowLimit": limit}
    try:
        resp = service.searchanalytics().query(siteUrl=site_url, body=body).execute()
        return [
            {
                "page": r["keys"][0],
                "clicks": r.get("clicks", 0),
                "impressions": r.get("impressions", 0),
                "ctr": round(r.get("ctr", 0) * 100, 2),
                "position": round(r.get("position", 0), 1),
            }
            for r in resp.get("rows", [])
        ]
    except Exception as exc:
        return [{"error": str(exc)}]


def get_sitemaps(service, site_url):
    try:
        resp = service.sitemaps().list(siteUrl=site_url).execute()
        return [
            {
                "path": s.get("path"),
                "last_submitted": s.get("lastSubmitted"),
                "last_downloaded": s.get("lastDownloaded"),
                "errors": s.get("errors", 0),
                "warnings": s.get("warnings", 0),
            }
            for s in resp.get("sitemap", [])
        ]
    except Exception as exc:
        return [{"error": str(exc)}]


def get_url_inspection(service, site_url, inspect_url):
    try:
        resp = service.urlInspection().index().inspect(
            body={"inspectionUrl": inspect_url, "siteUrl": site_url}
        ).execute()
        result = resp.get("inspectionResult", {})
        index_status = result.get("indexStatusResult", {})
        mobile = result.get("mobileUsabilityResult", {})
        return {
            "url": inspect_url,
            "verdict": index_status.get("verdict"),
            "coverage_state": index_status.get("coverageState"),
            "last_crawl_time": index_status.get("lastCrawlTime"),
            "page_fetch_state": index_status.get("pageFetchState"),
            "robots_txt_state": index_status.get("robotsTxtState"),
            "indexing_state": index_status.get("indexingState"),
            "mobile_usability": mobile.get("verdict"),
        }
    except Exception as exc:
        return {"url": inspect_url, "error": str(exc)}


def detect_opportunities(data):
    opportunities = []
    for row in data:
        pos = row.get("position", 0)
        ctr = row.get("ctr", 0)
        imps = row.get("impressions", 0)
        if 4 <= pos <= 20 and imps >= 20:
            opportunities.append({
                "type": "striking_distance",
                "severity": "High",
                "query": row["query"],
                "page": row["page"],
                "position": pos,
                "impressions": imps,
                "finding": f"Posizione {pos} con {imps} impressioni — a tiro della Top 3.",
                "fix": "Ottimizza il contenuto per questa query: aggiungi la keyword in H1/H2, espandi la sezione correlata.",
            })
        elif pos <= 3 and ctr < 5 and imps >= 50:
            opportunities.append({
                "type": "low_ctr_top_position",
                "severity": "Medium",
                "query": row["query"],
                "page": row["page"],
                "position": pos,
                "ctr": ctr,
                "finding": f"Posizione {pos} ma solo {ctr}% CTR — il titolo non attira clic.",
                "fix": "Riscrivi il title tag: aggiungi un beneficio concreto o un numero (es. 'Risparmia 10 ore').",
            })
        elif imps >= 100 and ctr < 2:
            opportunities.append({
                "type": "high_impressions_low_ctr",
                "severity": "Medium",
                "query": row["query"],
                "page": row["page"],
                "ctr": ctr,
                "impressions": imps,
                "finding": f"{imps} impressioni ma {ctr}% CTR — meta description poco convincente.",
                "fix": "Riscrivi la meta description con una call to action chiara.",
            })
    return opportunities


def main():
    parser = argparse.ArgumentParser(description="GSC Checker via OAuth2")
    parser.add_argument("site_url", help="URL proprietà GSC (es. https://laroccadigitale.it/)")
    parser.add_argument("--days", type=int, default=28)
    parser.add_argument("--inspect", default="", help="URL da ispezionare")
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args()

    service = build_service()
    report = {"site_url": args.site_url, "days": args.days}

    perf = get_performance_data(service, args.site_url, days=args.days)
    report["performance"] = perf

    if "data" in perf:
        report["opportunities"] = detect_opportunities(perf["data"])

    report["top_pages"] = get_top_pages(service, args.site_url, days=args.days)
    report["sitemaps"] = get_sitemaps(service, args.site_url)

    if args.inspect:
        report["url_inspection"] = get_url_inspection(service, args.site_url, args.inspect)

    if args.json:
        print(json.dumps(report, indent=2, default=str))
    else:
        print(f"\nGSC Report — {args.site_url}")
        print("=" * 60)
        if "data" in perf:
            print(f"\nTop Query (ultimi {args.days} giorni):")
            for row in perf["data"][:15]:
                print(f"  [{row['position']:>5.1f}] {row['query'][:45]:<45} click={row['clicks']:<4} impr={row['impressions']:<6} CTR={row['ctr']}%")
        if report.get("opportunities"):
            print(f"\nOpportunita' ({len(report['opportunities'])}):")
            for opp in report["opportunities"]:
                print(f"  ⚡ {opp['query']} — {opp['finding']}")
        if report.get("top_pages"):
            print(f"\nTop Pagine:")
            for p in report["top_pages"][:10]:
                if "error" not in p:
                    print(f"  {p['page']}")
                    print(f"    click={p['clicks']} impr={p['impressions']} CTR={p['ctr']}% pos={p['position']}")


if __name__ == "__main__":
    main()
