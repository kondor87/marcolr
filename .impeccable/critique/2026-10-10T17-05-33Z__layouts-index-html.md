---
target: sito attuale laroccadigitale.it (re-check)
total_score: 22
max_score: 32
na_heuristics: 7,10
p0_count: 0
p1_count: 2
target_identity: "file:C:\\Users\\Peggy18\\Documents\\Marco\\Progetti\\SitoVetrina\\layouts\\index.html"
target_fingerprint: "sha256:fe682e7888d680ac357324be6845623d9276234a4e9bc7490a26f3d09ccba53f"
target_path: "C:\\Users\\Peggy18\\Documents\\Marco\\Progetti\\SitoVetrina\\layouts\\index.html"
timestamp: 2026-10-10T17-05-33Z
slug: layouts-index-html
---
Method: dual-agent (A: design review · B: detector + browser)

## Design Health Score: 22/32 (69%), Acceptable/Good border. n/a: 7, 10.
| # | Heuristic | Score |
|---|---|---|
| 1 | Visibility of system status | 3 |
| 2 | Match real world | 3 |
| 3 | User control | 3 |
| 4 | Consistency | 2 |
| 5 | Error prevention | 3 |
| 6 | Recognition | 3 |
| 7 | Flexibility | n/a |
| 8 | Aesthetic/minimalist | 2 |
| 9 | Error recovery | 3 |
| 10 | Help | n/a |

## Priority issues
- [P1] Home sales copy at 12-13px grey: FIXED same session (CSS to 14.5-16px, whyme 1 col mobile).
- [P1] iubenda banner covers half of mobile screen, off-brand: needs iubenda dashboard (Marco).
- [P2] Social proof weak: testimonial typography FIXED; /lavori/ thin, Martina case needs mobile screenshot + facts (Marco).
- [P2] Inconsistent FAQ components, #contacts under sticky nav, mail icon stroke #fff: FIXED.
- [P3] Terminal hidden on mobile, English "Available": home text, ask Marco.

## Detector
CLI: home low-contrast x3 (.process-num light 2.1:1) FIXED; flat-type-hierarchy (section labels, intentional). Browser: low-contrast on --green-dark text in dark (badge, tag, active pill) FIXED; placeholders FIXED; tap targets pills/FAQ/TOC FIXED.
