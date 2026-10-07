# Local SEO - laroccadigitale.it (Marco La Rocca)

Data audit: 2026-10-07. Fonti: home renderizzata (raw), sorgente `content/blog/siti-web-castelli-romani.md`. Non verificati con strumenti a pagamento: posizioni local pack, citazioni live, GBP esistenti (nessuna ricerca DataForSEO).

## Punteggio Local SEO: 31/100 (cap reale con il vincolo "no P.IVA / no sede")

| Dimensione | Peso | Punti | Nota |
|---|---|---|---|
| GBP Signals | 25% | 3/25 | Nessuna scheda, nessuna mappa (coerente con assenza sede) |
| Reviews & Reputation | 20% | 4/20 | 1 testimonianza on-site, nessun aggregateRating, nessuna recensione terza parte |
| Local On-Page SEO | 20% | 13/20 | Title/H1/badge con Frascati e Castelli Romani, blog geo, ma niente pagine servizio dedicate |
| NAP & Citazioni | 15% | 2/15 | Nessun telefono, nessun indirizzo, email offuscata, zero citazioni |
| Local Schema | 10% | 5/10 | ProfessionalService presente, ma indirizzo fittizio e geo impreciso |
| Link & Authority locali | 10% | 4/10 | Solo GitHub in sameAs, nessun link locale |

Nota proximity: ~55% della varianza di ranking local dipende dalla prossimita (fuori dal controllo). Senza GBP il local pack e comunque fuori portata; l'obiettivo realistico e l'organico (risultati blu) + AI/citazioni.

## Tipo di attivita e verticale
- Tipo rilevato: SAB puro, anzi "SAB senza ufficio": nessun indirizzo visibile, nessuna Maps, nessun "directions".
- Verticale: servizi professionali/web agency (ProfessionalService e corretto; non rientra nei 6 verticali standard).
- Contraddizione: lo schema dichiara un `PostalAddress` con `streetAddress: "Frascati"` (non e una via) + CAP 00044 + geo 41.808/12.682 (3 decimali, centroide cittadino). Dichiara una sede che non esiste.

## NAP audit

| Fonte | Nome | Indirizzo | Telefono | Email |
|---|---|---|---|---|
| HTML visibile | Marco La Rocca | solo "Frascati - Castelli Romani - Roma" (badge) | assente | offuscata (click per vedere, JS) |
| JSON-LD ProfessionalService | "Marco La Rocca - Siti Web" | "Frascati, 00044, RM" (street = citta) | assente | assente |
| JSON-LD Person | Marco La Rocca | solo locality | assente | assente |
| Meta/OG | "Marco La Rocca" / "Marco La Rocca - Siti Web Frascati" | - | - | - |

Discrepanze: (1) nome variabile ("Marco La Rocca", "- Siti Web", "- Siti Web Frascati"); (2) indirizzo schema senza via e non visibile in pagina (schema deve rispecchiare il contenuto visibile); (3) nessun telefono ne email in schema/HTML statico, quindi un crawler non trova alcun contatto. Il footer cita "ricevuta per prestazione occasionale", coerente con il vincolo ma non e un dato NAP.

Raccomandazione NAP "sicuro": nome unico = "Marco La Rocca" (brand: "La Rocca Digitale" solo se usato ovunque); niente indirizzo (SAB); email dedicata (es. info@laroccadigitale.it) esposta in schema come `email` e in HTML come testo/mailto offuscato leggero (JS-less, es. entita HTML o immagine+form) oppure solo form; telefono opzionale: un numero VoIP/secondario e utile ma non obbligatorio per un sito di contatti via form. `areaServed` va mantenuto, `address` ridotto a `addressLocality` + `addressRegion` + `addressCountry` (senza streetAddress/postalCode), geo rimosso o spostato a `areaServed` come GeoCircle.

## Google Business Profile: si o no?

Risposta breve: sconsigliato ora; rimandare finche non c'e P.IVA/attivita abituale. Non e illegale creare la scheda, ma e rischioso e poco redditizio.

Rischi:
1. Linee guida Google: la scheda e per attivita che "hanno contatto di persona con i clienti" (sede o servizio presso il cliente). Un web designer che lavora da remoto da casa e a rischio di non-eleggibilita; i SAB devono nascondere l'indirizzo ma Google richiede comunque un indirizzo/area di servizio reali e puo chiedere videoverifica (mostrare prova del business, strumenti, insegna, documenti) che Marco non puo fornire.
2. Coerenza legale: una scheda GBP con categoria, orari, "Prenota/Chiama" e recensioni pubbliche proietta attivita continuativa e commerciale. Contrasta con la dicitura art. 2222 c.c. del sito ("non abituale"); un controllo (Agenzia Entrate/INPS/datore di lavoro, clausole di esclusiva del contratto da dipendente) potrebbe usare la scheda come indizio di abitualita. Questa e una valutazione di rischio, non consulenza legale: confermare con un commercialista/consulente del lavoro. Nota: la soglia di legge per prestazioni occasionali (5.000 euro/anno per committente per gli obblighi contributivi INPS gestione separata sopra 5.000 euro totali) conta piu della presenza di una scheda, ma la scheda rende l'abitualita piu "provabile".
3. Sospensione: indirizzo di casa come sede, uso di indirizzo virtuale/coworking non presidiato, o categoria sbagliata sono motivi frequenti di sospensione; una scheda sospesa danneggia l'immagine del brand.
4. Nome: deve essere il nome reale usato al pubblico (nessuna keyword stuffing "Siti Web Frascati").
5. Rendimento: un SAB senza indirizzo, in categoria "Web designer", compare nel local pack quasi solo entro pochi km dal centroide di servizio, e i clienti target (professionisti) cercano spesso "web designer Frascati" con intento B2B che e meno local-pack-driven. Beneficio atteso basso rispetto al rischio.

Quando diventerebbe ok: apertura P.IVA (anche regime forfettario) + indirizzo reale o SAB regolare con verifica superata + categoria primaria "Web designer" (o "Servizio di consulenza SEO"), area di servizio Frascati/Castelli Romani, nessun indirizzo pubblico. Checklist al momento dell'apertura: categoria primaria (fattore #1), area servizio max 20 aree, servizi con descrizioni, foto reali (lavori, persona), post mensili, domanda-risposta, link a sito e `sameAs` in schema.

Alternative sicure ora:
- Nessuna scheda propria; costruire presenza su pagine "persona/progetti" non commerciali: LinkedIn personale (profilo + sezione Progetti), GitHub (gia presente), Behance/Dribbble se portfolio.
- Elenco su directory B2B/freelance senza obbligo P.IVA o con "prestazione occasionale": Malt (richiede P.IVA, verificare), Freelancer.com/Upwork (profili non-locali), Workana. Verificare i termini di ciascuna.
- Wikidata/Crunchbase non adatti (nessuna notability).
- Menzioni locali: guest post, interviste, ordini professionali dei clienti (link dal loro sito "Realizzato da Marco La Rocca - Frascati", con consenso). E il canale piu sicuro e piu efficace.
- Lavorare sulle schede GBP dei clienti: e il servizio che offre. Resta lecito spiegarlo nel blog.

## Valutazione post "siti-web-castelli-romani" come geo landing page

Pro: URL con keyword, title "Realizzazione Siti Web Castelli Romani" (include intent commerciale), H1 coerente, 8+ comuni citati, link interno verso `/blog/google-business-sito-vetrina/` e verso servizi/contatti, tag geo.

Problemi:
1. Funzione ambigua: e scritto per un cliente generico ("se hai uno studio ad Albano Laziale...") non come offerta di Marco; e un articolo informativo travestito da landing. Per query transazionali ("web designer Frascati") un blog post posiziona peggio di una pagina servizio.
2. Sezione "Quali zone sono piu redditizie": "Dai dati che analizzo costantemente per i miei clienti" non e verificabile (Marco ha pochissimi clienti) e rischia di essere un claim ingannevole; i dati di ricerca (70% da smartphone) non hanno fonte. Sostituire con dati reali (Search Console, Google Trends, Keyword Planner) citati.
3. Elenco comuni a "lista" senza contenuto specifico per ciascuno: rischio di apparire thin/keyword-stuffing; ok in un articolo, non da replicare per ogni comune.
4. Il testo parla di "tua posizione fisica", "Chiama Ora": il sito di Marco non ha ne telefono ne sede; l'esempio non vale per lui ma e coerente come consiglio ai clienti.
5. Manca: prova sociale (caso studio reale), prezzo/ordine di grandezza, FAQ (con FAQPage non piu rich result per questo sito, ma utile ai modelli AI), autore/Person schema, data aggiornamento, immagine con alt locale.
6. Nel footer legale e nel testo "collaborazione occasionale" e coerente, ma "Servizi" + "prezzi onesti" e CTA senza telefono limitano la conversione.

Azioni: trasformare in pagina servizio vera (`/siti-web-castelli-romani/` o `/servizi/siti-web-frascati/`) con Service schema, 1-2 casi studio, FAQ, area servita, processo; mantenere il post come guida e linkarlo alla pagina.

## Strategia location page senza doorway pages
- Non creare una pagina per comune con testo clonato e cambio di nome (swap test fallito = doorway, violazione spam policy Google).
- Struttura consigliata: 1 hub `Siti web Castelli Romani` (pagina servizio) + al massimo 2-3 pagine locali dove c'e valore autentico (Frascati; eventualmente Grottaferrata se c'e un caso reale). Ogni pagina con >=60% contenuto unico: clienti/progetti reali in quel comune (con consenso), problemi tipici del settore locale (es. ristoranti a Frascati: cantine, turismo, fraschette), foto, FAQ, testimonianze.
- Senza clienti/progetti locali: nessuna pagina comunale; usare invece pagine per verticale (osteopata, nutrizionista, psicologo, ristorante: i post blog "ai-automazione-*" gia esistono) con modificatore "Frascati/Castelli Romani" e prove.
- Link interni: home -> hub -> verticali/comune -> blog; profondita max 2 clic dalla home. Breadcrumb + schema BreadcrumbList.
- Schema: Service con `provider` {@id #business} e `areaServed` (City/AdministrativeArea) e non `Place` con indirizzo; non usare `branchOf`/multi-location (non applicabile).

## Recensioni e reputazione
- Presente: 1 testimonianza on-site, da cliente di Pescara (fuori area target, il che indebolisce il messaggio locale ma e autentico; non nasconderlo, evitare di presentarla come locale).
- Schema: nessun `Review`/`aggregateRating`; con 1 sola recensione self-hosted non marcare aggregateRating (policy Google su self-serving reviews per LocalBusiness/Organization: comunque non genera rich result per "self-serving"). Non aggiungere.
- Velocita/risposta: n/a. Senza GBP le recensioni esterne possibili: Trustpilot (gratuito, nessuna P.IVA richiesta per essere recensiti, ma il profilo business richiede dominio), Facebook Raccomandazioni (se si apre pagina; poco coerente con "non attivita"), LinkedIn Recommendations (ideale, persona fisica).
- Piano: ottenere 3-5 testimonianze scritte (nome, ruolo, comune, link al loro sito) dai clienti reali, con consenso, e le raccomandazioni LinkedIn; mostrarle in pagina servizio con Person/Organization del cliente come autore, senza aggregateRating.

## Citazioni Tier 1 fattibili senza P.IVA
- Yelp, BBB, Pagine Gialle/PagineBianche, Virgilio, Tuttocitta: richiedono attivita commerciale/ indirizzo o telefono; non adatti, evitare per coerenza con "occasionale".
- Fattibili: LinkedIn (persona), GitHub (gia presente, aggiungere URL sito nel profilo), profili sui siti dei clienti ("sito realizzato da"), Google Search Console/GA gia installati, Bing Webmaster Tools (aggiungere), Trustpilot (facoltativo), Medium/dev.to articoli con backlink, pagine autore guest. Direttori freelance italiani solo se accettano occasionali.
- Coerenza NAP minima ripetuta ovunque: "Marco La Rocca - Web designer - Frascati (RM) - laroccadigitale.it - email".
- Brand search: chiedere ai clienti link con anchor "Marco La Rocca", non keyword-rich.

## Schema locale (validazione)
- Subtype: `ProfessionalService` OK (non `LocalBusiness` generico). Per un SAB senza P.IVA, valutare `Person` + `Service` invece di Organization: oggi l'Organization/business e `worksFor` della Person, e implica impresa.
- Obbligatori: name OK; address presente ma non reale (da correggere).
- Raccomandati: telefono assente, email assente, `openingHoursSpecification` assente (corretto per assenza sede), `geo` a 3 decimali (se si mantiene servono 5 decimali ma meglio rimuoverlo: non esiste sede), `url` OK, `image` OK, `sameAs` solo GitHub (aggiungere LinkedIn), `priceRange` assente.
- `@id` stabili e Person collegata: buono. `hasOfferCatalog` ok.
- Il Person.address con locality e accettabile.

## Top 10 azioni
1. CRITICA: Non aprire GBP finche non c'e P.IVA e sede/SAB conforme; confermare con commercialista/clausole contratto da dipendente.
2. CRITICA: Rimuovere da JSON-LD `streetAddress: "Frascati"`, `postalCode`, `geo`; lasciare solo locality/region/country + `areaServed`.
3. ALTA: Esporre un'email di contatto reale in schema e in HTML crawlabile (o almeno mailto in noscript/immagine alt) e uniformare il nome (una sola forma).
4. ALTA: Creare pagina servizio dedicata "Siti web Frascati / Castelli Romani" (fattore #1 organico) con Service schema e CTA a form; usare il post come supporto.
5. ALTA: Raccogliere 3-5 testimonianze/raccomandazioni LinkedIn con consenso; dichiarare l'origine (anche Pescara) senza claim locali falsi.
6. ALTA: Correggere/riscrivere i claim non dimostrabili nel post ("dati che analizzo costantemente per i miei clienti", 70%) con fonti reali o con dati propri da Search Console.
7. MEDIA: Strategia pagine locali: massimo 2-3 con contenuto unico + pagine per verticale; vietare cloni per comune.
8. MEDIA: Creare/ottimizzare LinkedIn con link al sito, aggiungere a `sameAs`; GitHub bio con URL; Bing Webmaster Tools.
9. MEDIA: Chiedere ai clienti un link "Sito realizzato da Marco La Rocca" nel footer (backlink locale + citazione NAP minima).
10. BASSA: Aggiungere casi studio/portfolio, FAQ sulla pagina servizio, Person schema con `knowsAbout`, data di aggiornamento nel post.

## Limitazioni
Non verificato: presenza di GBP preesistenti o schede duplicate, posizioni local pack, citazioni live, backlink (nessuno strumento a pagamento), contenuto reale di contratto da dipendente, regime fiscale: il giudizio sui rischi legali/fiscali e indicativo, va validato con un professionista. Le soglie e linee guida Google vanno controllate nella versione corrente. File sorgente non modificati.
