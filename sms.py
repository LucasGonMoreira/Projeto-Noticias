from twilio.rest import Client
from datetime import date
import emoji


def notificar_comentario(logi, comentario):
    account_sid = (ACCOUNT_SID)
    auth_token = (AUTH_TOKEN)

    client = Client(account_sid, auth_token)

    client.messages.create(from_=('14157671948'), to=(NUMBER), body=(f'{logi} = {comentario} | {date.today()}'))

def notificar_curtida():
    account_sid = ((ACCOUNT_SID)
    auth_token = (AUTH_TOKEN)

    client = Client(account_sid, auth_token)

    client.messages.create(from_=('14157671948'), to=(NUMBER), body=(emoji.emojize('Alguém curtiu sua notícia :red_heart:')))
