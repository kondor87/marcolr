# Re-check di laroccadigitale.it, 10 ottobre 2026

Seconda review completa, tre giorni dopo quella del 7 ottobre, fatta sul sito online (commit 17e1079, pubblicato).
Strumenti: skill `seo` (agenti tecnico, contenuti, schema, prestazioni, Google, SXO) e skill `impeccable` (critica con due valutazioni separate e rilevatore automatico).

## Punteggi

| Area | 7 ottobre | 10 ottobre | Dopo le correzioni di oggi (stima) |
|---|---|---|---|
| Tecnico | 68 | 92 | 94 |
| Contenuti | 52 | 68 | circa 78 |
| Dati strutturati (schema) | n/d | 38 (errore di codifica) | circa 85 |
| Prestazioni mobile (Lighthouse, laboratorio) | n/d | 49 | da rimisurare dopo la pubblicazione |
| UI/UX (Nielsen, impeccable) | 21/32 | 22/32 | da rimisurare dopo la pubblicazione |

## Corretto oggi (da pubblicare a mano su Netlify)

- **Dati strutturati**: titoli e descrizioni uscivano con virgolette doppie (`"\"...\""`) per un problema di escape di Hugo nei blocchi `ld+json`. Corretto con `jsonify | safeJS`. Aggiunti dati per /blog/ (Blog) e /lavori/ (CollectionPage), WebPage + Service sulla pagina servizio, Martina come Person.
- **robots.txt**: tolto `Disallow: /grazie/`, che impediva a Google di leggere il noindex. Aggiunto redirect `/favicon.ico` → `/favicon.png`.
- **Font**: ospitati sul sito (`static/fonts/`, `assets/css/fonts.css`), con preload dei due principali. Niente più richieste a Google Fonts. Lo script di iubenda resta sincrono di proposito: deve partire prima degli altri per bloccarli.
- **Articoli**: i post AI per psicologi, nutrizionisti, osteopati e la guida ora rispettano le regole dell'articolo GDPR (niente minori o urgenze gestiti dal chatbot, niente sintomi raccolti, niente invio automatico, niente "sembra scritto da te"). Tolti numeri senza fonte, formule da pubblicità, emoji nei titoli, i tre blocchi "Articoli correlati" con titoli vecchi e le frasi da attività continuativa. Aggiunti link interni tra articoli collegati, title più brevi (`seoTitle`) per 5 articoli, la description di /blog/ e aggiornati 5 link di fonti che facevano redirect.
- **Pagina servizio e Lavori**: "Un sito fatto da me ha", link alla checklist su dominio e accessi, introduzione di /lavori/ onesta (un solo lavoro pubblicato).
- **UI**: testi della home da 12-13px a 14.5-16px (solo CSS, nessuna parola cambiata), testimonianza con tipografia da citazione, "Perché lavorare con me" su una colonna da telefono, FAQ uguali tra home e pagina servizio, il menu non copre più i titoli quando si salta a #contacts, icona mail visibile sul pulsante verde, contrasti a norma (`.service-badge`, `.portfolio-tag`, filtro attivo del blog, numeri dei passi, segnaposto del form), tocchi da 44px su filtri e FAQ, link privacy/cookie senza badge iubenda.

## Resta da fare (serve Marco)

1. **Pubblicare** il deploy su Netlify.
2. **Search Console**: chiedere l'indicizzazione di /siti-web-frascati-castelli-romani/, /lavori/, /lavori/martina-iannotti-nutrizionista/ e /blog/ (per Google sono "URL sconosciuti"). Ricontrollare i dati dopo il 17 ottobre.
3. **Banner iubenda** (pannello iubenda): versione compatta in basso, colori del sito. Oggi copre metà schermo su telefono.
4. ~~Decisioni sulla home~~ fatte il 10/10 con il sì di Marco: terminale in italiano ("disponibile su richiesta") e visibile da telefono, campo telefono facoltativo nel modulo, FAQ sulla ritenuta corretta per i forfettari (da far confermare al commercialista).
5. **Caso Martina** più ricco (dati veri, screenshot da telefono): è la pagina che Google premierebbe per "sito web per nutrizionista".
6. ~~GTM + GA4~~ tolti il 10/10 (GA4 non raccoglieva dati con iubenda gratuito). ID per rimetterli nel commento di `layouts/partials/shared/head.html`. Clarity resta, bloccato da iubenda fino al consenso.

Dettagli: `technical.md`, `content.md`, `schema.md`, `performance.md`, `google.md`, `sxo.md` in questa cartella.
