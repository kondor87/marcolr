# Global SEO Action Plan: laroccadigitale.it

Questo piano d'azione elenca i passi per portare la salute del sito al **Grado A (90+)**.

## 1. Priorità Critica (Fix Immediati) 🔴
- [ ] **Configurazione `og:image` globale**: Assicurarsi che ogni pagina abbia un'immagine di anteprima per i social (Home, Blog, Servizi).
- [ ] **Creazione `llms.txt`**: Creare il file `/llms.txt` per rendere il sito citabile dalle intelligenze artificiali (SearchGPT, Perplexity).
- [ ] **Riparare Pagine Orfane**: Aggiungere un link alla pagina `/archivio` nel footer o nel menu per permetterne la scansione completa.

## 2. Priorità Alta (Miglioramento Fiducia) ⚠️
- [ ] **Aggiornamento Schema Person**: Inserire i link social (`sameAs`) nel markup JSON-LD di Marco La Rocca.
- [ ] **Header di Sicurezza**: Aggiungere `Content-Security-Policy` (CSP) nelle impostazioni di Netlify (`netlify.toml`) o tramite tag meta.

## 3. Priorità Media (Contenuti) 🔵
- [ ] **Audit Leggibilità**: Semplificare le descrizioni dei servizi sulla homepage. Attualmente hanno un punteggio Flesch troppo basso (troppo complesse).
- [ ] **Link Interni**: Creare collegamenti diretti tra i singoli articoli del blog e le schede dei servizi correlate sulla home.

## 4. Manutenzione Permanente ✅
- [ ] **Monitoraggio Google Search Console**: Verificare settimanalmente che non appaiano nuovi errori di indicizzazione.
- [ ] **Esecuzione Audit Mensile**: Rilanciare `/seo audit` ogni 30 giorni per intercettare regressioni.

---

### Prossimo Win: IA-Ready
La creazione del file `llms.txt` è il task con il più alto rapporto "sforzo/risultato" per il 2026.
