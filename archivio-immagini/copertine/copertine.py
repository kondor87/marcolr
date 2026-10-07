"""Copertine del blog: un solo sistema, una sola mano.
Tavole al tratto (grafite) su intonaco con griglia leggera, un'unica campitura ottone,
cartiglio in basso a destra. Uscita: static/images/copertine/<slug>.png 1200x675.

Nuovo articolo: aggiungi una voce a COVERS con lo slug del file .md e il disegno
(usa gli aiuti browser/phone/bubble/pin/gear/lines), poi: python strumenti/copertine.py
Richiede: pip install playwright && playwright install chromium"""
import os
from playwright.sync_api import sync_playwright

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "static", "images", "copertine")
os.makedirs(OUT, exist_ok=True)

INK = "#24272b"
BRASS = "#b8913a"
WALL = "#e4e5e1"
PAPER = "#f4f4f1"

S = f'fill="none" stroke="{INK}" stroke-width="5" stroke-linecap="round" stroke-linejoin="round"'
B = f'fill="{BRASS}"'
P = f'fill="{PAPER}"'

def browser(x, y, w, h, extra=""):
    return (f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="14" {P} {S}/>'
            f'<line x1="{x}" y1="{y+38}" x2="{x+w}" y2="{y+38}" {S}/>'
            f'<circle cx="{x+22}" cy="{y+19}" r="5" fill="{INK}"/><circle cx="{x+40}" cy="{y+19}" r="5" fill="{INK}"/><circle cx="{x+58}" cy="{y+19}" r="5" fill="{INK}"/>' + extra)

def phone(x, y, w=150, h=280, extra=""):
    return (f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="24" {P} {S}/>'
            f'<line x1="{x+w/2-18}" y1="{y+18}" x2="{x+w/2+18}" y2="{y+18}" {S}/>' + extra)

def lines(x, y, n, w, gap=22, last=0.6):
    out = ""
    for i in range(n):
        ww = w * (last if i == n - 1 else 1)
        out += f'<line x1="{x}" y1="{y+i*gap}" x2="{x+ww}" y2="{y+i*gap}" {S} stroke-width="4"/>'
    return out

def bubble(x, y, w, h, tail="left", fill=P):
    t = (f'M{x+30},{y+h} l-10,26 l34,-26' if tail == "left" else f'M{x+w-30},{y+h} l10,26 l-34,-26')
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="18" {fill} {S}/><path d="{t}" {fill} {S}/>'

def pin(x, y, s=1.0, fill=B):
    return (f'<g transform="translate({x},{y}) scale({s})"><path d="M0,0 C-48,-60 -40,-118 0,-118 C40,-118 48,-60 0,0 Z" {fill} {S}/>'
            f'<circle cx="0" cy="-74" r="16" {P} {S}/></g>')

def gear(cx, cy, r, fill=P):
    teeth = "".join(f'<rect x="{cx-9}" y="{cy-r-16}" width="18" height="22" rx="3" {fill} {S} transform="rotate({a} {cx} {cy})"/>' for a in range(0, 360, 45))
    return teeth + f'<circle cx="{cx}" cy="{cy}" r="{r}" {fill} {S}/><circle cx="{cx}" cy="{cy}" r="{r*0.38}" {P} {S}/>'

COVERS = {
 "siti-web-frascati-castelli-romani": ("Siti web",
   f'<path d="M80,400 C200,260 300,240 420,300 C520,200 640,170 760,260 C860,210 960,240 1020,400 Z" {P} {S}/>'
   f'<path d="M520,330 a90,60 0 1 0 1,0" {B} {S} transform="translate(0,-10)"/>'
   + pin(300, 300, 0.8, P) + pin(560, 250, 1.1) + pin(820, 290, 0.8, P)),
 "ai-chatbot-dati-pazienti-gdpr": ("AI e automazione",
   bubble(170, 110, 300, 120) + lines(200, 150, 3, 230) +
   bubble(330, 270, 260, 100, "right") + lines(360, 305, 2, 190) +
   f'<path d="M700,120 L800,90 L900,120 L900,230 C900,300 840,345 800,360 C760,345 700,300 700,230 Z" {B} {S}/>'
   f'<rect x="760" y="210" width="80" height="62" rx="8" {P} {S}/><path d="M775,210 v-22 a25,25 0 0 1 50,0 v22" {S}/>'),
 "sito-web-ristorante-cosa-deve-avere": ("Business digitale",
   phone(240, 70, 170, 320, lines(270, 150, 6, 110, 26)) +
   f'<circle cx="720" cy="240" r="140" {P} {S}/><circle cx="720" cy="240" r="96" {B} {S}/>'
   f'<path d="M540,120 v80 M520,120 v55 a20,20 0 0 0 40,0 v-55 M540,200 v190" {S}/>'
   f'<path d="M900,120 c40,20 40,110 0,130 v140" {S}/>'),
 "chi-possiede-il-tuo-sito-dominio-hosting-accessi": ("Business digitale",
   browser(170, 90, 430, 300, lines(210, 180, 5, 300, 34)) +
   f'<circle cx="780" cy="200" r="70" {B} {S}/><circle cx="780" cy="200" r="24" {P} {S}/>'
   f'<path d="M830,250 L960,380 M915,335 l-26,26 M945,365 l-22,22" {S}/>'),
 "come-scegliere-parole-chiave-attivita-locale": ("SEO locale",
   f'<rect x="170" y="150" width="620" height="90" rx="45" {P} {S}/>' + lines(230, 195, 1, 360, last=1) +
   f'<circle cx="840" cy="250" r="78" {B} {S}/><circle cx="840" cy="250" r="44" {P} {S}/><line x1="895" y1="305" x2="960" y2="370" {S} stroke-width="12"/>'
   + lines(200, 300, 3, 300, 30)),
 "ai-automazione-guida-attivita-locali": ("AI e automazione",
   gear(330, 240, 92) + gear(500, 150, 56) +
   f'<path d="M620,250 h90" {S}/><path d="M690,225 l25,25 l-25,25" {S}/>' +
   bubble(760, 140, 250, 120, "left", B) + lines(790, 180, 2, 180)),
 "ai-automazione-nutrizionista": ("AI e automazione",
   f'<path d="M380,140 C300,110 230,170 250,260 C270,350 340,390 380,370 C420,390 490,350 510,260 C530,170 460,110 380,140 Z" {B} {S}/>'
   f'<path d="M380,140 C380,110 395,90 420,80" {S}/><path d="M392,110 C430,80 470,95 470,95 C450,125 410,125 392,110 Z" {P} {S}/>'
   f'<rect x="620" y="110" width="330" height="270" rx="14" {P} {S}/><line x1="620" y1="165" x2="950" y2="165" {S}/>'
   + "".join(f'<rect x="{650+c*72}" y="{190+r*58}" width="44" height="38" rx="6" {B if (r,c)==(1,2) else P} {S} stroke-width="4"/>' for r in range(3) for c in range(4))),
 "ai-automazione-osteopata": ("AI e automazione",
   f'<path d="M250,170 a110,110 0 0 1 220,0 v110 l30,40 h-280 l30,-40 Z" {B} {S}/><path d="M330,345 a30,30 0 0 0 60,0" {S}/>'
   f'<path d="M250,120 l-30,-30 M470,120 l30,-30" {S}/>' +
   phone(660, 70, 190, 320, bubble(690, 130, 130, 70) + bubble(690, 240, 130, 70, "right", B))),
 "ai-automazione-psicologo": ("AI e automazione",
   f'<path d="M230,330 v-140 a40,40 0 0 1 80,0 v60 h180 v-60 a40,40 0 0 1 80,0 v140 Z" {B} {S}/>'
   f'<rect x="310" y="120" width="180" height="130" rx="20" {P} {S}/><line x1="260" y1="330" x2="260" y2="380" {S}/><line x1="540" y1="330" x2="540" y2="380" {S}/>' +
   bubble(680, 100, 280, 110) + lines(710, 140, 2, 210) + bubble(720, 250, 240, 90, "right") + lines(750, 285, 1, 170, last=1)),
 "ai-automazione-ristorante": ("AI e automazione",
   phone(230, 70, 190, 320, bubble(260, 130, 130, 70, "left", B) + bubble(260, 240, 130, 70, "right")) +
   f'<path d="M640,110 h150 c0,110 -30,150 -75,150 c-45,0 -75,-40 -75,-150 Z" {P} {S}/><path d="M650,170 h130 c-5,60 -30,80 -65,80 c-35,0 -60,-20 -65,-80 Z" {B} {S}/>'
   f'<line x1="715" y1="260" x2="715" y2="360" {S}/><line x1="665" y1="365" x2="765" y2="365" {S}/>'),
 "errori-online-attivita-locali": ("Business digitale",
   browser(170, 90, 470, 300, lines(210, 170, 6, 330, 32)) +
   f'<path d="M820,110 L950,350 H690 Z" {B} {S}/><line x1="820" y1="190" x2="820" y2="280" {S} stroke-width="10"/><circle cx="820" cy="315" r="8" fill="{INK}"/>'),
 "quanto-costa-sito-web": ("Business digitale",
   f'<path d="M230,140 h260 l90,100 l-90,100 h-260 Z" {B} {S}/><circle cx="460" cy="240" r="18" {P} {S}/>'
   f'<text x="290" y="268" font-family="Geist, sans-serif" font-weight="700" font-size="84" fill="{INK}">€</text>'
   f'<rect x="680" y="90" width="260" height="310" rx="10" {P} {S}/>' + lines(715, 150, 6, 190, 36) +
   f'<line x1="715" y1="350" x2="905" y2="350" {S} stroke-width="8"/>'),
 "perche-professionista-locale-sito-web": ("Business digitale",
   browser(150, 100, 430, 290, f'<rect x="185" y="175" width="160" height="110" rx="8" {B} {S}/>' + lines(370, 190, 4, 170, 30)) +
   phone(690, 90, 170, 300, f'<rect x="715" y="140" width="120" height="150" rx="8" {P} {S}/>' + pin(775, 260, 0.75))),
 "blog-e-trucchi-seo-semplici": ("SEO locale",
   f'<rect x="230" y="70" width="330" height="340" rx="10" {P} {S}/>'
   f'<line x1="270" y1="120" x2="470" y2="120" {S} stroke-width="12"/>' + lines(270, 170, 3, 240, 26) +
   f'<line x1="270" y1="270" x2="420" y2="270" {S} stroke-width="9"/>' + lines(270, 310, 3, 240, 26) +
   f'<path d="M700,380 L740,260 L900,100 L940,140 L780,300 Z" {B} {S}/><path d="M740,260 l40,40" {S}/><path d="M700,380 l18,-52 l34,34 Z" fill="{INK}"/>'),
 "sito-monopagina-o-sito-completo": ("Business digitale",
   f'<rect x="230" y="60" width="200" height="360" rx="12" {B} {S}/>' + lines(260, 110, 8, 140, 36) +
   "".join(f'<rect x="{620+i*40}" y="{90+i*40}" width="220" height="250" rx="12" {P} {S}/>' for i in range(3)) + lines(720, 220, 4, 140, 30)),
 "google-business-sito-vetrina": ("SEO locale",
   f'<path d="M200,380 V200 L260,120 H560 L620,200 V380 Z" {P} {S}/><path d="M200,200 H620" {S}/>'
   + "".join(f'<path d="M{200+i*84},200 a42,42 0 0 0 84,0" {B if i%2==0 else P} {S}/>' for i in range(5)) +
   f'<rect x="270" y="270" width="110" height="110" {S}/><rect x="430" y="250" width="120" height="80" rx="6" {S}/>'
   + pin(820, 330, 1.6)),
 "perche-aggiornare-plugin-wordpress": ("Manutenzione",
   browser(170, 90, 450, 300, f'<path d="M360,250 a60,60 0 1 1 18,43" {S}/><path d="M352,300 l26,-8 l-6,-26" {S}/>') +
   f'<path d="M760,110 a70,70 0 0 0 -60,105 l-100,100 a28,28 0 0 0 40,40 l100,-100 a70,70 0 0 0 105,-60 l-45,25 l-35,-35 Z" {B} {S}/>'),
}

HTML = """<!doctype html><html><head><meta charset="utf-8">
<link href="https://fonts.googleapis.com/css2?family=Geist:wght@500;700&family=Geist+Mono:wght@500&display=swap" rel="stylesheet">
<style>
html,body{{margin:0}} body{{width:1200px;height:675px;background:{wall};
background-image:linear-gradient(rgba(36,39,43,.07) 1px,transparent 1px),linear-gradient(90deg,rgba(36,39,43,.07) 1px,transparent 1px);
background-size:40px 40px;background-position:-1px -1px;position:relative;overflow:hidden;font-family:Geist,sans-serif}}
svg{{position:absolute;left:60px;top:50px}}
.cart{{position:absolute;right:48px;bottom:40px;display:grid;grid-template-columns:auto auto;border:2px solid {ink};background:{paper};
font:500 15px/1 'Geist Mono',monospace;color:{ink};letter-spacing:.06em;text-transform:uppercase}}
.cart span{{padding:10px 14px}} .cart span+span{{border-left:2px solid {ink}}}
.frame{{position:absolute;inset:24px;border:2px solid {ink}}}
</style></head><body><div class="frame"></div>
<svg width="1080" height="500" viewBox="0 0 1080 500">{svg}</svg>
<div class="cart"><span>Tav. {n:02d}</span><span>{cat}</span></div></body></html>"""

with sync_playwright() as p:
    b = p.chromium.launch()
    pg = b.new_page(viewport={"width": 1200, "height": 675})
    for n, (slug, (cat, svg)) in enumerate(COVERS.items(), 1):
        pg.set_content(HTML.format(wall=WALL, ink=INK, paper=PAPER, svg=svg, n=n, cat=cat), wait_until="networkidle")
        pg.screenshot(path=f"{OUT}/{slug}.png")
        print("ok", slug)
    b.close()
