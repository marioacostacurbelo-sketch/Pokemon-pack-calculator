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


# Todas las cartas
with open("pokemon_cards.json", "w", encoding="utf-8") as f:
    json.dump(cards, f, ensure_ascii=False, separators=(",", ":"))


# =========================================================
# PITCH BLACK
# =========================================================

PITCH_BLACK_ID = 1585

pitch_black = [
    card for card in cards
    if card["idExpansion"] == PITCH_BLACK_ID
]


# Guardamos las cartas de Pitch Black SIN inventar
# números todavía.
with open("pitch_black.json", "w", encoding="utf-8") as f:
    json.dump(
        pitch_black,
        f,
        ensure_ascii=False,
        separators=(",", ":")
    )


print(f"Cartas procesadas: {len(cards)}")
print(f"Cartas Pitch Black: {len(pitch_black)}")
