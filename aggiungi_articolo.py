#!/usr/bin/env python3
# ═══════════════════════════════════════════════════════════════
#  CAPOVOLTO — Aggiungi articolo al catalogo
#  Uso:  python3 aggiungi_articolo.py
#  Con ID diretto: python3 aggiungi_articolo.py 7
# ═══════════════════════════════════════════════════════════════

import os, sys, re

CATALOG_FILE = "catalogo.js"
ASSETS_DIR   = "assets/catalog"

R    = "\033[91m"
G    = "\033[92m"
Y    = "\033[93m"
C    = "\033[96m"
DIM  = "\033[2m"
BOLD = "\033[1m"
RST  = "\033[0m"

def clear():
    os.system("cls" if os.name == "nt" else "clear")

def header():
    print(f"""
{R}╔══════════════════════════════════════════════╗
║        CAPOVOLTO — Aggiungi Articolo         ║
╚══════════════════════════════════════════════╝{RST}
""")

def ask(label, required=True, default=None, options=None):
    while True:
        hint = f" {DIM}[invio = {default}]{RST}" if default is not None else ""
        if options:
            hint += f"\n  {DIM}Opzioni: {' | '.join(options)}{RST}"
        val = input(f"  {BOLD}{label}{RST}{hint}: ").strip()
        if not val and default is not None:
            return default
        if not val and required:
            print(f"  {R}⚠  Campo obbligatorio.{RST}")
            continue
        if options and val not in options:
            print(f"  {R}⚠  Scegli tra: {', '.join(options)}{RST}")
            continue
        return val

def ask_price(label):
    while True:
        raw = input(f"  {BOLD}{label}{RST} {DIM}(es. 25 oppure 25.50){RST}: ").strip().replace(",", ".")
        try:
            v = float(raw)
            if v > 0:
                return round(v, 2)
        except ValueError:
            pass
        print(f"  {R}⚠  Inserisci un numero valido.{RST}")

def ask_bool(label, default=False):
    d = "s" if default else "n"
    while True:
        raw = input(f"  {BOLD}{label}{RST} {DIM}[s/n  invio={d}]{RST}: ").strip().lower()
        if not raw:
            return default
        if raw in ("s", "si", "sì", "y", "yes"):
            return True
        if raw in ("n", "no"):
            return False
        print(f"  {R}⚠  Digita s oppure n.{RST}")

def get_existing_ids(content):
    return [int(m) for m in re.findall(r"\bid\s*:\s*(\d+)", content)]

def next_id(content):
    ids = get_existing_ids(content)
    return max(ids) + 1 if ids else 1

def find_images(product_id):
    folder = os.path.join(ASSETS_DIR, str(product_id))
    exts = (".jpg", ".jpeg", ".png", ".webp", ".gif", ".avif")
    if not os.path.isdir(folder):
        return [], folder
    imgs = [f for f in sorted(os.listdir(folder)) if f.lower().endswith(exts)]
    return imgs, folder

def pick_image(product_id):
    imgs, folder = find_images(product_id)
    if not imgs:
        print(f"\n  {Y}⚠  Nessuna immagine trovata in: {folder}{RST}")
        print(f"  {DIM}Crea la cartella e mettici le foto, oppure incolla un URL.{RST}")
        url = input(f"\n  {BOLD}URL immagine{RST} {DIM}(invio per saltare){RST}: ").strip()
        return url
    print(f"\n  {G}✓ Trovate {len(imgs)} foto in: {folder}/{RST}")
    for i, img in enumerate(imgs, 1):
        print(f"    {DIM}{i}.{RST}  {img}")
    print(f"    {DIM}0.{RST}  Inserisci URL manualmente")
    while True:
        raw = input(f"\n  {BOLD}Immagine principale{RST} {DIM}[0-{len(imgs)}]{RST}: ").strip()
        if raw == "0":
            return input(f"  {BOLD}URL{RST}: ").strip()
        try:
            idx = int(raw) - 1
            if 0 <= idx < len(imgs):
                path = os.path.join(ASSETS_DIR, str(product_id), imgs[idx])
                return path.replace("\\", "/")
        except ValueError:
            pass
        print(f"  {R}⚠  Scegli un numero tra 0 e {len(imgs)}.{RST}")

def escape_js(s):
    return s.replace("\\", "\\\\").replace('"', '\\"')

def item_to_js(item):
    def q(v):
        return f'"{escape_js(str(v))}"'
    def bl(v):
        return "true" if v else "false"
    lines = [
        "  {",
        f"    id: {item['id']},",
        f"    name: {q(item['name'])},",
        f"    category: {q(item['category'])},",
        f"    size: {q(item['size'])},",
        f"    price: {item['price']},",
        f"    condition: {q(item['condition'])},",
        f"    image: {q(item['image'])},",
        f"    description: {q(item['description'])},",
        f"    brand: {q(item['brand'])},",
        f"    color: {q(item['color'])},",
        f"    new: {bl(item['new'])},",
        f"    sold: {bl(item['sold'])},",
        "  },",
    ]
    return "\n".join(lines)

def insert_item(content, new_item):
    js_block = "\n" + item_to_js(new_item) + "\n"
    marker = "// \u2550" * 1
    # cerca il commento marker "👆 AGGIUNGI"
    idx = content.find("\u2550\n  //  \U0001f446 AGGIUNGI")
    if idx != -1:
        # trova inizio della riga del marker
        line_start = content.rfind("\n", 0, idx) + 1
        return content[:line_start] + js_block + "  " + content[line_start:]
    # fallback: prima della chiusura ];
    m = re.search(r"\n\s*\];", content)
    if m:
        return content[:m.start()] + js_block + content[m.start():]
    raise RuntimeError("Non trovo il punto di inserimento in catalogo.js")

def show_summary(item):
    yn = lambda v: f"{G}sì{RST}" if v else f"{DIM}no{RST}"
    print(f"""
{C}┌─────────────────────────────────────────────┐
│              RIEPILOGO ARTICOLO             │
└─────────────────────────────────────────────┘{RST}

  {BOLD}ID:{RST}           {item['id']}
  {BOLD}Nome:{RST}         {item['name']}
  {BOLD}Categoria:{RST}   {item['category']}
  {BOLD}Taglia:{RST}      {item['size']}
  {BOLD}Prezzo:{RST}      \u20ac {item['price']:.2f}
  {BOLD}Condizione:{RST}  {item['condition']}
  {BOLD}Immagine:{RST}    {item['image'] or '(nessuna)'}
  {BOLD}Brand:{RST}       {item['brand'] or '—'}
  {BOLD}Colore:{RST}      {item['color'] or '—'}
  {BOLD}Descrizione:{RST} {item['description'] or '—'}
  {BOLD}Nuovo arrivo:{RST} {yn(item['new'])}
  {BOLD}Venduto:{RST}     {yn(item['sold'])}
""")

def main():
    clear()
    header()

    if not os.path.isfile(CATALOG_FILE):
        print(f"{R}\u2717  File non trovato: {CATALOG_FILE}{RST}")
        print(f"   {DIM}Esegui lo script dalla cartella del sito (dove c'\u00e8 index.html).{RST}\n")
        sys.exit(1)

    with open(CATALOG_FILE, "r", encoding="utf-8") as f:
        content = f.read()

    nxt      = next_id(content)
    existing = get_existing_ids(content)

    # ID
    if len(sys.argv) > 1:
        try:
            product_id = int(sys.argv[1])
        except ValueError:
            print(f"{R}\u2717  ID non valido: {sys.argv[1]}{RST}\n")
            sys.exit(1)
    else:
        print(f"  {DIM}Prossimo ID disponibile: {nxt}{RST}\n")
        raw = input(f"  {BOLD}ID prodotto{RST} {DIM}[invio = {nxt}]{RST}: ").strip()
        product_id = int(raw) if raw else nxt

    if product_id in existing:
        print(f"\n  {Y}\u26a0  Esiste gi\u00e0 un articolo con ID {product_id}.{RST}")
        if not ask_bool("Vuoi sovrascriverlo?", default=False):
            print(f"\n  {DIM}Annullato.{RST}\n")
            sys.exit(0)
        content = re.sub(
            r"\n\s*\{[^{}]*\bid\s*:\s*" + str(product_id) + r"\b[^{}]*\},?\n",
            "\n", content, flags=re.DOTALL
        )

    print(f"\n{C}  \u2500\u2500 Informazioni articolo \u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500{RST}\n")

    name = ask("Nome del capo")
    cats = ["Jeans", "Top", "Giacche", "Accessori", "Abiti", "Maglioni", "Gonne", "Scarpe", "Altro"]
    print(f"\n  {DIM}Categorie suggerite: {' | '.join(cats)}{RST}")
    category  = ask("Categoria")
    size      = ask("Taglia", default="Unica")
    price     = ask_price("Prezzo (\u20ac)")
    condition = ask("Condizione", default="Ottime condizioni",
                    options=["Ottime condizioni", "Buone condizioni", "Come nuovo"])

    print(f"\n{C}  \u2500\u2500 Immagine \u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500{RST}")
    image = pick_image(product_id)

    print(f"\n{C}  \u2500\u2500 Dettagli opzionali (invio per saltare) \u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500{RST}\n")
    description = ask("Descrizione", required=False, default="")
    brand       = ask("Brand/Marca", required=False, default="")
    color       = ask("Colore",      required=False, default="")
    is_new      = ask_bool("Nuovo arrivo? (badge giallo)", default=False)
    is_sold     = ask_bool("Gi\u00e0 venduto?",            default=False)

    new_item = {
        "id": product_id, "name": name, "category": category,
        "size": size, "price": price, "condition": condition,
        "image": image, "description": description,
        "brand": brand, "color": color,
        "new": is_new, "sold": is_sold,
    }

    show_summary(new_item)

    if not ask_bool(f"{BOLD}Salvare nel catalogo?{RST}", default=True):
        print(f"\n  {DIM}Annullato. Nessuna modifica.{RST}\n")
        sys.exit(0)

    # Backup
    backup = CATALOG_FILE + ".bak"
    with open(backup, "w", encoding="utf-8") as f:
        f.write(content)

    try:
        new_content = insert_item(content, new_item)
        with open(CATALOG_FILE, "w", encoding="utf-8") as f:
            f.write(new_content)
        print(f"\n{G}  \u2713 Articolo '{name}' aggiunto! (ID: {product_id}){RST}")
        print(f"  {DIM}Backup salvato in: {backup}{RST}")
        print(f"  {DIM}Ricarica index.html nel browser per vedere il risultato.{RST}\n")
    except Exception as e:
        print(f"\n{R}  \u2717 Errore: {e}{RST}\n")
        sys.exit(1)

if __name__ == "__main__":
    main()