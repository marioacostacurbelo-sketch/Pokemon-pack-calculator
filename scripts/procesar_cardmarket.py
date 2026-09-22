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
# COMPARAR EXPANSIONES CANDIDATAS
# =========================================================

expansiones = [1543, 1546]

print("")
print("===== COMPARACIÓN DE EXPANSIONES =====")

for expansion_id in expansiones:

    cartas_expansion = [
        card for card in cards
        if card["idExpansion"] == expansion_id
    ]

    print("")
    print("idExpansion:", expansion_id)
    print("Número de cartas:", len(cartas_expansion))

    for card in cartas_expansion[:30]:
        print(" -", card["name"])

print("")
print("======================================")
