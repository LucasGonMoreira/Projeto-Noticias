from twilio.rest import Client
from datetime import date


def notificar_noticia(logi, comentario):
    account_sid = ('AC61687f37af782bf8b2245948965a4491')
    auth_token = ('7ae954de8b6c09a3a0ba985565a507e3')

    client = Client(account_sid, auth_token)

    client.messages.create(from_=('14157671948'),
                        to=('5583993509222'),
                        body=(f'{logi} = {comentario} | {date.today()}'))
