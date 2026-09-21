export default async function handler(req, res) {
    try {
        const respuesta = await fetch(
            "https://www.cardmarket.com/en/Pokemon/Data/Price-Guide"
        );

        const texto = await respuesta.text();

        res.status(200).json({
            status: respuesta.status,
            longitud: texto.length,
            primerosCaracteres: texto.substring(0, 500)
        });

    } catch (error) {
        res.status(500).json({
            error: error.message
        });
    }
}
