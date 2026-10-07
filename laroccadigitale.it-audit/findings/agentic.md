# Agent-readiness: laroccadigitale.it (controllo del 2026-10-07)

## Sintesi
Il sito e leggibile dagli agenti: contenuto server-rendered (987 parole senza JS), albero di accessibilita buono, llms.txt valido, 404 reali. Il problema principale e una incoerenza di policy: robots.txt blocca tutti i crawler AI (compresi quelli di ricerca) mentre llms.txt li invita a citare il sito.

## Lighthouse Agentic Browsing
Non disponibile: PSI ha risposto HTTP 429 (quota giornaliera esaurita, nessuna API key configurata) sia per mobile sia per desktop. Nessuna frazione X/N riportata. Riprovare con una API key (`/seo google setup`). Riferimento: Lighthouse 13.5.0 (matrice verificata 2026-09-23).

## Agent-UX heuristic (separato da Lighthouse)
Punteggio 100/100, stato: complete. 9 button, 18-19 link, 0 widget div-onclick, 0 nodi interattivi senza nome, 652 nodi nell'albero. Quindi i toggle FAQ con `<button onclick>` sono esposti correttamente come ruolo button: non sono un difetto. Nota minore: 4 input senza aria (hanno comunque label).

## Policy di accesso (robots.txt)
- Training: GPTBot, ClaudeBot, anthropic-ai, Google-Extended, Applebot-Extended, CCBot, Bytespider, Amazonbot bloccati. Scelta coerente e legittima.
- Search: PerplexityBot bloccato (dal check: "search crawler bloccato alla radice"). Non risulta bloccato OAI-SearchBot/Claude-SearchBot (nessun gruppo, quindi consentiti da `*`). Il blocco di PerplexityBot esclude il sito dalle risposte di quel motore.
- User-triggered: ChatGPT-User bloccato (OpenAI: puo non applicare robots.txt). Claude-User non nominato, quindi consentito. Perplexity-User e Google-Agent in generale ignorano robots.txt: robots.txt non e un controllo di accesso.
- Content-Signal: assente (bozza/proposta Cloudflare, bozza IETF scaduta 2026-04-04, Google non la usa; verificato 2026-09-23). Opzionale.

## Findings per priorita
**P1 - Policy incoerente robots.txt vs llms.txt.** Evidenza: robots.txt Disallow per GPTBot, ChatGPT-User, ClaudeBot, PerplexityBot; llms.txt dice "Guida per ... ChatGPT, Perplexity, Claude, Gemini". Fix: decidere. Per un sito di lead generation locale conviene di solito consentire i bot di ricerca/utente (ChatGPT-User, PerplexityBot) e bloccare solo il training se lo si desidera. In alternativa lasciare tutto com'e e togliere dal llms.txt il riferimento ai bot bloccati. Non e garantito alcun effetto su ranking, citazioni o traffico.

**P2 - Email visibile solo dopo click (base64).** Gli agenti che leggono HTML/albero non vedono l'email; llms.txt la rimanda al form. E una scelta anti-spam accettabile. Fix proporzionato: nessuno obbligatorio; se si vuole, esporre l'email come testo/mailto o nel JSON-LD (`ContactPoint`), accettando piu spam.

**P2 - Form contatto Netlify senza testo di consenso privacy.** Evidenza: `<form class='contact-form' method='POST' name='contatto'>`; nella pagina esiste il link Iubenda alla privacy policy, ma non e legato al form. Non e un difetto di leggibilita per agenti, ma e una questione GDPR: aggiungere una riga "Inviando accetti la Privacy Policy" con link (e checkbox se il consenso va documentato). Gli agenti compilano il form piu facilmente se ogni campo ha label e una checkbox ha nome chiaro.

**P3 - Filtri blog con onclick su pill.** Se sono `<button>` vanno bene (score 100). Verificare che abbiano `aria-pressed` e che l'elenco completo degli articoli sia comunque nell'HTML e raggiungibile da link normali (paginazione o sitemap), cosi un agente senza JS vede tutto.

**P3 - FAQ.** `<button onclick>` ok. Miglioria facoltativa: `aria-expanded` e `aria-controls`; oppure `<details>` (nessun JS). Il testo delle risposte dovrebbe essere nel DOM anche se chiuso.

**P3 - llms.txt.** Passa le regole Lighthouse. Leggero miglioramento: l'email "tramite form" va bene; i tre link servizi puntano tutti a `/#servizi` (uguali). llms-full.txt assente (non necessario).

## Opportunita (non difetti)
- Markdown: nessuna versione (Accept: text/markdown restituisce HTML, `/index.md` 404). Nessun agente consumer confermato la richiede. Saltare.
- WebMCP: 0 tool registrati, 1 form non annotato. Bozza W3C Community Group, non standard (WebKit contrario, Mozilla neutrale; verificato 2026-09-23). Per un sito vetrina di questa dimensione non vale lo sforzo.
- /.well-known: ai-catalog.json (bozza), api-catalog, agent-card, ucp assenti o 404: non applicabili a un sito vetrina. Web Bot Auth (bozza IETF -00, 2026-09-01): riguarda chi invia traffico, non serve qui.

## Azioni consigliate (proporzionate)
1. Decidere la policy AI e allineare robots.txt e llms.txt (10 minuti).
2. Aggiungere testo di consenso privacy sotto il form.
3. Facoltativo: aria-expanded sulle FAQ, aria-pressed sui filtri.
4. Rieseguire Lighthouse Agentic con API key PSI per ottenere la frazione X/N.
