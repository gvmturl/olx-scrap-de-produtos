from telegram.ext import Updater, CommandHandler
from params import token
from bot_functions import *
from db_connection import db
import time

def listener():
    ''' Script que fica sempre ativo, aguardando comandos do bot. '''

    updater     = Updater(token=token, use_context=True)
    dispatcher  = updater.dispatcher

    start_handler   = CommandHandler('start', start)
    busca_handler   = CommandHandler('busca', busca)
    cancela_handler = CommandHandler('cancela', cancela)

    dispatcher.add_handler(start_handler)
    dispatcher.add_handler(busca_handler)
    dispatcher.add_handler(cancela_handler)

    updater.start_polling()


if __name__ == '__main__':
    listener()
    db.close()


while True:
    exec(open('checker.py').read())
    time.sleep(3600) #A cada hora ele executa o checker.py
    print("Checker executado depois de 1 hora") #Informa o administrador sobre checker.py executado
