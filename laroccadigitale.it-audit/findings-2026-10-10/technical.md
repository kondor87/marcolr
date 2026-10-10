# Audit tecnico (re-audit) – laroccadigitale.it – 2026-10-10

**Punteggio tecnico: 92/100** (7 ottobre: 68). Nessuna regressione. Verifica sul sito LIVE con curl su tutte le 26 URL della sitemap + /grazie/.

## Esito per categoria
| Categoria | Esito |
|---|---|
| Crawlability (robots.txt, sitemap) | Pass (1 nota) |
| Indexability (canonical, noindex) | Pass |
| Sicurezza (HTTPS, header, CSP) | Pass |
| URL e redirect | Pass |
| Mobile | Pass |
| Link interni | Pass: 41 URL interne uniche, tutte 200 |
| Rendering | Pass: HTML statico (Hugo), nessun JS necessario per i contenuti |

## Verificato, tutto OK
- robots.txt 200: `Allow: /`, `Disallow: /grazie/`, Bytespider bloccato, `Sitemap:` valido.
- sitemap.xml 200: 26 URL, tutte 200 e con canonical autoreferenziale, nessun redirect/noindex dentro.
- Redirect 301 corretti: `/blog/siti-web-castelli-romani/` -> `/siti-web-frascati-castelli-romani/`; `/categories/manutenzione/` -> `/categories/wordpress/`; `/tags/seo/` e `/tags/` -> `/blog/`.
- http -> https e www -> apex: 301 diretti (nessuna catena). `/blog` -> `/blog/` 301.
- 404 vero: `/pagina-inesistente/` risponde 404 con pagina dedicata.
- `/grazie/`: 200, `<meta name=robots content="noindex, follow">`, fuori dalla sitemap.
- Header presenti: HSTS (preload), X-Frame-Options DENY, nosniff, Referrer-Policy, Permissions-Policy, CSP con frame-ancestors 'none'. Corrispondono a netlify.toml.
- CSP: coerente con le risorse usate (iubenda, GTM, GA, Clarity, Google Fonts).
- Mobile: `viewport width=device-width,initial-scale=1` su tutte le pagine; `lang=it`; 1 solo H1, title e description presenti ovunque.
- Performance da sorgente: home 24 KB HTML, 0,29 s; CSS con hash e `immutable`; immagini WebP con width/height, srcset e lazy; favicon.png, og-default.png, llms.txt 200.
- Link esterni: tutti raggiungibili (eur-lex risponde 202, normale).

## Problemi

### Critico
Nessuno.

### Alto
Nessuno.

### Medio
1. **/grazie/: noindex non leggibile dai crawler.** `robots.txt` ha `Disallow: /grazie/`, quindi Google non scarica la pagina e non vede il `noindex`. Se qualcuno la linka, può comparire come URL senza snippet. Correzione: togliere `Disallow: /grazie/` da robots.txt e lasciare solo il noindex (già presente).
2. **`/index.html` risponde 200** (duplicato della home, con canonical corretto a `/`). Rischio basso grazie al canonical. Correzione opzionale: redirect `/index.html` -> `/` in netlify.toml (`status = 301`, `force = true`).

### Basso
3. **`/archivio/` nella sitemap senza `<lastmod>`** (tutte le altre ce l'hanno) e senza meta robots. Pagina di archivio a basso valore: valutare `noindex` e toglierla dalla sitemap, oppure aggiungere la data.
4. **HTML senza cache a lungo** (`max-age=0,must-revalidate`): normale per Netlify, nessuna azione.
5. **`/favicon.ico` 404**: il sito usa `/favicon.png` (200). Alcuni crawler richiedono ancora .ico. Aggiungere un favicon.ico in `static/`.
6. **Google Fonts ancora da CDN** (render-blocking + 2 connessioni extra, già in ACTION-PLAN). Servirli da `/fonts/` (le regole di cache esistono già in netlify.toml).
7. **CSP con `'unsafe-inline'` in script-src** e `connect-src https:` troppo largo: accettabile per GTM/iubenda inline, miglioramento solo se si passa a nonce/hash.
8. **sitemap `changefreq`/`lastmod` uniformi (2026-10-07)**: Google ignora changefreq; lastmod tutti uguali non è informativo. Nessuna azione urgente.

## Cambiato rispetto al 7 ottobre
- Risolti: redirect landing locale, categoria manutenzione, tag; landing in sitemap; /grazie/ noindex; header e CSP attivi.
- Nuovo: nessun problema introdotto. Nota 1 (Disallow + noindex) è un conflitto da sistemare.
- Non verificabile da qui: Core Web Vitals reali (PageSpeed/CrUX), Google Consent Mode in iubenda, errori CSP in console, stato indicizzazione in Search Console.
