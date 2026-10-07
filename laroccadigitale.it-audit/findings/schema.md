# Audit JSON-LD — laroccadigitale.it (2026-10-07)

## 1. Rilevato
| Pagina | Blocchi | Esito |
|---|---|---|
| Home | 1 @graph: WebSite, ProfessionalService (#business), Person (#person) | Valido ma rischioso (vedi 2) |
| /blog/quanto-costa-sito-web/ | BlogPosting + BreadcrumbList | Valido, incompleto |
| /archivio/ | BlogPosting + BreadcrumbList (!) | ERRORE: pagina indice marcata come articolo, breadcrumb "Blog" falso |

Tutto server-rendered (HTML statico Hugo), @context https corretto, URL assoluti.
Causa dell'errore su /archivio/: in baseof.html il ramo `{{ if .IsPage }}` scatta per ogni pagina di contenuto (archivio, privacy, ecc.), non solo per i post.

## 2. ProfessionalService/LocalBusiness vs Person-centric
Problemi dell'attuale ProfessionalService:
- `streetAddress: "Frascati"` non e' un indirizzo: dato fittizio/poco valido. `geo` 41.808/12.682 e' il centro del comune, non una sede: fa sembrare una sede fisica che non esiste.
- LocalBusiness/ProfessionalService implica un'attivita' d'impresa con sede. Marco opera senza P.IVA, con prestazione occasionale (art. 2222 c.c.): dichiarare un "business" strutturato (nome "Siti Web", worksFor) e' incoerente con la realta' e con le linee Google (il markup deve rispecchiare il contenuto visibile e vero).
- Nessun beneficio SERP concreto: il local pack dipende da Google Business Profile (che richiede sede o service-area verificata), non dallo schema.
- Fuori ambito schema ma da segnalare: la prestazione occasionale ha limiti (occasionalita', soglia 5.000 EUR/anno per committente). Verificare con il commercialista che branding e promesse del sito non suggeriscano attivita' abituale.

RACCOMANDAZIONE: grafo Person-centric. Il Person e' l'entita' principale; i servizi sono `Service` con `provider` = Person e `areaServed`. Niente address con strada, niente geo, niente LocalBusiness. Il valore SEO resta: entita' autore (E-E-A-T), knowsAbout, areaServed locale (Frascati/Castelli Romani) leggibile da Google e dagli LLM. Quando esistera' P.IVA/sede: passare a ProfessionalService con indirizzo reale (o service-area business senza address) collegato via `@id`.
`worksFor` rimosso: non c'e' un'organizzazione.

## 3. Home — @graph proposto (Hugo)
Sostituisce il blocco `{{ if .IsHome }}`.
```html
{{ if .IsHome }}
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@graph": [
    {
      "@type": "WebSite",
      "@id": "{{ .Site.BaseURL }}#website",
      "url": "{{ .Site.BaseURL }}",
      "name": "Marco La Rocca — Siti Web a Frascati",
      "description": {{ .Site.Params.description | jsonify }},
      "inLanguage": "it-IT",
      "publisher": {"@id": "{{ .Site.BaseURL }}#person"}
    },
    {
      "@type": "WebPage",
      "@id": "{{ .Site.BaseURL }}#webpage",
      "url": "{{ .Site.BaseURL }}",
      "name": {{ .Title | jsonify }},
      "isPartOf": {"@id": "{{ .Site.BaseURL }}#website"},
      "about": {"@id": "{{ .Site.BaseURL }}#person"},
      "primaryImageOfPage": {"@type": "ImageObject", "url": "{{ "/images/marco-avatar.png" | absURL }}"},
      "inLanguage": "it-IT"
    },
    {
      "@type": "Person",
      "@id": "{{ .Site.BaseURL }}#person",
      "name": "Marco La Rocca",
      "url": "{{ .Site.BaseURL }}",
      "image": {"@type": "ImageObject", "url": "{{ "/images/marco-avatar.png" | absURL }}", "width": 400, "height": 400},
      "jobTitle": "Web designer e consulente SEO/AI",
      "description": "Web designer freelance a Frascati: siti web, SEO locale e automazione AI per professionisti e attivita locali dei Castelli Romani.",
      "homeLocation": {"@type": "City", "name": "Frascati"},
      "knowsAbout": ["Web design", "Siti vetrina", "SEO locale", "Automazione con intelligenza artificiale", "Hugo", "Performance web"],
      "knowsLanguage": "it",
      "sameAs": ["https://github.com/kondor87"],
      "makesOffer": [
        {"@type": "Offer", "itemOffered": {"@id": "{{ .Site.BaseURL }}#service-siti-web"}},
        {"@type": "Offer", "itemOffered": {"@id": "{{ .Site.BaseURL }}#service-seo-locale"}},
        {"@type": "Offer", "itemOffered": {"@id": "{{ .Site.BaseURL }}#service-automazione-ai"}}
      ]
    },
    {
      "@type": "Service",
      "@id": "{{ .Site.BaseURL }}#service-siti-web",
      "name": "Realizzazione siti web per professionisti e attivita locali",
      "serviceType": "Web design",
      "provider": {"@id": "{{ .Site.BaseURL }}#person"},
      "areaServed": [
        {"@type": "City", "name": "Frascati"}, {"@type": "City", "name": "Grottaferrata"},
        {"@type": "City", "name": "Marino"}, {"@type": "City", "name": "Albano Laziale"},
        {"@type": "City", "name": "Velletri"}, {"@type": "City", "name": "Genzano di Roma"},
        {"@type": "City", "name": "Rocca di Papa"}, {"@type": "City", "name": "Castel Gandolfo"},
        {"@type": "AdministrativeArea", "name": "Castelli Romani"}
      ]
    },
    {
      "@type": "Service",
      "@id": "{{ .Site.BaseURL }}#service-seo-locale",
      "name": "Consulenza SEO locale",
      "serviceType": "SEO",
      "provider": {"@id": "{{ .Site.BaseURL }}#person"},
      "areaServed": {"@type": "AdministrativeArea", "name": "Castelli Romani"}
    },
    {
      "@type": "Service",
      "@id": "{{ .Site.BaseURL }}#service-automazione-ai",
      "name": "Automazione con AI per professionisti",
      "serviceType": "Consulenza AI",
      "provider": {"@id": "{{ .Site.BaseURL }}#person"},
      "areaServed": {"@type": "Country", "name": "Italia"}
    }
  ]
}
</script>
{{ end }}
```
Non inserire `price` nelle Offer se non e' pubblicato in pagina (deve coincidere col visibile).

## 4. BlogPosting — correzioni
Difetti: manca `publisher`, `mainEntityOfPage`, `author.url/@id`; `{{ .Title }}` e `{{ .Description }}` non escapati (un `"` rompe il JSON: usare `jsonify`); date senza ora/fuso; mancano `inLanguage`, `wordCount`, `keywords`, `articleSection`; `image` assente se manca `.Params.image` (usare fallback). Va applicato solo ai post, non a /archivio/.

Condizione: `{{ if and .IsPage (eq .Section "blog") }}` (verificare `.Section` reale del post).
```html
{{ if and .IsPage (eq .Section "blog") }}
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@graph": [
    {
      "@type": "BlogPosting",
      "@id": "{{ .Permalink }}#article",
      "mainEntityOfPage": {"@type": "WebPage", "@id": "{{ .Permalink }}"},
      "headline": {{ .Title | jsonify }},
      "description": {{ (cond (ne .Description "") .Description .Site.Params.description) | jsonify }},
      "datePublished": "{{ .Date.Format "2006-01-02T15:04:05-07:00" }}",
      "dateModified": "{{ .Lastmod.Format "2006-01-02T15:04:05-07:00" }}",
      "inLanguage": "it-IT",
      "image": ["{{ with .Params.image }}{{ . | absURL }}{{ else }}{{ "/images/marco-avatar.png" | absURL }}{{ end }}"],
      "author": {"@id": "{{ .Site.BaseURL }}#person"},
      "publisher": {"@id": "{{ .Site.BaseURL }}#person"},
      "isPartOf": {"@id": "{{ .Site.BaseURL }}#website"},
      "wordCount": {{ .WordCount }}{{ with .Params.categories }},
      "articleSection": {{ index . 0 | jsonify }}{{ end }}{{ with .Params.tags }},
      "keywords": {{ delimit . ", " | jsonify }}{{ end }}
    },
    {
      "@type": "Person",
      "@id": "{{ .Site.BaseURL }}#person",
      "name": "Marco La Rocca",
      "url": "{{ .Site.BaseURL }}",
      "image": "{{ "/images/marco-avatar.png" | absURL }}",
      "sameAs": ["https://github.com/kondor87"]
    }
  ]
}
</script>
{{ end }}
```
Nota: `publisher` = Person e' valido (Organization non necessaria). Il Person ripetuto nel post rende il blocco autonomo anche per validatori che non risolvono @id tra script diversi.

## 5. BreadcrumbList
Difetti: ultimo elemento senza `item` (tollerato, meglio con URL); `.Title` non escapato; breadcrumb "Blog" applicato anche a /archivio/ e pagine non-blog (errore); URL concatenati a mano.
```html
{{ if and .IsPage (eq .Section "blog") }}
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "BreadcrumbList",
  "itemListElement": [
    {"@type": "ListItem", "position": 1, "name": "Home", "item": "{{ .Site.BaseURL }}"},
    {"@type": "ListItem", "position": 2, "name": "Blog", "item": "{{ "blog/" | absURL }}"},
    {"@type": "ListItem", "position": 3, "name": {{ .Title | jsonify }}, "item": "{{ .Permalink }}"}
  ]
}
</script>
{{ else if and .IsPage (ne .Section "lavori") }}
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "BreadcrumbList",
  "itemListElement": [
    {"@type": "ListItem", "position": 1, "name": "Home", "item": "{{ .Site.BaseURL }}"},
    {"@type": "ListItem", "position": 2, "name": {{ .Title | jsonify }}, "item": "{{ .Permalink }}"}
  ]
}
</script>
{{ end }}
```
Opzionale per /archivio/ (CollectionPage), da adattare al nome reale del layout:
```html
<script type="application/ld+json">
{"@context":"https://schema.org","@type":"CollectionPage","@id":"{{ .Permalink }}#webpage","url":"{{ .Permalink }}","name":{{ .Title | jsonify }},"isPartOf":{"@id":"{{ .Site.BaseURL }}#website"},"inLanguage":"it-IT"}
</script>
```

## 6. Case study per /lavori/ (CreativeWork con about/creator)
Front matter suggerito: `client`, `clientUrl`, `sector`, `image`, `services` (lista), `results`. Non pubblicare il nome del cliente senza consenso. `CreativeWork` e' il tipo piu' sicuro (nessun rich result Google, ma entita' chiara).
```html
{{ if and .IsPage (eq .Section "lavori") }}
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@graph": [
    {
      "@type": ["CreativeWork", "WebPage"],
      "@id": "{{ .Permalink }}#casestudy",
      "url": "{{ .Permalink }}",
      "name": {{ .Title | jsonify }},
      "description": {{ .Description | jsonify }},
      "inLanguage": "it-IT",
      "genre": "Case study",
      "datePublished": "{{ .Date.Format "2006-01-02" }}",
      "dateModified": "{{ .Lastmod.Format "2006-01-02" }}",
      "creator": {"@id": "{{ .Site.BaseURL }}#person"},
      "author": {"@id": "{{ .Site.BaseURL }}#person"},
      "publisher": {"@id": "{{ .Site.BaseURL }}#person"},
      "isPartOf": {"@id": "{{ .Site.BaseURL }}#website"},
      "image": "{{ with .Params.image }}{{ . | absURL }}{{ else }}{{ "/images/marco-avatar.png" | absURL }}{{ end }}",
      "about": [
        {"@type": "Thing", "name": "Realizzazione sito web"}{{ with .Params.sector }},
        {"@type": "Thing", "name": {{ . | jsonify }}}{{ end }}
      ]{{ with .Params.client }},
      "recipient": {"@type": "Organization", "name": {{ . | jsonify }}{{ with $.Params.clientUrl }}, "url": {{ . | jsonify }}{{ end }}}{{ end }}{{ with .Params.services }},
      "keywords": {{ delimit . ", " | jsonify }}{{ end }}{{ with .Params.clientUrl }},
      "exampleOfWork": {"@type": "WebSite", "url": {{ . | jsonify }}}{{ end }}
    }
  ]
}
</script>
<script type="application/ld+json">
{"@context":"https://schema.org","@type":"BreadcrumbList","itemListElement":[
 {"@type":"ListItem","position":1,"name":"Home","item":"{{ .Site.BaseURL }}"},
 {"@type":"ListItem","position":2,"name":"Lavori","item":"{{ "lavori/" | absURL }}"},
 {"@type":"ListItem","position":3,"name":{{ .Title | jsonify }},"item":"{{ .Permalink }}"}]}
</script>
{{ end }}
```
Indice `/lavori/` (list): `CollectionPage` con `mainEntity` = `ItemList` delle `.Pages` (ListItem con position e url). Non usare Review/AggregateRating per testimonianze proprie (self-serving, non idonee): solo recensioni di terzi verificabili e visibili.

## 7. Priorita'
1. (Alta) Sostituire ProfessionalService con address/geo fittizi con grafo Person + Service.
2. (Alta) Correggere /archivio/ (BlogPosting e breadcrumb errati) restringendo per `.Section`.
3. (Alta) `jsonify` su titoli/descrizioni (rischio JSON invalido).
4. (Media) publisher, mainEntityOfPage, author @id nel BlogPosting.
5. (Media) Schema /lavori/ al lancio.
6. (Bassa) Rivalutare ProfessionalService con P.IVA/sede; aggiungere sameAs (LinkedIn ecc.) se profili reali.
Validare con Rich Results Test e validator.schema.org dopo il deploy. Nessun file sorgente modificato.
