# import asyncio
from telegram import (
        Update,
        BotCommand,
        ReplyKeyboardMarkup
    )
from telegram.ext import (
        ApplicationBuilder,
        CommandHandler,
        ContextTypes,
        MessageHandler,
        filters
    )
from data import texts


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(texts.data["start"])


async def about(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(texts.data["about"])


async def services(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(texts.data["services"])


async def contacts(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(texts.data["contacts"])


async def address(updete: Update, context: ContextTypes.DEFAULT_TYPE):
    await updete.message.reply_text(texts.data["address"])


async def polygraphy(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(texts.data["polygraphy"])


async def outdoor(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(texts.data["outdoor"])


async def souvenirs(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(texts.data["souvenirs"])


async def print(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(texts.data["print"])


async def faq(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(texts.data["faq"])


async def feedback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(texts.data["feedback"])


async def team(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(texts.data["team"])


async def set_commands(application):
    commands = [
        BotCommand(command="about",
                   description="Информация о рекламном агентстве Мега Принт"),
        BotCommand(command="services",
                   description="Перечень предоставляемых услуг"),
        BotCommand(command="contacts",
                   description="Контактная информация агентства"),
        BotCommand(command="address",
                   description="Адрес и график работы"),
        BotCommand(command="polygraphy",
                   description="Полиграфическая продукция"),
        BotCommand(command="outdoor",
                   description="Наружная реклама"),
        BotCommand(command="souvenirs",
                   description="Сувинирная продукция"),
        BotCommand(command="print",
                   description="Широкоформатная печать"),
        BotCommand(command="faq",
                   description="Часто задаваемые вопросы"),
        BotCommand(command="feedback",
                   description="Как связаться с нами"),
        BotCommand(command="team",
                   description="Информация о сотрудниках агентства")
        ]
    await application.bot.set_my_commands(commands)


def main():
    app = (
        ApplicationBuilder()
        .token("7085327475:AAGV91vKfdkd_ShhkpTqfmip9qtIHsrP4p8")
        .post_init(set_commands)
        .build()
    )

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("about", about))
    app.add_handler(CommandHandler("services", services))
    app.add_handler(CommandHandler("contacts", contacts))
    app.add_handler(CommandHandler("address", address))
    app.add_handler(CommandHandler("polygraphy", polygraphy))
    app.add_handler(CommandHandler("outdoor", outdoor))
    app.add_handler(CommandHandler("souvenirs", souvenirs))
    app.add_handler(CommandHandler("print", print))
    app.add_handler(CommandHandler("faq", faq))
    app.add_handler(CommandHandler("feedback", feedback))
    app.add_handler(CommandHandler("team", team))
    app.run_polling(stop_signals=None)


if __name__ == "__main__":
    main()
