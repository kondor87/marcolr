---
target: sito attuale laroccadigitale.it (template root)
total_score: 21
max_score: 32
na_heuristics: 7,10
p0_count: 0
p1_count: 2
target_identity: "file:C:\\Users\\Peggy18\\Documents\\Marco\\Progetti\\SitoVetrina\\layouts\\index.html"
target_fingerprint: "sha256:d78647798731ada2dd25c9d58cc7d29f656dc9654170ec8f191bf33748d86d5d"
target_path: "C:\\Users\\Peggy18\\Documents\\Marco\\Progetti\\SitoVetrina\\layouts\\index.html"
timestamp: 2026-10-07T20-39-55Z
slug: layouts-index-html
---
Method: dual-agent (A: design review · B: detector + browser)

Punteggio Nielsen 21/32 (7 e 10 n/a). Specificità: testi molto specifici, grafica generica (gradient text, codex grid, pulsing dot, dark glow, palette verde-ciano, terminale).

Problemi prioritari:
- [P1] CTA .btn-primary in light: bianco su gradiente #10F090→#059669, 1.5–3.8:1. Anche --text-tertiary (meta, label form, footer-legal), .section-label con opacity .75. Fix: bg #047857 pieno in light, tertiary #64748B/#8B97AA, niente opacity, :focus-visible globale. (/impeccable harden)
- [P1] Mobile: .hero-right display:none ≤520px nasconde la foto; nav 31px, Invia 37px, link footer 16px. Fix: avatar 64px accanto al nome, togliere Home dal nav, tap target ≥44px. (/impeccable adapt)
- [P2] Gerarchia piatta: h2 = label mono 11px, tagline 15px light grigia. Fix: tagline ~20px --text, titolo di sezione leggibile, .blog-content max 68ch. (/impeccable typeset)
- [P2] Home lunga e ordine: Chi sono settima sezione, 6 post, strumenti. Fix: Chi sono dopo lavori, 3 post, via strumenti, liste da 4, rassicurazione al form. (/impeccable distill)
- [P3] Residui: .ai-card indaco, gradiente sul nome, dot-pulse, griglia, CTA mancante su pagina servizio, .reveal senza fallback no-JS, categoria "Manutenzione". (/impeccable polish)

Falso positivo escluso: overflow orizzontale mobile (era l'overlay del detector).
