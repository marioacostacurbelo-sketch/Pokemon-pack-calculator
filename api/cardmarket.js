export default async function handler(req, res) {
    try {
        const respuesta = await fetch(
            "https://www.cardmarket.com/en/Pokemon/Data/Price-Guide"
        );

        res.status(200).json({
            estado: "Cardmarket accesible",
            status: respuesta.status
        });

    } catch (error) {
        res.status(500).json({
            estado: "Error",
            mensaje: error.message
        });
    }
}
