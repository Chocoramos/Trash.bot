import discord
from discord.ext import commands

RECICLABLES = {
    "papel", "cartón", "botella de plástico", "lata", "vidrio", "tetrabrik", "periódico", "revista", "hojas de papel",
    "botellas de vidrio", "envases de plástico", "latas de aluminio", "tapas de plástico", "cajas de cartón", "tubos de cartón",
    "papel de oficina", "sobres", "libros", "papel kraft", "cartón corrugado", "botellas de PET", "plástico HDPE",
    "plástico PVC", "bolsas de papel", "bolsas de plástico reciclable", "envases de yogur", "latas de conserva",
    "botes de aerosol vacíos", "envases de shampoo", "envases de detergente", "tetra pack", "vidrio transparente",
    "vidrio de color", "botellas de cerveza", "frascos de vidrio", "tarros de vidrio"
}

NO_RECICLABLES = {
    "chicle", "pañal", "papel higiénico", "vaso de unicel", "colilla de cigarro", "pañuelos desechables", "papel encerado",
    "papel aluminio", "papel plastificado", "esponjas", "cotonetes", "cepillos de dientes", "cables", "pilas",
    "baterías", "bombillas", "cerámica", "espejos", "vidrio roto", "pañales desechables", "toallas femeninas",
    "pañales para adultos", "hisopos", "envases contaminados con grasa", "papel térmico", "servilletas usadas",
    "cubiertos de plástico", "bolsas metalizadas", "telas sintéticas", "ropa vieja", "zapatos desgastados",
    "tapetes", "caucho", "látex", "plástico contaminado", "desechos electrónicos", "cascos de huevo", "huesos",
    "restos de comida", "comida en mal estado", "aceite usado", "productos químicos", "fármacos vencidos",
    "radiografías", "tubos fluorescentes", "termómetros de mercurio", "aerosoles con contenido"
}

intents = discord.Intents.default()
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f'Conectado como {bot.user}')
    
@bot.command()
async def clasificar(ctx, *, objeto: str):
    objeto = objeto.lower()
    if objeto in RECICLABLES:
        await ctx.send(f'♻️ {objeto.capitalize()} es reciclable. ¡No lo tires a la basura! Puedes depositarlo en el contenedor adecuado para su reutilización.')
    elif objeto in NO_RECICLABLES:
        await ctx.send(f'🚮 {objeto.capitalize()} no es reciclable. Tíralo en la basura común o busca opciones de disposición adecuada en tu localidad.')
    else:
        reciclables_str = ", ".join(RECICLABLES)
        no_reciclables_str = ", ".join(NO_RECICLABLES)
        await ctx.send(f'''❓ No estoy seguro sobre "{objeto}". Ejemplos de bjetos conocidos:
Reciclables:  lata, tetrabrik, vidrio, papel, cartón, botella de plástico.
No reciclables: papel higiénico, pañal, colilla de cigarro, vaso de unicel, chicle.''')

@bot.command()
async def ayuda(ctx):
    mensaje = """🤖 **¡Hola! Soy EcoBot, tu asistente de reciclaje.**
    
🔹 **Usa `!clasificar [objeto]` para saber si algo es reciclable.**
🔹 Ejemplo: `!clasificar botella de plástico`
🔹 Obtendrás una respuesta indicando si el objeto se puede reciclar o no.

🌱 ¡Juntos podemos cuidar el planeta!"""
    await ctx.send(mensaje)


bot.run("Ya sabes que poner ;)")
