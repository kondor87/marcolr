# Cosa resta da fare

## Subito, prima di pubblicare

- [ ] Guardare le tre versioni: `versioni/avvia-versioni.bat` (attuale su 8811, Targa su 8812, Programma su 8813).
- [ ] Rileggere il diff (`git diff`) e i 3 articoli nuovi.
- [ ] **iubenda → Cookie Solution → attivare "Google Consent Mode"**. Senza questo GA4 non riceve il consenso e conta solo in forma anonima.
- [ ] Controllare la data del lavoro Martina in `content/lavori/martina-iannotti-nutrizionista.md` (ho messo settembre 2025 come segnaposto; non viene mostrata, ma finisce nello schema).
- [ ] Commit e push. Netlify pubblica da solo.

## Subito dopo il deploy

- [ ] Aprire il sito con la console del browser (F12): nessun errore CSP, banner iubenda visibile, Clarity che registra.
- [ ] Search Console: inviare di nuovo `sitemap.xml` e chiedere l'indicizzazione di `/siti-web-frascati-castelli-romani/` e `/lavori/`.
- [ ] Verificare il redirect `/blog/siti-web-castelli-romani/` → nuova pagina (deve rispondere 301).
- [ ] PageSpeed Insights su home e un articolo, mobile.
- [ ] validator.schema.org su home, un articolo e il lavoro Martina.
- [ ] GA4: segnare come conversione la visita a `/grazie/`.

## Nelle prossime settimane

- [ ] Scegliere la grafica (consiglio V3 Programma) e applicarla seguendo `versioni/README.md`.
- [ ] Servire i font dal sito invece che da Google Fonts.
- [ ] Profilo LinkedIn personale con link al sito, e 2-3 raccomandazioni.
- [ ] Osteria Gemelli: quando il sito è online e il cliente acconsente, `draft: false` e completare "Com'è andata".
- [ ] Chiedere una testimonianza scritta (con consenso) a ogni nuovo cliente.
- [ ] Copertine originali per gli articoli che ne condividono una.

## Lavoro occasionale (con il commercialista)

- [ ] Togliere dai preventivi la **manutenzione annuale a canone** (Osteria: 180/390 €/anno). Proporre solo interventi singoli.
- [ ] Verificare il contratto da dipendente (fedeltà, esclusiva, non concorrenza).
- [ ] Tenere il conto dei compensi annui (soglia INPS dei 5.000 €).
- [ ] Usare con parsimonia le email a freddo.
