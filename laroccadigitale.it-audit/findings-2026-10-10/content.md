# Re-audit contenuti / E-E-A-T: laroccadigitale.it

Data: 2026-10-10. Audit precedente: `../FULL-AUDIT-REPORT.md` e `../findings/content.md` (2026-10-07).
Sorgenti lette per intero: `content/_index.md`, `content/siti-web-frascati-castelli-romani.md`, `content/lavori/*`, `content/blog/*.md` (16 articoli), più i testi fissi dei template (`layouts/partials/author-box.html`, `layouts/blog/single.html`, `layouts/lavori/*`, `layouts/index.llms.txt`, `layouts/partials/shared/schema.html`).
Nessun file del sito è stato modificato. I numeri di riga si riferiscono ai file com'erano al commit `17e1079`.

Vincolo di riferimento: Marco è dipendente e fa siti solo come prestazione occasionale (senza P.IVA, pochi lavori l'anno). Ogni frase che suona da agenzia o promette servizi continuativi è segnalata. È un rilievo editoriale, non un parere fiscale.

---

## 1. Punteggi

| Metrica | 07/10 | **10/10** | Nota |
|---|---|---|---|
| **Qualità contenuti complessiva** | 52 | **68/100** | Statistiche inventate quasi tutte eliminate, fonti in 16 articoli su 16, tono "occasionale" ben dichiarato. Restano contraddizioni nei post AI sanitari, contenuti sovrapposti e link interni deboli |
| E-E-A-T: Experience (20%) | 30 | **45** | Un caso reale (Martina) con testimonianza, accenno al lavoro sull'osteria. Mancano dettagli di prima mano negli articoli |
| E-E-A-T: Expertise (25%) | 50 | **62** | Correzioni tecniche fatte. Restano frasi imprecise (vedi §3, §5) |
| E-E-A-T: Authoritativeness (25%) | 25 | **50** | Fonti ufficiali in ogni articolo (EUR-Lex, Normattiva, Google, WordPress.org). Nessun riconoscimento esterno, bio senza credenziali verificabili |
| E-E-A-T: Trustworthiness (30%) | 40 | **66** | Pagamento e natura occasionale spiegati con chiarezza, disclaimer legali, articolo GDPR. Pesano i consigli sanitari che contraddicono l'articolo GDPR e la FAQ sulla ritenuta |
| **E-E-A-T pesato** | 37 | **57/100** | Pesi interni della skill, non di Google |
| **AI citation readiness** | 45 | **60/100** | Buone tabelle e H2 a domanda; l'articolo GDPR è molto citabile. Penalizzano emoji negli heading, blocchi duplicati, numeri ipotetici |
| Metadati templati (`metadata_template.py`, 21 pagine) | low | **site_risk low**, `templated_ratio` 0.0, nessuna `shared_cta_phrases` | Nessun flag |
| Fonti esterne (controllo di tutti i 32 URL) | n/d | **32/32 rispondono** | 200 dopo redirect; EUR-Lex risponde 202 (challenge anti-bot, nel browser si apre). Dettagli in §8 |

---

## 2. Priorità ALTA

### A1. I post AI per studi sanitari contraddicono l'articolo GDPR del sito stesso (YMYL)

L'articolo `ai-chatbot-dati-pazienti-gdpr.md` è il migliore del blog e fissa regole chiare: niente domande sui sintomi, niente anamnesi via chatbot, dati minimi, dichiarare l'AI, revisione periodica (righe 59-79). Diversi passaggi dei post verticali dicono il contrario. Per un lettore sanitario è il punto che più abbassa la fiducia: il sito si contraddice su un tema di salute e di legge.

| Evidenza | Problema | Correzione proposta |
|---|---|---|
| `ai-automazione-psicologo.md:36` "Ho bisogno di un appuntamento **urgente**, è per **mio figlio di 14 anni**… e propone lo slot giusto" | Esempio con minore e urgenza gestiti dal chatbot. Contraddice la riga 75 dello stesso post ("per un minore deve limitarsi a raccogliere il contatto") e la riga 74 (crisi) | Sostituire con un esempio neutro: "Vorrei un primo colloquio, anche online, preferibilmente al mattino". Aggiungere: "Se il messaggio parla di urgenza o riguarda un minore, il chatbot raccoglie solo il contatto e ti avvisa" |
| `ai-automazione-psicologo.md:86-92` follow-up AI "dopo una seduta intensa… più empatico" | Per generarlo bisogna dare all'AI il contenuto della seduta: dato sanitario e segreto professionale | Ridurre a promemoria e materiali scelti da te; aggiungere "non inserire nell'AI contenuti delle sedute" |
| `ai-automazione-psicologo.md:92` e `ai-automazione-osteopata.md:103` "Ogni messaggio **sembra scritto da te**" | Va contro l'obbligo di informare il cliente sull'uso dell'AI (L. 132/2025 art. 13), che il post stesso cita nel box alla riga 23 | "Ogni messaggio segue il tuo tono; i pazienti sanno che usi uno strumento di supporto (vedi l'informativa)" |
| `ai-automazione-nutrizionista.md:66` "(o lasci inviare **in automatico** se ti fidi)" | Già segnalato il 07/10, ancora presente. Messaggi generati dall'AI su dati di salute inviati senza revisione | Eliminare la parentesi: "L'AI propone una bozza, tu la rivedi e la invii" |
| `ai-automazione-nutrizionista.md:92` chatbot che dà "**chiarimenti sulle indicazioni del piano alimentare**" | Contraddice la riga 91 ("non dà consigli personalizzati") e la tabella dell'articolo GDPR ("domande sulla terapia: meglio di no") | Eliminare il punto. Lasciare solo indicazioni generali scritte da te e link a materiali |
| `ai-automazione-osteopata.md:68-71` il paziente scrive "dolore cervicale… fisioterapia senza risultati" e il chatbot "raccoglie **tutte** le informazioni" | Raccolta di dati sanitari via chatbot, contro il punto 3 della checklist GDPR ("niente campi su salute") | "Raccoglie nome, recapito e preferenza di orario; dei sintomi parlerete in visita" |
| `ai-automazione-osteopata.md:101` "spero che **la schiena** stia già meglio" nella richiesta di recensione | Informazione sanitaria su un canale terzo, e la recensione così richiesta può esporre il paziente. Già segnalato | "Grazie per la visita di oggi. Se ti va, una recensione su Google mi aiuta: ecco il link." |
| `ai-automazione-osteopata.md:123` "si configurano una volta e **poi funzionano da sole**" | Già segnalato. Falso per i chatbot e in contrasto con il punto 9 della checklist GDPR ("revisione periodica") | "Si configurano una volta, poi basta controllarli ogni tanto: per un chatbot, rileggere un campione di conversazioni" |
| `ai-automazione-guida-attivita-locali.md:60-62` esempio "Soffro di cervicale…" + "raccoglie le informazioni e te le manda organizzate"; righe 135 e 143 "form per raccolta dati pre-visita" e "follow-up personalizzati con AI" | Stesso problema nella guida pillar | Esempio senza sintomi; rimando esplicito al box "Se lavori con dati sanitari" (riga 120) già prima dello Step 2 |

### A2. Articoli correlati scritti a mano con titoli vecchi

| Evidenza | Problema | Correzione |
|---|---|---|
| `perche-professionista-locale-sito-web.md:55-57`, `errori-online-attivita-locali.md:86-88`, `come-scegliere-parole-chiave-attivita-locale.md:141-144` | Anchor con titoli che non esistono più ("Accoppiata Vincente", "4 Trucchi SEO Pratici", "Perché un Professionista ha Bisogno di un Sito Web") in Title Case. Doppione del blocco automatico "potrebbe interessarti anche" del template | Eliminare i tre blocchi manuali e mettere i link dentro il testo (vedi §4), oppure aggiornare gli anchor ai titoli attuali |

### A3. Affermazioni già segnalate il 07/10 e ancora presenti

| Evidenza | Correzione |
|---|---|
| `sito-monopagina-o-sito-completo.md:14` "**Nel 90% dei casi** ci si ritrova a scegliere tra tre categorie" | "Di solito la scelta è tra tre tipi di sito" |
| `ai-automazione-guida-attivita-locali.md:145` "I primi due step risolvono **l'80% dei problemi**" | "Spesso i primi due step bastano, con strumenti che non sono nemmeno AI" |
| `ai-automazione-guida-attivita-locali.md:2` title "la guida onesta (**senza fuffa**)" e righe 22, 34, 46, 56, 64, 70, 74 (emoji ⚙️ 🤖 🤝 negli H3) | Title: "AI e automazione per piccole attività: cosa fanno davvero e quanto costano". Emoji fuori dagli heading (finiscono negli id delle ancore e nell'indice) |
| `perche-professionista-locale-sito-web.md:4` description "trovare clienti **in automatico**" | "…un sito ti fa trovare da chi cerca il tuo servizio su Google, senza dipendere dagli algoritmi dei social." |
| `google-business-sito-vetrina.md:4` "è **il trucco** per convertire contatti in clienti"; riga 32 "Una cosa che **molti ignorano**"; riga 8 tag "google my business" | Description neutra; togliere la formula; tag "google business profile" |
| `blog-e-trucchi-seo-semplici.md:4` "È **l'arma più potente** per farti trovare"; riga 28 "trucco SEO **potentissimo**" (contraddice la riga 31, corretta) | "Un blog fatto bene ti aiuta a farti trovare…"; riga 28: "Un'abitudine che richiede due secondi" |
| `errori-online-attivita-locali.md:24` "Bastano **30 minuti una tantum**" subito dopo "rispondi a tutte le recensioni" | "Per sistemarla bastano 30 minuti; poi qualche minuto a settimana per le recensioni" |
| `ai-automazione-osteopata.md:28` segretaria part-time "600-900€ (lordo)" senza fonte | Togliere la cifra ("costa diverse centinaia di euro al mese", come già fatto nella guida, riga 102) |

---

## 3. Priorità MEDIA

### M1. Frasi da "agenzia" o da attività continuativa (vincolo prestazione occasionale)

La situazione è molto migliorata: "collaborazione occasionale", "nessun canone", "intervento singolo" compaiono nei punti giusti (`quanto-costa-sito-web.md:86`, `siti-web-frascati-castelli-romani.md:25,62`, `perche-aggiornare-plugin-wordpress.md:53`, chiusura dei post AI "Io mi occupo di siti web"). Restano queste:

| Evidenza | Rischio | Riformulazione |
|---|---|---|
| `layouts/blog/single.html` (box CTA a fine articolo) "Hai bisogno di un sito **o vuoi semplificare il lavoro del tuo studio?**" | Medio: residuo dell'AI/automazione come servizio, compare su tutti i 16 articoli | "Hai bisogno di un sito per il tuo studio o la tua attività? Scrivimi, senza impegno." |
| `chi-possiede-il-tuo-sito-dominio-hosting-accessi.md:83` "Se vuoi **un controllo di come stanno le cose sul tuo sito**, scrivimi" | Medio: offre una verifica/consulenza come servizio separato | "Se stai per rifare il sito e vuoi capire da dove partire, scrivimi." Oppure chiudere solo con la checklist |
| `come-scegliere-parole-chiave-attivita-locale.md:135` "**Facciamo una chiacchierata gratuita** e ti dico su cosa concentrarti" | Medio-basso: consulenza SEO offerta in sé | "Se stai pensando a un sito nuovo, scrivimi: ne parliamo quando ci sentiamo." |
| `content/lavori/_index.md:7` "**Alcune collaborazioni recenti**" | Medio per la fiducia: ne è pubblicata una sola (l'osteria è `draft: true`), del 2025 | "Qui racconto i siti che ho realizzato, con il consenso dei clienti: cosa serviva, cosa ho fatto, com'è andata." |
| `siti-web-frascati-castelli-romani.md:27` "**Ogni sito che consegno** ha:" | Basso: suggerisce una produzione regolare | "Un sito fatto da me ha:" |
| `google-business-sito-vetrina.md:47` "**Quando realizzo** un sito, il collegamento… è compreso nel lavoro"; `chi-possiede…md:83` "Quando realizzo un sito, dominio e accessi…" | Basso | "Se realizzo io il tuo sito, …" |
| `errori-online-attivita-locali.md:80` "Ti dico cosa sistemare per primo"; `sito-web-ristorante-cosa-deve-avere.md:74` "ti dico cosa sistemerei per primo" | Basso: ok se riferito a un sito da fare, non a una diagnosi gratuita ricorrente | Lasciare, oppure legare al rifacimento: "…e valutiamo se conviene rifarlo" |
| `ai-automazione-guida-attivita-locali.md:124-143` "Il percorso consigliato: 3 step" con settimane e mesi | Basso: letto insieme a "li integro io" (riga 155) sembra un accompagnamento di mesi | Titolo "Se vuoi provarci da solo: un ordine sensato" e togliere le durate tra parentesi |
| `layouts/lavori/*` "Il prossimo potrebbe essere il tuo." | Basso: tono commerciale | "Ti serve qualcosa di simile? Scrivimi." (che c'è già) |
| `sito-monopagina-o-sito-completo.md:40` "Il Sito **'Segretario'**", Title Case "Sito Standard" | Basso: effetto listino a livelli | "3. Il sito con prenotazioni e moduli" |

### M2. Cannibalizzazione

| Cluster | Pagine | Stato | Azione |
|---|---|---|---|
| "siti web Frascati Castelli Romani" (commerciale) | Home (title fisso in `layouts/partials/shared/head.html:44` "Siti web a Frascati e Castelli Romani — Marco La Rocca") e pagina servizio (`siti-web-frascati-castelli-romani.md:3` "Realizzazione siti web a Frascati e Castelli Romani — Marco La Rocca") | **Aperto**: stesso intento, title quasi uguali | Solo proposta per la home: title "Marco La Rocca, siti web per professionisti a Frascati" (persona + categoria), lasciando la query geografica piena alla pagina servizio. In alternativa, puntare la pagina servizio sui comuni ("…Grottaferrata, Marino, Albano") |
| "sito vs social / sito + scheda Google" | `perche-professionista-locale-sito-web` (493 parole), `google-business-sito-vetrina` (490), `errori-online-attivita-locali` §2 | **Aperto** (consigliata la fusione il 07/10, non fatta) | Unire i primi due in "Sito, scheda Google e social: cosa serve davvero a un professionista" con redirect 301; in `errori-online` ridurre il §2 a 2 righe e un link |
| Blocchi ripetuti nei post AI | "AI o automazione? In breve" identico in 4 post (`psicologo:20`, `nutrizionista:20`, `osteopata:18`, `ristorante:18`); box GDPR identico in 3 (`psicologo:23`, `nutrizionista:23`, `osteopata:21`); paragrafo di chiusura identico in 4 | Migliorato (il blocco lungo è sparito), ma ~200 parole uguali per post | Variare il paragrafo di chiusura per settore e accorciare il box a una frase + link, visto che l'articolo GDPR esiste |
| Ristorante | `sito-web-ristorante-cosa-deve-avere` e `ai-automazione-ristorante` | Intenti diversi (va bene) ma **non si linkano** | Link reciproci (vedi §4) |

### M3. Inesattezze e incoerenze residue

| Evidenza | Problema | Correzione |
|---|---|---|
| `ai-chatbot-dati-pazienti-gdpr.md:17,40` e box nei post sanitari "l'AI Act **obbliga** [lo studio] a dichiarare…" | L'art. 50(1) pone l'obbligo sul **fornitore** del sistema (provider); lo studio che usa un chatbot di terzi è "deployer". In pratica il consiglio resta giusto, ma l'attribuzione è imprecisa in un articolo che si propone come riferimento legale | "L'AI Act (art. 50) chiede che chi parla con un chatbot sappia che è un'AI: l'obbligo è di chi fornisce lo strumento, ma conviene verificarlo e scriverlo comunque nel messaggio di apertura (e la legge 132/2025 chiede a te di informare il cliente)" |
| `ai-chatbot-dati-pazienti-gdpr.md:38` "Il **rinvio deciso nel 2026** riguarda soprattutto i sistemi ad alto rischio" | Affermazione senza fonte su un iter normativo (Digital Omnibus) | Aggiungere il link all'atto ufficiale (EUR-Lex o comunicato del Consiglio/Commissione), oppure togliere la frase |
| `ai-chatbot-dati-pazienti-gdpr.md:53` "Per chi lavora in sanità la legge contiene anche regole specifiche" | Manca l'articolo | Citare l'art. 7 della L. 132/2025 |
| `ai-chatbot-dati-pazienti-gdpr.md:67`, `ai-automazione-psicologo.md:74` "112 e i servizi di ascolto" | Generico | Indicare almeno un servizio con numero (es. Telefono Amico Italia, Samaritans Onlus), verificando i numeri |
| `google-business-sito-vetrina.md:32` "per decidere chi mostrare sulla mappa Google guarda anche il sito collegato alla scheda. Secondo [Google stesso]…" | La pagina citata (support.google.com/business/answer/7091, controllata) parla di pertinenza, distanza, evidenza, ma **non nomina il sito web**. Il link sembra sostenere una tesi che non contiene | "Google dice che contano pertinenza, distanza ed evidenza [link]. Un sito chiaro e coerente con la scheda aiuta soprattutto la pertinenza: è un'indicazione di buon senso, non una regola dichiarata" |
| `ai-automazione-guida-attivita-locali.md:100` totale "~80-150€/mese" | La somma delle righe 94-99 fa ~65-180€ | "~65-180€/mese (dipende da quali strumenti usi)" |
| `ai-automazione-nutrizionista.md:38` "15 nuovi pazienti al mese" vs riga 99 "20-25 pazienti attivi" | Incoerenza interna tra gli scenari; 15×15-20 min = 3,75-5 h, non "oltre 4" | Usare un solo scenario (es. 6-8 nuovi pazienti al mese, 2-3 ore risparmiate) |
| `ai-automazione-nutrizionista.md:72` "La maggior parte lo abbandona dopo 3 giorni" | Numero senza fonte | "Molti lo abbandonano dopo pochi giorni" |
| `ai-automazione-osteopata.md:83` "tasso di risposta **molto più alto**" | Senza fonte | "di solito ottiene più risposte" o togliere |
| `ai-automazione-ristorante.md:43` "Tempo risparmiato: circa 1-2 ore al giorno" | Non etichettato come stima | "Stima: fino a 1-2 ore al giorno nei periodi pieni" |
| `perche-aggiornare-plugin-wordpress.md:28` "Se il tuo smartphone si aggiorna, le vecchie app smettono di funzionare" | Falso come regola | "…alcune app vecchie possono smettere di funzionare" |
| `perche-aggiornare-plugin-wordpress.md:38,44-45` "prima i moduli minori, per ultimi i componenti vitali"; checklist plugin → tema → core | Ordine discutibile, nessun cenno alla compatibilità | "Controlla nella pagina del plugin con quale versione di WordPress è testato; se puoi, prova prima su una copia (staging)". Aggiungere il link a WordPress.org già in fonte |
| `perche-aggiornare-plugin-wordpress.md:37` "torni indietro in 3 minuti" | Promessa non realistica | "torni indietro" |
| `come-scegliere-parole-chiave-attivita-locale.md:116` "ne mostra una sola, **di solito quella che c'era prima**" | Google sceglie la canonica con molti segnali, non per anzianità | "…ne mostra una sola, e non è detto che sia la tua" |
| `come-scegliere-parole-chiave-attivita-locale.md:84` "psicologo ansia adolescenti Frascati **recensioni**" = probabilità di contatto "Altissima" | Tabella inventata; chi aggiunge "recensioni" sta confrontando, non prenotando | Togliere la riga |
| `come-scegliere-parole-chiave-attivita-locale.md:88` "**ogni** parola chiave deve contenere il riferimento geografico" | Contraddice l'esempio "nutrizionista vicino a me" (riga 18); Google deduce la posizione | "Nelle pagine dei servizi metti sempre la zona" |
| `errori-online-attivita-locali.md:74` "Sito vecchio/lento → **Google ti ignora**" | Esagerato | "Meno contatti, e Google ti preferisce chi è più utile" |
| `perche-professionista-locale-sito-web.md:47` "nessuno può toglierti visibilità" | Anche Google cambia | "nessun algoritmo social decide chi vede le tue informazioni" |
| `perche-professionista-locale-sito-web.md:28` "le recensioni dei pazienti" sul sito | Per le professioni sanitarie la pubblicità deve essere informativa; le testimonianze dei pazienti vanno valutate con l'Ordine | Aggiungere "(se il tuo Ordine lo consente)" |

### M4. Contenuti sottili

Soglie della skill (copertura, non obiettivi): servizio 800, articolo 1.500. Conteggio sul corpo, senza front matter e fonti.

| Pagina | Parole | Nota |
|---|---|---|
| `siti-web-frascati-castelli-romani.md` | **466** | Pagina servizio principale, sotto soglia. Proposta: aggiungere "Cosa mi serve da te" (testi, foto, accessi), "Cosa non faccio" (niente manutenzione a canone, niente gestione social, niente pubblicità a pagamento: rafforza anche il vincolo occasionale), il link ai casi e a `quanto-costa-sito-web` |
| `lavori/martina-iannotti-nutrizionista.md` | **173** | Unico caso pubblicato. "Com'è andata" (righe 29-33) promette "cosa è cambiato" (`lavori/_index.md:7`) ma riporta solo la testimonianza. Aggiungere fatti verificabili: quando è andato online, quante pagine, cosa aggiorna Martina da sola, una schermata della versione mobile |
| `google-business-sito-vetrina` / `perche-professionista-locale-sito-web` | 490 / 493 | Da unire (M2) |
| `perche-aggiornare-plugin-wordpress` | 534 | Ok come checklist; vedi M3 |
| `blog-e-trucchi-seo-semplici` | 566 | Aggiungere un esempio reale (il nome file e l'alt di una foto del sito di Martina, con permesso) |

### M5. Title troppo lunghi nel risultato di ricerca

Il template aggiunge " — Marco La Rocca" (17 caratteri) a ogni title senza `seoTitle` (`layouts/partials/shared/head.html:46`). Risultato: `perche-professionista` ~91 caratteri, `perche-aggiornare-plugin-wordpress` ~90, `ai-automazione-guida` ~85, `come-scegliere-parole-chiave` ~82, `errori-online` ~79. Google li taglierà. Aggiungere un `seoTitle` di 50-60 caratteri a questi cinque. Description lunghe: pagina servizio 178 caratteri (`siti-web-frascati-castelli-romani.md:6`), home 177 (`_index.md:3`, solo proposta).

---

## 4. Link interni

Mappa attuale (solo link nel testo, esclusi `/#contacts`):

- **Senza alcun link in entrata dal testo**: `ai-automazione-ristorante`, `chi-possiede-il-tuo-sito-dominio-hosting-accessi`, `perche-aggiornare-plugin-wordpress`, `sito-monopagina-o-sito-completo`, `sito-web-ristorante-cosa-deve-avere`.
- **Senza link in uscita**: `google-business-sito-vetrina`, `perche-aggiornare-plugin-wordpress`, `quanto-costa-sito-web`.
- La guida pillar AI non linka i 4 post verticali (riceve link solo da loro).
- La pagina servizio linka 2 articoli; la FAQ "Quanto costa" (`siti-web-frascati-castelli-romani.md:14`) cita "la guida su quanto costa un sito web" senza link.

Link da aggiungere (ordine di utilità):

1. `siti-web-frascati-castelli-romani.md` → `quanto-costa-sito-web` (FAQ riga 14), `chi-possiede-il-tuo-sito…` (riga 34, "dominio e accessi intestati a te"), `sito-web-ristorante-cosa-deve-avere` (esempio "ristorante Marino", riga 19).
2. `quanto-costa-sito-web.md:66` → `chi-possiede…` ("Il sito è mio alla fine?"); riga 44 → `sito-monopagina-o-sito-completo`.
3. `sito-monopagina-o-sito-completo.md:51` → `quanto-costa-sito-web`.
4. `sito-web-ristorante-cosa-deve-avere.md:34` ↔ `ai-automazione-ristorante.md:20` (TheFork in entrambi).
5. `ai-automazione-guida-attivita-locali.md` → i 4 verticali (sezione "Cosa può fare l'AI").
6. `google-business-sito-vetrina.md:47` → pagina servizio; `errori-online-attivita-locali.md:41` → `sito-web-ristorante…` o pagina servizio.
7. `perche-aggiornare-plugin-wordpress.md` → `chi-possiede…` (backup, accessi amministratore).

---

## 5. Priorità BASSA

### B1. Refusi e stile

| Evidenza | Correzione |
|---|---|
| `ai-automazione-guida-attivita-locali.md:85` "**Un email** automatica" (segnalato il 07/10, ancora presente) | "Un'email automatica" |
| `quanto-costa-sito-web.md:35` "**Qui è dove** le cose si complicano" (calco dall'inglese) | "Qui le cose si complicano" |
| `quanto-costa-sito-web.md:16` "Le 3 voci di costo **che nessuno ti spiega**"; riga 14 "una volta per tutte, con numeri veri" (le fasce non hanno fonte) | "Le 3 voci di costo"; "con numeri indicativi" e una riga "prezzi indicativi, ottobre 2026", come nella guida AI |
| `quanto-costa-sito-web.md:78` "Anni successivi ~30-100€" vs righe 74-75 (15€ + 0-80€) | "~15-100€/anno" |
| `come-scegliere-parole-chiave-attivita-locale.md:2` title in Title Case; `sito-monopagina…md:14,18,29` "Sito Standard", "Biglietto da Visita"; `google-business…md` "Sito Vetrina", "Scheda Google" | Maiuscola solo iniziale, come negli altri post |
| Formule tipiche dei testi generati: "Spoiler:" (`guida:16`), "La differenza chiave?" (`guida:44`), "vale oro" (`psicologo:38`), "oro puro" (`parole-chiave:52`), "La regola d'oro" (`parole-chiave:37`), "facciamo una cosa che quasi nessuno fa" (`psicologo:16`, `nutrizionista:16`), "Non è un costo enorme. È un investimento" (`quanto-costa:80`), "Questa è la trappola in cui cadono quasi tutti" (`plugin:18`), "l'investimento più potente" (`perche-professionista:18`) | Sostituire con frasi piane; il tono degli articoli del 07/10 (ristorante, chi possiede, GDPR) è il modello giusto: 0 lineette, 0 formule |
| Lineette lunghe (—): 12 nella guida AI, 12 in parole chiave, 5-8 negli altri post AI; 0 nei tre articoli nuovi | Uniformare allo stile dei post nuovi (virgole, due punti) |
| `blog/_index.md` senza `description` | La meta description della pagina /blog/ ricade su quella generale del sito. Aggiungere: "Guide pratiche su siti web, Google e strumenti digitali per professionisti e attività locali, scritte da Marco La Rocca." |

### B2. Date e lastmod

- Offset orari corretti per l'ora legale in tutti i file (controllati: novembre-marzo `+01:00`, aprile-ottobre `+02:00`).
- 13 articoli + pagina servizio + caso Martina hanno lo stesso `lastmod: 2026-10-07`. È vero (revisione del 07/10), e il template mostra "aggiornato il" solo oltre 48 ore. In futuro aggiornare `lastmod` solo per modifiche sostanziali, non per ritocchi, altrimenti la data perde valore come segnale.
- Tre articoli pubblicati lo stesso giorno (07/10 alle 08:00, 09:00, 10:00). Non è un problema, ma per i prossimi meglio distanziare le pubblicazioni.
- `quanto-costa-sito-web.md:2` "nel 2026" nel titolo: da aggiornare a gennaio 2027 insieme ai prezzi, oppure togliere l'anno.

### B3. Link delle fonti: redirect da aggiornare (tutti funzionano)

| URL nel testo | Destinazione finale |
|---|---|
| `https://developers.facebook.com/docs/whatsapp/pricing/` (`guida:164`, `ristorante:119`) | `https://developers.facebook.com/documentation/business-messaging/whatsapp/pricing` |
| `https://wordpress.org/documentation/article/wordpress-backups/` (`plugin:58`) | `https://developer.wordpress.org/advanced-administration/security/backup/` |
| `https://www.psy.it/codice-deontologico-degli-psicologi-italiani/` (`gdpr:93`, `psicologo:125`) | `https://www.psy.it/la-professione-psicologica/codice-deontologico-degli-psicologi-italiani/` |
| `https://pages.cloudflare.com/` (`quanto-costa:97`) | `https://www.cloudflare.com/products/pages/` |
| `https://search.google.com/search-console` (`chi-possiede:48,89`) | `https://search.google.com/search-console/about` |

Controllo di merito a campione: la pagina Vercel conferma "Hobby teams are restricted to non-commercial personal use only" (ok); la pagina Google 7091 contiene pertinenza/distanza/evidenza ma non il sito web (vedi M3); Normattiva apre la L. 132/2025.

---

## 6. Home (`content/_index.md`): solo proposte, nessuna modifica

I testi della home sono coerenti con il vincolo: "su richiesta, uno alla volta" (riga 57), "nessun canone" (righe 53, 62), "ogni modifica è un intervento a sé" (riga 70), prestazione occasionale spiegata (riga 68). Nessuna frase da agenzia. Proposte:

1. **FAQ pagamento, riga 68 (priorità media, precisione).** "Se sei un'impresa o un professionista con partita IVA, trattieni la ritenuta d'acconto del 20%" non vale per tutti: chi è in **regime forfettario** non è sostituto d'imposta e non applica la ritenuta. Molti dei destinatari del sito (nutrizionisti, psicologi a inizio attività) sono forfettari. Proposta: "Se sei un sostituto d'imposta (un'impresa, o un professionista in regime ordinario), trattieni la ritenuta d'acconto del 20% e la versi tu; se sei in regime forfettario, no." Da far confermare a un commercialista.
2. **Experience/Expertise (riga 56).** "il software è il mio mestiere" è vago. Aggiungere un dato verificabile senza nominare il datore di lavoro, per esempio: "Faccio lo sviluppatore software di professione da N anni" e, se c'è, il titolo di studio. È il segnale di competenza che oggi manca in tutto il sito (anche nel box autore).
3. **Servizi, righe 18 e 28.** "Collegamento con la scheda Google Business" ripetuto in entrambe le card. Nella seconda si può sostituire con "Nessun abbonamento a piattaforme, se non serve".
4. **Title della home (template `head.html:44`).** Vedi M2: differenziarlo dalla pagina servizio.
5. **Description, riga 3** (177 caratteri): accorciare sotto i 160, es. "Siti web per professionisti e attività di Frascati e dei Castelli Romani. Parli con chi li realizza, il sito è tuo e non paghi canoni."

---

## 7. E-E-A-T: cosa farebbe salire di più il punteggio

1. **Experience**: un secondo caso pubblicato (l'osteria, appena c'è il consenso) e, nel caso Martina, 3-4 fatti concreti. Negli articoli, un dettaglio vissuto per pezzo (es. in `chi-possiede…`: "mi è capitato di recuperare un dominio intestato a un ex fornitore", solo se vero).
2. **Expertise**: credenziali nel box autore (`layouts/partials/author-box.html`) e nello schema Person (`hasCredential` o `description`), e una pagina o ancora "chi sono" a cui puntare l'autore (oggi `url` = home).
3. **Trust**: risolvere A1 (coerenza con l'articolo GDPR). Pesa più di tutto il resto.
4. **AI citation**: aprire ogni H2 dei post lunghi con una frase-risposta autosufficiente; togliere emoji e titoli clickbait; un riepilogo in 3 punti in apertura della guida AI e di `quanto-costa`.

---

## 8. Dati strutturati per audit-data.json (categoria Content Quality)

```json
{
  "category": "Content Quality",
  "date": "2026-10-10",
  "score": 68,
  "eeat": {"experience": 45, "expertise": 62, "authoritativeness": 50, "trustworthiness": 66, "weighted": 57},
  "ai_citation_readiness": 60,
  "metadata_template": {"pages_checked": 21, "site_risk": "low", "templated_ratio": 0.0, "shared_cta_phrases": {}},
  "sources_checked": {"total": 32, "ok": 32, "redirects_to_update": 5},
  "findings": [
    {"id": "A1", "severity": "high", "title": "Post AI sanitari in contraddizione con l'articolo GDPR (minore/urgenza, invio automatico, raccolta sintomi, 'sembra scritto da te', 'funzionano da sole')", "files": ["content/blog/ai-automazione-psicologo.md:36,86-92", "content/blog/ai-automazione-nutrizionista.md:66,92", "content/blog/ai-automazione-osteopata.md:68-71,101,103,123", "content/blog/ai-automazione-guida-attivita-locali.md:60-62"]},
    {"id": "A2", "severity": "high", "title": "Articoli correlati manuali con titoli obsoleti", "files": ["content/blog/perche-professionista-locale-sito-web.md:55-57", "content/blog/errori-online-attivita-locali.md:86-88", "content/blog/come-scegliere-parole-chiave-attivita-locale.md:141-144"]},
    {"id": "A3", "severity": "high", "title": "Claim già segnalati ancora presenti (90%, 80%, 'senza fuffa', 'in automatico', 'il trucco', 'l'arma più potente', 30 minuti una tantum, costo segretaria)"},
    {"id": "M1", "severity": "medium", "title": "Frasi da attività continuativa residue (CTA template, 'controllo del sito', 'chiacchierata gratuita', 'alcune collaborazioni recenti')"},
    {"id": "M2", "severity": "medium", "title": "Cannibalizzazione home/pagina servizio e perche-professionista/google-business"},
    {"id": "M3", "severity": "medium", "title": "Inesattezze: soggetto obbligato art. 50 AI Act, rinvio senza fonte, fonte Google 7091 che non sostiene la tesi, somme e scenari incoerenti"},
    {"id": "M4", "severity": "medium", "title": "Pagina servizio 466 parole, caso Martina 173 parole"},
    {"id": "M5", "severity": "medium", "title": "Title oltre 75 caratteri con suffisso del template"},
    {"id": "L1", "severity": "medium", "title": "5 articoli senza link in entrata dal testo; pillar AI senza link ai verticali"},
    {"id": "B1", "severity": "low", "title": "Refusi e formule da testo generato ('Un email', 'Qui è dove', Title Case, emoji negli H3)"},
    {"id": "B3", "severity": "low", "title": "5 link fonte con redirect"},
    {"id": "HOME", "severity": "medium", "title": "Solo proposta: FAQ ritenuta d'acconto imprecisa per i forfettari; credenziali assenti"}
  ]
}
```
