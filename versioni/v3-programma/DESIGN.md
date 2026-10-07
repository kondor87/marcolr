# DESIGN · V3 "Programma"

Programma grafico modernista all'italiana, **ridotto all'essenziale**: nero tipografico e vermiglione su carta, più un grigio di appoggio. Campi pieni, nessuna sfumatura, nessuna ombra, angoli vivi. Fonte: `assets/css/main.css`.

## Colori

| Token | Valore | Uso |
|---|---|---|
| `--paper` | `#fafaf7` | fondo |
| `--paper-2` | `#efeee8` | bande alternate (lavori, chi sono, correlati) |
| `--rule` | `#d9d7cf` | filetti |
| `--ink` / `--ink-2` | `#111111` / `#44443f` | testo, campi neri / testo secondario |
| `--red` | `#c8321a` | accento unico: parte dell'H1, bottone principale, cerchio, sezione contatti |
| `--red-deep` | `#a8280f` | hover del rosso |
| `--grey` | `#dcdbd5` | campo secondario (servizio automazioni, riquadri negli articoli, tessere) |

Il vermiglione è scurito apposta: il testo bianco sopra resta leggibile (circa 5,3:1). Prima c'erano anche cobalto, giallo e verde: tolti su richiesta, troppi colori.

## Tipografia

Albert Sans 400-900 (`ss01`). Display 800-900 con tracking fino a −0,04em, H1 fino a 5,4rem. Testo a 1,6 di interlinea; articoli 1,14rem su 68ch.

## Griglia

12 colonne; **il rango si esprime con la larghezza**: servizio principale su 7 colonne, secondario su 5; screenshot dei lavori su 7, testo su 4.

## Componenti

- **Marchio**: quattro quadratini (rosso con un angolo curvo, nero, grigio, nero) + nome.
- **Composizione dell'hero**: tessere quadrate con la M (su grigio) e la L (bianca su nero), un cerchio rosso, quarti di cerchio nero, rosso e grigio.
- **Servizi**: due campi pieni affiancati, nero e grigio.
- **Lavori**: screenshot su campo pieno (rosso / nero alternati), numero d'ordine in colore pieno.
- **Metodo**: numerali grandi in rosso/nero (la sequenza conta).
- **Elenco articoli**: righe con un simbolo per categoria (cerchio o quadrato, rosso o nero), titolo, categoria, data; il più recente ha l'etichetta "Nuovo" grigia.
- **Contatti**: campo rosso pieno con il modulo su carta.
- **Piè di pagina**: nero, con una barra a quattro segmenti (rosso, grigio, grafite, rosso) sopra.

## Movimento

Le tessere dell'hero si compongono al caricamento muovendosi di pochi pixel (solo `transform`, sono visibili da subito). Sottolineature dei link che si accorciano all'hover.

## Da non fare

Altri colori oltre a rosso, nero e grigio. Ombre, gradienti, angoli arrotondati sui contenitori. Numeri di sezione decorativi. Etichette sopra i titoli.
