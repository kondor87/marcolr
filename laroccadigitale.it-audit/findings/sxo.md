# SXO — Search Experience Analysis: laroccadigitale.it

**Data analisi:** 07/10/2026
**URL analizzato:** https://laroccadigitale.it/ (+ /blog/siti-web-castelli-romani/, /blog/quanto-costa-sito-web/)
**Rendering:** `render_page.py --mode always` (Playwright, status 200, non-SPA) + `parse_html.py`
**Vincolo di posizionamento:** Marco lavora da solo, in **collaborazione occasionale** (senza Partita IVA). Niente "agenzia", niente pacchetti, niente abbonamenti. Tutte le raccomandazioni rispettano questo vincolo.

> Questo è uno **SXO Gap Score**, separato dall'SEO Health Score.

---

## 0. Il risultato principale (in breve)

**Mismatch di tipo pagina: CRITICAL su "realizzazione siti web Castelli Romani" e "sito per nutrizionista", HIGH su "siti web Frascati".**

Per le query commerciali locali, Google mostra quasi solo **pagine servizio locali dedicate** con lo slug `/realizzazione-siti-web-[città]/`: in 9 risultati su 9 della query raffinata "realizzazione siti web Frascati" e in 7 su 9 per "Castelli Romani".
laroccadigitale.it risponde invece con:
- una **homepage monopagina generica**, che deve coprire contemporaneamente Frascati, Castelli Romani, nutrizionisti, AI e automazione;
- un **articolo del blog** (`/blog/siti-web-castelli-romani/`, 637 parole) usato come landing geografica. Per la tassonomia, un "Blog Post targeting [service] in [city]" è un mismatch **CRITICAL**.

Per "sito per nutrizionista" il sito **non ha nessuna pagina** con quell'intento. Esiste solo "AI per Nutrizionisti", che risponde a un'altra domanda, anche se l'unico caso studio pubblicato è proprio di una nutrizionista.

**SXO Gap Score complessivo (cluster commerciale): 51/100.**

---

## 1. Pagina target: cosa c'è oggi

| Elemento | Valore rilevato |
|---|---|
| Title | "Siti Web Frascati e Castelli Romani — Marco La Rocca" |
| H1 | "Marco La Rocca — Siti Web per Professionisti a Frascati e Castelli Romani" |
| Meta description | "Realizzo siti web per professionisti e attività locali a Frascati e nei Castelli Romani. Design curato, SEO locale, prezzi onesti. Scrivimi senza impegno." |
| H2 | **0**: le sezioni usano etichette stilistiche ("// cosa posso fare per te", "// lavori recenti", "// domande frequenti") che non sono heading |
| Parole | ~963 (testo estratto principale ~3.400 caratteri) |
| Schema | ProfessionalService, Person, WebSite, Service, OfferCatalog/Offer, PostalAddress, City, GeoCoordinates. Mancano FAQPage (la FAQ c'è in pagina) e BreadcrumbList |
| Immagini | 8 |
| Link interni | 9, quasi tutti ancore (#servizi, #contacts) + 6 articoli del blog |
| CTA | "Scrivimi" / "Scrivimi, senza impegno" che portano tutte a #contacts. È l'unica azione disponibile |
| Portfolio | 1 lavoro (Martina Iannotti, nutrizionista, **Pescara**), con link esterno e 1 testimonianza |
| Sezioni | Hero, Servizi (Siti vetrina + AI e automazione), Processo in 3 step, A chi è rivolto, Lavori recenti, Blog, Chi sono, Perché lavorare con me, FAQ, Strumenti, Contatti |
| Pagine indicizzabili | Homepage, /blog/ (14 articoli), /archivio/. **Non esistono** pagine servizio, città, settore o portfolio |

**Classificazione (tassonomia):** la homepage è una **Landing Page / Service Page ibrida** (hero con proposta di valore, CTA unica, processo, testimonianza, schema ProfessionalService). Non ha indirizzo né mappa, quindi non è una Local Page. Gli articoli `/blog/siti-web-castelli-romani/` e `/blog/quanto-costa-sito-web/` sono **Blog Post**.

**Osservazione tecnica utile all'analisi UX:** nel DOM renderizzato la CSP blocca `https://scripts.clarity.ms/0.8.70/clarity.js` (è consentito solo `www.clarity.ms`) e il CSS del badge iubenda. **Microsoft Clarity probabilmente non registra sessioni**: le heatmap e le registrazioni, che servirebbero per validare questa analisi SXO, oggi non arrivano. Da segnalare a chi si occupa degli header in `netlify.toml`.

---

## 2. Analisi SERP query per query (SERP-backwards)

> Nota di metodo: lo strumento di ricerca disponibile è basato negli USA e non restituisce local pack, PAA, annunci né AI Overview di google.it. Per le query brevi ("siti web Frascati", "web designer Frascati") i primi risultati erano rumore informativo (Wikipedia, turismo). Ho quindi ripetuto ogni query con varianti più esplicite ("realizzazione siti web Frascati agenzia web", "web designer freelance Frascati") per ricostruire la SERP commerciale realistica. Vedi la sezione Limiti.

### 2.1 "siti web Frascati" / "realizzazione siti web Frascati"

| # | Risultato | Tipo pagina |
|---|---|---|
| 1 | sitisrl.it/web-agency-frascati | Service Page locale (agenzia, sede fuori zona) |
| 2 | avavo.it/realizzazione-siti-web-frascati/ | Service Page locale (freelance/brand personale "by Alessio Basili") |
| 3 | inconnect.it/agenzia-web-realizzazione-siti-web-frascati/ | Service Page locale, prezzo esplicito "da 450€", "in 2 giorni" |
| 4 | digitalwebitalia.it/realizzazione-siti-web-frascati/ | Service Page locale (sede a Valmontone) |
| 5 | adarte.pro/realizzazione-siti-web-frascati.html | Service Page locale |
| 6 | adarte.pro/agenzia-web-frascati.html | Service Page locale (seconda pagina dello stesso dominio) |
| 7 | suitedesignstudio.com/realizzazione-siti-web-frascati/ | Service Page locale |
| 8 | lumiaweb.com/realizzazione-siti-web-frascati-... | Service Page locale |
| 9 | clion.it/lazio/roma/frascati/realizzazione_siti_web_frascati/... | Service Page locale programmatica (network nazionale) |
| + | castelliromanicomputer.it/realizzazione-siti-web-frascati/ · paginegialle.it/lazio/frascati/creazione_di_siti_web.html | Service Page locale · Directory |

**Consenso SERP:** Service Page locale dedicata (`/realizzazione-siti-web-frascati/`), **9/9 = ~100%**. Molte sono pagine "città" di agenzie che **non hanno sede a Frascati**: il vantaggio reale di Marco ("sono di Frascati") qui è un differenziatore non sfruttato.
**Segnali ricorrenti:** prezzo d'ingresso esplicito (InConnect "da 450€"), velocità ("in 2 giorni"), anzianità ("da oltre 10 anni", "fondata nel 2006", "1500 clienti").
**Sito oggi:** homepage generica con "Frascati" in title e H1.
**Mismatch:** **HIGH.** Il tipo pagina è vicino (servizio), ma manca una pagina dedicata a Frascati e la homepage diluisce il tema con AI, automazione e Castelli Romani.

### 2.2 "realizzazione siti web Castelli Romani"

| # | Risultato | Tipo |
|---|---|---|
| 1 | dbnet.it/shop/realizzazione-siti-web/realizzazione-sito-web-castelli-romani/ | Service/Product (scheda "shop") |
| 2 | gestione-siti-web.it (Web2000) | Homepage servizio + assistenza |
| 3 | avavo.it/realizzazione-siti-web-castelli-romani/ | Service Page locale |
| 4 | inconnect.it/agenzia-web-realizzazione-siti-web-castelli-romani/ | Service Page locale |
| 5 | eccolomarketing.it/realizzazione-siti-web-roma/ | Service Page locale (Roma) |
| 6 | gbnet.it/siti-web/ (Genzano) | Service Page |
| 7 | webrex2000.com | Homepage servizio |
| 8 | studioinweb.com | Homepage servizio |
| 9 | gianlucagentile.com/realizzazione-siti-web-albano-laziale | Service Page locale (freelance, comune specifico) |
| + | tfagency.it/agenzia-marketing/castelli-romani · webrex2000.com/realizzazione-siti-web-albano-laziale.html · prontopro.it/grottaferrata-web-designer | Service locale · Service locale per comune · Directory |

**Consenso:** Service Page locale **7/9 (~78%)**, Homepage servizio 2/9. **Nessun articolo di blog** in top 9.
**Sito oggi:** `/blog/siti-web-castelli-romani/`, un Blog Post di 637 parole con breadcrumb /blog/, data, categoria "SEO Locale" e tono da guida ("Come farsi trovare").
**Mismatch:** **CRITICAL** (Blog Post su query "[servizio] + [zona]").

### 2.3 "web designer Frascati"

| Risultato | Tipo |
|---|---|
| paginegialle.it/lazio/frascati/creazione_di_siti_web.html (37 risultati) | Directory |
| prontopro.it/grottaferrata-web-designer ("I 40 migliori Web Designer a Grottaferrata") | Directory/marketplace con recensioni |
| addlance.com/web-designer/rm/roma | Directory freelance |
| cbinsights.com/company/mitdesign (studio con sede a Frascati) | Profilo azienda |
| unirufa.it (Emanuele Frascà), webflow.com/@..., framer.com/... | Rumore omonimia / profili personali |
| marcopanichi.com/servizi/web-design-freelance/, valentinaolini.com, cri-art.it/web-designer-freelance/, lawebstrategist.it | Service Page di freelance (brand personale, senza città) |

**Consenso:** SERP **mista e debole**: directory ~40%, siti personali di freelance ~35%, rumore ~25%. Nessun formato domina.
**Lettura:** chi cerca "web designer" cerca **una persona** e un volto, e confronta profili con recensioni.
**Sito oggi:** homepage personale (nome nel title, "Non sono un'agenzia", foto e chi sono). Il tipo è **allineato**, ma il termine "web designer" non compare né nel title né nell'H1, e mancano recensioni verificabili.
**Mismatch:** **MEDIUM.** Opportunità reale: la SERP è poco presidiata e premia brand personali e directory.

### 2.4 "sito per nutrizionista" / "sito web nutrizionista"

| Risultato | Tipo |
|---|---|
| nutrivivacreativa.it/sito-web-nutrizionista-... | Service Page verticale (offerta per settore) |
| nutrivivacreativa.it/sito-web-per-nutrizionista-cosa-deve-avere-... | Guida blog verticale |
| websanitario.it/siti-web-nutrizionisti.html | Service Page verticale |
| sitiinternet.pro/siti-per-studi-medici/siti-per-nutrizionisti/ | Service Page verticale |
| luismeta.com/siti-web-per-nutrizionisti | Service Page verticale (abbonamento 49€/mese) |
| webepc.it/nutrizionistavicinoame-it/ | Caso studio / portfolio di settore |
| digitalwebitalia.it/siti-web-per-nutrizionisti-... | Ibrido (guida + servizio) |
| waas.it/sito-web-per-nutrizionisti/ · gutflg.com/sito-web-nutrizionista-guida-... | Ibrido / guida |
| it.squarespace.com/blog/crea-un-sito-web-per-il-settore-nutrizione · framework360.com · bowwe.com · mobirise.com (template) | Guide e template di piattaforme |
| sitiweba100euro.it/creazione-siti-web-per-nutrizionista | Service Page low-cost |

**Consenso:** **Hybrid (servizio verticale + contenuto)**, circa 60% service/hybrid verticali e 40% guide "cosa deve avere". Segnali: elenchi di pagine indispensabili (chi sono, servizi, metodo, FAQ, prenotazione), CTA "Prenota", prezzi espliciti (297€, 299€, 49€/mese), esempi reali.
**Sito oggi:** **nessuna pagina** su questo intento. Esistono "AI per Nutrizionisti" (intento diverso: automazione) e il caso studio Martina Iannotti, che però sta solo in una card della homepage con link esterno.
**Mismatch:** **CRITICAL (pagina assente).** È la query dove Marco ha la **prova più forte** (caso reale e testimonianza) e la **visibilità più bassa**.

### 2.5 "quanto costa un sito web"

| Risultato | Tipo |
|---|---|
| shopify.com/it/blog/quanto-costa-un-sito-web | Blog Post (piattaforma) |
| hostinger.com/it/tutorial/quanto-costa-un-sito-web | Blog Post (hosting) |
| wpforms.com/it/..., elementor.com/blog/it/..., supporthost.com/it/costo-sito-web/, html.it/guide/... | Blog Post / guide |
| seahawkmedia.com/it/... (x2), ekeria.com/it/blog/... | Blog Post |
| damicomarco.it, dgtatelier.it, cfweb.it, pacitto.dev, onionlabs.it, fabioangelici.com, argentodev.com, matechstudio.com, catonebros.it | **Blog Post di freelance e piccoli studi, quasi tutti con "2026" nel title** |

**Consenso:** **Blog Post / guida, ~100%.** Il segmento "piccola attività" è dominato da **freelance italiani** con title datati ("Quanto costa un sito web nel 2026? Prezzi reali...") e fasce di prezzo per tipologia (vetrina 1.200-3.000€; freelance 1.200-3.500€ contro agenzia 5.000-15.000€; dominio e hosting 100-300€/anno).
**Sito oggi:** `/blog/quanto-costa-sito-web/`, "Quanto Costa un Sito Web? Guida ai Prezzi Reali", 707 parole, 24/03/2026, con tabelle di costo. **Tipo allineato.**
**Mismatch:** **ALIGNED**, con gap di profondità (707 parole contro guide molto più estese), freschezza (manca "2026" nel title) e collegamento interno: l'articolo **non è linkato dalla homepage**, che mostra solo gli ultimi 6 post. In più non spiega mai "quanto costa *con me*".

### Riepilogo mismatch

| Query | Tipo dominante SERP | Confidenza | Pagina attuale | Severità |
|---|---|---|---|---|
| realizzazione siti web Castelli Romani | Service Page locale | ~78% | Blog Post | **CRITICAL** |
| sito per nutrizionista | Hybrid servizio verticale | ~60% | Nessuna | **CRITICAL** |
| siti web Frascati | Service Page locale dedicata | ~100% | Homepage generica | **HIGH** |
| web designer Frascati | Directory + siti personali | ~40% (debole) | Homepage personale | **MEDIUM** |
| quanto costa un sito web | Blog Post / guida | ~100% | Blog Post | **ALIGNED** (gap di profondità) |

---

## 3. User story (derivate dai segnali SERP)

1. **Consapevolezza.** Come *professionista dei Castelli Romani che non ha mai fatto un sito*, voglio capire quanto spenderò davvero, perché temo di essere spennato, ma mi blocca la **sensibilità al prezzo**: ogni guida dà fasce diverse (da 100€ a 15.000€).
   *Segnale: 18 risultati "quanto costa" con fasce divergenti e "2026" nel title; offerte low-cost "siti web a 100 euro", "297€ in 3 rate", "da 450€".*

2. **Considerazione.** Come *nutrizionista che apre lo studio*, voglio vedere un sito di una collega e sapere quali pagine mi servono, perché devo sembrare credibile in ambito sanitario, ma mi blocca il **gap informativo**: non so cosa deve contenere e non voglio un abbonamento mensile.
   *Segnale: guide "cosa deve avere" (nutrivivacreativa, squarespace, gutflg), offerte in abbonamento (luismeta 49€/mese), caso portfolio webepc "nutrizionistavicinoame".*

3. **Considerazione.** Come *titolare di un'attività a Frascati*, voglio qualcuno della zona che possa incontrarmi, perché non mi fido di un'agenzia lontana, ma mi blocca un **gap di fiducia**: tutte le pagine "Frascati" sembrano uguali e non capisco chi è davvero del posto.
   *Segnale: 9/9 pagine `/realizzazione-siti-web-frascati/` di agenzie con sede a Valmontone, Velletri, in Brianza (sitisrl) o con network nazionale (Clion).*

4. **Decisione.** Come *chi cerca "web designer Frascati"*, voglio confrontare profili con recensioni e lavori, perché scelgo una persona e non un'azienda, ma mi blocca la **fatica da confronto**: le directory elencano "i 40 migliori" senza differenze chiare.
   *Segnale: ProntoPro "I 40 migliori Web Designer a Grottaferrata", PagineGialle "37 risultati", Addlance "724 a Roma".*

5. **Decisione.** Come *ristoratore di Marino con un sito vecchio o solo Facebook*, voglio un sito veloce da aggiornare (menu, orari), perché ho poco tempo, ma mi blocca la **pressione del tempo** e il timore di dipendere da altri per ogni modifica.
   *Segnale: promesse "in 2 giorni" (InConnect), offerte "assistenza, gestione siti internet" (Web2000), TF Agency che cita esplicitamente Marino, Albano e Ariccia.*

---

## 4. Gap analysis — SXO Gap Score

| Dimensione | Punteggio | Evidenza |
|---|---|---|
| Page Type | **6/15** | Le query locali vogliono Service Page dedicate. Il sito ha 1 homepage + 1 blog post come landing. Nessuna pagina per città o settore. |
| Content Depth | **6/15** | Homepage ~963 parole divise tra 2 servizi e 11 sezioni. Il post Castelli Romani ha 637 parole, senza esempi locali concreti, senza FAQ di zona e senza prezzi. Contiene un'affermazione non verificabile ("Dai dati che analizzo costantemente per i miei clienti"), rischiosa per l'E-E-A-T con un solo cliente pubblico. |
| UX Signals | **10/15** | Punti forti: hero chiaro, processo in 3 step, tono semplice, CTA ripetuta. Punti deboli: 0 H2 reali (le etichette "// ..." non danno struttura né a utenti né a Google), un'unica azione possibile (#contacts), nessuna navigazione verso approfondimenti di servizio. |
| Schema | **9/15** | ProfessionalService, Person, Service e OfferCatalog sono presenti e validi. Mancano FAQPage (FAQ già presente) e BreadcrumbList. Non c'è schema per caso studio/CreativeWork, perché la pagina non esiste. |
| Media | **7/15** | 8 immagini. Il caso studio non ha screenshot prima/dopo né mockup desktop/mobile in pagina: solo una card con link esterno. |
| Authority | **5/15** | 1 sola testimonianza, di una cliente di **Pescara** (non locale). Nessuna recensione Google o directory. Un solo lavoro pubblicato. I competitor esibiscono "10 anni", "1500 clienti". |
| Freshness | **8/10** | Blog attivo (ultimo post 27/07/2026). La guida costi è del 24/03/2026 senza anno nel title. |
| **Totale** | **51/100** | **Needs Work.** Il collo di bottiglia è l'architettura delle pagine, non la qualità del design. |

---

## 5. Persona scoring

### Persona card (sintesi)

- **P1 — Nutrizionista di Frascati** (libera professionista, apre o rinnova lo studio). Fase: considerazione. Domande: "Che pagine mi servono?", "Hai già fatto siti per nutrizionisti?", "C'è un canone?". *Evidenza: SERP 2.4.*
- **P2 — Ristoratore di Marino** (trattoria o osteria, oggi solo Facebook o un sito vecchio). Fase: decisione/considerazione. Domande: "Posso cambiare il menu da solo?", "Quanto ci vuole?", "Hai fatto siti per ristoranti?". *Evidenza: SERP 2.2 (TF Agency, Marino), promesse "in 2 giorni".*
- **P3 — Professionista attento al budget** (Grottaferrata/Albano, confronta preventivi). Fase: consapevolezza → considerazione. Domande: "Quanto costa con te, all'incirca?", "Ci sono costi ricorrenti?". *Evidenza: SERP 2.5, "da 450€".*
- **P4 — Chi cerca "web designer Frascati" in directory** (vuole una persona e recensioni). Fase: decisione. *Evidenza: SERP 2.3.*
- **P5 — Professionista con sito vecchio da rifare** (osteopata, psicologo). Fase: considerazione. Domande: "Puoi rifare il mio sito WordPress?", "Mi lasci autonomo?". *Evidenza: SERP 2.2 (Web2000 "assistenza, gestione"), articolo interno sui plugin WordPress.*

### Punteggi (homepage + pagine raggiungibili)

| Persona | Relevance | Clarity | Trust | Action | Totale | Rating |
|---|---|---|---|---|---|---|
| P2 Ristoratore di Marino | 8/25 | 9/25 | 6/25 | 13/25 | **36/100** | Critical Mismatch |
| P5 Sito vecchio da rifare | 10/25 | 10/25 | 12/25 | 13/25 | **45/100** | Needs Work |
| P3 Attento al budget | 13/25 | 7/25 | 13/25 | 14/25 | **47/100** | Needs Work |
| P4 Web designer da directory | 15/25 | 15/25 | 8/25 | 14/25 | **52/100** | Needs Work |
| P1 Nutrizionista di Frascati | 18/25 | 14/25 | 17/25 | 14/25 | **63/100** | Good |

**Evidenze chiave per i punteggi:**
- P2: "Piccole attività locali" è una sola etichetta. Nessun esempio di ristorazione, nessuna parola su menu, orari o prenotazioni. La card AI per ristoranti esiste solo nel blog (`ai-automazione-ristorante`) e non compare in homepage.
- P5: il rifacimento non è mai nominato. "Disponibile per eventuali interventi futuri" è l'unico aggancio.
- P3: la homepage dice "prezzi onesti" (meta description) ma non dà **nessuna indicazione** né link alla guida costi. Il trust è salvato da "senza vincoli, canoni mensili o sorprese".
- P4: una testimonianza non locale, nessuna stella, nessun profilo directory collegato.
- P1: caso studio e testimonianza sono esattamente del suo settore. Perde punti perché la cliente è di Pescara e manca una pagina dedicata (deve scorrere fino a "lavori recenti" e uscire dal sito per vedere il lavoro).

### Persona più debole: P2 Ristoratore di Marino (36/100)
**Problema principale:** nessuna prova e nessun linguaggio per la ristorazione. Il sito parla a "professionisti della salute".
**Fix concreto:** nella futura pagina `/siti-web-castelli-romani/` aggiungere un blocco H2 "Ristoranti, trattorie e attività del territorio" con menu aggiornabile in autonomia, orari, collegamento alla Scheda Google e link a WhatsApp/telefono. Appena un lavoro di ristorazione sarà online (con consenso del cliente), pubblicarlo come caso studio in `/lavori/` e collegarlo da quel blocco. Linkare anche "AI per Ristoranti" come approfondimento.

### Problemi sistemici
- **Action (13-14/25 per tutte le persona):** esiste un'unica CTA generica "Scrivimi" verso un form. Mancano CTA per fase (es. "Vedi il caso della nutrizionista", "Quanto costa un sito con me") e un contatto rapido (WhatsApp o telefono, se Marco vuole esporlo).
- **Trust locale:** l'unica prova sociale non è dei Castelli Romani. Il punto di forza "sono di Frascati" è dichiarato ma non dimostrato (nessuna foto in zona, nessun cliente locale, nessuna recensione).

---

## 6. Raccomandazioni di architettura (cambi di tipo pagina)

Ordinate per impatto. Tutte compatibili con la collaborazione occasionale: si parla di **"preventivo su misura, pagamento una tantum, nessun canone"** e mai di pacchetti o abbonamenti.

### 6.1 `/lavori/` + `/lavori/martina-iannotti-nutrizionista/` (PRIORITÀ 1)
Tipo: **Service/Case study**. Sblocca il trust per tutte le persona ed è il prerequisito delle pagine 6.2-6.4.
Struttura del caso studio:
- H1 "Sito per nutrizionista: il caso di Martina Iannotti"
- Situazione di partenza → Obiettivo → Cosa ho fatto (pagine create, SEO locale, formazione per gestirlo in autonomia)
- Screenshot desktop e mobile (prima/dopo se disponibili)
- Testimonianza completa
- Risultati misurabili, se Martina li condivide (chiamate, richieste dal form, posizionamento su "nutrizionista Pescara")
- CTA "Vuoi un sito così per il tuo studio? Scrivimi"

Schema: CreativeWork o Article + Review. La card in homepage deve linkare qui, non solo al sito esterno.
Aggiungere altri lavori (es. il progetto Osteria Gemelli) **solo quando sono online e con il consenso del cliente**.

### 6.2 `/siti-web-nutrizionisti/` (PRIORITÀ 2, mismatch CRITICAL)
Tipo: **Hybrid servizio verticale + guida.** Struttura suggerita da quello che la SERP premia:
- H1 "Sito web per nutrizionisti e biologi nutrizionisti"
- H2 "Cosa deve avere il sito di un nutrizionista" (chi sono, percorsi, metodo, FAQ, prenotazione, privacy dei dati sanitari)
- H2 "Un esempio reale" (caso Martina, link a 6.1)
- H2 "Come lavoro" (i 3 step)
- H2 "Quanto costa" (preventivo una tantum, nessun canone, cosa è incluso; eventuale range indicativo a discrezione di Marco)
- H2 "Automazioni utili" (link a "AI per Nutrizionisti")
- FAQ (FAQPage)
- CTA "Scrivimi per un sito per il tuo studio"

Collegarla da "AI per Nutrizionisti" e dalla card "Professionisti della salute" in homepage. Lo stesso modello è replicabile per osteopati e psicologi **solo** quando ci sarà un caso reale (niente pagine vuote).

### 6.3 `/siti-web-castelli-romani/` (PRIORITÀ 3, mismatch CRITICAL)
Tipo: **Service Page locale.** Trasformare `/blog/siti-web-castelli-romani/` in pagina servizio con **redirect 301** dal vecchio URL. Interviene sul sorgente, quindi è da fare in fase di implementazione.
Struttura:
- H1 "Realizzazione siti web ai Castelli Romani"
- H2 "Un web designer che vive a Frascati" (differenziatore contro le agenzie "città" con sede altrove)
- H2 "Per chi lavoro" (salute, studi professionali, ristoranti e attività del territorio: blocco per P2)
- H2 "Comuni in cui lavoro" (Frascati, Grottaferrata, Marino, Albano, Ariccia, Genzano, Velletri, Rocca di Papa, Monte Porzio...): **testo unico, non una pagina per comune** (eviterebbe le doorway page, che con un solo lavoro sarebbero solo un rischio)
- H2 "Come lavoro e quanto costa" (una tantum, ricevuta per prestazione occasionale)
- Lavori (link a 6.1), FAQ locali, CTA

Rimuovere o motivare la frase "Dai dati che analizzo costantemente per i miei clienti".

### 6.4 `/siti-web-frascati/` oppure homepage riposizionata (PRIORITÀ 4, mismatch HIGH)
Due opzioni, da **scegliere una sola** per evitare cannibalizzazione su "siti web Frascati":
- **A (consigliata):** creare `/siti-web-frascati/` come Service Page locale (slug simile ai 9/9 della SERP) e riposizionare la homepage come brand personale. Title suggerito: "Marco La Rocca — Web Designer a Frascati | Siti per professionisti". L'H1 dovrebbe includere "web designer", così la homepage copre la query 2.3 (personale, MEDIUM) e la pagina dedicata copre la 2.1.
- **B:** la homepage resta la pagina per "siti web Frascati", ma va resa più focalizzata (H2 veri, meno spazio ad AI e automazione, contenuto specifico su Frascati) e "web designer Frascati" si lavora solo con directory e profili.

In entrambi i casi la pagina Frascati deve contenere ciò che le agenzie concorrenti non possono dire: incontro di persona a Frascati, conoscenza del territorio, riferimenti locali concreti.

### 6.5 Guida costi: aggiornare, non cambiare tipo (PRIORITÀ 5, ALIGNED)
- Title: "Quanto costa un sito web nel 2026? Prezzi reali per piccole attività"
- Portarla a ~1.300-1.800 parole: fasce per tipologia (monopagina, vetrina 3-5 pagine, rifacimento), differenza freelance/agenzia, costi ricorrenti, costi nascosti
- Aggiungere il box "Quanto costa lavorare con me": preventivo su misura, pagamento una tantum, nessun canone, sito di tua proprietà
- FAQPage, dateModified aggiornata
- **Link dalla homepage** (sezione FAQ o servizi) e dalle pagine 6.2-6.4

### 6.6 Homepage: interventi di supporto
- Convertire le etichette "// ..." in **H2 reali**, mantenendo lo stile visivo
- Card "A chi è rivolto" cliccabili verso 6.2 e 6.3
- Card "Lavori recenti" verso `/lavori/...`
- Aggiungere la voce **"Rifacimento siti esistenti"** nei servizi (persona P5)
- Seconda CTA a basso attrito: "Guarda un lavoro" / "Quanto costa?"

### 6.7 Fuori sito (Authority)
- Profili gratuiti su PagineGialle e ProntoPro (Frascati/Grottaferrata), che sono i formati che rankano per "web designer Frascati"
- Chiedere a Martina (e ai clienti futuri) una recensione dove sarà raccolta
- Google Business Profile: valutarlo con prudenza. Senza sede né Partita IVA la scheda "area servita" va verificata rispetto alle linee guida Google e alla posizione fiscale. Da chiarire prima di aprirla.

### Cross-skill
- E-E-A-T e affermazioni non verificabili → `/seo content`
- FAQPage, BreadcrumbList, CreativeWork per i casi studio → `/seo schema`
- Local pack e fattibilità GBP → `/seo local`
- Audit delle nuove pagine dopo la pubblicazione → `/seo page`

---

## 7. Limiti dell'analisi

- **SERP non localizzate:** lo strumento di ricerca è basato negli USA. Non ho potuto osservare local pack, People Also Ask, annunci Google Ads, ricerche correlate né AI Overview su google.it. Le user story si basano su title, URL, snippet e offerte dei risultati, non su PAA e ads.
- **Query brevi rumorose:** "siti web Frascati" e "web designer Frascati" in forma esatta hanno restituito risultati informativi e omonimie. La SERP commerciale è stata ricostruita con varianti esplicite, quindi l'ordine reale su google.it può differire.
- **Posizioni attuali di laroccadigitale.it:** non verificate (servono dati di Search Console, installata da poco).
- **Profondità dei competitor:** non ho fatto il render delle pagine concorrenti. Lunghezze e schema sono stimati da title e snippet.
- **Comportamento utenti:** Clarity sembra bloccato dalla CSP (vedi §1), quindi non ci sono dati reali di scroll o click.
- **Aspetti fiscali e GBP:** le note su prestazione occasionale e Google Business Profile sono indicazioni di posizionamento, non consulenza fiscale.
- Wireframe IST/SOLL non generati (non richiesti). Disponibili su richiesta.

**Generare un report PDF? Usa `/seo google report`.**

---

## 8. Dati strutturati per audit-data.json (categoria "Search Experience")

```json
{
  "category": "Search Experience",
  "sxo_gap_score": 51,
  "score_breakdown": {"page_type": 6, "content_depth": 6, "ux_signals": 10, "schema": 9, "media": 7, "authority": 5, "freshness": 8},
  "mismatches": [
    {"query": "realizzazione siti web Castelli Romani", "serp_dominant": "Service Page locale", "confidence": 0.78, "current": "Blog Post /blog/siti-web-castelli-romani/", "severity": "CRITICAL"},
    {"query": "sito per nutrizionista", "serp_dominant": "Hybrid servizio verticale", "confidence": 0.6, "current": "nessuna pagina", "severity": "CRITICAL"},
    {"query": "siti web Frascati", "serp_dominant": "Service Page locale dedicata", "confidence": 1.0, "current": "Homepage generica", "severity": "HIGH"},
    {"query": "web designer Frascati", "serp_dominant": "Directory + siti personali (debole)", "confidence": 0.4, "current": "Homepage personale", "severity": "MEDIUM"},
    {"query": "quanto costa un sito web", "serp_dominant": "Blog Post / guida", "confidence": 1.0, "current": "Blog Post /blog/quanto-costa-sito-web/", "severity": "ALIGNED"}
  ],
  "personas": [
    {"name": "Ristoratore di Marino", "score": 36},
    {"name": "Professionista con sito da rifare", "score": 45},
    {"name": "Professionista attento al budget", "score": 47},
    {"name": "Cerca web designer in directory", "score": 52},
    {"name": "Nutrizionista di Frascati", "score": 63}
  ],
  "recommended_pages": ["/lavori/", "/lavori/martina-iannotti-nutrizionista/", "/siti-web-nutrizionisti/", "/siti-web-castelli-romani/ (301 da /blog/siti-web-castelli-romani/)", "/siti-web-frascati/"],
  "side_findings": ["CSP blocca scripts.clarity.ms: Clarity probabilmente non registra", "Homepage con 0 H2 reali", "Guida costi non linkata dalla homepage"]
}
```

---

**Fonti SERP:** sitisrl.it, avavo.it, inconnect.it, digitalwebitalia.it, adarte.pro, suitedesignstudio.com, lumiaweb.com, clion.it, castelliromanicomputer.it, paginegialle.it, prontopro.it, addlance.com, dbnet.it, gestione-siti-web.it, gbnet.it, webrex2000.com, studioinweb.com, gianlucagentile.com, tfagency.it, eccolomarketing.it, nutrivivacreativa.it, websanitario.it, sitiinternet.pro, luismeta.com, webepc.it, waas.it, gutflg.com, it.squarespace.com, sitiweba100euro.it, shopify.com/it, hostinger.com/it, supporthost.com, html.it, damicomarco.it, dgtatelier.it, cfweb.it, pacitto.dev, onionlabs.it, fabioangelici.com, argentodev.com, matechstudio.com, catonebros.it (ricerche del 07/10/2026).
