"""Immagini per la condivisione (WhatsApp, Facebook, LinkedIn, Google Discover).

Per ogni articolo del blog e per la pagina servizio genera static/images/og/<slug>.png
(1200x630) con il titolo, la categoria e il nome del sito. Gli articoli non hanno
copertina nella pagina: questa immagine compare solo quando il link viene condiviso.

Uso:   python strumenti/immagini-social.py
Serve: pip install playwright && playwright install chromium
Nel front matter dell'articolo: ogImage: "/images/og/<slug>.png"
"""
import html, os, re, glob
from playwright.sync_api import sync_playwright

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
OUT = os.path.join(ROOT, "static", "images", "og")
os.makedirs(OUT, exist_ok=True)

STONE, BRASS, TEXT, MUTED = "#2c2e2a", "#c09a45", "#f1efe9", "#bdbbb2"


def front(path):
    s = open(path, encoding="utf-8").read()
    fm = s.split("---")[1]
    def get(k):
        m = re.search(rf'^{k}:\s*"?(.*?)"?\s*$', fm, re.M)
        return m.group(1) if m else ""
    cat = re.search(r'^categories:\s*\["([^"]+)"', fm, re.M)
    return get("title"), (cat.group(1) if cat else "Siti web")


PAGE = """<!doctype html><html><head><meta charset="utf-8">
<link href="https://fonts.googleapis.com/css2?family=Public+Sans:wght@500;700;800&display=swap" rel="stylesheet">
<style>
html,body{{margin:0}}
body{{width:1200px;height:630px;background:{stone};color:{text};font-family:'Public Sans',sans-serif;
display:flex;flex-direction:column;justify-content:space-between;padding:72px 84px;box-sizing:border-box}}
.cat{{font-weight:700;font-size:26px;color:{brass};letter-spacing:.01em}}
h1{{margin:0;text-wrap:balance;font-weight:800;font-size:{size}px;line-height:1.08;letter-spacing:-.03em;max-width:1000px}}
.foot{{display:flex;align-items:center;gap:22px;font-size:26px;font-weight:500;color:{muted}}}
.foot i{{width:56px;height:6px;background:{brass}}}
.foot b{{color:{text};font-weight:700}}
</style></head><body>
<div class="cat">{cat}</div>
<h1>{title}</h1>
<div class="foot"><i></i><span><b>Marco La Rocca</b> · laroccadigitale.it</span></div>
</body></html>"""


def pages():
    for p in sorted(glob.glob(os.path.join(ROOT, "content", "blog", "*.md"))):
        slug = os.path.basename(p)[:-3]
        if slug != "_index":
            yield slug, p
    yield "siti-web-frascati-castelli-romani", os.path.join(ROOT, "content", "siti-web-frascati-castelli-romani.md")


with sync_playwright() as pw:
    b = pw.chromium.launch()
    pg = b.new_page(viewport={"width": 1200, "height": 630})
    for slug, path in pages():
        title, cat = front(path)
        size = 76 if len(title) < 45 else 64 if len(title) < 70 else 54
        pg.set_content(PAGE.format(stone=STONE, text=TEXT, brass=BRASS, muted=MUTED, size=size,
                                   cat=html.escape(cat), title=html.escape(title)), wait_until="networkidle")
        pg.screenshot(path=os.path.join(OUT, f"{slug}.png"))
        print("ok", slug)
    b.close()
