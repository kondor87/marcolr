# Performance / Core Web Vitals - laroccadigitale.it (2026-10-07)

## Metodo e limiti
- PSI API senza chiave: **HTTP 429** (quota giornaliera condivisa esaurita) su entrambe le URL. Nessun dato lab/CrUX ottenuto: i CWV sotto sono **stime** da misure reali di peso/TTFB e dal codice.
- Misure reali (curl, 2026-10-07): TTFB home 0,30 s; TTFB articolo 0,64 s (entrambi sotto 0,8 s); HTML ~8,7 KB / 7,9 KB (gzip).
- Riprovare con chiave API (PSI + CrUX) per i dati ufficiali.

## Stima CWV (mobile)
| Metrica | Stima | Esito probabile |
|---|---|---|
| LCP | 3,5-5 s su 4G lento (home: avatar 1,5 MB, hero; articolo: cover PNG 968 KB) | Needs improvement / Poor |
| INP | <200 ms (JS proprio minimo; rischio solo da GTM+GA4+Clarity+iubenda) | Good, a rischio |
| CLS | 0,1-0,25: img senza width/height, font swap, banner iubenda | Needs improvement |
Punteggio Lighthouse mobile stimato: **45-65**.

## Peso immagini (misurato)
| File | Byte | Uso reale |
|---|---|---|
| marco-avatar.png | 1.555.766 (1,48 MiB) | ~120 px home, 70 px articolo, og:image |
| blog_ai_guida.png | 991.108 | cover articolo (LCP) + card home |
| blog_ai_psicologo / nutrizionista / osteopata | 866.505 / 816.740 / 651.615 | card |
| blog_parole_chiave.png | 559.598 | card |
| ai-vs-automazione.png | 396.919 | corpo articolo |
| martina.jpeg | 180.709 | portfolio home |
- **Home: ~5,7 MB di immagini (5,4 MiB)**; **articolo: ~3,1 MB (2,9 MiB)**. Il solo avatar e' ~27% / ~51%.
- Nessun `width/height`, `loading=lazy`, `srcset`, `decoding=async`; nessuna immagine above-the-fold con `fetchpriority`.
- Netlify serve `Cache-Control: public,max-age=0,must-revalidate` su immagini e CSS (nessun header di cache in netlify.toml): ogni visita ripetuta rivalida.

## Altri colli di bottiglia
1. **Google Fonts render-blocking** (layouts/_default/baseof.html ~r.186-190): 2 famiglie (Space Mono 400/700, DM Sans variabile opsz+wght+italic) = CSS bloccante + 2 origini (DNS+TLS) + file woff2. Ritarda FCP/LCP di ~300-800 ms su mobile.
2. **CSS con `?v={{ now.Unix }}`**: cambia a ogni build (verificato: v=1785169996), quindi invalida cache a ogni deploy anche senza modifiche; combinato con max-age=0 non porta beneficio. CSS 31 KB non minificato, render-blocking.
3. **Script in `<head>`**: GTM (async, ok), gtag.js (async) **duplicato** con GTM (GA4 caricato due volte se GTM contiene gia' GA4: doppio conteggio pageview e ~2 download gtag/gtm), Clarity (async), iubenda `iubenda.js` su load + `embeds.iubenda.com/widgets/...js` caricato sincrono (script senza async/defer a fine body, blocca parsing). Costo: ~150-250 KB JS di terze parti, aumenta TBT/INP.
4. og:image di fallback = avatar da 1,5 MB (scaricato da crawler/social): usare immagine 1200x630.

## Fix Hugo concreti (non applicati)
### 1. Immagini con Hugo Pipes
Spostare `static/images/*` in `assets/images/` (o page bundle accanto al .md; oggi `image:` nel front matter e' un path stringa). Partial `layouts/partials/img.html`:
```go-html-template
{{- $src := .src -}}
{{- $res := resources.Get $src -}}
{{- if $res -}}
  {{- $w := .w | default 800 -}}
  {{- $sizes := slice 400 800 1200 -}}
  {{- $lazy := not .eager -}}
  {{- $def := $res.Resize (printf "%dx webp q80" $w) -}}
  <img src="{{ $def.RelPermalink }}"
       srcset="{{ range $sizes }}{{ ($res.Resize (printf "%dx webp q80" .)).RelPermalink }} {{ . }}w, {{ end }}"
       sizes="{{ .sizes | default "(max-width:700px) 100vw, 700px" }}"
       width="{{ $def.Width }}" height="{{ $def.Height }}"
       alt="{{ .alt }}"
       {{ if $lazy }}loading="lazy" decoding="async"{{ else }}fetchpriority="high" decoding="async"{{ end }}>
{{- end -}}
```
- Avatar: `{{ partial "img.html" (dict "src" "images/marco-avatar.png" "w" 240 "sizes" "120px" "alt" "Marco La Rocca" "eager" true) }}` -> 240x240 webp ~10-15 KB (da 1,5 MB, -99%). In single.html 140 px.
- Cover articolo (LCP): `eager` + `<link rel="preload" as="image" fetchpriority="high" imagesrcset=... imagesizes=...>` in `{{ block "head" }}`; w=1200 webp q75 ~60-90 KB (da 968 KB).
- Card (list/home): lazy, w=600 webp ~25-40 KB ciascuna. Immagini nel Markdown: render hook `layouts/_default/_markup/render-image.html` che chiama lo stesso partial (con `.Page.Resources` o `resources.Get`).
- Fallback og:image: generare `$res.Fill "1200x630 webp"` (nota: alcuni scraper preferiscono jpg: usare `jpg q85`).
- Stima risparmio: home 5,7 MB -> ~0,35 MB; articolo 3,1 MB -> ~0,25 MB.
- CSS: aggiungere `aspect-ratio` a `.blog-card-image`/`.blog-cover` per bloccare il CLS.

### 2. CSS fingerprint + minify
```go-html-template
{{ $css := resources.Get "css/style.css" | minify | fingerprint }}
<link rel="stylesheet" href="{{ $css.RelPermalink }}" integrity="{{ $css.Data.Integrity }}">
```
(spostare style.css in `assets/css/`). L'URL cambia solo se il contenuto cambia. Con il CSS inline possibile se <14 KB dopo minify+gzip (valutare critical CSS).

### 3. Caching Netlify (netlify.toml)
```toml
[[headers]]
  for = "/css/*"   # e /images/*, /fonts/*
  [headers.values]
    Cache-Control = "public, max-age=31536000, immutable"
[[headers]]
  for = "/images/*"
  [headers.values]
    Cache-Control = "public, max-age=31536000, immutable"
```
(Hugo Pipes genera in /css e /images con hash nel nome; per i resource generati usare `/images/*` o la dir di output.)

### 4. Font: self-hosting
- Scaricare woff2 latin (Space Mono 400/700; DM Sans variable) in `assets/fonts/` o `static/fonts/`, `@font-face` con `font-display: swap` e `unicode-range` latin; rimuovere preconnect+link Google. Ridurre pesi (valutare togliere italic 300 e opsz).
- Preload solo i 1-2 font above-the-fold: `<link rel="preload" href="/fonts/dm-sans-var.woff2" as="font" type="font/woff2" crossorigin>`.
- `size-adjust`/`ascent-override` sul fallback per ridurre CLS da swap.
- Alternativa rapida: mantenere Google Fonts ma con `media="print" onload="this.media='all'"` + `<noscript>` (meno consigliato: FOUT).

### 5. Script terze parti
- Eliminare il blocco gtag.js diretto e configurare GA4 **dentro GTM** (o viceversa): oggi duplicato.
- Clarity: caricarlo da GTM dopo consenso, non nell'head. Entrambi gia' async: spostarli in fondo al body o inizializzarli su `requestIdleCallback`/primo input.
- iubenda: aggiungere `async` (o `defer`) a `embeds.iubenda.com/widgets/...js`. Verificare che il banner cookie abbia spazio riservato (`position: fixed`) per non causare CLS.
- Aggiungere `<link rel="preconnect" href="https://www.googletagmanager.com">` solo se GTM resta sopra la fold del waterfall; altrimenti non serve.

## Priorita' (impatto/sforzo)
1. Avatar + cover + card in webp ridimensionate con width/height/lazy (LCP -1,5/-2,5 s, CLS) - alto/basso
2. Self-host font + preload (FCP/LCP -300/-800 ms) - medio/basso
3. Header cache immutable + CSS fingerprint/minify - medio/basso
4. Deduplicare GA4 (GTM+gtag), iubenda async, Clarity differito (TBT/INP) - medio/basso
5. og:image 1200x630 dedicata - basso/basso
Target: LCP <2,5 s, CLS <0,1, INP <200 ms, Lighthouse mobile >90.
