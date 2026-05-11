// ═══════════════════════════════════════════════════════════════
//  CATALOGO PRODOTTI — Pre-Loved With Love
//  ✏️  Aggiungi, modifica o rimuovi articoli solo qui!
// ═══════════════════════════════════════════════════════════════
//
//  COME AGGIUNGERE UN ARTICOLO
//  ────────────────────────────
//  1. Copia uno dei blocchi qui sotto
//  2. Cambia "id" con il numero successivo (non usare lo stesso id due volte)
//  3. Compila tutti i campi
//  4. Salva il file — il sito si aggiorna automaticamente!
//
//  CAMPI DISPONIBILI
//  ──────────────────
//  id          → numero univoco (obbligatorio)
//  name        → nome del capo (obbligatorio)
//  category    → categoria: es. "Jeans", "Top", "Giacche", "Accessori", "Abiti", "Maglioni"
//  size        → taglia: es. "XS", "S", "M", "L", "XL", "W28", "Unica"
//  price       → prezzo in euro (numero, es. 25.00)
//  condition   → "Ottime condizioni" | "Buone condizioni" | "Come nuovo"
//  image       → percorso foto: "foto/nome-foto.jpg"  oppure URL da web
//  description → breve descrizione (opzionale ma consigliata)
//  brand       → marca (opzionale)
//  color       → colore (opzionale)
//  new         → true se è un nuovo arrivo (mostra badge giallo), false altrimenti
//  sold        → true se venduto, false se disponibile
// ═══════════════════════════════════════════════════════════════

const CATALOG = [

  // ── ESEMPIO 1 ──────────────────────────────────────────────
  {
    id: 1,
    name: "Jeans Levi's 501",
    category: "Jeans",
    size: "W30",
    price: 45.00,
    condition: "Ottime condizioni",
    image: "https://lh3.googleusercontent.com/aida-public/AB6AXuCMjbhcguwNnKMGV1SATuhUl7vnt9wvq8xouykt-FRpjVG0aOTJDRat0cuZDwYG9ja9HEfyd10G_3Lljtwu5FCy-yo0lFMCiMpqrN6mmNVPxQuPN2Ay-ymCjj0E1Hrxu5LjbW0qAj6OVQ48bvxkpwBBFS1_45ZvAWixhY_nNm1rdoeQCKYzeajR9rdz8TGis-hglsh8jLv_yazoeRuaENuow1n0FaXvrlml7WdVnpxCbUkjU4yJKYNXNfbdFqbl1o7j5IhOKdBqsA",
    description: "Classico jeans 501 a vita alta, lavaggio chiaro. Taglia comoda, perfetto con qualsiasi look.",
    brand: "Levi's",
    color: "Denim chiaro",
    new: false,
    sold: false,
  },

  // ── ESEMPIO 2 ──────────────────────────────────────────────
  {
    id: 2,
    name: "Camicia in Seta",
    category: "Top",
    size: "M",
    price: 32.00,
    condition: "Ottime condizioni",
    image: "https://lh3.googleusercontent.com/aida-public/AB6AXuAL9HIB_GI6lVZtWGKLstW9G3cb5uMtZKFM5z20t_HGLrB_5lMHG3i8qhiPR7N5THpe1xI0-Mvx4j_2SdzbDTNPBKW8V3XvafpvHNHKj_311WU-Mr89NMV0C95zlGBLHI1zbxtUAvnDZkeqnu9n4KvS6wBYenikB7lrrDCifaF1Zb3edw9f_uh55HWyQNviZnBap8VfGX7e1uH3-pgq5euBINc97QM56B2S1FM09szXZHXCg8nr2T80yNk7a7OUQDqsR9hPajtl5g",
    description: "Camicia in seta avorio con collo classico. Leggera, elegante, versatile. Ideale estate e non solo.",
    brand: "",
    color: "Avorio",
    new: true,
    sold: false,
  },

  // ── ESEMPIO 3 ──────────────────────────────────────────────
  {
    id: 3,
    name: "Giacca Vintage Beige",
    category: "Giacche",
    size: "L",
    price: 58.00,
    condition: "Buone condizioni",
    image: "https://lh3.googleusercontent.com/aida-public/AB6AXuAEj3_FirQTUjOXOZhGDdi6Jj0gxbsHosx2mKZDl7W-eh4q5I8j2KIbXVOuj0lYnNGyW0wqUFzcd3KW4WDyFFGd-iPdDbYE1iaXGMMXHKXjY9lWdeFqdgIHf7e7x6hcT9oysgmBUl4EsTV86S_VAapnC2eBxEs-j7zkCS5ky7KUes5Kbkb0u0YZLPMr2xRDRo7IRFWgkfEHnlC-Hmt8JHPwEgWD9WXn62DPE_QtC3faK2qytZF74x3sO-qXW29FxHpnpC7h7S612Q",
    description: "Blazer strutturato anni '90, colore beige caldo. Ottimo per look business o casual chic.",
    brand: "",
    color: "Beige",
    new: false,
    sold: false,
  },

  // ── ESEMPIO 4 ──────────────────────────────────────────────
  {
    id: 4,
    name: "Maglione Oversize Grigio",
    category: "Maglioni",
    size: "Oversize",
    price: 28.00,
    condition: "Ottime condizioni",
    image: "https://lh3.googleusercontent.com/aida-public/AB6AXuB3AAorbI2majgLe3Enf_5EU84Y9VSeTQza6cnpteeEg-9w4Y65qmtWFOfjKW1MGVTPAvd0GdocF47dy92I8bvS6i1E4fhVr-I7-wbC11Bd3eXZ_bq_yHKY0S91D0SUnl22WQLlnkHooJBGxopUNLj13PPeNViK6UJ1JCuFNsomTDoUnu0LeEYCLXgNYhAlz78jqlQyD228HK51MMkEvSTuHkXkQ6ZgW3YxjWndzyFS5soaej-xVBkN49JvMxAhf2lJQ8KwdqVe4Q",
    description: "Maglione a trecce grigio chiaro, morbidissimo. Caldo ma non pesante. Perfetto per l'autunno.",
    brand: "",
    color: "Grigio",
    new: false,
    sold: false,
  },

  // ── ESEMPIO 5 ──────────────────────────────────────────────
  {
    id: 5,
    name: "Gonna a Pieghe Navy",
    category: "Gonne",
    size: "S",
    price: 22.00,
    condition: "Come nuovo",
    image: "https://lh3.googleusercontent.com/aida-public/AB6AXuAE5uIHEl2ngR1R0lBA-R_h8j6JvkcFrqd7IhFFjmBm3monKvTukPYIobECJQ_GB0bRMDlCBakRwjDJ5cqTH-VpGuXq_wHX7SOBSgBeKyeMDwO4l_8rGk6JMC6gIAxUBMZI-8ZVKJkjixxxajp1nce8ZaBVS0zl3TiEikIQ_dgW9oLHx2LKFt7IRA8VW08n9KSIib6yLuMRY9KnT11ms8Dh8Ansp5-ptygqAQt_trGvNX12T86tS2iPAcBtMpy-oxuAoozapCFQ7g",
    description: "Gonna a pieghe blu navy, lunghezza midi. Praticamente nuova, indossata pochissimo.",
    brand: "",
    color: "Navy",
    new: true,
    sold: false,
  },

  // ── ESEMPIO 6 ──────────────────────────────────────────────
  {
    id: 6,
    name: "Accessorio Vintage",
    category: "Accessori",
    size: "Unica",
    price: 15.00,
    condition: "Ottime condizioni",
    image: "https://lh3.googleusercontent.com/aida-public/AB6AXuBixWFMTKLteJW-oxy15jcWzAiykwbLYjmlFylH2-jrrQtLQ-me9QJ-sslfTq8m7PEhAUzSDAtH24HV7TDa-kfLyRNCyFdLxdO4bgHN9KKI-9rpycchSTZ9B0K_wwANJE8ODNflmAYP-yVIwmaPxLE5sBXYb_zVR6ApL6vhdl6yjMrfMVbCwdlzHAdIcx2FkLMrmmS7MWW-Y7XKAI6WBemXReHWUqdmIZDtfO-kpiT0QubA8uOdrV5gFj7QVnIGItYsQICh_Uhokw",
    description: "Set di accessori vintage: cintura in pelle e foulard in seta. Pezzo unico.",
    brand: "",
    color: "Multicolore",
    new: false,
    sold: false,
  },

  // ═══════════════════════════════════════════════════════════
  //  👆 AGGIUNGI I TUOI ARTICOLI QUI SOTTO, copia il blocco:
  // ═══════════════════════════════════════════════════════════

  // {
  //   id: 7,                          ← numero progressivo
  //   name: "Nome del capo",
  //   category: "Categoria",
  //   size: "M",
  //   price: 30.00,
  //   condition: "Ottime condizioni",
  //   image: "foto/mia-foto.jpg",     ← metti la foto nella cartella "foto/"
  //   description: "Descrizione...",
  //   brand: "Zara",
  //   color: "Bianco",
  //   new: true,
  //   sold: false,
  // },

];
