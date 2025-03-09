import discord
from discord.ext import commands
intents = discord.Intents.default()
bot = commands.Bot(command_prefix="!", intents=intents)

RECICLABLES = {
    "papel": "♻️ Reciclable. Puede reutilizarse para fabricar más papel.",
    "cartón": "♻️ Reciclable. Asegúrate de que no esté mojado o sucio.",
    "botella de plástico": "♻️ Reciclable. Depósitalas limpias en el contenedor adecuado.",
    "lata": "♻️ Reciclable. El aluminio se puede reciclar infinitamente.",
    "vidrio": "♻️ Reciclable. Se funde para fabricar nuevos envases.",
    "tetrabrik": "♻️ Reciclable. Separa sus materiales correctamente.",
    "periódico": "♻️ Reciclable. Puede usarse para fabricar papel reciclado.",
    "revista": "♻️ Reciclable. Retira grapas y cubiertas plastificadas.",
    "hojas de papel": "♻️ Reciclable. No deben estar sucias ni arrugadas con grasa.",
    "botellas de vidrio": "♻️ Reciclable. Se funden para fabricar más vidrio.",
    "envases de plástico": "♻️ Reciclable. Lávalos antes de reciclar.",
    "latas de aluminio": "♻️ Reciclable. Compacta las latas para facilitar su reciclaje.",
    "tapas de plástico": "♻️ Reciclable. Muchas veces se reciclan aparte de las botellas.",
    "cajas de cartón": "♻️ Reciclable. Despliégalas antes de depositarlas en el contenedor.",
    "tubos de cartón": "♻️ Reciclable. Se pueden reutilizar en manualidades o reciclarse.",
    "papel de oficina": "♻️ Reciclable. Ideal para fabricar más papel.",
    "sobres": "♻️ Reciclable. Sin ventanas plásticas o adhesivos.",
    "libros": "♻️ Reciclable. Si no los necesitas, dónalos antes de reciclar.",
    "botellas de PET": "♻️ Reciclable. Son reutilizadas para hacer nuevas botellas o textiles.",
    "bolsas de papel": "♻️ Reciclable. Mejor opción que las bolsas plásticas.",
    "latas de conservas": "♻️ Reciclable. Lávalas bien antes de reciclarlas.",
    "envases de shampoo": "♻️ Reciclable. Enjuágalos antes de reciclarlos.",
    "botes de aerosol vacíos": "♻️ Reciclable. Solo si están completamente vacíos.",
    "envases de yogur": "♻️ Reciclable. Lávalos bien antes de depositarlos.",
    "tetra pack": "♻️ Reciclable. Asegúrate de que tu municipio acepte este tipo de material.",
    "vidrio de color": "♻️ Reciclable. Separa los colores si es posible.",
    "botellas de cerveza": "♻️ Reciclable. Se pueden devolver o reciclar.",
    "frascos de vidrio": "♻️ Reciclable. Retira tapas y etiquetas antes.",
    "tarros de vidrio": "♻️ Reciclable. Limpios y sin residuos."
}

NO_RECICLABLES = {
    "chicle": "❌ No reciclable. Se adhiere a otras superficies y no puede reprocesarse.",
    "pañal": "❌ No reciclable. Contiene residuos biológicos peligrosos.",
    "papel higiénico": "❌ No reciclable. Se degrada y no puede ser reprocesado.",
    "vaso de unicel": "❌ No reciclable. Su material es difícil de reciclar.",
    "colilla de cigarro": "❌ No reciclable. Contiene sustancias tóxicas y contaminantes.",
    "pañuelos desechables": "❌ No reciclable. Se contaminan fácilmente.",
    "papel encerado": "❌ No reciclable. Tiene una capa de cera que impide su reciclaje.",
    "papel aluminio": "❌ No reciclable. Suele estar contaminado con residuos de comida.",
    "papel plastificado": "❌ No reciclable. Su mezcla de materiales impide su reprocesamiento.",
    "esponjas": "❌ No reciclable. Hechas de materiales sintéticos que no se pueden recuperar.",
    "cotonetes": "❌ No reciclable. Contienen plástico y residuos biológicos.",
    "cepillos de dientes": "❌ No reciclable. Mezcla de plásticos y otros materiales.",
    "cables": "❌ No reciclable en contenedores normales. Llévalos a un punto de reciclaje electrónico.",
    "pilas": "❌ No reciclable en basura común. Contienen metales pesados contaminantes.",
    "baterías": "❌ No reciclable en basura común. Se deben llevar a puntos de recolección especializados.",
    "bombillas": "❌ No reciclable. Contienen gases y materiales peligrosos.",
    "cerámica": "❌ No reciclable. No se funde a la misma temperatura que el vidrio.",
    "espejos": "❌ No reciclable. Tienen recubrimientos metálicos que impiden su reciclaje.",
    "vidrio roto": "❌ No reciclable. Puede ser peligroso y difícil de reciclar.",
    "pañales desechables": "❌ No reciclable. Contienen residuos biológicos.",
    "toallas femeninas": "❌ No reciclable. Contienen materiales sintéticos y residuos biológicos.",
    "pañales para adultos": "❌ No reciclable. Mismo problema que los pañales de bebé.",
    "hisopos": "❌ No reciclable. Contienen plástico y algodón no reciclable.",
    "envases contaminados con grasa": "❌ No reciclable. La grasa impide su reprocesamiento.",
    "papel térmico": "❌ No reciclable. Usado en recibos, contiene químicos que impiden su reciclaje.",
    "servilletas usadas": "❌ No reciclable. Se contaminan con residuos de comida.",
    "cubiertos de plástico": "❌ No reciclable. Suelen estar hechos de plásticos de baja calidad.",
    "bolsas metalizadas": "❌ No reciclable. Mezcla de plástico y aluminio.",
    "telas sintéticas": "❌ No reciclable. Contienen fibras no biodegradables.",
    "ropa vieja": "❌ No reciclable. Mejor opción: donar o reutilizar.",
    "zapatos desgastados": "❌ No reciclable. Mezcla de materiales sintéticos.",
    "tapetes": "❌ No reciclable. Contienen fibras sintéticas difíciles de reprocesar.",
    "caucho": "❌ No reciclable. Material muy complejo de reprocesar.",
    "látex": "❌ No reciclable. No se puede descomponer fácilmente.",
    "plástico contaminado": "❌ No reciclable. Debe estar limpio para reciclarse.",
    "desechos electrónicos": "❌ No reciclable en contenedores comunes. Llévalos a centros de reciclaje especializados.",
    "cascos de huevo": "❌ No reciclable. Se recomienda compostaje en lugar de tirarlos a la basura.",
    "huesos": "❌ No reciclable. Compostables en algunos casos.",
    "restos de comida": "❌ No reciclable. Se recomienda compostaje.",
    "comida en mal estado": "❌ No reciclable. Compostaje o desecho en orgánicos.",
    "aceite usado": "❌ No reciclable en contenedores normales. Puede contaminar el agua y el suelo.",
    "productos químicos": "❌ No reciclable. Requieren tratamiento especial.",
    "fármacos vencidos": "❌ No reciclable. Deben llevarse a puntos de recolección especializados.",
    "radiografías": "❌ No reciclable. Contienen materiales tóxicos.",
    "tubos fluorescentes": "❌ No reciclable. Contienen mercurio y otros elementos peligrosos.",
    "termómetros de mercurio": "❌ No reciclable. Altamente tóxicos, llévalos a un punto de recolección especializado.",
    "aerosoles con contenido": "❌ No reciclable. Pueden contener sustancias peligrosas."
}






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

async def ayuda(ctx):
    mensaje = """🤖 **¡Hola! Soy TrashBot, tu asistente de reciclaje.**
    
🔹 **`!clasificar [objeto]`** → Indica si el objeto es reciclable o no.
🔹 **`!lista_reciclables`** → Muestra una lista de objetos reciclables.
🔹 **`!lista_no_reciclables`** → Muestra una lista de objetos no reciclables.
🔹 **`!consejo`** → Te da un consejo ecológico aleatorio.

🌱 ¡Juntos podemos cuidar el planeta!"""
    await ctx.send(mensaje)

@bot.command()
async def lista_reciclables(ctx):
    lista = ", ".join(RECICLABLES.keys())
    await ctx.send(f'♻️ **Objetos reciclables:** {lista}')

@bot.command()
async def lista_no_reciclables(ctx):
    lista = ", ".join(NO_RECICLABLES.keys())
    await ctx.send(f'🚮 **Objetos no reciclables:** {lista}')

@bot.command()
async def consejo(ctx):
    consejos = [
        "🌍 Usa bolsas reutilizables en lugar de plásticas.",
        "🔋 Recicla las pilas y baterías en puntos de recolección adecuados.",
        "💧 Reduce tu consumo de agua cerrando el grifo cuando no lo uses.",
        "🚲 Usa bicicleta o transporte público para reducir la contaminación.",
        "🍃 Planta un árbol y ayuda al medio ambiente."
    ]
    import random
    await ctx.send(random.choice(consejos))


bot.run("Ya sabes que poner ;)")
