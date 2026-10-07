# Audit tecnico - laroccadigitale.it (07/10/2026)

Punteggio tecnico stimato: **68/100**. Hugo statico: SSR completo, nessun problema di rendering JS.

## Cosa funziona (PASS)
- HTTP -> HTTPS 301; www -> non-www 301 (https://www -> https://laroccadigitale.it/). Nota: http://www fa 2 hop (http://www -> https://www -> https://root).
- 404 reale (status 404) su URL inesistenti. robots.txt 200 con Sitemap dichiarata; sitemap.xml 200 (~72 URL, valida).
- Canonical self-referencing su tutte le pagine controllate (home, tag, archivio, post). 1 solo H1 per pagina.
- Header presenti: HSTS (preload), X-Frame-Options, nosniff, Referrer-Policy, Permissions-Policy, CSP.

## CRITICAL
Nessuno.

## HIGH

### H1. La CSP blocca Microsoft Clarity (script-src)
Evidenza: `script-src` ammette solo `www.clarity.ms`. Il tag https://www.clarity.ms/tag/xt34tbj6ym carica a sua volta `https://scripts.clarity.ms/0.8.70/clarity.js` (verificato sul sorgente live), host non in lista, quindi bloccato. Il beacon `t.clarity.ms/collect` passerebbe (connect-src `https:`), ma senza clarity.js non parte nessuna registrazione.
Fix: aggiungere `https://scripts.clarity.ms` a script-src (meglio `https://*.clarity.ms`). Verificare in DevTools > Console ("Refused to load the script").

### H2. La CSP puo' degradare iubenda (stili e link policy); il banner non e' bloccato del tutto
Evidenza live: `embeds.iubenda.com/widgets/e9b3...js` carica `cdn.iubenda.com/cookie_solution/iubenda_cs/1.108.0/core-*.js` (script-src OK, quindi il banner in genere appare). Pero':
- `cdn.iubenda.com/iubenda.js` carica `iubenda_i_badge.js` e i CSS `cdn.iubenda.com/iubenda_i_badge.css`, `iubenda_badge.css` e `www.iubenda.com/assets/privacy_policy.css`. `style-src` ammette solo self, 'unsafe-inline' e fonts.googleapis.com, quindi questi fogli di stile sono bloccati: i link policy/cookie policy (classe `iubenda-embed`) perdono stile/modale.
- font-src non include cdn.iubenda.com (font eventuali del banner bloccati). Le chiamate API (consent/geo) passano con connect-src `https:`, le immagini con img-src `https:`.
Conclusione: script e connect sono permessi, quindi il banner dovrebbe comparire; rischio di rendering parziale. Non verificabile al 100% senza browser: controllare la console su una pagina live.
Fix: `style-src 'self' 'unsafe-inline' https://fonts.googleapis.com https://cdn.iubenda.com https://www.iubenda.com; font-src 'self' https://fonts.gstatic.com https://cdn.iubenda.com; script-src ... https://www.iubenda.com; frame-src 'self' https://www.googletagmanager.com https://www.iubenda.com`. Poi testare.

### H3. Analytics caricati PRIMA del consenso; Consent Mode non cablato
Evidenza (layouts/_default/baseof.html): GTM (riga ~8), gtag/GA4 (riga ~17) e Clarity (riga ~30) sono nell'head, incondizionati; lo script iubenda e' in fondo al body. La config iubenda ha `googleConsentModeV2: true`, ma non esiste alcun `gtag('consent','default',{...denied})` prima di GTM/gtag: i primi hit GA4 partono col consenso implicito. Lo script tag standard non e' marcato `_iub_cs_activate`, quindi l'auto-blocking non lo ferma. Clarity non riceve alcun segnale di consenso.
Rischio: non conformita' GDPR/ePrivacy (non SEO, ma legale e qualita' dati).
Fix: (1) prima di GTM impostare `gtag('consent','default',{ad_storage:'denied',analytics_storage:'denied',ad_user_data:'denied',ad_personalization:'denied',wait_for_update:500})`; (2) spostare lo script iubenda in cima all'head, prima di GTM; (3) Clarity: usare `clarity('consent', ...)` o caricarlo via GTM con trigger sul consenso, oppure marcarlo `type="text/plain" class="_iub_cs_activate"`.

## MEDIUM

### M1. Pagine tassonomia (tag/categorie) in sitemap e indicizzabili
Evidenza: la sitemap contiene ~58 URL su /tags/* e /categories/* su ~72 totali (14 articoli + home + blog + archivio). Nessun `noindex` sulle pagine tag (verificato /tags/seo/). Quasi ogni tag ha 1 solo post: thin content, spreco di crawl budget.
Fix: in hugo.toml `disableKinds = ["taxonomy","term"]` se non servono; altrimenti in baseof `{{ if in (slice "term" "taxonomy") .Kind }}<meta name="robots" content="noindex,follow">{{ end }}` e escluderle dalla sitemap (`sitemap: disable: true` via cascade). Ridurre il numero di tag.

### M2. Schema BlogPosting su `archivio` (e su ogni `.IsPage`)
Evidenza: `/archivio/` serve JSON-LD `BlogPosting` + `BreadcrumbList` (Home > Blog > Archivio). baseof usa `{{ if .IsPage }}`, vero per qualunque pagina contenuto. Inoltre: `description` vuota se manca, nessun `publisher`/`mainEntityOfPage`/`image` di default, titoli non escapati (usare `jsonify`).
Fix: `{{ if and .IsPage (eq .Section "blog") }}`; per archivio niente schema o `CollectionPage`; costruire il JSON con `dict | jsonify`; aggiungere publisher e image di fallback.

### M3. Cache busting `?v={{ now.Unix }}`
Evidenza: `style.css?v=1785169996` cambia a ogni build anche se il CSS e' identico, invalidando la cache dei visitatori. Netlify serve comunque `Cache-Control: max-age=0, must-revalidate` su tutti gli asset (anche CSS), quindi il parametro e' inutile e la cache e' di fatto sempre rivalidata.
Fix: Hugo Pipes `{{ $css := resources.Get "css/style.css" | minify | fingerprint }}` (file in assets/) e in netlify.toml `Cache-Control: public, max-age=31536000, immutable` per file fingerprintati e `/images/*`.

### M4. Pagina 404 generica in inglese
Evidenza: `<title>Page not found</title>`, H1 "Page not found" (default Netlify), nessun `layouts/404.html`.
Fix: creare `layouts/404.html` in italiano con link a home/blog e `noindex`.

### M5. GA4 non e' duplicato oggi, ma c'e' rischio latente
Evidenza: il container GTM-5TD66VKJ scaricato non contiene tag GA4 ne' G-XH543Y70CJ, quindi GA4 viene contato 1 volta (gtag diretto); GTM serve solo come contenitore vuoto. Se in GTM si aggiunge un tag Google/GA4 si avra' doppio pageview.
Fix: un solo canale. Consigliato: GA4 dentro GTM con Consent Mode e rimozione dello snippet gtag diretto.

## LOW
- L1. `<meta name="keywords">`: ignorato da Google; sulle pagine con tag espone i tag, fallback globale per le altre. Rimuoverlo.
- L2. H1 sr-only: la home ha `<h1>Marco<br>La Rocca<span class="sr-only"> - Siti Web per Professionisti a Frascati e Castelli Romani</span></h1>`. Sr-only con clip e' accessibile e non e' cloaking, ma il testo keyword e' invisibile ai vedenti e Google lo pesa meno. Fix: sottotitolo/H1 visibile descrittivo.
- L3. Sitemap: tutte le voci con changefreq weekly, priority 0.5 e lastmod identico (2026-07-27T10:00): segnali non attendibili. `enableGitInfo = true` per lastmod reale; togliere changefreq/priority. `archivio` ridondante.
- L4. http://www fa 2 hop: configurare redirect diretto.
- L5. robots.txt blocca GPTBot, ClaudeBot, PerplexityBot, Google-Extended, ecc. e si pubblica anche llms.txt: incoerente. Valutare di consentire crawler di ricerca/citazione (OAI-SearchBot, PerplexityBot, ChatGPT-User) per GEO.
- L6. CSP: `'unsafe-inline'` su script-src annulla gran parte della protezione XSS; `img-src https:` e `connect-src https:` troppo larghi. Dopo aver sistemato i terzi, restringere a host espliciti e usare nonce/hash.
- L7. Google Fonts da terzi: CSS render-blocking, 2 connessioni extra e trasferimento IP a Google (GDPR). Self-host dei font.
- L8. og:type `article` su ogni pagina contenuto (anche archivio); og:image di fallback 400x400 con `summary_large_image`: usare 1200x630.
- L9. JSON-LD home: `sameAs` solo GitHub; aggiungere Google Business Profile/LinkedIn se esistono; indirizzo generico ("Frascati").

## Priorita' interventi
1. CSP: aggiungere scripts.clarity.ms + host iubenda in style/font; testare in console (H1, H2).
2. Consent Mode default denied prima di GTM, iubenda in cima, Clarity dopo consenso (H3).
3. Noindex/disabilitare tag e categorie e ripulire la sitemap (M1, L3).
4. Schema BlogPosting solo su /blog/*; jsonify (M2).
5. Fingerprint CSS + cache lunga, 404 italiana, rimuovere keywords, un solo canale GA4 (M3-M5, L1).

Non verificato (serve browser): rendering effettivo del banner iubenda con la CSP attuale; Core Web Vitals reali (nessun dato CrUX).
