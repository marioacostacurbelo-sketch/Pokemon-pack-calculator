import json

# Cargar productos de Cardmarket
with open("products_singles.json", "r", encoding="utf-8") as f:
    products = json.load(f)["products"]

# Cargar precios de Cardmarket
with open("price_guide.json", "r", encoding="utf-8") as f:
    prices = json.load(f)["priceGuides"]


# Crear índice de precios usando idProduct
prices_by_id = {
    item["idProduct"]: item
    for item in prices
}


# Unir cartas + precios
cards = []

for product in products:

    product_id = product["idProduct"]
    price = prices_by_id.get(product_id)

    if price is None:
        continue

    cards.append({
        "idProduct": product_id,
        "name": product["name"],
        "idCategory": product["idCategory"],
        "categoryName": product["categoryName"],
        "idExpansion": product["idExpansion"],
        "idMetacard": product["idMetacard"],

        "avg": price.get("avg"),
        "low": price.get("low"),
        "trend": price.get("trend"),

        "avg7": price.get("avg7"),
        "avg30": price.get("avg30"),

        "avgHolo": price.get("avg-holo"),
        "lowHolo": price.get("low-holo"),
        "trendHolo": price.get("trend-holo")
    })


# Guardar todas las cartas
with open("pokemon_cards.json", "w", encoding="utf-8") as f:
    json.dump(cards, f, ensure_ascii=False, separators=(",", ":"))


# =========================================================
# PITCH BLACK
# =========================================================

PITCH_BLACK_ID = 1585

pitch_black = [
    card
    for card in cards
    if card["idExpansion"] == PITCH_BLACK_ID
]


# =========================================================
# NUMERACIÓN OFICIAL DE PITCH BLACK
# =========================================================

numeros_pitch_black = [
    "Tropius",
    "Grubbin",
    "Fomantis",
    "Lurantis ex",
    "Poltchageist",
    "Sinistcha",
    "Heatran",
    "Mega Delphox ex",
    "Sizzlipede",
    "Centiskorch",
    "Charcadet",
    "Armarouge",
    "Goldeen",
    "Seaking",
    "Wailmer",
    "Wailord ex",
    "Relicanth",
    "Popplio",
    "Brionne",
    "Primarina",
    "Finizen",
    "Palafin",
    "Electrike",
    "Manectric",
    "Charjabug",
    "Vikavolt",
    "Mega Zeraora ex",
    "Miraidon",
    "Slowpoke",
    "Slowbro",
    "Mega Slowbro ex",
    "Jynx",
    "Shuppet",
    "Banette",
    "Spiritomb",
    "Litwick",
    "Lampent",
    "Mega Chandelure ex",
    "Dhelmise",
    "Marshadow",
    "Annihilape",
    "Mankey",
    "Primeape",
    "Cranidos",
    "Rampardos ex",
    "Drilbur",
    "Koraidon",
    "Mega Darkrai ex",
    "Vullaby",
    "Mandibuzz",
    "Inkay",
    "Malamar",
    "Nickit",
    "Thievul",
    "Morpeko ex",
    "Zarude",
    "Maschiff",
    "Mabosstiff",
    "Chi-Yu",
    "Skarmory",
    "Shieldon",
    "Bastiodon",
    "Bronzor",
    "Bronzong",
    "Mega Excadrill ex",
    "Pikipek",
    "Trumbeak",
    "Toucannon",
    "Type: Null",
    "Silvally",
    "Bombirdier",
    "Antique Armor Fossil",
    "Antique Skull Fossil",
    "Backtrack Badge",
    "Dark Bell",
    "Fossil Quarry",
    "Gladion’s Final Battle",
    "Gwynn",
    "Jett",
    "Misty’s Vitality",
    "Rust Syndicate Grunt",
    "Tremendous Bomb",
    "Shadowy {D} Energy",
    "Voltaic {L} Energy",
    "Fomantis",
    "Armarouge",
    "Goldeen",
    "Primarina",
    "Manectric",
    "Slowbro",
    "Dhelmise",
    "Thievul",
    "Bastiodon",
    "Toucannon",
    "Silvally",
    "Lurantis ex",
    "Wailord ex",
    "Mega Zeraora ex",
    "Mega Chandelure ex",
    "Rampardos ex",
    "Mega Darkrai ex",
    "Morpeko ex",
    "Mega Excadrill ex",
    "Brave Bangle",
    "Crushing Hammer",
    "Dark Bell",
    "Energy Switch",
    "Gladion’s Final Battle",
    "Gwynn",
    "Iron Defender",
    "Misty’s Vitality",
    "Rust Syndicate Grunt",
    "Tremendous Bomb",
    "Mega Zeraora ex",
    "Mega Chandelure ex",
    "Mega Darkrai ex",
    "Morpeko ex",
    "Gladion’s Final Battle",
    "Gwynn",
    "Mega Darkrai ex"
]


# =========================================================
# CREAR MAPA NOMBRE → CARTAS
# =========================================================

por_nombre = {}

for card in pitch_black:
    nombre = card["name"]

    if nombre not in por_nombre:
        por_nombre[nombre] = []

    por_nombre[nombre].append(card)


# =========================================================
# ASIGNAR NÚMERO OFICIAL
# =========================================================

resultado_pitch_black = []

contadores = {}

for numero, nombre in enumerate(numeros_pitch_black, start=1):

    opciones = por_nombre.get(nombre, [])

    posicion = contadores.get(nombre, 0)

    if posicion >= len(opciones):
        print(f"AVISO: No se encontró la carta #{numero}: {nombre}")
        continue

    card = opciones[posicion]
    contadores[nombre] = posicion + 1

    card = dict(card)
    card["number"] = numero

    resultado_pitch_black.append(card)


# Guardar Pitch Black
with open("pitch_black.json", "w", encoding="utf-8") as f:
    json.dump(
        resultado_pitch_black,
        f,
        ensure_ascii=False,
        separators=(",", ":")
    )


print(f"Cartas procesadas: {len(cards)}")
print(f"Cartas Pitch Black encontradas: {len(resultado_pitch_black)}")
