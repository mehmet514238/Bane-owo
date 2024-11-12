import discord
from discord.ext import commands
import os
from dotenv import load_dotenv
from owo_commands import owo_balance, owo_inventory
from owo_info import get_item_info, get_weapon_info
from database import log_balance
from Moderation.moderation import handle_moderation
from Captcha.captcha_handler import solve_captcha, toggle_captcha

# .env dosyasından bilgileri yükle
load_dotenv()
bot_token = os.getenv("BOT_TOKEN")
owo_bot_id = int(os.getenv("OWO_BOT_ID"))

# Bot intents ayarları
intents = discord.Intents.all()
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"{bot.user} olarak giriş yapıldı!")

# Yardım komutu
@bot.command()
async def yardım(ctx):
    help_text = """
**Komutlar:**
!yardım - Tüm komutları gösterir.
!captcha aç - CAPTCHA otomatik çözme işlemini açar.
!captcha kapa - CAPTCHA otomatik çözme işlemini kapatır.
!moderasyon - Moderasyon komutlarını gösterir.
!owo_info - OwO bot hakkındaki eşyalar ve silahlar hakkında bilgi verir.
    """
    await ctx.send(help_text)

# CAPTCHA komutları
@bot.command()
async def captcha(ctx, arg):
    if arg.lower() == "aç":
        toggle_captcha(True)
        await ctx.send("CAPTCHA çözme işlemi **açıldı**.")
    elif arg.lower() == "kapa":
        toggle_captcha(False)
        await ctx.send("CAPTCHA çözme işlemi **kapandı**.")
    else:
        await ctx.send("Lütfen 'aç' veya 'kapa' şeklinde komut verin.")

# Moderasyon komutu
@bot.command()
async def moderasyon(ctx):
    await handle_moderation(ctx)

# OwO eşyaları ve silah bilgisi komutu
@bot.command()
async def owo_info(ctx, category="item"):
    if category == "item":
        info = get_item_info()
    elif category == "weapon":
        info = get_weapon_info()
    else:
        info = "Lütfen geçerli bir kategori girin: 'item' veya 'weapon'."
    await ctx.send(info)

@bot.event
async def on_message(message):
    # CAPTCHA mesajı algılandığında
    if "CAPTCHA" in message.content and message.author.id == owo_bot_id:
        captcha_image_url = "..."  # CAPTCHA resim URL'sini buradan al
        captcha_result = solve_captcha(captcha_image_url)
        await message.channel.send(f"CAPTCHA çözümü: {captcha_result}")

    await bot.process_commands(message)

bot.run(bot_token)
