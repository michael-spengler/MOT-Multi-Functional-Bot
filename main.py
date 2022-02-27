#!/usr/bin/env python

from importlib.metadata import entry_points
import requests
from telegram import Update, ForceReply
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext, ConversationHandler
from conf import API_KEY
from main_commands import start, help_command, nudel, cat, echo
from wordle_commands import wordle, guess
from TicTacToe.TicTacToe_commands import *
import TicTacToe.TicTacToe


# Define a few command handlers. These usually take the two arguments update and
# context.


def main() -> None:
    """Start the bot."""
    # Create the Updater and pass it your bot's token.
    updater = Updater(API_KEY)

    # Get the dispatcher to register handlers
    dispatcher = updater.dispatcher

    TicTacToe_handler = ConversationHandler(
        entry_points = [CommandHandler("tic", TicTacToe_Single)],
        states = {
            TicTacToe.TicTacToe.PLAYER: [MessageHandler(Filters.regex('^[0-2],[0-2]$'), TicTacToe.TicTacToe.player)]
        },
        fallbacks = [CommandHandler('stop_Tic', stop_Tic)] 

    )

    # on different commands - answer in Telegram
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("help", help_command))
    dispatcher.add_handler(CommandHandler("nudel", nudel))
    dispatcher.add_handler(CommandHandler("cat", cat))
    
    # TicTacToe commands
    dispatcher.add_handler(CommandHandler("multiTic", TicTacToe_Multiplayer))
    dispatcher.add_handler(TicTacToe_handler)
    #dispatcher.add_handler(CommandHandler("stop", stop))
    


    # on non command i.e message - echo the message on Telegram
    dispatcher.add_handler(MessageHandler(
        Filters.text & ~Filters.command, echo))

    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()


if __name__ == '__main__':
    main()
