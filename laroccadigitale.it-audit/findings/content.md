# Content Quality / E-E-A-T: blog di laroccadigitale.it

Data audit: 2026-10-07. Fonte: `content/blog/*.md` (14 post + `_index.md`), template `layouts/blog/single.html`, `layouts/_default/baseof.html`.
Metodo: lettura integrale dei post, conteggio parole (corpo, senza front matter), indice Gulpease, scansione dei caratteri Unicode invisibili, controllo metadati con `metadata_template.py` (euristico), mappa dei link interni.
Nessun post è stato modificato.

---

## 1. Punteggi sintetici

| Metrica | Punteggio | Nota |
|---|---|---|
| **Qualità contenuti (complessiva)** | **52/100** | Leggibilità buona, struttura pulita, ma numeri inventati, duplicazioni e rischi di compliance |
| E-E-A-T: Experience (20%) | 30/100 | Nessun caso reale; il "caso reale" del post nutrizionista è un'ipotesi ("Immagina questa situazione") |
| E-E-A-T: Expertise (25%) | 50/100 | Spiegazioni chiare (AI vs automazione), ma errori tecnici (Google Translate "non AI", "Google non ha gli occhi", densità keyword, penalità per contenuti duplicati) |
| E-E-A-T: Authoritativeness (25%) | 25/100 | Zero fonti esterne in 13/14 post (unico link esterno: business.google.com) |
| E-E-A-T: Trustworthiness (30%) | 40/100 | Statistiche non verificabili, incoerenze interne nelle tabelle ROI, nessun caveat GDPR/AI Act nei post sanitari, nessun `lastmod` |
| **E-E-A-T pesato** | **37/100** | Modello interno della skill, non pesi Google |
| **AI citation readiness** | **45/100** | Buoni H2 a domanda e tabelle; penalizzati da numeri senza fonte, emoji negli heading, nessun TL;DR o blocco FAQ, definizione duplicata 5 volte |
| Metadati templati | site_risk **low** | `templated_ratio` 0.0, nessuna `shared_cta_phrases`, nessun flag |

---

## 2. Rischio "prestazione occasionale" (PRIORITÀ ALTA)

Marco è un dipendente e realizza siti solo come prestazione occasionale (senza Partita IVA). Le frasi qui sotto descrivono un'attività abituale, continuativa o organizzata (base di clienti ricorrente, servizi ricorrenti, offerta a livelli o pacchetti). Vanno riformulate. Questo è un rilievo editoriale, non un parere fiscale: la valutazione formale spetta a un commercialista.

| Post | Testo | Rischio | Riformulazione suggerita |
|---|---|---|---|
| siti-web-castelli-romani | "Dai dati che analizzo **costantemente per i miei clienti**" | **Alto** (abitualità + affermazione non verificabile) | Eliminare. Al suo posto: "Da ricerche fatte con Google Trends / Search Console sul mio sito…", con fonte |
| siti-web-castelli-romani | "Realizzo siti web… con un focus particolare su Frascati"; "sono uno sviluppatore web e consulente" | Medio | "Mi capita di realizzare, occasionalmente, siti per…". Evitare "consulente" come qualifica professionale |
| perche-aggiornare-plugin-wordpress | Tutto il post è un pitch di manutenzione ricorrente: "qualcuno che **di tanto in tanto** entri, faccia i backup, aggiorni…"; "**Io dico sempre**: …il tuo lavoro è fatturare" | **Alto** | Trasformarlo in una checklist per fare da sé, oppure togliere la CTA di manutenzione. In alternativa, depubblicare (vedi §8) |
| google-business-sito-vetrina | "Quando realizzo un sito per un professionista, il collegamento… **fanno sempre parte del lavoro**" | Medio | "Se ti realizzo il sito, ti spiego anche come collegarlo alla scheda" |
| ai-automazione-guida-attivita-locali | "**Totale 'pacchetto completo'** ~80-150€/mese" e "Il percorso consigliato: 3 step" (settimana 1-2, mese 2-3, mese 3+) | Medio | "Totale strumenti (canoni dei fornitori)". Presentare il percorso come fai-da-te, non come accompagnamento di più mesi |
| sito-monopagina-o-sito-completo | Tre livelli (Monopagina / Standard / "Sito Segretario", "livello Pro") | Basso-medio (sembra un listino a pacchetti) | Presentarli come tipologie di sito generiche, non come offerta propria |
| ai-automazione-ristorante | "la domanda che mi fanno **più spesso i ristoratori** dei Castelli Romani" | Medio | "Una domanda che sento spesso, anche tra amici ristoratori…" oppure eliminare |
| perche-professionista-locale-sito-web | "la domanda che **mi fanno spesso i professionisti** (nutrizionisti, terapisti, consulenti)" | Medio | Come sopra |
| ai-automazione-psicologo | "un'obiezione che **sento spesso**" | Basso | Neutralizzare |
| errori-online-attivita-locali | "lo sento dire spessissimo", "Situazioni che vedo troppo spesso" | Basso | Accettabile se riferito alla navigazione web, non ai clienti |

**Fuori dal blog, ma sullo stesso tema (template):** il box autore ("Aiuto le attività locali a crescere grazie all'AI e all'automazione"), lo schema Person con `jobTitle: "Web Designer e Consulente AI"` e `worksFor: #business` (LocalBusiness) presentano un'impresa strutturata. Va segnalato all'orchestratore (categoria Schema/Trust).

---

## 3. Statistiche non verificabili o inventate (PRIORITÀ ALTA)

Nessuno dei numeri sotto ha una fonte. Diversi sono anche incoerenti con il resto dello stesso post. In base alle QRG, affermazioni non verificabili su risparmi ed entrate abbassano la Trust. Inoltre sono proprio i passaggi che un LLM citerebbe, propagando dati falsi.

| Post | Affermazione | Problema |
|---|---|---|
| errori-online, siti-web-castelli-romani | "il 70% delle ricerche locali viene fatto da smartphone" | Senza fonte, ripetuto in 2 post |
| errori-online | "più di 3 secondi → il 53% degli utenti se ne va" | È il dato Google/DoubleClick del 2016, valido solo per i siti mobile. Citarlo con anno e fonte oppure eliminarlo |
| errori-online | "Una risposta… a una critica vale più di 10 recensioni a 5 stelle" | Inventato |
| ai-automazione-osteopata | "i no-show calano dell'80%" (2 volte, anche in un H2); "70% dei benefici al 10% del costo"; "Errori umani: quasi zero" | Inventati. "Quasi zero errori" è falso per un chatbot LLM (allucinazioni) |
| ai-automazione-psicologo | "i no-show calano dal 15-20% al 3-5%" | **Incoerenza interna**: con 20-25 sedute/settimana (~90/mese), un 15-20% di no-show fa 13-18 assenze/mese, ma la tabella ROI dello stesso post indica 4/mese |
| ai-automazione-nutrizionista | "L'aderenza passa dal 30% a oltre il 70%"; "~30% → ~10% spariscono"; "8-10 ore a settimana" | Inventati. Il titolo promette "8 ore", la tabella indica un risparmio di 6-7 h |
| ai-automazione-ristorante | "Il ritorno è di oltre 10 volte"; "Recensioni con risposta 20% → 95%" | **Incoerenza**: il calcolo usa 360€/anno di costo, la tabella 500-800€/anno. 6.240/800 = 7,8x, non ">10x" |
| ai-automazione-guida | "I primi due step risolvono l'80% dei problemi"; "segretaria part-time 600-900€/mese" | 80% senza fonte. Il costo aziendale di una segretaria part-time (CCNL Studi professionali) è sottostimato: citare la fonte o eliminare il confronto |
| come-scegliere-parole-chiave | "9 volte su 10", "il 90% dei professionisti sbaglia" | Inventati |
| sito-monopagina | "Nel 90% dei casi"; "si ripaga letteralmente nei primi mesi" | Inventati |
| perche-professionista | "risparmiando decine di ore ogni mese" | Inventato |
| Tutte e 4 le tabelle ROI dei post AI | Incassi recuperati 1.500-6.000€/anno | Le ipotesi non sono dichiarate. Etichettarle come "esempio ipotetico" e mostrare la formula, come già fa bene `quanto-costa-sito-web` ("Se il tuo sito ti porta anche solo 2 clienti…") |

**Altre inesattezze tecniche da correggere:**
- **ai-automazione-guida**: "Traduzione… in modo naturale (non come Google Translate)". Anche Google Translate è AI (traduzione automatica neurale): l'esempio contraddice la tesi stessa del post.
- **blog-e-trucchi-seo-semplici**: "Google non ha gli occhi, legge solo il testo" (falso: Google analizza le immagini). Il nome del file "vale oro" (è un segnale minore). "Google penalizza chi non formatta i testi" (falso).
- **come-scegliere-parole-chiave**: "Titolo della pagina (H1)" confonde il `<title>` con l'H1. "È il fattore SEO più importante" è un'esagerazione. "3-5 volte in 600 parole è perfetto" ripropone il mito della densità di keyword. "Google penalizza i contenuti duplicati": Google li filtra, non li penalizza, salvo intento manipolativo. "Primi 100 parole" va corretto in "Prime 100 parole".
- **quanto-costa-sito-web**: consiglia Vercel gratuito per il sito di un professionista, ma il piano Hobby di Vercel vieta l'uso commerciale. "Wix e Squarespace sono più lenti → Google penalizza" è una generalizzazione.
- **google-business-sito-vetrina**: la sezione Q&A della scheda Google è in dismissione (da verificare alla data di pubblicazione). Il tag "google my business" usa il vecchio nome. "Un segreto che molti ignorano" è clickbait.
- **ai-automazione-ristorante**: "Un chatbot WhatsApp… zero commissioni" (la WhatsApp Business API è a pagamento per conversazione). "TheFork prende una commissione su ogni prenotazione" va precisato (dipende dal canale e dal piano). Refuso: "risponderegli".
- **perche-aggiornare-plugin-wordpress**: "Aggiornare prima i moduli minori, e solo per ultimi i componenti vitali" è un consiglio discutibile (meglio staging e controllo della compatibilità con il core). "carrozziere" va corretto in "meccanico". La data usa `+01:00` a ottobre, ma l'ora legale richiede `+02:00`.
- **ai-automazione-guida**: "Un email" va corretto in "Un'email".
- **ai-automazione-osteopata**: "si configurano una volta e poi funzionano da sole". Falso per i chatbot, che vanno monitorati.

---

## 4. Post sanitari: GDPR art. 9, AI Act, deontologia (PRIORITÀ ALTA)

I post per psicologi, nutrizionisti e osteopati suggeriscono di raccogliere ed elaborare **dati relativi alla salute** con strumenti extra-UE (Calendly, Typeform, Google Forms, ChatGPT, app di riconoscimento foto, WhatsApp) e con chatbot LLM, **senza alcuna avvertenza**. Per un pubblico di professionisti sanitari è il punto più debole del blog sul piano della Trust (YMYL). Espone anche l'autore: un consiglio pubblicato che porta il lettore a un trattamento illecito.

**Caveat mancanti (inserire un box "Privacy e regole" in ciascun post o nel post unificato):**
1. **GDPR art. 9**: anamnesi, patologie, allergie, stato psicologico e foto dei pasti di un paziente in percorso sono dati sanitari. Servono una base giuridica idonea, informativa, minimizzazione e sicurezza.
2. **Art. 28 (DPA) e trasferimenti extra-UE (capo V)**: un contratto di nomina a responsabile con ogni fornitore e la verifica del Data Privacy Framework o delle SCC (Calendly, Typeform e OpenAI sono statunitensi).
3. **Art. 35 (DPIA)**: probabilmente necessaria per chatbot che trattano dati sanitari su larga scala o con tecnologie nuove.
4. **AI Act (Reg. UE 2024/1689) art. 50**: obbligo di informare l'utente che sta interagendo con un sistema di AI, in vigore dal 2 agosto 2026 e quindi già applicabile. Nessun post lo menziona.
5. **L. 132/2025 (legge italiana sull'AI)**: per le professioni intellettuali, l'AI può essere usata solo come supporto e il professionista deve informare il cliente. Citare l'articolo dopo verifica.
6. **Deontologia e pubblicità sanitaria**: il Codice deontologico degli psicologi (segreto professionale, consenso per i minori) e le regole sulla pubblicità sanitaria (osteopatia, professione sanitaria ai sensi della L. 3/2018).

**Passaggi specifici da riscrivere:**
- **psicologo**: "Primo contatto e **screening** intelligente". Lo "screening" è un atto clinico e un chatbot non deve farlo. L'esempio "è per mio figlio di 14 anni" riguarda un minore (consenso di entrambi i genitori). Il follow-up generato dall'AI "dopo una seduta intensa" richiede di passare contenuti clinici a un LLM. Manca un protocollo di crisi: un chatbot su un sito di psicologia deve indirizzare ai numeri di emergenza in caso di ideazione suicidaria.
- **nutrizionista**: il chatbot risponde a "Posso mangiare la pizza durante il percorso?" in modo personalizzato, che equivale a un consiglio professionale. "lasci inviare in automatico se ti fidi" va eliminato o accompagnato da un'avvertenza. Il questionario su patologie e allergie con Google Forms richiede una nota privacy.
- **osteopata**: il chatbot scrive "L'osteopatia può essere indicata per problematiche cervicali", cioè un'indicazione sanitaria generata dall'AI. Il messaggio WhatsApp "spero che la schiena stia già meglio" per chiedere una recensione rivela dati sanitari su un canale terzo.
- **ristorante** (non sanitario, ma stesso rischio): un chatbot AI che risponde "uno è celiaco, avete qualcosa?" tocca le informazioni sugli allergeni (Reg. UE 1169/2011). Una risposta allucinata è un rischio per la salute e per la responsabilità del ristoratore. Serve un caveat: "per allergeni, rimanda sempre al personale".
- **sito-monopagina**: suggerisce questionari Typeform per "filtrare i pazienti". Serve la stessa nota GDPR.

---

## 5. Duplicazioni tra i 5 post AI

I 5 post (`ai-automazione-*`) condividono la stessa struttura, che si stima copra il 35-45% di ciascun post:

| Blocco ripetuto | guida | nutriz. | osteo. | psico. | ristor. |
|---|---|---|---|---|---|
| H2 "AI vs automazione" + **stessa immagine** `/images/ai-vs-automazione.png` con **stesso alt** | x | x | x | x | x |
| Elenco "Automazione = regole fisse… / AI = il sistema capisce il contesto…" | x | x | x | x | x |
| Calendly / Cal.com / promemoria 24h | x | x | x | x | (TheFork) |
| "Non è un menu con bottoni… È un assistente che conversa" | x | | x | | x |
| Follow-up "versione automazione vs versione AI" | | x | x | x | |
| Tabella "Il ROI" "Senza automazione/AI \| Con automazione + AI" | (costi) | x | x | x | x |
| Obiezione "Ma io non sono un tecnico / non capisco di tecnologia" con analogia di un professionista esterno | | | x (elettricista) | x (variante) | x (commercialista) |
| "facciamo una cosa che (quasi) nessuno fa: essere onesti" | | x | | x | |
| CTA quasi identica "cosa ha senso automatizzare, dove l'AI aggiunge valore" | x | x | x | x | |

Altre immagini riusate: `blog_website_local_pro.png` in 3 post (errori-online, perche-professionista, siti-web-castelli-romani) e `blog_scelta_sito.png` in 2 (quanto-costa, sito-monopagina).

**Raccomandazione:** tenere la definizione e l'immagine **solo nella guida pillar**. Nei post verticali basta una frase più un link: "Se non hai chiara la differenza tra AI e automazione, parti da [qui](/blog/ai-automazione-guida-attivita-locali/)". Unire i 3 post sanitari (vedi §8).

---

## 6. Cannibalizzazione delle keyword

| Cluster | Pagine in competizione | Azione |
|---|---|---|
| "siti web / realizzazione siti Frascati Castelli Romani" | **Homepage** (tagline "Realizzazione siti internet a Frascati e Castelli Romani") e `siti-web-castelli-romani` (title "Realizzazione Siti Web Castelli Romani…") | Intento commerciale identico. O si sposta il post in una landing fuori dal blog con un focus diverso (es. pagina per comune), o si riscrive in chiave informativa ("Come scegliere chi ti fa il sito ai Castelli Romani") con un link in evidenza alla home |
| "perché un professionista ha bisogno di un sito / sito vs social / sito + Google Business" | `perche-professionista-locale-sito-web`, `google-business-sito-vetrina`, `errori-online` §2-3 | Unire i primi due. In `errori-online` lasciare 2 righe più un link |
| "automazione studio / gestione pazienti AI" | `ai-automazione-psicologo`, `-osteopata`, `-nutrizionista` (tag "gestione pazienti AI" identico in osteopata e nutrizionista) | Unire in un unico post per studi sanitari con sezioni per professione, oppure differenziare i contenuti per almeno il 60% |
| "AI per piccole attività" | guida e i 4 post verticali | Accettabile come pillar con cluster, **ma solo se collegati** (oggi 0 link) |
| "SEO pratica / titoli / nomi immagini" | `blog-e-trucchi-seo-semplici` e `come-scegliere-parole-chiave` | Sovrapposizione bassa, già collegati in un verso. Aggiungere il link di ritorno |

---

## 7. Link interni

- **10 post su 14 hanno 0 link nel corpo verso altri post**: tutti e 5 i post AI, blog-e-trucchi, google-business, plugin-wordpress, quanto-costa, sito-monopagina.
- Il blocco "potrebbe interessarti anche" nel template usa `shuffle`, quindi cambia a ogni build. È casuale e non tematico, per cui non costruisce cluster.
- Solo `siti-web-castelli-romani` linka ai servizi (`/#servizi`). Tutti gli altri linkano solo a `/#contacts`.

**Mappa minima consigliata:**
- guida AI → i 4 post verticali (e viceversa: i verticali → guida)
- quanto-costa ↔ sito-monopagina ↔ perche-professionista
- google-business ↔ errori-online ↔ siti-web-castelli-romani
- blog-e-trucchi ↔ come-scegliere-parole-chiave
- Template: sostituire `shuffle` con `.Site.RegularPages.Related .` (correlazione per tag/categorie di Hugo)

---

## 8. Verdetto per post

| # | Post | Parole | Gulpease | Verdetto | Top 3 fix |
|---|---|---|---|---|---|
| 1 | ai-automazione-guida-attivita-locali | ~1050 | 74 | **Tenere** (pillar) | 1) Correggere l'esempio Google Translate ed eliminare "80%" / il costo della segretaria non fondato. 2) Aggiungere la sezione "Regole: AI Act art. 50 + GDPR" e i link ai 4 verticali. 3) "pacchetto completo" → "totale strumenti"; accorciare il title (68 car.) e la description (177 car.) |
| 2 | ai-automazione-nutrizionista | ~1020 | 78 | **Unire** (post "AI e automazione per studi sanitari") | 1) Togliere l'H2 "Il caso reale" su uno scenario ipotetico ("Immagina…") e il dato aderenza 30→70%. 2) Box GDPR art. 9 (questionari, app foto, DPA, trasferimenti extra-UE); niente invio automatico. 3) Title senza la promessa "8 ore"; eliminare il blocco AI vs automazione duplicato |
| 3 | ai-automazione-osteopata | ~1000 | 79 | **Unire** (come sopra) | 1) Eliminare "-80% no-show", "70% al 10% del costo", "errori quasi zero". 2) Il chatbot non deve dare indicazioni sanitarie; regole sulla pubblicità sanitaria; niente dati sanitari nelle richieste di recensione. 3) Tabella ROI con ipotesi dichiarate |
| 4 | ai-automazione-psicologo | ~920 | 79 | **Unire / riscrivere** (rischio più alto) | 1) Togliere "screening" e l'esempio del minore; aggiungere il protocollo di crisi e il segreto professionale. 2) Sconsigliare il follow-up AI basato sul contenuto delle sedute; informativa L. 132/2025 e AI Act. 3) Correggere l'incoerenza no-show 15-20% vs 4/mese |
| 5 | ai-automazione-ristorante | ~975 | 81 | **Riscrivere** | 1) Rendere coerenti ROI e costi (non ">10x"), correggere "zero commissioni" WhatsApp e la commissione TheFork. 2) Caveat su allergeni e celiachia (Reg. 1169/2011). 3) Togliere "mi fanno più spesso i ristoratori"; eliminare il blocco duplicato; refuso "risponderegli" |
| 6 | blog-e-trucchi-seo-semplici | ~525 | 81 | **Riscrivere** (sottile) | 1) Correggere "Google non ha gli occhi" e "penalizza chi non formatta". 2) Title e description meno clickbait ("l'arma più potente"); aggiungere esempi reali. 3) Link a come-scegliere e alla guida |
| 7 | come-scegliere-parole-chiave-attivita-locale | ~1085 | 76 | **Tenere** (il migliore) | 1) Togliere "9 su 10", "90%" e la regola "3-5 volte in 600 parole". 2) Distinguere `<title>` e H1; "duplicati penalizzati" → "filtrati". 3) Aggiungere uno screenshot reale di autocomplete/PAA per Frascati (Experience); "Primi" → "Prime" |
| 8 | errori-online-attivita-locali | ~640 | 87 | **Tenere** + fix | 1) Citare o togliere 70% e 53%. 2) Eliminare "vale più di 10 recensioni" e la contraddizione "30 minuti una tantum" vs "rispondi a tutte". 3) Introduzione di una sola riga: aggiungere un contesto; immagine riusata |
| 9 | google-business-sito-vetrina | ~470 | 75 | **Unire** con #11 | 1) Q&A in dismissione e nome "Google My Business" da aggiornare. 2) Togliere "un segreto che molti ignorano"; aggiungere la fonte Google sui fattori di ranking locale (pertinenza, distanza, prominenza). 3) "fanno sempre parte del lavoro" → formulazione occasionale |
| 10 | perche-aggiornare-plugin-wordpress | ~480 | 71 | **Riscrivere come checklist fai-da-te o depubblicare** | 1) Togliere il pitch di manutenzione ricorrente e "Io dico sempre". 2) Correggere l'ordine di aggiornamento (backup, staging, core, plugin, test); "carrozziere"; offset della data. 3) Incongruenza: il sito di Marco è su Hugo, non WordPress. Chiarire il perché del tema o rimuovere il post |
| 11 | perche-professionista-locale-sito-web | ~500 | 81 | **Unire** con #9 (301) | 1) Togliere "la domanda che mi fanno spesso i professionisti". 2) Eliminare "decine di ore ogni mese" e "clienti in automatico" (description). 3) Un unico post "Sito, scheda Google e social: cosa serve davvero a un professionista" |
| 12 | quanto-costa-sito-web | ~600 | 83 | **Tenere** + fix | 1) Vercel Hobby non consentito per uso commerciale: proporre Netlify o Cloudflare Pages verificandone i termini. 2) Aggiungere "prezzi aggiornati a [mese/anno]" e un `lastmod`. 3) Link a sito-monopagina e perche-professionista; smorzare "Wix più lento → penalizza" |
| 13 | siti-web-castelli-romani | ~565 | 73 | **Riscrivere** | 1) Eliminare "dati che analizzo costantemente per i miei clienti" e "consulente". 2) Risolvere la cannibalizzazione con la home (vedi §6); togliere "facilmente dominare" e il 70%. 3) Title di 77 car. e description di 184: accorciare a ~60 e ~155 |
| 14 | sito-monopagina-o-sito-completo | ~615 | 73 | **Tenere** + fix | 1) Presentare i 3 tipi senza effetto listino ("livello Pro"). 2) Nota GDPR sui questionari per filtrare i pazienti. 3) Togliere "nel 90% dei casi"; link a quanto-costa |

Parole: conteggio del corpo senza front matter, markup e link. Nessun post supera la soglia indicativa di 1.500 parole per un blog post, che è un riferimento di copertura e non un obiettivo. I veri post "sottili" sono #6, #9, #10, #11 e #13 (~470-565 parole) e si sovrappongono tra loro.

---

## 9. Leggibilità, stile, tracce di AI

- **Gulpease 71-87**: tutti i post sono accessibili a un lettore con licenza media. Paragrafi brevi e un buon uso di elenchi e tabelle. Nessun intervento necessario sulla leggibilità di base.
- **Unicode invisibile**: scansione delle categorie Cf/Zs (ZWSP, ZWJ, NBSP, soft hyphen, BOM ecc.). **Nessun carattere trovato** in tutti i 14 file.
- **Lineette (—)**: 11-15 per post nei post AI e in come-scegliere, 0 nei post più vecchi. È un marcatore tipico della scrittura LLM e mostra lo stacco di stile tra i post vecchi e quelli recenti.
- **Formule ricorrenti tipiche dei testi generati**: "Spoiler:", "Ecco dove…", "La differenza chiave?", "Non è X. È Y." (3 post), "La regola d'oro" (2 post), "vale oro" / "oro puro" (3 post), "senza fuffa", "facciamo una cosa che quasi nessuno fa", tabelle "In sintesi" in chiusura (3 post), H2 "Il ROI: …" identici.
- **Emoji negli H2/H3** (⚙️ 🤖 ✅ ❌) nei post AI: finiscono nell'indice dei contenuti e negli id delle ancore, e peggiorano l'estrazione dei passaggi da parte dei motori AI. Meglio spostarle nel testo o in un badge.
- **Title clickbait**: "Risparmia 8 Ore a Settimana" (nutrizionista) e "Risparmia 10 Ore a Settimana" (ristorante) sono promesse numeriche non dimostrate. Poi "la guida onesta (senza fuffa)", "Accoppiata Vincente", "puoi facilmente dominare", "Un segreto che molti ignorano", "l'arma più potente".
- **Metadati**: `metadata_template.py` restituisce site_risk **low** (0/14 templati, nessuna CTA condivisa nelle description). Le CTA "Scrivimi, senza impegno" sono nel corpo di 12/14 post e non nei metadati, il che va bene.

---

## 10. AI citability (struttura dei passaggi)

**Punti di forza:** H2 spesso formulati come domande ("Quanto costa?", "Quando conviene"), tabelle comparative, definizione netta di AI e automazione nella guida (molto citabile, se esistesse solo lì).

**Da migliorare:**
1. Aprire ogni H2 con una frase-risposta autosufficiente di 40-60 parole, citabile da sola, con soggetto esplicito (non "Questo è…").
2. Dare una fonte con link a ogni numero, oppure togliere il numero. Un LLM che cita "i no-show calano dell'80%" attribuendolo a laroccadigitale.it è un rischio reputazionale.
3. Aggiungere un riepilogo di 3 punti in apertura nei post lunghi e un blocco FAQ reale (con FAQPage solo se le FAQ sono visibili).
4. Una sola definizione canonica (guida) invece di 5 varianti quasi uguali, che diluiscono il segnale.
5. Aggiungere `lastmod` nel front matter: oggi `dateModified` = `datePublished` per tutti i post. Aggiungere all'autore nello schema BlogPosting `url` e `sameAs`, che puntino alla pagina "chi sono".

---

## 11. Experience: cosa aggiungere

- Nessun post contiene un caso documentato. Prove reali e lecite già disponibili: la costruzione del proprio sito (stack Hugo, punteggi Lighthouse, configurazione di GA4/GTM/Clarity/Search Console, screenshot di autocomplete e PAA per "Frascati"), test di strumenti fatti in prima persona con data e risultato.
- Etichettare sempre gli scenari ipotetici come "esempio" (il post nutrizionista oggi presenta un'ipotesi come "caso reale").
- Bio autore: aggiungere competenze verificabili (formazione, GitHub già in `sameAs`, progetti) senza qualifiche da impresa.

---

## 12. Dati strutturati per audit-data.json (categoria Content Quality)

```json
{
  "category": "Content Quality",
  "score": 52,
  "eeat": {"experience": 30, "expertise": 50, "authoritativeness": 25, "trustworthiness": 40, "weighted": 37},
  "ai_citation_readiness": 45,
  "metadata_template": {"site_risk": "low", "templated_ratio": 0.0, "shared_cta_phrases": {}},
  "findings": [
    {"id": "CQ-01", "severity": "high", "title": "Formulazioni che implicano attività abituale (incompatibile con prestazione occasionale)", "pages": ["siti-web-castelli-romani", "perche-aggiornare-plugin-wordpress", "google-business-sito-vetrina", "ai-automazione-guida-attivita-locali", "ai-automazione-ristorante", "perche-professionista-locale-sito-web", "sito-monopagina-o-sito-completo"]},
    {"id": "CQ-02", "severity": "high", "title": "Statistiche senza fonte e tabelle ROI incoerenti", "pages": ["errori-online-attivita-locali", "siti-web-castelli-romani", "ai-automazione-osteopata", "ai-automazione-psicologo", "ai-automazione-nutrizionista", "ai-automazione-ristorante", "ai-automazione-guida-attivita-locali", "come-scegliere-parole-chiave-attivita-locale", "sito-monopagina-o-sito-completo"]},
    {"id": "CQ-03", "severity": "high", "title": "Nessun caveat GDPR art. 9 / AI Act art. 50 / L. 132/2025 / deontologia nei post sanitari (YMYL)", "pages": ["ai-automazione-psicologo", "ai-automazione-nutrizionista", "ai-automazione-osteopata"]},
    {"id": "CQ-04", "severity": "high", "title": "Scenario ipotetico presentato come 'caso reale'", "pages": ["ai-automazione-nutrizionista"]},
    {"id": "CQ-05", "severity": "medium", "title": "Blocco 'AI vs automazione' e stessa immagine/alt duplicati in 5 post (~35-45% di sovrapposizione)", "pages": ["ai-automazione-guida-attivita-locali", "ai-automazione-nutrizionista", "ai-automazione-osteopata", "ai-automazione-psicologo", "ai-automazione-ristorante"]},
    {"id": "CQ-06", "severity": "medium", "title": "Cannibalizzazione: post Castelli Romani vs homepage; perche-professionista vs google-business; 3 post sanitari", "pages": ["siti-web-castelli-romani", "perche-professionista-locale-sito-web", "google-business-sito-vetrina"]},
    {"id": "CQ-07", "severity": "medium", "title": "10/14 post senza link interni nel corpo; correlati casuali (shuffle)", "pages": ["*"]},
    {"id": "CQ-08", "severity": "medium", "title": "Inesattezze tecniche (Google Translate, 'Google non ha gli occhi', densità keyword, Vercel Hobby commerciale, Q&A GBP, WhatsApp zero commissioni)", "pages": ["ai-automazione-guida-attivita-locali", "blog-e-trucchi-seo-semplici", "come-scegliere-parole-chiave-attivita-locale", "quanto-costa-sito-web", "google-business-sito-vetrina", "ai-automazione-ristorante"]},
    {"id": "CQ-09", "severity": "medium", "title": "Title clickbait con promesse numeriche", "pages": ["ai-automazione-nutrizionista", "ai-automazione-ristorante", "ai-automazione-guida-attivita-locali", "siti-web-castelli-romani"]},
    {"id": "CQ-10", "severity": "low", "title": "Post sottili e sovrapposti (~470-565 parole)", "pages": ["google-business-sito-vetrina", "perche-aggiornare-plugin-wordpress", "perche-professionista-locale-sito-web", "blog-e-trucchi-seo-semplici", "siti-web-castelli-romani"]},
    {"id": "CQ-11", "severity": "low", "title": "Marcatori stilistici da LLM (lineette, emoji negli heading, formule ripetute); nessun Unicode invisibile", "pages": ["ai-automazione-*", "come-scegliere-parole-chiave-attivita-locale"]},
    {"id": "CQ-12", "severity": "low", "title": "Nessun lastmod; dateModified = datePublished; autore nello schema senza url/sameAs", "pages": ["*"]},
    {"id": "CQ-13", "severity": "low", "title": "Refusi: risponderegli, Primi 100 parole, Un email, carrozziere; offset +01:00 a ottobre", "pages": ["ai-automazione-ristorante", "come-scegliere-parole-chiave-attivita-locale", "ai-automazione-guida-attivita-locali", "perche-aggiornare-plugin-wordpress"]}
  ],
  "verdicts": {
    "ai-automazione-guida-attivita-locali": "keep",
    "ai-automazione-nutrizionista": "merge",
    "ai-automazione-osteopata": "merge",
    "ai-automazione-psicologo": "merge+rewrite",
    "ai-automazione-ristorante": "rewrite",
    "blog-e-trucchi-seo-semplici": "rewrite",
    "come-scegliere-parole-chiave-attivita-locale": "keep",
    "errori-online-attivita-locali": "keep",
    "google-business-sito-vetrina": "merge",
    "perche-aggiornare-plugin-wordpress": "rewrite-or-unpublish",
    "perche-professionista-locale-sito-web": "merge",
    "quanto-costa-sito-web": "keep",
    "siti-web-castelli-romani": "rewrite",
    "sito-monopagina-o-sito-completo": "keep"
  }
}
```

Nota: i riferimenti normativi (AI Act art. 50, L. 132/2025, Reg. 1169/2011, L. 3/2018) vanno verificati sul testo vigente prima di citarli nei post. Questo audit non costituisce consulenza legale o fiscale.
