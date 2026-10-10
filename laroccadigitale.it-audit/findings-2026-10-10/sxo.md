# SXO: analisi della search experience di laroccadigitale.it

**Data:** 10/10/2026
**Pagine analizzate:** `/`, `/siti-web-frascati-castelli-romani/`, `/lavori/`, `/lavori/martina-iannotti-nutrizionista/`, `/blog/`, `/blog/quanto-costa-sito-web/`
**Metodo:** `render_page.py --mode always` (Playwright, tutte 200, nessuna SPA) + `parse_html.py`; SERP con WebSearch (query originali + varianti commerciali esplicite); confronto con il sorgente Hugo nel repository.
**Vincoli rispettati:** Marco lavora da solo, con prestazione occasionale e senza partita IVA, e fa pochi lavori l'anno. Nessuna proposta usa toni da agenzia, listini, pacchetti o canoni. **I testi della home non vanno toccati:** per la home ci sono solo proposte, marcate con [PROPOSTA HOME].

> Questo è uno **SXO Gap Score**. È separato dall'SEO Health Score e non va sommato a quello.

---

## 0. Il risultato principale

**Su 5 query, 1 mismatch è CRITICAL: "sito web per nutrizionista".** Google premia pagine verticali ("Siti web per nutrizionisti") e casi studio lunghi su siti di nutrizionisti. Marco ha l'unica prova vera che serve, cioè una nutrizionista reale con una testimonianza, ma la mostra in una scheda di 206 parole che nessuna query intercetta.

Sulle due query geografiche il tipo di pagina ora è **allineato**: dopo il 301 dal vecchio articolo del blog esiste una vera pagina servizio. Restano però due problemi:

1. **La pagina che Google mostra è ancora la home**, non la pagina servizio. Nelle SERP di "realizzazione siti web Frascati" e "web developer freelance Frascati Castelli Romani" compare `laroccadigitale.it/` con il vecchio title "Siti Web Frascati e Castelli Romani — Marco La Rocca". La pagina servizio non compare mai. Le due pagine si fanno concorrenza (cannibalizzazione).
2. **La pagina servizio non contiene prove.** Mancano screenshot dei lavori e la testimonianza di Martina, l'unica immagine è l'avatar con alt vuoto, e il modulo di contatto non c'è: entrambe le CTA rimandano a `/#contacts`. Le pagine concorrenti che vincono hanno tutte portfolio, recapiti e un elenco di comuni.

**Problema tecnico che blocca la parte Schema (da verificare con `/seo schema`).** Il JSON-LD online **non corrisponde al template del repository**. Sulla pagina servizio online ci sono solo `BreadcrumbList` e `FAQPage`, e tutte le stringhe hanno le virgolette raddoppiate. Esempio: `"name":"\"Lavori solo a Frascati?\""`. Lo stesso succede nella `description` del WebSite e nella FAQ della home, mentre `/lavori/` non ha nessun JSON-LD. Ho rifatto la build del working tree attuale in una cartella temporanea: l'output è corretto, con `WebPage` + `Service` come mainEntity e stringhe pulite. **Serve quindi solo un deploy** (le modifiche a `layouts/partials/shared/schema.html` non sono ancora committate né pubblicate).

**SXO Gap Score della pagina servizio `/siti-web-frascati-castelli-romani/`: 52/100.** Dopo il solo deploy dello schema corretto salirebbe a circa 57.

---

## 1. Le pagine di Marco oggi (DOM renderizzato)

| Pagina | Title | H1 | Parole | H2 | Schema online | Immagini | CTA |
|---|---|---|---|---|---|---|---|
| `/` | Siti web a Frascati e Castelli Romani — Marco La Rocca | "Marco La Rocca" + "Siti web per professionisti e attività locali, a Frascati e nei Castelli Romani" (nel DOM le parole sono attaccate: "MarcoLa RoccaSiti web…") | 990 | 9, tutti con il prefisso stilistico "// …" | WebSite, Person, Service, Offer, City, AdministrativeArea + FAQPage (stringhe con virgolette doppie) | ~8 | "Raccontami cosa ti serve", "Guarda i lavori", modulo in pagina |
| `/siti-web-frascati-castelli-romani/` | Realizzazione siti web a Frascati e Castelli Romani — Marco La Rocca | Siti web a Frascati e nei Castelli Romani | 685 | Cosa faccio, in pratica · Come si fa a comparire nelle ricerche della tua zona · Dove lavoro · Come funziona la collaborazione · FAQ | BreadcrumbList + FAQPage (virgolette doppie), **niente Service** | 1 (avatar, alt vuoto) | 2 link a `/#contacts`, nessun modulo in pagina |
| `/lavori/` | Lavori realizzati — Marco La Rocca, siti web a Frascati | Lavori | 161 | 1 (Martina Iannotti) | nessuno (nel sorgente c'è CollectionPage, non ancora pubblicato) | 2 | "Raccontami cosa ti serve" → `/#contacts` |
| `/lavori/martina-iannotti-nutrizionista/` | Martina Iannotti, biologa nutrizionista — Marco La Rocca | idem | 206 | Cosa serviva · Cosa ho fatto · Com'è andata | CreativeWork/WebPage, BreadcrumbList | 1 screenshot | link al sito del cliente |
| `/blog/` | Blog — Marco La Rocca | Blog | 789 | 16 titoli di articoli | nessuno online | — | — |
| `/blog/quanto-costa-sito-web/` | Quanto costa un sito web nel 2026? Guida ai prezzi reali | idem | 762 | 8 | BlogPosting, Person, BreadcrumbList | — | "Scrivimi, senza impegno" → `/#contacts` |

Altre osservazioni utili per la UX:
- La meta description di `/blog/` è quella generica del sito ("Realizzo siti web… Scrivimi senza impegno"). Non descrive il blog.
- La pagina servizio non ha date visibili. `htmldate` le attribuisce 01/01/2026, anche se il `lastmod` è 07/10/2026.
- Il modulo (Nome, Email, Messaggio) esiste solo in home: chi arriva da Google sulla pagina servizio o sul caso studio deve cambiare pagina per scrivere.
- Nel primo schermo della home c'è il widget a terminale `$ marco --status ✓ Available / $ stack --list`. Per uno sviluppatore è simpatico, ma per un ristoratore è rumore in inglese (vedi Persona B).

**Classificazione (tassonomia):** la home è un ibrido Landing/Service (CTA dominante, processo, testimonianza, modulo). `/siti-web-frascati-castelli-romani/` è una **Service Page** con segnali locali deboli: elenco di comuni, ma niente indirizzo né mappa, il che va bene perché non c'è una sede. Il caso studio è un **portfolio/case study**, che nella tassonomia è il blocco "case study" di una Service Page. `/blog/quanto-costa-sito-web/` è un **Blog Post**.

---

## 2. Analisi SERP all'indietro, query per query

> Lo strumento di ricerca è basato negli USA. **Non restituisce local pack, PAA, annunci né AI Overview di google.it**, e per le query brevi i primi risultati sono rumore (turismo, Wikipedia). Ogni query l'ho quindi fatta due volte: (a) com'era, per capire l'ambiguità dell'intento; (b) con una variante commerciale esplicita, per ricostruire la SERP che vede chi compra. Le percentuali di consenso si basano sui risultati della variante (b).

### 2.1 "siti web frascati"

**SERP (a), query com'era:** visitlazio.com (x2), amministrazionicomunali.it, en.wikipedia.org/Frascati, italia.it (ristoranti), registroaziende.it, agriturismo.it. Intento **ambiguo**: per Google "siti web Frascati" vuol dire anche "i siti di Frascati" (comune, turismo).
**SERP (b), "realizzazione siti web Frascati web designer":**

| # | Risultato | Tipo |
|---|---|---|
| 1 | prontopro.it/frascati-progettazione-siti-web | Directory / elenco |
| 2 | prontopro.it/frascati-programmazione-siti-web | Directory / elenco |
| 3 | **laroccadigitale.it/** (vecchio title) | Landing/Service (home) |
| 4 | avavo.it/realizzazione-siti-web-frascati/ | Service Page locale: 42 lavori in portfolio, indirizzo ad Ariccia, 16 comuni, telefono |
| 5 | sitisrl.it/web-agency-frascati | Service Page locale (agenzia) |
| 6 | antonellileonardo.com/realizzazione-siti-web-frascati/ | Service Page locale (freelance) |
| 7 | suitedesignstudio.com/realizzazione-siti-web-frascati/ | Service Page locale (pagina datata) |
| 8 | inconnect.it/…-siti-web-frascati/ | Service Page locale con "da 450 €", "in 2 giorni" |
| 9 | adarte.pro/realizzazione-siti-web-frascati.html | Service Page locale |

**Consenso:** Service Page locale 6/9 (67%), directory 2/9 (22%). Pattern ricorrente: slug `/realizzazione-siti-web-frascati/`, H1 uguale alla query, portfolio, recapiti.
**Pagina di Marco:** si posiziona la **home**. La pagina servizio, che sarebbe la risposta giusta, non compare.
**Mismatch: MEDIUM.** Il tipo è giusto (Service), ma l'URL sbagliato fa concorrenza a quello giusto.
**Cosa manca:**
- un **segnale interno forte** che dica a Google quale pagina vale per "Frascati". Oggi la home linka la pagina servizio solo dal menu ("Siti web") e da un link "Come lavoro sui siti per attività locali →";
- **prove sulla pagina servizio**: screenshot del sito di Martina, la sua citazione, un riquadro "Lavori realizzati";
- modulo di contatto **nella pagina** invece del rimando a `/#contacts`.

### 2.2 "realizzazione siti web castelli romani"

**SERP (a):** Parco dei Castelli Romani, turismoroma.it, wikivoyage, airbnb, un PDF diocesano, reteimprese. Nessun fornitore locale.
**SERP (b), con i comuni (Albano, Velletri, Grottaferrata):**

| # | Risultato | Tipo |
|---|---|---|
| 1 | dbnet.it/shop/…/realizzazione-sito-web-castelli-romani/ | Product Page (pacchetto a 700 € + IVA) |
| 2 | gestione-siti-web.it/internet-web-designer-castelli-roma-albano | Service Page locale (Albano) |
| 3 | superyapp.it | Home di freelance (Grottaferrata) |
| 4 | tfagency.it/agenzia-marketing/castelli-romani | Service Page locale (marketing) |
| 5 | webrex2000.com/realizzazione-siti-web-albano-laziale.html | Service Page per singolo comune |
| 6 | eccolomarketing.it/realizzazione-siti-web-roma/ | Service Page (Roma, cita i Castelli) |
| 7 | gbnet.it/siti-web/ | Service Page locale (Genzano, "da 20 anni") |
| 8 | studioinweb.com | Home di agenzia |
| 9 | inconnect.it/…-siti-web-castelli-romani/ | Service Page locale |

Nella SERP di 2.4 compare anche `avavo.it/realizzazione-siti-web-castelli-romani/`.
**Consenso:** Service Page locale 6/9 (67%), home di freelance/agenzia 2/9, Product 1/9. Quasi tutti **elencano i comuni serviti** e hanno sede nei Castelli.
**Pagina di Marco:** `/siti-web-frascati-castelli-romani/` (Service).
**Mismatch: ALIGNED** sul tipo, **gap di contenuto HIGH**.
**Cosa manca rispetto ai vincitori:**
- **Profondità:** 685 parole contro 750-1.700. Non serve allungare il testo in modo artificiale: serve aggiungere sezioni che rispondono a domande vere (vedi 5).
- **Portfolio visibile:** i concorrenti mostrano da 1 a 42 lavori, Marco 0 sulla pagina.
- **Il secondo servizio, prenotazioni online e moduli, è assente dalla pagina servizio.** Esiste solo in home, ed è un elemento di differenza che i concorrenti locali non mettono in evidenza.
- Il **legame con il territorio** c'è ("Vivo a Frascati", "il primo incontro nel tuo studio"), ed è un vantaggio reale su chi ha sede a Roma o a Velletri. Però è sepolto in "Dove lavoro", al terzo schermo.

### 2.3 "sito web per nutrizionista"

**SERP (a):** template e builder (mobirise x2, nicepage, wix, tema WordPress "Nutrition Diet"), un articolo spagnolo (neolo), un articolo scientifico. **Intento fai-da-te** forte.
**SERP (b), "sito web per nutrizionisti realizzazione biologo nutrizionista":**

| # | Risultato | Tipo |
|---|---|---|
| 1 | websanitario.it/siti-web-nutrizionisti.html | Service Page verticale: ~1.700 parole, 15 FAQ, prenotazioni (WhatsApp/Calendly), privacy/GDPR, 1 portfolio |
| 2 | webepc.it/nutrizionistavicinoame-it/ | Case study / portfolio |
| 3 | cinziagiachelle.it/project/realizzazione-sito-web-per-biologa-nutrizionista/ | Case study lungo (~2.000 parole, 9 min): obiettivi, architettura, grafico Search Console, CTA "Prenota discovery call" |
| 4 | digitalwebitalia.it/portfolio/realizzazione-siti-web-nutrizionista/ | Case study / portfolio |
| 5 | metadieta.it/blog/il-biologo-nutrizionista-online… | Blog Post (settore) |
| 6 | nutrivivacreativa.it/sito-web-nutrizionista… | Service Page verticale |
| 7 | francescozaccagnini.com/portfolio/sito-web-biologo-nutrizionista/ | Case study di un freelance |
| 8 | gutflg.com/sito-web-nutrizionista-guida-alla-realizzazione/ | Guida (Blog Post) |
| 9 | luismeta.com/siti-web-per-nutrizionisti | Service Page verticale |

**Consenso:** **case study** 4/9 (44%), **Service Page verticale** 3/9 (33%), guida 2/9 (22%). È una SERP in cui un singolo freelance con **un solo caso studio ben raccontato** può competere: lo dimostrano cinziagiachelle e francescozaccagnini.
**Pagina di Marco:** nessuna pagina mirata. Le candidate sono `/lavori/martina-iannotti-nutrizionista/`, 206 parole con H1 "Martina Iannotti, biologa nutrizionista" (non contiene "sito web per nutrizionista"), e `/blog/ai-automazione-nutrizionista/`, che risponde a un'altra domanda (AI, non sito).
**Mismatch: CRITICAL** (nessuna pagina del tipo premiato).
**Cosa manca:**
- un **caso studio esteso** sul modello di cinziagiachelle, con title/H1 tipo "Sito web per una biologa nutrizionista: il caso di Martina Iannotti". Dovrebbe raccontare obiettivi, struttura delle pagine, scelta di WordPress perché lei potesse gestirlo da sola, screenshot desktop e mobile, la testimonianza completa e "cosa farei uguale per uno studio dei Castelli";
- **temi di settore che la SERP premia** e che oggi mancano: prenotazione della prima visita, numero di iscrizione all'Albo dei biologi nella pagina "chi sono", testi che restano nei limiti della qualifica (pubblicità sanitaria), moduli con pochi dati e consenso privacy, Instagram vs sito;
- in alternativa o in aggiunta, **una sola pagina verticale "Siti web per nutrizionisti"**. Non deve essere un catalogo di "pacchetti" come quello di websanitario, ma una pagina che spiega cosa serve a uno studio di nutrizione e linka il caso reale. Vista la scelta di fare pochi lavori l'anno, **parti dal caso studio esteso**: costa meno e sfrutta una prova che i concorrenti spesso non hanno (cinziagiachelle, per esempio, non ha una testimonianza diretta della cliente).

### 2.4 "web developer frascati"

**SERP (a):** goodfirms (Frascati GmbH, un'agenzia svizzera), profilo Symfony di "Stefano Frasca", Wikipedia "Web developer", Randstad/Masterin (schede di professione), Adobe Stock, un elenco UE. **Intento informativo o da ricerca di lavoro**, con la località quasi ignorata.
**SERP (b), "web developer freelance Frascati Castelli Romani siti web":** romacomunicaweb.it (Service locale), dbnet (Product), link2me (directory), gestione-siti-web.it, **laroccadigitale.it/** (home), addlance.com (directory di freelance a Frascati), castelliromanicomputer.it (Service locale x2), avavo (Service locale), webrex2000.
**Consenso:** Service Page locale ~60%, directory/profilo ~30%. Il termine "web developer" lo cerca soprattutto chi vuole **una persona**, non un'agenzia.
**Pagina di Marco:** la home, con segnali Person forti (foto, nome, "informatico di Frascati").
**Mismatch: ALIGNED.** La home è la pagina giusta per una query su una persona.
**Cosa manca (priorità bassa, volume probabilmente minimo):** il termine "sviluppatore web" / "web developer" non compare in title, H1 o lead. Lo schema Person non è collegato ai profili esterni (`sameAs` verso LinkedIn/GitHub, se esistono) e non ha un `jobTitle` esplicito. **[PROPOSTA HOME]** valutare "informatico e sviluppatore web di Frascati" nel lead, senza cambiare il tono. Nessuna pagina nuova.

### 2.5 "sito web piccola attività prezzo"

**SERP (a):** surmado.com (x3, guide in USD), lenovo, mailchimp, seahawkmedia, reteimprese (annunci "da 499 €"), economia-italia.
**SERP (b), "quanto costa un sito web per una piccola attività prezzi 2026 sito vetrina":** inputcomm, dgtatelier, damicomarco, simonebotosso, dsidesign, cfweb, holein, pacitto.dev, matechstudio: **9/9 Blog Post "Quanto costa un sito web nel 2026"**, quasi tutti di freelance o piccole agenzie. Struttura tipica (simonebotosso): "La risposta breve" in apertura → tabella delle fasce → costi ricorrenti → come chiedere un preventivo → Fonti → FAQ (4) → link alla pagina servizio e ai lavori.
**Consenso:** Blog Post/guida 100%.
**Pagina di Marco:** `/blog/quanto-costa-sito-web/` (Blog Post, 762 parole, tabella delle fasce di mercato, sezione Fonti, "E con me quanto costa?" senza listino).
**Mismatch: ALIGNED.**
**Cosa manca:**
- **una risposta breve in apertura.** La tabella delle fasce arriva dopo dominio e hosting, mentre i vincitori mettono la cifra nelle prime righe, che è anche il formato adatto al featured snippet;
- **una FAQ in pagina con FAQPage**, su domande come "quanto costa un sito vetrina per un ristorante", "ci sono costi dopo la pubblicazione?" e "posso aggiornarlo da solo?";
- le parole **"piccola attività"** e **"sito vetrina"** nel title o in un H2. Oggi il title punta solo su "sito web 2026";
- **link alla pagina servizio e al caso studio** dalla sezione "E con me quanto costa?". Ora c'è solo `/#contacts`;
- una piccola incoerenza: l'esempio "un sito da 500 € si ripaga…" non corrisponde alla riga "Sito su misura (freelance) 800-2.500 €". Conviene allinearli, sempre come **fasce di mercato e non come prezzo di Marco**.

---

## 3. Riepilogo dei mismatch

| Query | Tipo premiato (consenso) | Pagina di Marco | Severità |
|---|---|---|---|
| sito web per nutrizionista | Case study / Service verticale (77%) | nessuna (scheda di 206 parole) | **CRITICAL** |
| siti web frascati | Service Page locale (67%) | si posiziona la home al posto della pagina servizio | **MEDIUM** (cannibalizzazione) |
| realizzazione siti web castelli romani | Service Page locale (67%) | pagina servizio, con poche prove | ALIGNED (gap di contenuto HIGH) |
| web developer frascati | Persona/Service + directory | home | ALIGNED |
| sito web piccola attività prezzo | Blog Post/guida (100%) | articolo sui costi | ALIGNED (gap di formato MEDIUM) |

---

## 4. User story (derivate dai segnali SERP)

1. **Consideration.** Come **biologa nutrizionista con uno studio ai Castelli**, voglio vedere un sito già fatto per una collega, perché temo un sito generico che non rispetti le regole della professione, ma sono bloccata da un **trust gap**: non trovo un esempio concreto del mio settore.
   *Segnali: 4/9 risultati sono case study di siti per nutrizionisti; websanitario e la sintesi SERP citano Albo, privacy e limiti della qualifica.*
2. **Awareness.** Come **professionista che pensava di usare un template**, voglio capire se un sito su misura vale la spesa rispetto a Wix o a un tema WordPress, ma sono bloccato da un **gap di informazione** (fai-da-te contro professionista).
   *Segnali: SERP (a) di "sito web per nutrizionista" dominata da mobirise, nicepage, wix e temi WordPress.*
3. **Decision.** Come **titolare di un'attività ai Castelli**, voglio qualcuno vicino che conosca la zona e che posso incontrare, perché non mi fido dei fornitori lontani, ma sono bloccato da una **comparison fatigue**: tutte le pagine dicono le stesse cose.
   *Segnali: 2 directory (prontopro) in cima, 6/9 pagine con elenco di comuni e sede nei Castelli, avavo con "oltre 100 progetti".*
4. **Consideration.** Come **piccola attività con budget limitato**, voglio una cifra indicativa prima di chiedere un preventivo, perché ho paura di costi nascosti e canoni, ma sono bloccato dalla **sensibilità al prezzo**.
   *Segnali: 9/9 guide "quanto costa"; inconnect "da 450 €", dbnet "700 € + IVA", reteimprese "499 €"; le guide mettono in evidenza i costi ricorrenti e la manutenzione.*
5. **Decision.** Come **ristoratore dei Castelli**, voglio un sito con menu, orari e prenotazione che si apra dal telefono, perché i clienti mi chiamano e scrivono su WhatsApp a tutte le ore, ma sono bloccato da un **trust gap**: non vedo lavori per ristoranti.
   *Segnali: romacomunicaweb e la guida dgtatelier citano esplicitamente "ristoranti, negozi e studi"; nelle SERP locali non compare nessun case study di ristorazione nei Castelli (spazio libero); nella sintesi dei prezzi c'è "sito vetrina da 500-700 euro per ristoranti".*

---

## 5. SXO Gap Score: `/siti-web-frascati-castelli-romani/`

| Dimensione | Punti | Evidenza |
|---|---|---|
| Page Type | 11/15 | È una Service Page come quelle premiate, ma Google posiziona la home al suo posto |
| Content Depth | 9/15 | 685 parole contro 750-1.700; mancano sezioni per settore e prenotazioni/moduli, il secondo servizio |
| UX Signals | 10/15 | H2 chiari e liste leggibili; nessun modulo in pagina, le 2 CTA portano a `/#contacts`; la frase sul legame con il territorio arriva al terzo schermo |
| Schema | 6/15 | Online solo Breadcrumb + FAQ con stringhe con virgolette doppie, senza Service. Il sorgente è già corretto: dopo il deploy circa 11/15 |
| Media | 3/15 | Una sola immagine (avatar, alt vuoto); nessuno screenshot di lavori |
| Authority | 6/15 | Esiste una testimonianza vera ma non è su questa pagina; un solo caso pubblicato; nessuna recensione esterna |
| Freshness | 7/10 | `lastmod` 07/10/2026, ma nessuna data visibile (htmldate legge 01/01/2026) |
| **Totale** | **52/100** | |

---

## 6. Personas e punteggi

Le personas richieste sono 3. La regola del framework ne prevede almeno 4: ho scelto di seguire la richiesta.

**A. Professionista sanitario locale** (nutrizionista, psicologa, osteopata ai Castelli)
- Obiettivo: un sito credibile, che rispetti le regole della professione e magari permetta di prenotare la prima visita.
- Stato emotivo: valuta con attenzione ed è scettica verso i template.
- Fase: Consideration → Decision.
- Pagina d'ingresso probabile: pagina servizio o caso studio.
- Segnali SERP: 2.3 (case study, verticali, Albo/privacy).

**B. Ristoratore dei Castelli** (osteria/trattoria a Frascati o Marino)
- Obiettivo: menu, orari, chiamata e indicazioni dal telefono, meno telefonate per le prenotazioni.
- Stato emotivo: poco tempo, poca pazienza per i tecnicismi.
- Fase: Decision.
- Pagina d'ingresso probabile: home o pagina servizio.
- Segnali SERP: 2.1/2.2 (Service locali che citano "ristoranti"), 2.5 ("sito vetrina per ristoranti 500-700 €").

**C. Titolare di piccola attività attento al prezzo**
- Obiettivo: capire quanto spendere e cosa evitare.
- Stato emotivo: sensibile al prezzo, teme canoni e costi nascosti.
- Fase: Awareness → Consideration.
- Pagina d'ingresso: `/blog/quanto-costa-sito-web/`.
- Segnali SERP: 2.5 (9/9 guide ai prezzi).

| Persona | Pagina valutata | Relevance | Clarity | Trust | Action | Totale | Giudizio |
|---|---|---|---|---|---|---|---|
| B. Ristoratore dei Castelli | home + pagina servizio | 10/25 | 13/25 | 9/25 | 15/25 | **47/100** | Needs Work |
| A. Professionista sanitario | pagina servizio + caso studio | 13/25 | 15/25 | 14/25 | 16/25 | **58/100** | Needs Work |
| C. Titolare attento al prezzo | articolo sui costi | 21/25 | 17/25 | 17/25 | 14/25 | **69/100** | Good |

### Persona più debole: B. Ristoratore dei Castelli (47/100)

**Evidenze:**
- Relevance 10: la ristorazione appare solo come esempio ("ristorante Marino") e in "A chi è rivolto". Né la pagina servizio né la home parlano di menu, orari o prenotazione dei tavoli, anche se il servizio "Prenotazioni e moduli" esiste.
- Clarity 13: nel primo schermo della home c'è il widget a terminale in inglese (`--status ✓ Available`).
- Trust 9: l'unica prova è una nutrizionista di Pescara; Osteria Gemelli è in bozza e aspetta il consenso del cliente.
- Action 15: c'è solo un modulo email, mentre questa persona di solito preferisce essere richiamata.

**Interventi concreti (in ordine):**
1. **Pubblicare il caso Osteria Gemelli** (`content/lavori/osteria-gemelli.md`, `draft: true`) appena il cliente dà il consenso e il sito è online. È l'unica prova possibile per questa persona e **non va sostituita con esempi inventati**.
2. Nella pagina servizio, aggiungere un H2 **"Per ristoranti e osterie: menu, orari e prenotazioni dal telefono"**: 3-4 punti, link a `/blog/sito-web-ristorante-cosa-deve-avere/` e, quando sarà pubblicato, a `/lavori/osteria-gemelli/`.
3. Nel modulo, un campo **facoltativo "Telefono, se preferisci che ti richiami"**. Rispetta il vincolo di non pubblicare il telefono e abbassa l'attrito per chi non scrive email.
4. **[PROPOSTA HOME]** sostituire o nascondere sul mobile il widget `$ marco --status` con una riga in italiano chiaro (es. "Disponibile per nuovi lavori"), oppure toglierlo. Va chiesto prima a Marco.

### A. Professionista sanitario (58/100)

**Evidenze:** la testimonianza vera di una nutrizionista è il segnale di fiducia più forte del sito, ma è in home e nella scheda di 206 parole, non nella pagina servizio. La pagina servizio non parla di Albo, prenotazione della prima visita o dati sanitari, temi che invece la home cita ("Strumenti scelti con attenzione a privacy e dati sanitari").

**Interventi concreti:**
1. **Estendere `/lavori/martina-iannotti-nutrizionista/`** a 800-1.200 parole come caso studio, con queste sezioni:
   - "Da dove partiva Martina"
   - "Le pagine che abbiamo scelto e perché"
   - "Perché WordPress: per aggiornarlo da sola"
   - "Ricerca locale: cosa abbiamo fatto"
   - "Cosa farei uguale per uno studio dei Castelli"

   Aggiungere 2-3 screenshot (desktop + mobile) con alt descrittivi, la testimonianza completa e una CTA in fondo "Hai uno studio di nutrizione? Raccontami com'è organizzato". Title suggerito: "Sito web per una biologa nutrizionista: il caso di Martina Iannotti — Marco La Rocca". **Non vanno inventati risultati numerici:** si usa Search Console di Martina solo se lei lo autorizza.
2. Nella pagina servizio, un riquadro **"Un lavoro realizzato"** con screenshot e citazione breve di Martina, sopra "Dove lavoro".
3. Nella pagina servizio, un H2 **"Per studi di nutrizionisti, psicologi e osteopati"** con: prenotazione della prima visita collegata al calendario, moduli pre-visita con pochi dati, Albo e qualifica nella pagina "chi sono", testi che restano nei limiti della pubblicità sanitaria. Con link al caso studio e a `/blog/ai-chatbot-dati-pazienti-gdpr/`.
4. Valutare in seguito una pagina verticale `/siti-web-nutrizionisti/`, solo se il caso studio esteso non basta. Nessun "pacchetto".

### C. Titolare attento al prezzo (69/100)

**Interventi concreti** su `/blog/quanto-costa-sito-web/`:
1. Un paragrafo **"In breve"** sotto l'H1 con le fasce di mercato in una riga. Sono generiche e ammesse; nessun prezzo di Marco.
2. Una FAQ di 3-4 domande (front matter `faq:`, che genera FAQPage dal template esistente).
3. In "E con me quanto costa?" aggiungere un link alla pagina servizio e al caso studio: "Guarda come ho lavorato per Martina".
4. Title: valutare "Quanto costa un sito web per una piccola attività nel 2026: guida ai prezzi reali".

### Problemi comuni a tutte le personas
- **Trust:** l'unica prova vera (Martina) è sfruttata poco fuori dalla home. È la leva che costa meno.
- **Action:** tutte le CTA fuori dalla home portano a `/#contacts`. Inserire il partial `contact-form.html` anche in fondo alla pagina servizio e al caso studio elimina un cambio di pagina, per le persone in fase Decision.

---

## 7. Piano d'azione ordinato (solo pagine diverse dalla home, salvo dove indicato)

| # | Azione | File | Persona / query | Impatto |
|---|---|---|---|---|
| 1 | Deploy del template schema corretto (Service sulla pagina servizio, niente virgolette doppie, CollectionPage su /lavori/) | `layouts/partials/shared/schema.html` (già modificato, da committare e pubblicare) | tutte | Alto, sforzo minimo |
| 2 | Estendere il caso studio di Martina (800-1.200 parole, screenshot, CTA, modulo) | `content/lavori/martina-iannotti-nutrizionista.md` | A / "sito web per nutrizionista" (CRITICAL) | Alto |
| 3 | Nella pagina servizio: riquadro "Un lavoro realizzato", H2 settori (salute, ristorazione), H2 "Prenotazioni e moduli", modulo in pagina | `content/siti-web-frascati-castelli-romani.md` + layout | A, B / query geografiche | Alto |
| 4 | Ridurre la cannibalizzazione: link contestuale dalla home alla pagina servizio con ancora "realizzazione siti web a Frascati e Castelli Romani" **[PROPOSTA HOME]**; link dagli articoli del blog verso la pagina servizio con ancore varie | blog + proposta home | "siti web frascati" | Medio |
| 5 | Articolo sui costi: "In breve", FAQ, link al servizio e al caso, title | `content/blog/quanto-costa-sito-web.md` | C | Medio |
| 6 | Pubblicare Osteria Gemelli quando il cliente acconsente | `content/lavori/osteria-gemelli.md` | B | Alto (dipende dal cliente) |
| 7 | Campo telefono facoltativo nel modulo | `layouts/partials/contact-form.html` | B | Medio |
| 8 | Alt dell'avatar nella pagina servizio ("Marco La Rocca, informatico di Frascati") dove non è decorativo; meta description dedicata a `/blog/` | layout / `content/blog/_index.md` | tutte | Basso |
| 9 | **[PROPOSTA HOME]** widget a terminale; "sviluppatore web" nel lead; H1 con lo spazio tra nome e titolo | `layouts/index.html`, `content/_index.md` | B, "web developer frascati" | Basso-medio |

**Rimandi ad altri skill:**
- `/seo schema` per verificare il deploy di Service/CollectionPage e le virgolette doppie;
- `/seo page` sul caso studio dopo l'estensione;
- `/seo content` per gli E-E-A-T sanitari (Albo, limiti della pubblicità sanitaria);
- `/seo local`: utilità limitata, perché senza una sede non è opportuna una scheda Google Business per Marco. Il lato locale passa da pagina servizio, comuni e link.

---

## 8. Limiti dell'analisi

- **Non ho una SERP google.it reale.** WebSearch è basato negli USA: niente local pack, PAA, annunci, AI Overview o related searches. Le personas e le user story si basano su titoli, tipi di pagina e sintesi dei risultati, non sui PAA.
- La SERP è **non personalizzata e non geolocalizzata**: chi cerca da Frascati vedrà probabilmente il local pack in alto, con aziende che hanno la scheda Google Business, una posizione a cui Marco senza sede non può ambire.
- **Volumi di ricerca non disponibili** (nessun accesso a Keyword Planner/DataForSEO): i pesi delle personas sono qualitativi. "web developer frascati" ha probabilmente un volume trascurabile.
- **Posizioni non misurate:** la presenza della home nelle SERP (b) è un indizio, non una posizione. Per conferma servono le query/pagine di Search Console (`/seo google`).
- Delle pagine dei concorrenti ho aperto solo avavo, websanitario, cinziagiachelle e simonebotosso. antonellileonardo.com non risolveva il DNS (ENOTFOUND); gli altri li ho classificati da title, URL e sintesi.
- Non ho dati di comportamento: secondo l'audit del 07/10, Clarity potrebbe non registrare per via della CSP. Non ho verificato in questa sessione.
- La build di controllo del working tree l'ho fatta in una cartella temporanea, senza modificare file del progetto.

**Report PDF?** Usa `/seo google report`.

---

## 9. Dati strutturati per `audit-data.json` (categoria Search Experience)

```json
{
  "category": "Search Experience",
  "sxo_gap_score": {"url": "https://laroccadigitale.it/siti-web-frascati-castelli-romani/", "score": 52, "max": 100,
    "dimensions": {"page_type": 11, "content_depth": 9, "ux_signals": 10, "schema": 6, "media": 3, "authority": 6, "freshness": 7}},
  "findings": [
    {"id": "sxo-01", "severity": "critical", "query": "sito web per nutrizionista", "serp_dominant_type": "Case study / Service verticale", "consensus": 0.77, "target": "/lavori/martina-iannotti-nutrizionista/ (206 parole)", "fix": "Estendere il caso studio a 800-1200 parole con screenshot, testimonianza, CTA e modulo"},
    {"id": "sxo-02", "severity": "medium", "query": "siti web frascati", "serp_dominant_type": "Service Page locale", "consensus": 0.67, "target": "home posizionata al posto della pagina servizio", "fix": "Link interni contestuali verso /siti-web-frascati-castelli-romani/ (home solo come proposta)"},
    {"id": "sxo-03", "severity": "high", "query": "realizzazione siti web castelli romani", "serp_dominant_type": "Service Page locale", "consensus": 0.67, "target": "/siti-web-frascati-castelli-romani/ (685 parole, 0 prove)", "fix": "Riquadro lavoro realizzato, H2 per settori e prenotazioni, modulo in pagina"},
    {"id": "sxo-04", "severity": "high", "query": "tutte", "issue": "JSON-LD online non allineato al sorgente: stringhe con virgolette doppie, Service assente, /lavori/ senza schema", "fix": "Commit e deploy di layouts/partials/shared/schema.html"},
    {"id": "sxo-05", "severity": "medium", "query": "sito web piccola attività prezzo", "serp_dominant_type": "Blog Post", "consensus": 1.0, "target": "/blog/quanto-costa-sito-web/", "fix": "Risposta breve in apertura, FAQ, link al servizio e al caso, title con 'piccola attività'"},
    {"id": "sxo-06", "severity": "low", "query": "web developer frascati", "serp_dominant_type": "Persona/Service + directory", "target": "home (allineata)", "fix": "Proposta: 'sviluppatore web' nel lead, sameAs/jobTitle nello schema Person"}
  ],
  "personas": [
    {"name": "Ristoratore dei Castelli", "relevance": 10, "clarity": 13, "trust": 9, "action": 15, "total": 47},
    {"name": "Professionista sanitario locale", "relevance": 13, "clarity": 15, "trust": 14, "action": 16, "total": 58},
    {"name": "Titolare attento al prezzo", "relevance": 21, "clarity": 17, "trust": 17, "action": 14, "total": 69}
  ]
}
```

---

## Fonti SERP

- [prontopro.it, progettisti siti web Frascati](https://prontopro.it/frascati-progettazione-siti-web)
- [prontopro.it, programmatori siti web Frascati](https://prontopro.it/frascati-programmazione-siti-web)
- [avavo.it, realizzazione siti web Frascati](https://www.avavo.it/realizzazione-siti-web-frascati/)
- [avavo.it, realizzazione siti web Castelli Romani](https://www.avavo.it/realizzazione-siti-web-castelli-romani/)
- [sitisrl.it, web agency Frascati](https://www.sitisrl.it/web-agency-frascati)
- [antonellileonardo.com](https://antonellileonardo.com/realizzazione-siti-web-frascati/)
- [suitedesignstudio.com](https://www.suitedesignstudio.com/realizzazione-siti-web-frascati/)
- [inconnect.it, Frascati](https://inconnect.it/agenzia-web-realizzazione-siti-web-frascati/)
- [inconnect.it, Castelli Romani](https://inconnect.it/agenzia-web-realizzazione-siti-web-castelli-romani/)
- [adarte.pro](https://www.adarte.pro/realizzazione-siti-web-frascati.html)
- [dbnet.it](https://www.dbnet.it/shop/realizzazione-siti-web/realizzazione-sito-web-castelli-romani/)
- [gestione-siti-web.it](https://www.gestione-siti-web.it/internet-web-designer-castelli-roma-albano)
- [superyapp.it](https://www.superyapp.it/)
- [tfagency.it](https://tfagency.it/agenzia-marketing/castelli-romani)
- [webrex2000.com](https://www.webrex2000.com/realizzazione-siti-web-albano-laziale.html)
- [eccolomarketing.it](https://www.eccolomarketing.it/realizzazione-siti-web-roma/)
- [gbnet.it](https://www.gbnet.it/siti-web/)
- [romacomunicaweb.it](https://romacomunicaweb.it/realizzazione-siti-web-frascati/)
- [castelliromanicomputer.it](https://www.castelliromanicomputer.it/realizzazione-siti-web-frascati/)
- [addlance.com](https://www.addlance.com/programmatore-web-e-mobile/rm/frascati)
- [websanitario.it](https://www.websanitario.it/siti-web-nutrizionisti.html)
- [webepc.it](https://www.webepc.it/nutrizionistavicinoame-it/)
- [cinziagiachelle.it](https://cinziagiachelle.it/project/realizzazione-sito-web-per-biologa-nutrizionista/)
- [digitalwebitalia.it](https://www.digitalwebitalia.it/portfolio/realizzazione-siti-web-nutrizionista/)
- [metadieta.it](https://www.metadieta.it/blog/il-biologo-nutrizionista-online-tra-opportunita-professionali-sfide-e-pericoli/)
- [nutrivivacreativa.it](https://nutrivivacreativa.it/sito-web-nutrizionista-nutrivivacreativa/)
- [francescozaccagnini.com](https://francescozaccagnini.com/portfolio/sito-web-biologo-nutrizionista/)
- [gutflg.com](https://gutflg.com/sito-web-nutrizionista-guida-alla-realizzazione/)
- [luismeta.com](https://luismeta.com/siti-web-per-nutrizionisti)
- [mobirise.com, template nutrizionisti](https://mobirise.com/website-templates/it/nutritionist-website-templates/)
- [goodfirms.co, Frascati GmbH](https://www.goodfirms.co/company/frascati-gmbh)
- [randstad.it, web developer](https://www.randstad.it/candidato/lavori-piu-richiesti/web-developer/)
- [inputcomm.it](https://www.inputcomm.it/quanto-costa-un-sito-web/)
- [dgtatelier.it](https://www.dgtatelier.it/blog/costo-sito-web-2026-guida-prezzi)
- [damicomarco.it](https://www.damicomarco.it/quanto-costa-un-sito-web/)
- [simonebotosso.it](https://simonebotosso.it/blog/quanto-costa-sito-web/)
- [cfweb.it](https://www.cfweb.it/quanto-costa-davvero-un-sito-web-guida-prezzi-2026/)
- [holein.it](https://www.holein.it/risorse/costo-sito-web-aziendale-2026/)
- [pacitto.dev](https://pacitto.dev/blog/quanto-costa-sito-web-2026)
- [matechstudio.com](https://matechstudio.com/blog/sito-web-quanto-costa)
- [surmado.com](https://www.surmado.com/it/blog/how-much-does-a-small-business-website-cost-2026)
- [reteimprese.it](https://www.reteimprese.it/ann_A55246B6574)
