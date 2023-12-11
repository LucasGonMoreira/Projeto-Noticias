from twilio.rest import Client
from datetime import date


def notificar_comentario(logi, comentario):
    account_sid = ('AC61687f37af782bf8b2245948965a4491')
    auth_token = ('d92e228488cb679705b893c2350d4c6d')

    client = Client(account_sid, auth_token)

    client.messages.create(from_=('14157671948'), to=('5583993509222'), body=(f'{logi} = {comentario} | {date.today()}'))

def notificar_curtida():
    account_sid = ('AC61687f37af782bf8b2245948965a4491')
    auth_token = ('d92e228488cb679705b893c2350d4c6d')

    client = Client(account_sid, auth_token)

    client.messages.create(from_=('14157671948'), to=('5583993509222'), body=('Alguém curtiu sua notícia..'))
