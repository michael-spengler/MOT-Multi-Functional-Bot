from ctypes.wintypes import INT
from telegram import Update, ForceReply
from telegram.ext import Updater, CallbackContext, ConversationHandler
import TicTacToe
import TicTacToe.TicTacToe


def log_input(update):
    print(str(update.message.chat_id) + " entered: " + update.message.text)


def TicTacToe_Multiplayer(update: Update, context: CallbackContext) -> None:
    update.message.reply_text("You are trying to play TicTacToe Multiplayer!")

    TicTacToe.TicTacToe_Multiplayer.TicTacToeMultiplayer.main(update, CallbackContext)


def TicTacToe_Single(update: Update, context: CallbackContext) -> None:
    update.message.reply_text("You are trying to play TicTacToe Singleplayer!")
    TicTacToe.TicTacToe.main(0,  update, CallbackContext)

def stop_Tic(update: Update, context: CallbackContext) -> int:
    update.message.reply_text("Du hast das TicTacToe Spiel beendet!")
    return ConversationHandler.END
