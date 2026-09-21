import json

# Cargar los dos archivos
with open("products_singles.json", "r", encoding="utf-8") as f:
    products = json.load(f)["products"]

with open("price_guide.json", "r", encoding="utf-8") as f:
    prices = json.load(f)["priceGuides"]


# Crear un índice de precios usando idProduct
prices_by_id = {
    item["idProduct"]: item
    for item in prices
}


# Unir información de cartas + precios
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


# Guardar resultado
with open("pokemon_cards.json", "w", encoding="utf-8") as f:
    json.dump(cards, f, ensure_ascii=False, separators=(",", ":"))


print(f"Cartas procesadas: {len(cards)}")
