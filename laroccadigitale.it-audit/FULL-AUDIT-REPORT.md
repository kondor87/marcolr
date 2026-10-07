# Review completa di laroccadigitale.it

7 ottobre 2026 · SEO, tecnica, grafica, blog e lavoro occasionale

Strumenti usati: skill `seo` (audit con 8 specialisti: tecnico, contenuti, schema, GEO, locale, performance, SXO, agent-readiness), `impeccable` (direzione grafica, detector, revisione finale indipendente, documentazione), `ui-ux-pro-max` / `frontend-design` come riferimento di stile, Playwright per gli screenshot. I report dei singoli specialisti sono in [findings/](findings/).

---

## 1. In breve

- **Il sito funzionava, ma aveva errori invisibili che costavano**: home da ~5,7 MB di immagini (ora ~0,1 MB), Microsoft Clarity bloccato dalla tua stessa CSP, analytics caricati prima del consenso, schema che dichiarava un ufficio in "via Frascati" che non esiste, circa 50 pagine-tag quasi vuote nella sitemap, robots.txt che bloccava proprio gli assistenti AI che `llms.txt` invitava.
- **Ho applicato quasi tutte le correzioni al sito attuale** (niente commit e niente push: rivedi tu il diff). L'elenco è nelle sezioni 3 e 4.
- **Due versioni grafiche nuove** in `versioni/`: *Targa* (portone, ottone, citofono) e *Programma* (modernismo all'italiana a campi di colore). Usano gli stessi contenuti. Si avviano con `versioni/avvia-versioni.bat`.
- **Nuova sezione Lavori** (`/lavori/`) con il caso Martina Iannotti e l'Osteria Gemelli in bozza nascosta. **Nuova pagina servizio** `/siti-web-frascati-castelli-romani/` (prima era un articolo del blog), con redirect 301.
- **Blog**: 13 articoli rivisti, 3 nuovi. Tolte statistiche inventate, frasi da "attività abituale", inesattezze tecniche; aggiunte le tutele GDPR/AI Act dove si parla di dati sanitari.

Punteggio SEO stimato **prima** delle correzioni: **~55/100** (tecnico 68, contenuti 52, schema ~45, performance ~50 stimata, AI search 54, locale 31). Non ho dati reali di Google: PageSpeed ha risposto "quota esaurita" e Search Console non è collegata a questa installazione delle skill.

---

## 2. Prima di tutto: il lavoro occasionale

Questo è il punto più importante, quindi lo metto in cima. **Non sono un commercialista**: quello che segue serve a farti le domande giuste, la risposta definitiva la dà il tuo consulente.

### Cosa conta davvero

Per il fisco e l'INPS la prestazione occasionale (art. 2222 c.c., redditi diversi art. 67 TUIR) è definita dai **fatti**, non dal sito: quanti lavori fai, con che regolarità, se c'è un'organizzazione stabile. Il sito è solo un indizio. Gli indizi più pesanti oggi sono **fuori dal sito**:

| Indizio | Dove l'ho visto | Rischio | Cosa fare |
|---|---|---|---|
| **Manutenzione annuale a canone** (180 o 390 €/anno) | Preventivo Osteria Gemelli | **Alto**: un canone ricorrente è l'opposto dell'occasionalità | Proporre solo interventi singoli, pagati quando servono. Niente "pacchetti annuali" |
| **Email a freddo** a nuovi clienti | `template_email_cold_clienti.md` | Medio: è marketing attivo e sistematico | Usarle con molta parsimonia, o solo dopo aver deciso di aprire la P.IVA |
| Blog con pubblicazione regolare + SEO per trovare clienti | Il sito stesso | Medio-basso: è presenza professionale continuativa | Tono personale (fatto), nessun listino (fatto), nessuna promessa di continuità (fatto) |
| Numero di lavori l'anno | — | Dipende | Con "pochi lavori l'anno" (2-3) sei nell'area più tranquilla |

### Adempimenti da ricordare (verifica con il commercialista)

- **Ricevuta** per ogni lavoro, con i dati delle parti, descrizione e compenso.
- **Ritenuta d'acconto del 20%** solo se il cliente è un sostituto d'imposta (impresa o professionista con P.IVA in regime ordinario); niente ritenuta con i privati e con i forfettari.
- **Marca da bollo da 2 €** sulle ricevute sopra 77,47 €.
- **INPS gestione separata** solo sulla parte di compensi occasionali che supera **5.000 € l'anno** (totale di tutti i committenti).
- **Comunicazione preventiva all'Ispettorato del Lavoro**: la fa il committente se è un'impresa (L. 215/2021). Conviene dirlo ai clienti-impresa prima di iniziare.
- In dichiarazione dei redditi vanno indicati come redditi diversi.
- **Sei dipendente**: controlla il contratto di lavoro (obbligo di fedeltà, art. 2105 c.c., eventuali clausole di esclusiva o di non concorrenza). Se fossi un dipendente pubblico servirebbe l'autorizzazione dell'ente.

Ho messo la parte pratica (ricevuta, ritenuta, bollo) anche nelle FAQ della home: rassicura i clienti e mostra trasparenza.

### Cosa ho cambiato nel sito per coerenza

- Dicitura fiscale unica in un solo file (`layouts/partials/shared/occasionale.html`), presente in ogni pagina e in tutte le versioni, con "senza partita IVA" esplicito.
- Rimosse le frasi che descrivevano un'attività abituale: "dati che analizzo costantemente per i miei clienti", "la domanda che mi fanno più spesso i ristoratori", "livello Pro", "pacchetto completo", il pitch di manutenzione periodica nell'articolo su WordPress, "fanno sempre parte del lavoro".
- Home riscritta in tono personale: "Di lavoro faccio l'informatico; i siti web li realizzo su richiesta, per poche persone l'anno". Le schede servizi dicono "Su richiesta".
- JSON-LD: tolto `ProfessionalService` con indirizzo e coordinate (dichiarava una sede inesistente), ora c'è una **persona** che offre servizi. Quando avrai la P.IVA si può tornare a un'entità "attività".
- **Google Business Profile: sconsigliato per ora.** Senza sede né P.IVA rischi la sospensione in verifica, e una scheda con orari e recensioni comunica un'attività continuativa. Alternative sicure: profilo LinkedIn personale con raccomandazioni, link "sito realizzato da Marco La Rocca" nei siti dei clienti (con il loro consenso), GitHub.

---

## 3. SEO: cosa andava e cosa no

Legenda: ✅ fatto · ⏳ da fare tu · 💡 suggerimento

### Tecnico

| Problema | Gravità | Stato |
|---|---|---|
| CSP bloccava `scripts.clarity.ms`: Clarity probabilmente non registrava nulla | Alta | ✅ `*.clarity.ms` in CSP |
| CSP bloccava CSS e font di iubenda (link privacy e banner parzialmente rotti) | Alta | ✅ `*.iubenda.com` in style/font/frame-src |
| GA4, GTM e Clarity partivano prima del consenso | Alta (GDPR) | ✅ Google Consent Mode v2 "denied" di default, iubenda caricato prima di GTM · ⏳ **attiva "Google Consent Mode" nel pannello iubenda**, altrimenti GA4 resta sempre in modalità negata |
| ~58 URL di tag e categorie quasi vuoti in sitemap | Media | ✅ tag disattivati (+ redirect 301 `/tags/*` → `/blog/`), indice categorie fuori sitemap e noindex |
| `/archivio/` riceveva schema BlogPosting e breadcrumb "Blog" | Media | ✅ schema solo per `Section = blog` |
| Titoli non escapati nel JSON-LD (un `"` nel titolo rompeva lo schema) | Media | ✅ `jsonify` ovunque |
| CSS con `?v={{ now.Unix }}`: cache invalidata a ogni deploy, e Netlify servendo tutto con `max-age=0` | Media | ✅ CSS minificato con fingerprint + `Cache-Control` immutabile per `/css/*`, 30 giorni per `/images/*` |
| Pagina 404 generica di Netlify in inglese | Media | ✅ `layouts/404.html` in italiano |
| `meta keywords` | Bassa | ✅ rimosso (Google lo ignora da anni) |
| H1 della home con testo nascosto (`sr-only`) | Bassa | ✅ H1 visibile: "Marco La Rocca — Siti web per professionisti e attività locali, a Frascati e nei Castelli Romani" |
| Nessuna pagina di ringraziamento dopo il form | Bassa | ✅ `/grazie/` (noindex): utile anche per misurare le conversioni in GA4 · ⏳ crea in GA4 l'evento "conversione" sulla visita a `/grazie/` |

### Performance

| Problema | Stato |
|---|---|
| `marco-avatar.png` da 1,5 MB mostrato a 120 px | ✅ WebP ridimensionata (~12 KB) via `partials/shared/img.html` |
| Copertine PNG da 650-990 KB, nessun `width/height`, nessun lazy loading | ✅ tutte le immagini passano da Hugo: WebP 1x/2x, `srcset`, `width/height`, `loading="lazy"`, `fetchpriority="high"` sull'immagine principale |
| Immagini dentro gli articoli Markdown non ottimizzate | ✅ render hook `layouts/_default/_markup/render-image.html` (es. 397 KB → 32 KB) |
| Peso immagini della home | ✅ da ~5,7 MB a **~108 KB** |
| Google Fonts che bloccano il rendering | 💡 scaricare i `.woff2` e servirli dal sito (lo farei sulla grafica scelta) |
| og:image di default quadrata 400×400 con `summary_large_image` | ✅ nuova `og-default.png` 1200×630 |

⏳ Misura i risultati veri con [PageSpeed Insights](https://pagespeed.web.dev/) dopo il deploy.

### Contenuti e on-page

| Problema | Stato |
|---|---|
| Nessuna pagina di servizio locale: per "realizzazione siti web Castelli Romani" Google mostra pagine di servizio, e tu rispondevi con un articolo del blog | ✅ nuova `/siti-web-frascati-castelli-romani/` (con FAQ e schema), l'articolo reindirizza in 301 |
| Nessuna sezione lavori / case study | ✅ `/lavori/` + `/lavori/martina-iannotti-nutrizionista/` |
| Titoli acchiappaclic ("Risparmia 10 ore a settimana") non sostenuti dai numeri | ✅ riscritti |
| Statistiche senza fonte (70%, 53%, no-show -80%, aderenza 30→70%, ROI 10x) | ✅ tolte o trasformate in esempi dichiaratamente ipotetici |
| Blocco "AI vs automazione" copiato in 5 articoli (contenuto duplicato) | ✅ sostituito da un paragrafo breve che rimanda alla guida |
| Articoli correlati scelti a caso (`shuffle`) | ✅ correlati per tag e categoria (`.Related`) |
| `alt` delle card del blog uguale al titolo della pagina (bug di template) | ✅ corretto |
| Date dell'archivio: tutte stampate come "02 Gen" (bug: `Gen` non è un formato Go) | ✅ `time.Format "02 Jan"`, ora localizzato |
| Hugo trasformava "AI e Automazione" in "AI E Automazione" | ✅ `titleCaseStyle = "none"` |
| Nessun `lastmod` (data di modifica sempre uguale alla pubblicazione) | ✅ `lastmod` sugli articoli rivisti, mostrato come "aggiornato il" |
| Una sola testimonianza, di Pescara | ⏳ chiedi 2-3 testimonianze scritte (con consenso a pubblicarle) ai prossimi clienti |

### Dati strutturati (schema)

✅ Grafo `WebSite` + `Person` + 2 `Service` con `areaServed` sui comuni dei Castelli Romani · `BlogPosting` completo (publisher, mainEntityOfPage, author @id, wordCount, articleSection) · `BreadcrumbList` corretto · `CreativeWork` per i case study · `FAQPage` generato in automatico da qualsiasi pagina con `faq:` nel front matter.
⏳ Dopo il deploy prova la home e un articolo su [validator.schema.org](https://validator.schema.org/) e nel Rich Results Test.

### Ricerca AI (ChatGPT, Perplexity, Gemini, Claude)

| Problema | Stato |
|---|---|
| `robots.txt` bloccava GPTBot, ChatGPT-User, ClaudeBot, PerplexityBot, Google-Extended… mentre `llms.txt` invitava gli stessi assistenti | ✅ robots.txt aperto a tutti tranne Bytespider. Se preferisci non far usare i testi per l'addestramento, rimetti solo `GPTBot` e `CCBot` in Disallow: le citazioni restano |
| `llms.txt` scritto a mano, con 8 articoli su 14 | ✅ generato da Hugo a ogni build (`layouts/index.llms.txt`) con tutti gli articoli e i lavori |
| Omonimia: esiste un giornalista Marco La Rocca citato su Wikipedia | 💡 rafforza l'entità: profilo LinkedIn con link al sito, stesso nome e foto ovunque, `sameAs` nello schema quando aggiungi profili |

---

## 4. Analisi tecnica (da sviluppatore)

**Scelta di fondo: ottima.** Un sito statico Hugo su Netlify è la scelta giusta per un sito personale: veloce, sicuro, senza manutenzione, costo zero. Tienilo così.

**Cosa non andava nel codice**

1. **Copia-incolla tra template.** Menu e footer erano ripetuti in 5 file: una modifica alla dicitura legale andava fatta 5 volte (e infatti le versioni non coincidevano). Ora sono partial unici.
2. **Contenuti dentro il codice.** I testi della home erano nell'HTML: per cambiare una FAQ dovevi toccare il template. Ora stanno nel front matter di `content/_index.md`, e le due nuove grafiche leggono gli stessi dati.
3. **Stili inline ovunque** (`style="..."` su decine di elementi, `onmouseover` per lo zoom): difficili da mantenere e in conflitto con una CSP rigorosa. Le nuove versioni non ne hanno quasi più.
4. **JSON-LD costruito concatenando stringhe** senza escaping: bastava un apice nel titolo per invalidarlo.
5. **Immagini servite così come caricate**, senza pipeline: il problema di performance più grande del sito.
6. **Cache busting sbagliato** (`now.Unix`): rompeva la cache del CSS a ogni deploy, senza alcun vantaggio.
7. **Consenso e CSP mai verificati in un browser vero**: Clarity risultava installato ma era bloccato.
8. **Accessibilità**: FAQ fatte con `<button onclick>` senza `aria-expanded` (ora `<details>` nativi), filtri del blog senza `aria-pressed` (aggiunto), animazioni senza alternativa per chi le disattiva (aggiunta, e corretto un caso in cui il contenuto restava invisibile).

**Come è organizzato ora**

```
layouts/partials/shared/   ← condiviso da tutte le grafiche
  head.html                consenso, analytics, meta, Open Graph
  schema.html              tutto il JSON-LD
  img.html                 immagini WebP responsive
  occasionale.html         dicitura fiscale
layouts/index.llms.txt     llms.txt generato
layouts/_default/_markup/  immagini responsive anche nel Markdown
content/_index.md          testi della home (dati, non HTML)
content/lavori/            case study
versioni/v2-targa/         grafica 2 (monta content, immagini e partial condivisi)
versioni/v3-programma/     grafica 3
```

**Cosa farei ancora**

- 💡 Fonti locali (`static/fonts/`) al posto di Google Fonts: meno richieste esterne, niente dati a Google, CSP più stretta.
- 💡 Spostare i PNG originali in `assets/` (oggi stanno anche in `static/`, quindi finiscono online pure gli originali pesanti, anche se nessuna pagina li usa più).
- 💡 Allineare la versione di Hugo: in locale hai la 0.160.1, Netlify usa la 0.158.0 (`netlify.toml`). Ho usato solo funzioni presenti in entrambe, ma conviene tenerle uguali.
- 💡 Un controllo automatico prima del push (build + verifica JSON-LD + link rotti), per esempio con lo script `pre_commit_seo_check.sh` che hai già in `.agent/skills/seo/scripts/`.
- 💡 Pulizia della root: `FULL-AUDIT-REPORT.md`, `ACTION-PLAN.md`, `FULL-SITE-AUDIT.md`, `GLOBAL-ACTION-PLAN.md`, `SEO-REPORT*.html` sono audit vecchi e in parte superati da questo; `martina.jpeg` in root è un doppione.

---

## 5. Le due versioni grafiche

Entrambe tengono gli stessi contenuti, la sezione Lavori, il blog, i form e tutta la SEO. Hanno ricevuto una revisione finale indipendente (con le correzioni applicate) e sono state controllate su desktop (1440 px) e mobile (390 px), senza scroll orizzontale.

### V2 · Targa (`versioni/v2-targa`)

Il sito come il portone di un palazzo di Frascati. In apertura una **targa d'ottone** con viti e incisione ("Marco La Rocca · Siti web su richiesta · Frascati · Castelli Romani"). Il menu è una **pulsantiera del citofono**: il pulsante della pagina in cui sei resta premuto e la spia si accende. I lavori sono gli "interni" del palazzo. Il blog è la **bacheca con le lettere bianche** dell'androne. Materiali: peperino (la pietra dei Castelli), ottone, intonaco. Caratteri: Krona One (incisione) e Public Sans.

- Pro: memorabile, profondamente locale, racconta "uno di Frascati" senza dirlo.
- Contro: più "di carattere" che istituzionale. A qualcuno può sembrare troppo giocosa.

### V3 · Programma (`versioni/v3-programma`)

Un programma grafico modernista all'italiana, sulla scia della grafica Olivetti. **Campi di colore pieno** (vermiglione, giallo, cobalto, verde) senza sfumature né ombre, una composizione geometrica con le iniziali M e L, griglia a 12 colonne, un solo carattere (Albert Sans). I lavori sono tavole su campo colorato, il blog un indice pulito con un simbolo colorato per categoria.

- Pro: è quella con lo **standing più professionale**, chiara e autorevole, adatta a chi ha uno studio sanitario o professionale.
- Contro: meno legata al territorio.

**La mia raccomandazione: V3 Programma**, perché risponde meglio alla tua richiesta di uno standing più professionale e parla bene a nutrizionisti, psicologi e studi. Se invece vuoi che ti ricordino come "quello di Frascati", scegli V2. Come metterne online una è spiegato in `versioni/README.md`.

---

## 6. Blog: revisione articolo per articolo

| Articolo | Cosa ho cambiato |
|---|---|
| AI e automazione: la guida onesta | Description accorciata; Google Traduttore *è* AI (era detto il contrario); "pacchetto completo" → "se usi tutto"; prezzi datati ottobre 2026; riquadro sui dati sanitari |
| AI per psicologi | Titolo; tolto il blocco duplicato; riquadro GDPR/AI Act; lo "screening intelligente" diventa un assistente per domande pratiche con limiti chiari (niente valutazioni cliniche, protocollo di crisi, minori); numeri resi coerenti e dichiarati ipotetici |
| AI per nutrizionisti | Titolo senza promessa "8 ore"; questionari con dati sanitari solo su strumenti conformi; tolta l'aderenza "30→70%"; "caso reale" → esempio dichiarato |
| AI per osteopati | Il chatbot non dà più pareri clinici; tolti "-80%" e "70% dei benefici al 10% del costo"; riquadro GDPR |
| AI per ristoranti | Titolo; "zero commissioni" corretto (WhatsApp Business ha costi); avviso su allergeni e celiachia; ROI reso coerente (era ">10x" con costi incoerenti) |
| Quanto costa un sito web | Titolo con l'anno; Vercel (il piano gratuito non permette usi commerciali) → Netlify/Cloudflare; Wix "penalizzato" → spiegazione corretta; nuova sezione "E con me quanto costa?" senza listino |
| Parole chiave | Distinzione tra title e H1; tolta la regola "3-5 ripetizioni"; contenuti duplicati spiegati correttamente; "9 volte su 10" e "90%" tolti |
| Blog e trucchi SEO | "Google non ha gli occhi" → nome file e testo alternativo; link alla guida sulle parole chiave |
| Google Business e sito | Come funziona davvero il ranking su Maps (pertinenza, distanza, notorietà); tolta la sezione Q&A (Google la sta dismettendo) |
| 5 errori online | Tolte le statistiche senza fonte; recensioni false → "vietate", non "penalizzate" |
| Plugin WordPress | Riscritto come checklist fai-da-te; via il pitch di manutenzione periodica; refuso "carrozziere" |
| Perché un professionista ha bisogno di un sito | Titolo; frasi da "molti clienti" rese neutre |
| Monopagina o completo | "Livello Pro" e iperboli tolti; rimando alla privacy per le prenotazioni |
| Siti web Castelli Romani | Diventato la pagina servizio `/siti-web-frascati-castelli-romani/` |

💡 Restano da valutare: copertine riusate in più articoli (`blog_website_local_pro.png` in 3 post), emoji nei titoletti dei post AI, e l'eventuale fusione dei 3 articoli sanitari in uno solo più forte.

### I 3 articoli nuovi

1. **[AI, chatbot e dati dei pazienti: cosa deve sapere uno studio](../content/blog/ai-chatbot-dati-pazienti-gdpr.md)**: GDPR art. 9, AI Act art. 50 (obbligo di dichiarare il chatbot dal 2 agosto 2026), legge 132/2025 art. 13 (informare il cliente), tabella "va bene / meglio di no", checklist. Fonti ufficiali linkate (EUR-Lex, Normattiva, Garante). Dà fiducia e completa i tuoi articoli sull'AI.
2. **[Sito per ristorante o osteria: le 9 cose che deve avere davvero](../content/blog/sito-web-ristorante-cosa-deve-avere.md)**: nato dal lavoro sull'osteria, senza nominare il cliente. Intercetta "sito per ristorante".
3. **[Chi possiede davvero il tuo sito? La checklist di dominio, hosting e accessi](../content/blog/chi-possiede-il-tuo-sito-dominio-hosting-accessi.md)**: trasforma il tuo punto di forza ("il sito è tuo") in contenuto utile e citabile.

💡 Prossimi articoli possibili: "Sito per nutrizionista: cosa deve esserci" (Google mostra pagine così e tu hai il caso Martina), "Sito nuovo: quanto tempo per comparire su Google", "Quanto costa un sito per un ristorante".

---

## 7. Cosa devi fare tu

Vedi [ACTION-PLAN.md](ACTION-PLAN.md).

---

## Aggiornamento · secondo giro (7 ottobre 2026)

Su indicazione di Marco:

- **Testi della home** riscritti in modo più professionale: niente più "di lavoro faccio l'informatico" e "per poche persone l'anno" (suonava come una scusa). Ora: "il software è il mio mestiere", "uno alla volta, così ogni progetto ha tutta la mia attenzione". Le "perché lavorare con me" non ripetono più il "chi sono".
- **Copertine del blog**: rifatte tutte e 17 (16 articoli + pagina servizio) con un unico stile disegnato a mano in SVG, più lo schema "AI vs automazione". Le vecchie mischiavano tre stili e contenevano testo inventato; una mostrava perfino un listino "Starter / Standard / Premium". Le vecchie immagini sono in `archivio-immagini/`, fuori da `static/`: il sito pubblicato scende a ~3,9 MB.
- **V2** rifatta piatta e moderna con la stessa palette (via targhe, viti, ottone spazzolato, citofono e pulsanti 3D). In apertura c'è l'ultimo lavoro.
- **V3** ridotta a nero, vermiglione e un grigio.
- **V4 Cartiglio**, nuova: tavola tecnica con quote di misura e cartiglio, un solo accento ottone, stesso linguaggio delle copertine. È quella che ora consiglio: la più professionale, la più coerente con le copertine, e usa la palette che ti piace.
