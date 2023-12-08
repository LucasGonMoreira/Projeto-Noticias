from art import *
def menu():
    menuuu = text2art("MENU")
    print('===============================')
    print(menuuu)
    print('===============================')
    print('1-Cadastrar como administrador'
          '\n2-Cadastrar como usuario'
          '\n3-Login'
          '\n4-sair')


def CDS_LOGIN():
    menu_login = text2art("LOGIN")
    print('===============================')
    print(menu_login)
    print('===============================')

def menu_noticias(logi,not_lista,lista_de_comentario):
    for n in not_lista:
        for p in n.values():
            if logi == p["autor"]:
                print('\n+--------------------------------------------------------------------+'
                        f'\n{p["titulo"]} ------- {p["hora"]}'
                        '\n'
                        f'\n{p["corpo"]}'
                        '\n'
                        f'\nautor: {p["autor"]} -------- Curtidas: {p["curtidas"]}'
                        '\n+-------------------------------------------------------------------+'
                        f"\nComentario: {f'{lista_de_comentario}'}"
                        '\n')
                print('════════════════════════════════════════════════════════════════════════════')

def noticias_cadastradas(not_lista,lista_de_comentario):
    for n in not_lista:
        for p in n.values():
            print('\n+--------------------------------------------------------------------+'
                    f'\n{p["titulo"]} ------- {p["hora"]}'
                    '\n'
                    f'\n{p["corpo"]}'
                    '\n'
                    f'\nautor: {p["autor"]} -------- Curtidas: {p["curtidas"]}'
                    '\n+-------------------------------------------------------------------+'
                    f"\nComentario: {f'{lista_de_comentario}'}"
                    '\n')
            print('════════════════════════════════════════════════════════════════════════════')