import httpx
import os
from dotenv import load_dotenv
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

load_dotenv()

TOKEN = os.getenv("TELEGRAM_TOKEN")
API_URL = "https://dashboard-financiero-production.up.railway.app"

async def gasto(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        partes = update.message.text.split()
        monto = float(partes[1])
        categoria = partes[2]

        async with httpx.AsyncClient() as client:
            await client.post(f"{API_URL}/transacciones", json={
                "tipo": "gasto",
                "monto": monto,
                "categoria": categoria
            })

        await update.message.reply_text(f"✅ Gasto de ${monto} en {categoria} guardado!")

    except:
        await update.message.reply_text("❌ Formato incorrecto. Usá: /gasto 200 comida")

async def ingreso(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        partes = update.message.text.split()
        monto = float(partes[1])
        categoria = partes[2]

        async with httpx.AsyncClient() as client:
            await client.post(f"{API_URL}/transacciones", json={
                "tipo": "ingreso",
                "monto": monto,
                "categoria": categoria
            })

        await update.message.reply_text(f"✅ Ingreso de ${monto} en {categoria} guardado!")

    except:
        await update.message.reply_text("❌ Formato incorrecto. Usá: /ingreso 10000 beca")

app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(CommandHandler("gasto", gasto))
app.add_handler(CommandHandler("ingreso", ingreso))

print("Bot corriendo...")
app.run_polling()