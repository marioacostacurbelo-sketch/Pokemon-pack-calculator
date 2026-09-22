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
    json.dump(
        cards,
        f,
        ensure_ascii=False,
        separators=(",", ":")
    )


# =========================================================
# BUSCAR PITCH BLACK
# =========================================================

pitch_black_names = [
    "Tropius",
    "Grubbin",
    "Fomantis",
    "Lurantis ex",
    "Poltchageist",
    "Sinistcha",
    "Heatran",
    "Mega Delphox ex",
    "Mega Chandelure ex",
    "Mega Slowbro ex",
    "Mega Zeraora ex",
    "Mega Excadrill ex",
    "Mega Darkrai ex",
    "Morpeko ex",
    "Wailord ex",
    "Rampardos ex",
    "Drilbur",
    "Type: Null"
]

print("")
print("===== BUSCANDO PITCH BLACK =====")

candidatos = {}

for card in cards:

    nombre = card["name"].lower()

    for objetivo in pitch_black_names:

        if objetivo.lower() in nombre:

            expansion = card["idExpansion"]

            if expansion not in candidatos:
                candidatos[expansion] = []

            candidatos[expansion].append(card["name"])

            break


for expansion, nombres in candidatos.items():

    print("")
    print("idExpansion:", expansion)
    print("Coincidencias:", len(nombres))

    for nombre in nombres:
        print(" -", nombre)


print("")
print("================================")
print(f"Cartas procesadas: {len(cards)}")
