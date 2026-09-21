export default async function handler(req, res) {
    try {
        const respuesta = await fetch(
            "https://downloads.s3.cardmarket.com/productCatalog/priceGuide/price_guide_6.json"
        );

        const datos = await respuesta.json();

        res.status(200).json({
            status: respuesta.status,
            productos: datos.length,
            primerProducto: datos[0]
        });

    } catch (error) {
        res.status(500).json({
            error: error.message
        });
    }
}
