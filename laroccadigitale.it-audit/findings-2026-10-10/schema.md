# Audit dati strutturati JSON-LD — laroccadigitale.it (10 ottobre 2026)

**Punteggio: 38/100**

Pagine verificate (tutte HTTP 200): home, /siti-web-frascati-castelli-romani/, /lavori/, /lavori/martina-iannotti-nutrizionista/, /blog/, e 3 articoli (quanto-costa-sito-web, ai-automazione-psicologo, chi-possiede-il-tuo-sito-dominio-hosting-accessi).
Generatore: `layouts/partials/shared/schema.html`. Nessun file modificato.

## Rilevato

| Pagina | Blocchi | JSON sintatticamente valido | Esito |
|---|---|---|---|
| Home | @graph (WebSite, Person, 2 Service) + FAQPage | si | valori errati (vedi P1) |
| /siti-web-frascati-.../ | BreadcrumbList + FAQPage | si | valori errati |
| /lavori/ | nessuno | - | assente |
| /lavori/martina-.../ | @graph (CreativeWork+WebPage, BreadcrumbList) | si | valori errati |
| /blog/ | nessuno | - | assente |
| 3 articoli | @graph (BlogPosting, Person, BreadcrumbList) | si | valori errati |

Immagini referenziate (marco-avatar.png, og/*.png, lavori/martina-iannotti.jpg): tutte 200 con content-type corretto.
@id: coerenti (`/#website`, `/#person`, `/#servizio-siti-web`, `/#servizio-prenotazioni`, `<permalink>#articolo`, `<permalink>#lavoro`), tutti i riferimenti `{"@id": ...}` risolvono. Contesto `https://schema.org`, URL assoluti, date ISO 8601: ok.

## Problemi per priorità

### P1 — Critico: doppia codifica delle stringhe (tutte le pagine con schema)
Nel JSON-LD live ogni stringa passata con `| jsonify` esce con virgolette letterali incluse, es.:
- `"headline": "\"Quanto costa un sito web nel 2026? ...\""`
- `"sameAs": ["\"https://github.com/kondor87\""]` (URL non valido: Person non collegata al profilo)
- `"url": "\"https://www.martinaiannottinutrizione.it/\""` (URL non valido)
- `"articleSection": "\"Business Digitale\""`, `"keywords": "\"a, b, c\""`
- Tutte le domande/risposte FAQPage, description di WebSite, name delle ListItem nei breadcrumb.

Causa: Hugo (html/template) tratta `<script type="application/ld+json">` come contesto JS e codifica già il valore; `jsonify` lo racchiude due volte. Effetto: titoli, descrizioni, nomi breadcrumb e URL sameAs/url sono errati per Google e i validatori; sameAs e url non sono utilizzabili.

Correzione (in `schema.html`, ogni uso di `| jsonify` fuori da virgolette):
```go-html-template
{{/* prima */}}  "headline": {{ .Title | jsonify }},
{{/* dopo  */}}  "headline": {{ .Title | jsonify | safeJS }},
```
Applicare `| safeJS` a: description WebSite, sameAs (`[{{ .Site.Params.github | jsonify | safeJS }}]`), headline, description BlogPosting, articleSection, keywords (`{{ delimit . ", " | jsonify | safeJS }}`), name/description CreativeWork, `about.name`/`about.url`, name ListItem, e a `$f.q` / `$f.a` nelle FAQ. Alternativa più robusta: costruire un `dict`/`slice` Hugo e stampare `{{ $schema | jsonify | safeJS }}`. Dopo il fix rieseguire una verifica live (le virgolette extra devono sparire).

### P2 — Alto: nessun JSON-LD su /lavori/ e /blog/
Le liste (section `_index`) non rientrano in nessun ramo (`.IsPage` è falso). Aggiungere almeno BreadcrumbList e CollectionPage:
```html
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@graph": [
    {"@type": "CollectionPage", "@id": "https://laroccadigitale.it/blog/#pagina", "url": "https://laroccadigitale.it/blog/",
     "name": "Blog", "inLanguage": "it-IT", "isPartOf": {"@id": "https://laroccadigitale.it/#website"}},
    {"@type": "BreadcrumbList", "itemListElement": [
      {"@type": "ListItem", "position": 1, "name": "Home", "item": "https://laroccadigitale.it/"},
      {"@type": "ListItem", "position": 2, "name": "Blog", "item": "https://laroccadigitale.it/blog/"}]}
  ]
}
</script>
```
(analogo per /lavori/). In Hugo: nuovo ramo `{{ else if and .IsSection (or (eq .Section "blog") (eq .Section "lavori")) }}`.

### P3 — Medio: pagina servizio senza entità Service/WebPage collegata
/siti-web-frascati-castelli-romani/ ha solo breadcrumb + FAQ. Il Service `#servizio-siti-web` è definito solo in home con `url` che punta alla pagina. Aggiungere sulla pagina un WebPage che lo colleghi:
```json
{"@context":"https://schema.org","@type":"WebPage","@id":"https://laroccadigitale.it/siti-web-frascati-castelli-romani/#pagina",
 "url":"https://laroccadigitale.it/siti-web-frascati-castelli-romani/","inLanguage":"it-IT",
 "isPartOf":{"@id":"https://laroccadigitale.it/#website"},"mainEntity":{"@id":"https://laroccadigitale.it/#servizio-siti-web"}}
```
Nota: nessun LocalBusiness/Organization, coerente con il vincolo (prestazione occasionale, nessun indirizzo).

### P4 — Medio: riferimenti @id a entità non presenti nella pagina
BlogPosting/CreativeWork puntano a `/#website` (definito solo in home). Valido per il grafo del sito, ma i validatori per singola pagina non risolvono il riferimento. Per i casi in cui interessa l'autonomia della pagina, incorporare un `WebSite` minimo (`@id`, `url`, `name`) nel grafo, come già fatto per Person.

### P5 — Medio: proprietà consigliate mancanti
- BlogPosting: `author` e `publisher` sono solo `{"@id"}` verso una Person. Google richiede/consiglia che author abbia `name` e `url`: la Person nel grafo li ha, quindi ok. Per Article non servono logo (publisher Person è accettabile). Aggiungere `author` con `name` inline per tool che non risolvono @id: `"author": {"@id": "...#person", "@type": "Person", "name": "Marco La Rocca"}`.
- Immagini: una sola immagine per articolo. Google consiglia più rapporti (16:9, 4:3, 1:1) o almeno una >= 1200 px. Verificare dimensioni dei PNG OG (HEAD ha restituito content-length 0, controllare con GET).
- `dateModified` di tutti gli articoli = 2026-10-07 (probabile aggiornamento massivo da git). Usare date di modifica reali solo quando il contenuto cambia davvero, per non segnalare freschezza falsa.
- CreativeWork: `datePublished`/`dateModified` solo data (valido ISO 8601); `about` come Organization per una persona fisica (Martina Iannotti, professionista) sarebbe più corretto come `Person` oppure usare `WebSite`/`sameAs`:
```json
"about": {"@type": "Person", "name": "Martina Iannotti", "url": "https://www.martinaiannottinutrizione.it/", "jobTitle": "Biologa nutrizionista"}
```
- Person home: aggiungere `jobTitle` (es. "Sviluppatore web") e `email`/`contactPoint` solo se pubblici; nessun indirizzo.

### P6 — Basso: Service
Il Service `#servizio-prenotazioni` non ha `url`; `Offer` senza prezzo (corretto, i prezzi sono su preventivo). Opzionale: `description` per entrambi i Service. `areaServed` con City senza `containedInPlace`: accettabile.

### Info — FAQPage
FAQPage presente su home (5 domande) e pagina servizio (3). Google ha ritirato i rich result FAQ dal 7 maggio 2026: nessun beneficio SERP; eventuale valore AI/GEO non confermato. Nessuna azione richiesta, si può lasciare; il bug P1 va comunque corretto perché rende errato anche il testo.

## Sintesi punteggio
- Sintassi/@id/URL immagini/date: ok (+45)
- Valori corretti: no, doppia codifica ovunque (-)
- Copertura pagine: 6 su 8 con schema (-)
- Dopo P1+P2 il punteggio atteso è circa 85/100.
