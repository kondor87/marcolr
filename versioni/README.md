# Versioni grafiche del sito

Tre proposte di nuova grafica per laroccadigitale.it. Usano gli **stessi contenuti**
del sito principale (`../content`), le stesse immagini (`../static/images`, comprese le
copertine del blog in `copertine/`) e gli stessi partial SEO (`../layouts/partials/shared`:
meta, consenso, analytics, JSON-LD, immagini). Cambiano solo layout e CSS.

| Cartella | Idea | Porta |
|---|---|---|
| `v2-targa/` | **Peperino.** La palette dei Castelli (pietra scura, intonaco, ottone, nero) in forma piatta e moderna. In apertura c'è subito l'ultimo lavoro. | 8812 |
| `v3-programma/` | **Programma.** Modernismo all'italiana ridotto all'essenziale: nero, vermiglione e un grigio. Composizione geometrica con le iniziali. | 8813 |
| `v4-cartiglio/` | **Cartiglio.** Il sito come una tavola di progetto: carta chiara, tratto grafite, quote di misura attorno ai lavori, cartiglio con i dati di Marco. Un solo accento ottone. Stesso linguaggio delle copertine del blog. | 8814 |

Il sito attuale (con le correzioni SEO già applicate) gira sulla porta 8811.

## Vederle

Doppio clic su `avvia-versioni.bat`, oppure:

```
hugo server -s versioni/v4-cartiglio -D --port 8814
```

`-D` mostra anche le bozze (il lavoro Osteria Gemelli, nascosto in produzione).

## Mettere online una versione

1. Copia `layouts/` della versione scelta nella `layouts/` principale, **tenendo** `layouts/partials/shared/`, `layouts/shortcodes/`, `layouts/_default/_markup/` e `layouts/index.llms.txt`.
2. Copia `assets/css/main.css` in `assets/css/` e cancella il vecchio `assets/css/style.css`.
3. `hugo server` dalla cartella principale, controlla, poi commit e push.

Ogni versione ha un `DESIGN.md` con colori, caratteri e regole. Le cartelle `.impeccable/review/` contengono gli screenshot di controllo.
