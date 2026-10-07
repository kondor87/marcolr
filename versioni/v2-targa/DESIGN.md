# DESIGN · V2 "Peperino"

Palette dei Castelli Romani (pietra di peperino, intonaco, ottone, nero) usata in forma **piatta e contemporanea**. Nessun rilievo, nessuna vite, nessun pulsante 3D: l'ottone è un colore d'accento, non un materiale finto. Fonte: `assets/css/main.css`.

## Colori

| Token | Valore | Uso |
|---|---|---|
| `--stone-900` | `#2c2e2a` | testata, piè di pagina, sezioni scure profonde |
| `--stone-800` | `#383a35` | hero e sezioni scure (con grana leggerissima) |
| `--stone-950` | `#222420` | cornici degli screenshot |
| `--on-stone` / `--on-stone-2` | `#eeece6` / `#c1bfb6` | testo su pietra / testo secondario |
| `--wall` | `#e3e4e0` | fondo di lettura |
| `--wall-3` | `#c3c5bf` | filetti su fondo chiaro |
| `--ink` / `--ink-2` | `#1b1c1a` / `#474842` | testo principale / secondario |
| `--brass` | `#c09a45` | bottone principale, punti elenco, sottolineature, stato attivo |
| `--brass-hi` | `#d9bb72` | accento su fondo scuro (H1, link, "Com'è andata") |
| `--brass-ink` | `#8a6a24` | ottone scuro per testo su fondo chiaro (numeri del metodo, marker) |

Regola: l'ottone non supera il 5-8% della superficie. Mai testo bianco sull'ottone: sull'ottone il testo è sempre `--ink`.

## Tipografia

Public Sans 400-800 per tutto. Scala fluida `--step--1` … `--step-4` (0,84 → 4,6 rem). Titoli 800, interlinea 1,02-1,1, tracking −0,025/−0,035em. Testo 1,65 di interlinea, articoli 1,1rem a 1,75 su max 48rem.

## Forme e profondità

Angoli 3px (bottoni, campi, chip) e 6px (card, screenshot). Unica ombra: morbida sotto gli screenshot (`0 30px 60px -30px`). Nessun gradiente, a parte la grana SVG quasi invisibile sulla pietra.

## Componenti

- **Testata**: marchio (quadratino ottone + nome + "Siti web · Frascati"), menu testuale con sottolineatura ottone che si traccia da sinistra; su mobile un `<details>` "Menu".
- **Hero**: H1 bianco con "a Frascati e nei Castelli Romani" in ottone; a destra lo **screenshot dell'ultimo lavoro** in una cornice da browser, con didascalia e link.
- **Servizi**: due card, la principale nera e la secondaria chiara; elenchi con quadratino ottone.
- **Lavori**: screenshot grande e testo affiancati, alternati; testimonianza sotto un filetto.
- **Metodo**: tre colonne con numero in ottone scuro (la sequenza conta).
- **Elenco articoli**: righe data / titolo / categoria su pietra; "Nuovo" solo sull'ultimo articolo.
- **FAQ**: `<details>` con segno + disegnato a due linee.
- **Contatti**: sezione pietra, modulo su intonaco con focus ottone.

## Movimento

Un solo momento: all'apertura i blocchi dell'hero salgono di 14px **partendo già visibili** (`transform` soltanto). Hover: sottolineature e frecce. Con `prefers-reduced-motion` tutto fermo.

## Da non fare

Targhe, viti, ottone spazzolato, pulsanti a rilievo, spie luminose (versione precedente, scartata perché sapeva di anni '90). Etichette sopra i titoli. Bordi colorati a sinistra.
