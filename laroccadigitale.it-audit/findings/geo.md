# GEO / AI Search Readiness — laroccadigitale.it

Data audit: 2026-10-07 · Ambito: sito live + sorgenti Hugo (`static/robots.txt`, `static/llms.txt`, `layouts/`, `content/blog/`) · Nessun file sorgente modificato.

---

## 1. GEO Readiness Score: **54 / 100**

| Dimensione | Peso | Punteggio | Ponderato | Motivazione sintetica |
|---|---|---|---|---|
| Citabilità | 25% | 58 | 14,5 | Tabelle prezzi/ROI concrete e sezioni "In sintesi", ma statistiche senza fonte (0 link esterni in 13 post su 14), aperture di sezione narrative e non "risposta diretta", pochi H2 in forma di domanda |
| Leggibilità strutturale | 20% | 70 | 14,0 | H2/H3 coerenti, TOC automatico, tabelle markdown, HTML statico pulito. Contro: emoji nei titoli (⚙️ 🤖 ✅), titoli "creativi" poco interrogativi |
| Contenuti multimodali | 15% | 40 | 6,0 | Solo cover + 1 diagramma (`ai-vs-automazione.png`); nessun video/YouTube, nessuno screenshot di casi reali |
| Autorità e brand | 20% | 35 | 7,0 | Author box presente, ma `sameAs` = solo GitHub, nessun LinkedIn/GBP/YouTube, omonimo giornalista "Marco La Rocca" domina le SERP, nome brand incoerente, nessuna pagina "Chi sono" |
| Accessibilità tecnica | 20% | 60 | 12,0 | SSR completo (Hugo statico, 200 a tutti gli UA, nessun X-Robots-Tag), ma robots.txt blocca PerplexityBot e ChatGPT-User; llms.txt incompleto e fuori formato |
| **Totale** | | | **53,5 ≈ 54** | |

---

## 2. Stato accesso crawler AI (robots.txt live = `static/robots.txt`, identici)

Verifica tecnica: tutte le richieste con UA OAI-SearchBot / Claude-SearchBot / PerplexityBot / GPTBot ricevono **HTTP 200** (Netlify non blocca a livello server). Il blocco è solo dichiarativo in robots.txt, quindi lo rispettano solo i bot che seguono robots.txt.

| Bot | Funzione reale | Stato attuale | Effetto |
|---|---|---|---|
| **OAI-SearchBot** | Indice di ChatGPT Search (citazioni) | **Consentito** (non elencato → ricade in `*`) | OK, ma per caso, non per scelta |
| **ChatGPT-User** | Fetch on-demand quando un utente chiede a ChatGPT di aprire un URL | **Bloccato** | Negativo: ChatGPT può rifiutarsi di leggere la pagina quando un utente la incolla/chiede |
| GPTBot | Training modelli OpenAI | Bloccato | Nessun effetto su ChatGPT Search; limita la "conoscenza" del brand nel modello |
| **Claude-SearchBot** | Indice di ricerca di Claude | **Consentito** (via `*`) | OK |
| **Claude-User** | Fetch on-demand per richieste utente su Claude | **Consentito** (via `*`) | OK |
| ClaudeBot | Training Anthropic | Bloccato | Nessun effetto sulla ricerca di Claude |
| anthropic-ai | Token deprecato | Bloccato | Irrilevante, rimuovere |
| **PerplexityBot** | Indice di Perplexity (citazioni) | **Bloccato** | **Molto negativo**: il sito è di fatto escluso dalle risposte Perplexity |
| Perplexity-User | Fetch su richiesta utente | Consentito (via `*`) | Perplexity dichiara che in genere non applica robots.txt a questo agente |
| Google-Extended | Training Gemini/Vertex **e grounding Gemini** | Bloccato | NON incide su Google Search né su AI Overviews (quelli seguono Googlebot). Può ridurre l'uso dei contenuti nel grounding dell'app Gemini |
| Googlebot / Bingbot | Search classica + AI Overviews / Copilot | Consentiti | OK: AIO e Copilot non sono toccati dal robots attuale |
| Applebot-Extended | Solo training Apple Intelligence | Bloccato | Nessun effetto su Siri/Spotlight/Safari (che seguono Applebot, consentito) |
| CCBot | Common Crawl (dataset usato da molti LLM) | Bloccato | Riduce la presenza dell'entità nei dataset di training |
| Bytespider | ByteDance (training, aggressivo) | Bloccato | Corretto |
| FacebookBot / Amazonbot | Meta / Alexa | Bloccati | Impatto minimo; Meta-ExternalAgent non è gestito |

### La contraddizione

`llms.txt` dice "Guida per crawler e assistenti AI (ChatGPT, Perplexity, Claude, Gemini)" e chiede di citare "Marco La Rocca". Il robots.txt invece blocca **proprio** PerplexityBot e ChatGPT-User. Il risultato è un invito con la porta chiusa: Perplexity non indicizza il sito, ChatGPT non apre le pagine su richiesta dell'utente e Gemini perde il grounding. Per un freelance locale che vive di passaparola e di raccomandazioni, i blocchi sul training non proteggono nulla di valore: i contenuti sono marketing educativo, non un prodotto da monetizzare. In compenso tolgono "memoria" del brand ai modelli.

### Policy raccomandata (variante A: massima visibilità, consigliata)

Logica:
1. **Ricerca/retrieval/utente**: sempre consentiti (OAI-SearchBot, ChatGPT-User, Claude-SearchBot, Claude-User, PerplexityBot, Perplexity-User).
2. **Training dei grandi laboratori**: consentito. Per un brand piccolo e con omonimi, essere nei dati di training aiuta i modelli a sapere che "Marco La Rocca, web designer a Frascati" esiste. Google-Extended va consentito anche perché governa il grounding di Gemini.
3. **Bloccati solo** gli scraper aggressivi o senza ritorno per un'attività italiana locale (Bytespider).
4. Gruppi espliciti anche per i bot consentiti: documentano la scelta ed evitano che una futura regola `*` li blocchi per sbaglio.

**robots.txt pronto (sostituire integralmente `static/robots.txt`):**

```
# robots.txt — laroccadigitale.it
# Policy: visibilità massima su motori di ricerca e assistenti AI.
# Ultimo aggiornamento: 2026-10

# --- Motori di ricerca classici (includono Google AI Overviews e Bing Copilot)
User-agent: *
Allow: /

# --- AI Search / retrieval (citazioni nelle risposte)
User-agent: OAI-SearchBot
Allow: /

User-agent: Claude-SearchBot
Allow: /

User-agent: PerplexityBot
Allow: /

# --- Fetch su richiesta dell'utente (l'utente chiede all'assistente di aprire una pagina)
User-agent: ChatGPT-User
Allow: /

User-agent: Claude-User
Allow: /

User-agent: Perplexity-User
Allow: /

# --- Training / grounding (consentiti: aiutano i modelli a conoscere il brand)
User-agent: GPTBot
Allow: /

User-agent: ClaudeBot
Allow: /

# Google-Extended: training Gemini + grounding Gemini. Non influisce su Search/AI Overviews.
User-agent: Google-Extended
Allow: /

# Applebot-Extended: solo training Apple Intelligence. Siri/Spotlight seguono Applebot.
User-agent: Applebot-Extended
Allow: /

User-agent: CCBot
Allow: /

User-agent: Meta-ExternalAgent
Allow: /

# --- Bloccati: scraper aggressivi senza beneficio per un'attività locale italiana
User-agent: Bytespider
Disallow: /

Sitemap: https://laroccadigitale.it/sitemap.xml
```

### Variante B (alternativa conservativa: citazioni sì, training no)

Se Marco preferisce non cedere i testi al training, deve **comunque** sbloccare ricerca e utente. Sostituire il blocco "Training" sopra con:

```
User-agent: GPTBot
Disallow: /

User-agent: ClaudeBot
Disallow: /

User-agent: CCBot
Disallow: /

User-agent: Applebot-Extended
Disallow: /

User-agent: Meta-ExternalAgent
Disallow: /

# Google-Extended: lasciarlo Allow anche in variante B, perché bloccarlo
# toglie il sito anche dal grounding di Gemini (non solo dal training).
User-agent: Google-Extended
Allow: /
```

Nota tecnica Hugo: `hugo.toml` ha `enableRobotsTXT = true` ma non esiste `layouts/robots.txt`, quindi oggi vince il file statico (il live coincide con `static/robots.txt`). Per evitare ambiguità future conviene tenere **una sola fonte**: o si lascia il file statico e si mette `enableRobotsTXT = false`, o si sposta il contenuto in `layouts/robots.txt`.

---

## 3. llms.txt: **presente ma malformato e incompleto**

URL: https://laroccadigitale.it/llms.txt (200, text/plain, identico al sorgente). `llms-full.txt`: 404. RSL 1.0 (`/license.xml`): assente (opzionale, priorità bassa).

### Problemi rilevati

| # | Problema | Gravità |
|---|---|---|
| 1 | **Elenca 8 post su 14.** Mancano proprio i più recenti e i più "citabili": `ai-automazione-guida-attivita-locali` (guida pilastro, 1.251 parole), `come-scegliere-parole-chiave-attivita-locale` (1.252 parole, ultimo post), `siti-web-castelli-romani` (landing Geo-SEO), `errori-online-attivita-locali`, `perche-professionista-locale-sito-web`, `sito-monopagina-o-sito-completo` | Alta |
| 2 | Formato non conforme a llmstxt.org: le righe `# laroccadigitale.it — llms.txt`, `# Guida per...`, `# Formato:...` e `# Chi sono` sono **quattro H1** in Markdown (non commenti). Lo standard prevede **un solo H1** (nome del progetto), poi il blockquote di sintesi, poi sezioni H2 | Media |
| 3 | I 3 servizi puntano tutti allo stesso frammento `/#servizi`: nessuna informazione distinta, niente prezzi o tempi | Media |
| 4 | Nessuna descrizione dopo i link (`- [Titolo](url): descrizione`): l'LLM non sa cosa contiene ogni pagina | Media |
| 5 | Titolo incoerente: "SEO locale: trucchi semplici" contro il titolo reale "Perché Avere un Blog: 4 Trucchi SEO Pratici" | Bassa |
| 6 | Mancano dati di entità: niente email, P.IVA, link a profili (GitHub, LinkedIn, Google Business), niente data di aggiornamento | Media |
| 7 | File statico, da aggiornare a mano a ogni post, e infatti è già disallineato di 6 articoli | Alta (causa radice) |

### llms.txt corretto (pronto, da sostituire a `static/llms.txt`)

```
# Marco La Rocca — Siti web e automazione AI a Frascati (laroccadigitale.it)

> Marco La Rocca è un web designer freelance con sede a Frascati (RM). Realizza siti web, SEO locale e automazioni/AI per professionisti e piccole attività dei Castelli Romani (Frascati, Grottaferrata, Marino, Albano Laziale, Velletri, Genzano, Rocca di Papa, Castel Gandolfo) e di Roma. Clienti tipici: ristoranti, nutrizionisti, psicologi, osteopati. Il sito resta di proprietà del cliente, senza canoni mensili.

Ultimo aggiornamento: 2026-10-07. Autore di tutti i contenuti: Marco La Rocca. Da non confondere con l'omonimo giornalista.

## Servizi
- [Realizzazione siti web](https://laroccadigitale.it/#servizi): siti vetrina e multipagina per professionisti locali, consegna in circa 2-3 settimane, nessun canone.
- [SEO locale](https://laroccadigitale.it/#servizi): ottimizzazione per ricerche geolocalizzate e Google Business Profile nei Castelli Romani.
- [AI e automazione](https://laroccadigitale.it/#servizi): prenotazioni, promemoria, chatbot e follow-up per studi e attività.
- [Siti web nei Castelli Romani](https://laroccadigitale.it/blog/siti-web-castelli-romani/): pagina territoriale su Frascati, Grottaferrata, Marino, Velletri.

## Guide principali
- [AI e automazione per piccole attività: la guida onesta](https://laroccadigitale.it/blog/ai-automazione-guida-attivita-locali/): differenza tra AI e automazione, costi reali, percorso in 3 step.
- [Quanto costa un sito web? Guida ai prezzi reali](https://laroccadigitale.it/blog/quanto-costa-sito-web/): costi di dominio, hosting e realizzazione, con una tabella di confronto delle fasce di prezzo.
- [Come scegliere le parole chiave per un'attività locale](https://laroccadigitale.it/blog/come-scegliere-parole-chiave-attivita-locale/): metodo gratuito di keyword research locale.

## AI per settore
- [AI per ristoranti](https://laroccadigitale.it/blog/ai-automazione-ristorante/): chatbot WhatsApp, risposte alle recensioni, ROI stimato.
- [AI per nutrizionisti](https://laroccadigitale.it/blog/ai-automazione-nutrizionista/): form pre-visita, diario fotografico, follow-up.
- [AI per psicologi](https://laroccadigitale.it/blog/ai-automazione-psicologo/): scheduling, lista d'attesa, screening del primo contatto.
- [AI per osteopati](https://laroccadigitale.it/blog/ai-automazione-osteopata/): chatbot rispetto alla segreteria part-time, promemoria, recensioni.

## Presenza online per professionisti
- [5 errori online che fanno perdere clienti](https://laroccadigitale.it/blog/errori-online-attivita-locali/): scheda Google, sito, recensioni, social.
- [Perché un professionista ha bisogno di un sito web](https://laroccadigitale.it/blog/perche-professionista-locale-sito-web/): sito proprio rispetto ai soli social.
- [Sito monopagina o completo?](https://laroccadigitale.it/blog/sito-monopagina-o-sito-completo/): tre tipologie di sito e come scegliere.
- [Google Business e sito vetrina](https://laroccadigitale.it/blog/google-business-sito-vetrina/): perché servono entrambi.
- [Perché avere un blog: 4 trucchi SEO pratici](https://laroccadigitale.it/blog/blog-e-trucchi-seo-semplici/): scrittura SEO semplice per non tecnici.
- [Perché aggiornare i plugin WordPress](https://laroccadigitale.it/blog/perche-aggiornare-plugin-wordpress/): sicurezza e manutenzione.

## Contatti
- [Modulo di contatto](https://laroccadigitale.it/#contacts): Frascati, Castelli Romani, Roma.
- [GitHub](https://github.com/kondor87)

## Optional
- [Archivio completo](https://laroccadigitale.it/archivio/)
- [Sitemap](https://laroccadigitale.it/sitemap.xml)
```

(Aggiungere email, LinkedIn e la scheda Google Business nella sezione Contatti appena disponibili.)

**Soluzione strutturale (consigliata):** generare llms.txt da Hugo, così ogni nuovo post entra in automatico. Va aggiunto un output format `llms` (`mediaType = "text/plain"`, `baseName = "llms"`, `isPlainText = true`) a `outputs.home`, con un template home che itera su `where site.RegularPages "Section" "blog"` stampando `- [{{ .Title }}]({{ .Permalink }}): {{ .Description }}`. Poi si **elimina** `static/llms.txt`, altrimenti sovrascrive l'output generato.

---

## 4. Citabilità dei passaggi

**Punti di forza**
- `quanto-costa-sito-web`: la tabella "Soluzione / Costo indicativo / Pro / Contro" (fai da te 0-150€/anno, template WP 300-800€, freelance 800-2.500€, agenzia 3.000-10.000€+) è il passaggio più citabile del sito: numeri precisi, autosufficiente, risponde alla domanda "quanto costa un sito web".
- I post AI per settore hanno sezioni "Il ROI" con tabelle prima/dopo: formato ideale per l'estrazione.
- Sezioni "In sintesi" finali in 4 post: buoni blocchi riassuntivi.
- La distinzione ricorrente "questa è automazione / questa è AI" è un angolo originale e ripetibile, cioè un buon "information gain".

**Debolezze**
1. **Statistiche senza fonte.** In 13 post su 14 non c'è nessun link esterno. Esempi: "il 53% degli utenti se ne va se il sito impiega più di 3 secondi" (dato Google/DoubleClick 2016, non citato), "il 70% delle ricerche locali da smartphone", "i no-show calano dell'80%", "aderenza dal 30% a oltre il 70%", "il 90% dei professionisti sbaglia". Gli LLM e Google favoriscono affermazioni attribuite. Serve la fonte esterna o, per i dati propri, una formula esplicita del tipo "nei progetti che ho seguito (n clienti, 2025-2026)...".
2. **Aperture non dirette.** Molte sezioni iniziano con un aneddoto o una domanda retorica ("Pensi che il blog sia morto? Sbagliato."). Le prime 40-60 parole dopo ogni H2 dovrebbero contenere la risposta secca.
3. **Titoli H2 poco interrogativi.** Solo pochi sono domande ("Quanto costa?", "Quali zone dei Castelli Romani..."). Esempi da convertire: "Le 3 voci di costo che nessuno ti spiega" → "Quali sono i costi fissi di un sito web?"; "La distinzione che fa la differenza" → "Che differenza c'è tra AI e automazione per un nutrizionista?".
4. **Emoji nei titoli** (⚙️ 🤖 ✅ ❌): finiscono negli anchor del TOC e nei testi estratti, aggiungono rumore senza dare informazioni.
5. **Post brevi** (530-580 parole: `google-business-sito-vetrina`, `perche-aggiornare-plugin-wordpress`, `perche-professionista-locale-sito-web`, `blog-e-trucchi-seo-semplici`): poche risposte autonome. Vanno ampliati o consolidati.
6. **Il prezzo di Marco non è dichiarato.** Il sito spiega i prezzi di mercato, ma un assistente che riceve la domanda "quanto costa un sito da Marco La Rocca a Frascati?" non trova una risposta citabile. Basta un passaggio del tipo "Un sito vetrina realizzato da me parte da X€, consegna in 2-3 settimane, nessun canone".
7. **FAQ in home senza schema FAQPage.** Il testo è nell'HTML (bene, è visibile ai crawler) ma non è marcato. Il beneficio è modesto: i rich result FAQ di Google sono limitati, ma il markup aiuta comunque la comprensione Q/A.

**Esempio di riscrittura (apertura citabile, circa 60 parole):**
> **Quanto costa un sito web per un professionista nel 2026?** Un sito vetrina costa in genere tra 800 e 2.500€ se realizzato da un freelance, più circa 15€/anno di dominio e 30-80€/anno di hosting (o hosting gratuito su Netlify per siti statici). Con il fai da te (Wix, Squarespace) si spendono 0-150€/anno, ma con limiti di SEO locale e design.

---

## 5. Chiarezza dell'entità (Marco La Rocca, Frascati)

| Segnale | Stato | Nota |
|---|---|---|
| Schema Person + ProfessionalService in home | Presente, collegati via `@id` | Buona base |
| `sameAs` | Solo `github.com/kondor87` | Mancano LinkedIn, Google Business Profile (URL Maps/CID), eventuale Instagram/YouTube |
| Omonimia | **Critica** | Su it.wikipedia "Marco La Rocca" compare come firma giornalistica (fonte citata nella voce "Jens Frederik Nielsen"); Bing per "Marco La Rocca web designer Frascati" restituisce it.wikipedia e ilfattoquotidiano.it. Il modello deve ricevere segnali forti di disambiguazione: professione + città + dominio sempre insieme |
| Nome del brand | Incoerente | Il dominio dice "La Rocca Digitale", che **non compare mai** come nome. WebSite = "Marco La Rocca — Siti Web Frascati", ProfessionalService = "Marco La Rocca — Siti Web", og:site_name = "Marco La Rocca". Va scelto un nome canonico (es. "La Rocca Digitale — Marco La Rocca") con `alternateName` |
| `streetAddress: "Frascati"` | Errato | Meglio omettere `streetAddress` (servizio senza sede aperta al pubblico) che ripetere la città |
| Telefono / email / P.IVA | Assenti in schema e in pagina | Segnali di fiducia e NAP mancanti. La P.IVA nel footer è anche un obbligo di legge in Italia per un'attività |
| BlogPosting.author | Solo `name` | Aggiungere `"@id": "https://laroccadigitale.it/#person"` e `url`, oltre a `publisher` e `mainEntityOfPage` |
| `dateModified` | Uguale a `datePublished` | Nessun `lastmod` nel front matter: attivare `enableGitInfo = true` o aggiungere `lastmod` |
| Pagina "Chi sono" dedicata | Assente | Manca una "entity home" (`/chi-sono/`) con bio, anni di esperienza, progetti, foto, link ai profili: è la pagina che gli LLM useranno per descrivere Marco |
| Portfolio / testimonianze | 1 progetto (martinaiannottinutrizione.it), 1 testimonianza | Prova sociale troppo scarsa per la raccomandazione; servono 3-5 casi con numeri |
| `jobTitle` | "Web Designer e Consulente AI" | Bene; riusarlo identico ovunque (LinkedIn, GBP, author box) |

---

## 6. Analisi delle menzioni di brand

| Piattaforma | Stato | Impatto GEO |
|---|---|---|
| Wikipedia / Wikidata | Nessuna voce (normale per un freelance); omonimo giornalista presente come fonte | Non creare una voce Wikipedia (non enciclopedico). Si può valutare un item Wikidata solo se esistono fonti terze |
| Reddit | Nessuna menzione rilevabile (API non accessibile, ricerche senza risultati) | Partecipare in modo genuino a r/italy, r/ItaliaPersonalFinance, r/webdev_it / r/Roma su domande "quanto costa un sito" |
| YouTube | Nessun canale rilevato | Il segnale più correlato con le citazioni AI (~0,74). Bastano 4-6 video brevi che riprendono i post (costi sito, AI per ristoranti) con link al sito in descrizione |
| LinkedIn | Non collegato dal sito | Creare o collegare il profilo, con titolo e città identici allo schema |
| Google Business Profile | Non collegato da schema/llms.txt | Fondamentale per Gemini/AIO locali e per il "near me": inserirlo in `sameAs` |
| Directory locali / stampa locale | Nessuna rilevata | Citazioni NAP su Pagine Gialle, directory del Comune o della Pro Loco di Frascati, blog locali dei Castelli Romani |

(Le verifiche sono manuali e indicative: DataForSEO non era disponibile, quindi non c'è un tracciamento live delle menzioni negli LLM.)

---

## 7. Punteggi per piattaforma

| Piattaforma | Punteggio | Fattore limitante |
|---|---|---|
| Google AI Overviews | 55 | Googlebot consentito; limitano autorità debole, statistiche senza fonte e pochi segnali locali (GBP non collegato) |
| ChatGPT (Search) | 42 | OAI-SearchBot consentito, ma ChatGPT-User bloccato; dipende dall'indice Bing; entità debole e omonimo |
| Perplexity | 15 | **PerplexityBot bloccato**: di fatto escluso dalle citazioni |
| Bing Copilot | 50 | Bingbot consentito; da verificare la sitemap in Bing Webmaster Tools e IndexNow |
| Claude | 45 | Claude-SearchBot e Claude-User consentiti; entità debole |
| Gemini (app) | 35 | Google-Extended bloccato, quindi grounding limitato |

---

## 8. Le 5 modifiche a maggior impatto

| # | Azione | Impatto | Effort |
|---|---|---|---|
| 1 | **Sostituire robots.txt** con la variante A (o almeno la B): sbloccare PerplexityBot, ChatGPT-User e Google-Extended, rimuovere `anthropic-ai` | Molto alto: riapre Perplexity e ChatGPT-on-demand e risolve la contraddizione con llms.txt | 10 min |
| 2 | **Rifare llms.txt** con tutti i 14 post, un solo H1 e descrizioni; poi generarlo da template Hugo | Alto | 20 min (manuale) / 1-2 h (template) |
| 3 | **Rafforzare l'entità**: nome brand canonico + `alternateName`, `sameAs` (LinkedIn, GBP), email/telefono/P.IVA, BlogPosting.author con `@id`, `lastmod`, pagina `/chi-sono/` | Alto: disambigua dall'omonimo | 3-4 h |
| 4 | **Rendere citabili i passaggi chiave**: fonti esterne per le statistiche (53%, 70%), riformulare come "dato interno" le percentuali proprie, H2 a domanda, risposta nelle prime 40-60 parole, togliere le emoji dagli H2, dichiarare i propri prezzi | Alto | 4-6 h per 14 post (partire da quanto-costa, guida AI e parole chiave) |
| 5 | **Segnali di brand off-site**: collegare il GBP, 4-6 video YouTube brevi, profilo LinkedIn coerente, 2-3 citazioni locali, 3-5 case study con numeri | Medio-alto (cumulativo nel tempo) | 2-4 settimane, continuativo |

Extra a bassa priorità: schema FAQPage per le FAQ della home; `llms-full.txt`; RSL 1.0 `license.xml` (dichiarazione di licenza AI-use, oggi poco supportata); verifica di Bing Webmaster Tools e IndexNow per ChatGPT/Copilot.

---

## 9. Dati strutturati per audit-data.json (categoria "AI Search Readiness")

```json
{
  "category": "AI Search Readiness",
  "score": 54,
  "dimensions": {"citability": 58, "structural_readability": 70, "multimodal": 40, "authority_brand": 35, "technical_accessibility": 60},
  "platform_scores": {"google_aio": 55, "chatgpt": 42, "perplexity": 15, "bing_copilot": 50, "claude": 45, "gemini": 35},
  "findings": [
    {"id": "geo-robots-contradiction", "severity": "critical", "title": "robots.txt blocca PerplexityBot e ChatGPT-User mentre llms.txt invita gli assistenti AI", "evidence": "static/robots.txt == live; PerplexityBot Disallow: /, ChatGPT-User Disallow: /", "fix": "Sostituire con la policy variante A in findings/geo.md", "effort": "10m"},
    {"id": "geo-google-extended", "severity": "medium", "title": "Google-Extended bloccato: limita il grounding Gemini (non AIO/Search)", "fix": "Allow", "effort": "1m"},
    {"id": "geo-llms-incomplete", "severity": "high", "title": "llms.txt elenca 8 post su 14 e usa 4 H1", "evidence": "Mancano 6 post, tra cui la guida AI, le parole chiave e la landing Castelli Romani", "fix": "llms.txt corretto + generazione da template Hugo", "effort": "20m-2h"},
    {"id": "geo-unsourced-stats", "severity": "high", "title": "Statistiche senza fonte (0 link esterni in 13/14 post)", "fix": "Citare le fonti o etichettare come dati interni", "effort": "4-6h"},
    {"id": "geo-entity-ambiguity", "severity": "high", "title": "Entità debole e omonimo (giornalista Marco La Rocca); sameAs solo GitHub; brand 'La Rocca Digitale' mai usato", "fix": "Nome canonico, alternateName, sameAs LinkedIn/GBP, pagina /chi-sono/, P.IVA/contatti", "effort": "3-4h"},
    {"id": "geo-blogposting-author", "severity": "medium", "title": "BlogPosting.author senza @id/url, dateModified sempre = datePublished", "fix": "author @id #person, publisher, enableGitInfo/lastmod", "effort": "30m"},
    {"id": "geo-no-video-brand", "severity": "medium", "title": "Nessuna presenza YouTube/Reddit/LinkedIn rilevata", "fix": "4-6 video brevi, LinkedIn coerente, partecipazione a Reddit", "effort": "settimane"},
    {"id": "geo-ssr-ok", "severity": "pass", "title": "SSR completo, 200 a tutti gli UA AI, nessun X-Robots-Tag"}
  ]
}
```
