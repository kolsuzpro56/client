import discord
from discord.ext import commands
import random
import asyncio

# Ayarlar
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user.name} göreve hazır !')

# !oyna Komutu
@bot.command()
async def oyna(ctx):
    embed = discord.Embed(title="Oyun Seçimi", description="Seç bakalım :", color=0x00ff00)
    embed.add_field(name="1. Yazı Tura", value="`!yazıtura` yazman yeterli.", inline=False)
    embed.add_field(name="2. Sayı Tahmin", value="`!sayıtahmin` ile şansını dene.", inline=False)
    await ctx.send(embed=embed)

# !yazıtura Komutu
@bot.command()
async def yazıtura(ctx):
    sonuc = random.choice(["Yazı", "Tura"])
    await ctx.send(f"Parayı fırlattım... Geldi: **{sonuc}**")

# !sayıtahmin Komutu (İnteraktif)
@bot.command()
async def sayıtahmin(ctx):
    sayi = random.randint(1, 10)
    await ctx.send("1 ile 10 arasında bir sayı tuttum. Bil bakalım hangisi?")

    def check(m):
        return m.author == ctx.author and m.channel == ctx.channel and m.content.isdigit()

    try:
        tahmin = await bot.wait_for('message', check=check, timeout=10.0)
        
        if int(tahmin.content) == sayi:
            await ctx.send(f"Helal olsun! Doğru bildin, sayı: {sayi}")
        else:
            await ctx.send(f"Bilemedin. Tuttuğum sayı: {sayi} idi.")
            
    except asyncio.TimeoutError:
        await ctx.send("Çok bekledin, zaman doldu.")

# Muhabbet Komutları
@bot.command()
async def selam(ctx):
    await ctx.send("Aleyküm selam, hoş geldin.")

@bot.command()
async def merhaba(ctx):
    await ctx.send("Merhaba .")

@bot.command()
async def nasılsın(ctx):
    await ctx.send("Fişek gibiyim, sen nasılsın?")

@bot.command()
async def iyiyim(ctx):
    await ctx.send("Allah iyilik versin, keyfin bol olsun.")

# Botun Tokeni (Buraya kendi tokenini yapıştıracaksın)
bot.run('TOKENİNİZİ YAZIN')
