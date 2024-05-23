import os
import logging
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
from dotenv import load_dotenv

# Carregar variáveis de ambiente do arquivo .env
load_dotenv()

# Configuração básica de logging para o bot
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

logger = logging.getLogger(__name__)

# Definir comandos do bot

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text('Bot Online, Test build 1.0')

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text('Aqui está um guia de como usar este bot...')

async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(update.message.text)

def main() -> None:
    token = os.getenv('TOKEN')

    if not token:
        logger.error('Erro: TOKEN não encontrado. Verifique suas variáveis de ambiente.')
        return

    # Cria a aplicação e passa o token do bot
    application = Application.builder().token(token).build()

    # Registra os handlers de comando
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_command))

    # Registra um handler para mensagens de texto (responde com o mesmo texto)
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))

    # Inicia o bot
    application.run_polling()

# Inicializar o bot
if __name__ == '__main__':
    main()
