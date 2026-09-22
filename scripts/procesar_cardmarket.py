import json

with open("products_singles.json", "r", encoding="utf-8") as f:
    products = json.load(f)["products"]

with open("price_guide.json", "r", encoding="utf-8") as f:
    prices = json.load(f)["priceGuides"]

prices_by_id = {
    item["idProduct"]: item
    for item in prices
}

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


with open("pokemon_cards.json", "w", encoding="utf-8") as f:
    json.dump(cards, f, ensure_ascii=False, separators=(",", ":"))


# =========================================================
# BUSCAR PITCH BLACK
# =========================================================

palabras_pitch_black = [
    "Tropius",
    "Grubbin",
    "Fomantis",
    "Lurantis",
    "Mega Darkrai",
    "Mega Zeraora",
    "Mega Chandelure",
    "Mega Excadrill"
]

print("")
print("===== POSIBLES CARTAS DE PITCH BLACK =====")

encontradas = {}

for card in cards:

    nombre = card["name"].lower()

    if any(palabra.lower() in nombre for palabra in palabras_pitch_black):

        expansion = card["idExpansion"]

        if expansion not in encontradas:
            encontradas[expansion] = []

        encontradas[expansion].append(card["name"])


for expansion, nombres in encontradas.items():

    print("")
    print("idExpansion:", expansion)
    print("Número de coincidencias:", len(nombres))

    for nombre in nombres[:10]:
        print(" -", nombre)


print("")
print("==========================================")
print(f"Cartas procesadas: {len(cards)}")
