# Re-check di laroccadigitale.it, 17 ottobre 2026

Sito online: commit 8279b2f, pubblicato il 10/10 alle 19:37. Search Console: dati fino al 14/10 (ritardo normale).

## "siti web frascati": cosa dicono i dati

- In Search Console, da agosto a oggi, **non c'è nessuna impressione per la query esatta "siti web frascati"**: il sito non compariva nelle prime pagine per quella ricerca nemmeno prima. Quello che si vede cercando da sé è influenzato da posizione, cronologia e personalizzazione.
- Le query vicine sono stabili: "realizzazione siti internet frascati" (home, posizione 12-15, uguale da agosto), "realizzazione siti web castelli romani" (posizione 11-13).
- Il 7/10 il vecchio articolo `/blog/siti-web-castelli-romani/` è stato spostato con un 301 su `/siti-web-frascati-castelli-romani/`. Google ha registrato il redirect il 13/10 e la nuova pagina è indicizzata dal 13/10, ma nei dati fino al 14/10 le impressioni sono ancora attribuite al vecchio indirizzo. **Il passaggio è in corso**: di solito si assesta in 2-6 settimane.
- La home ("Siti web a Frascati e Castelli Romani") e la pagina servizio ("Realizzazione siti web a Frascati e Castelli Romani") puntano alla stessa ricerca: Google le alterna. Proposta: titolo della home centrato sulla persona, ricerca geografica lasciata alla pagina servizio (serve il sì di Marco).

## Indicizzazione (URL Inspection)

| Pagina | Stato | Ultima scansione |
|---|---|---|
| / | Indicizzata | 11/10 |
| /siti-web-frascati-castelli-romani/ | Indicizzata | 13/10 |
| /lavori/ | Indicizzata | 10/10 |
| /lavori/martina-iannotti-nutrizionista/ | Indicizzata | 10/10 |
| /blog/ | Indicizzata | 12/10 |
| /blog/siti-web-castelli-romani/ | Redirect riconosciuto, canonica = pagina servizio | 13/10 |

## Punteggi

| Area | 7/10 | 10/10 | 17/10 |
|---|---|---|---|
| Tecnico | 68 | 92 | 95 (26/26 pagine ok, redirect ok, nessun link rotto) |
| Dati strutturati | – | 38 | 95 (24 blocchi validi su 26 pagine) |
| Lighthouse mobile home: prestazioni / accessibilità / SEO | – | 49 / – / – | 55 / 99 / 100 (peso pagina da 540-745 KiB a 347 KiB) |
| UI/UX (impeccable, /32) | 21 | 22 | 23 |

Il collo di bottiglia della velocità ora è solo **iubenda**: circa 2,3 s di lavoro sul telefono e 0,9 s di blocco del primo disegno. Gli unici script esterni rimasti sono iubenda e Clarity; tutto il resto è link.

## Corretto oggi (da pubblicare)

- Pagina servizio: sotto il titolo, frase di apertura, pulsanti "Raccontami cosa ti serve" / "Guarda i lavori" e la scheda del lavoro per Martina con la sua frase (prima la pagina sembrava un articolo, senza azioni fino in fondo).
- Anteprima dei lavori: si vede dall'alto, logo compreso (prima era tagliata al centro).
- Titoli negli articoli più compatti su telefono; riquadri negli articoli senza bordo laterale spesso; sottotitolo del caso Martina meno pesante.
- Footer: colore dei link che puntava a una variabile inesistente.
- Tocchi da 44px su foto nel menu e indice degli articoli; nessuno scorrimento orizzontale da 320px in su.
- Salto a #contacts su telefono: il titolo non finisce più sotto il menu.

## Da decidere (Marco)

1. Titolo della home (cannibalizzazione con la pagina servizio).
2. Clarity e banner cookie: Clarity non raccoglie dati (piano iubenda gratuito). Senza Clarity il sito non usa cookie non tecnici, il banner non è obbligatorio e il telefono guadagna circa 2 secondi.
