# DESIGN · V4 "Cartiglio"

Il sito come **una tavola di progetto**: carta da disegno chiara, tratto grafite, quote di misura attorno agli screenshot, un cartiglio con i dati di Marco. Un solo accento: ottone. Stesso linguaggio delle copertine del blog (`static/images/copertine/`), così sito e articoli sono fatti dalla stessa mano. Fonte: `assets/css/main.css`.

## Colori

| Token | Valore | Uso |
|---|---|---|
| `--paper` | `#f3f4f1` | fondo |
| `--paper-2` | `#e9eae6` | riquadri negli articoli, codice |
| `--line` | `#c9cdc8` | filetti secondari |
| `--ink` | `#22252a` | testo, filetti principali, bottone pieno, sezione contatti |
| `--ink-2` / `--ink-3` | `#4b4f56` / `#6b6f75` | testo secondario / etichette dati |
| `--brass` | `#b38b33` | accento unico: pallino del menu attivo, primo punto del metodo, focus, sottolineature dei link |
| `--brass-ink` | `#7e6020` | ottone per testo (hover dei link) |

L'ottone resta sotto il 3% della superficie. Sull'ottone il testo è sempre `--ink`.

## Tipografia

- **Schibsted Grotesk** 400-800 per tutto il testo; titoli 650, tracking −0,03/−0,04em.
- **Red Hat Mono** 400-500 **solo per dati**: quote di misura, etichette del cartiglio, date, categorie, numero tavola, etichette dei campi del modulo. Sempre maiuscolo, 0,7-0,76rem, tracking 0,04em. Mai per il testo corrente.

## Linee e forme

Filetti da 1px in grafite per le strutture (testata, sezioni, cartiglio, specifiche) e in `--line` per le divisioni interne. Angoli vivi ovunque. Nessuna ombra, nessun gradiente, nessuna griglia di sfondo. Su schermi oltre 1100px la pagina è racchiusa in una **cornice fissa da 1px** a 10px dal bordo, come il riquadro di una tavola.

## Componenti

- **Quote** (`partials/quoted.html`): ogni screenshot ha una quota orizzontale ("1440 px") e una verticale ("16 : 10") con estremità a T. Al caricamento le linee si tracciano: è l'unico momento animato.
- **Cartiglio**: tabella a due colonne (etichetta in mono · valore) con Autore, Luogo, Modalità ("Su richiesta, collaborazione occasionale"), Consegna, Ultimo lavoro.
- **Specifiche** (servizi): due colonne in un unico riquadro, voci numerate 01-06 in mono.
- **Tavole** (lavori): screenshot quotato su 7 colonne, testo su 4 con "Tav. 01 · luogo".
- **Metodo**: una linea orizzontale con tre punti, il primo in ottone; su mobile diventa verticale.
- **Elenco articoli**: titolo, categoria e data in mono; "Nuovo" in ottone solo sull'ultimo.
- **Contatti**: sezione grafite piena, modulo su carta con campi a sola linea di base.
- **Piè di pagina**: un cartiglio che contiene marchio, menu, dicitura fiscale e copyright.

## Movimento

Solo il tracciamento delle quote (scaleX/scaleY, 0,9s). Pallino ottone del menu che compare all'hover. Con `prefers-reduced-motion` tutto fermo.

## Da non fare

Altri colori d'accento. Monospace per testo che non sia un dato. Griglie millimetrate di sfondo (cliché). Mockup patinati, ombre, gradienti.
