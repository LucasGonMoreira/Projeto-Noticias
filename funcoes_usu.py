#funções
from funcoes_adm import *
from funcoes_usu import *
from usuario import *
from Login import *
from datetime import date
from sms import notificar_noticia

def comentar_noticia(not_lista,logi,lista_de_comentario,comment): #função para comentar na noticia, não sei se está funcionando
    noticia_para_comentar = input('Digite o título da notícia para comentar: ').capitalize()
    for p in not_lista:
        for n in p.values():
                print('════════════COMENTARIOS════════════')
                if noticia_para_comentar == n["titulo"]:
                    comentario = input('Digite o comentario: ')
                    lista_de_comentario.append(logi)
                    lista_de_comentario.append(comentario)
                    lista_de_comentario.append(date.today())

                    print('\n+--------------------------------------------------------------------+'
                         f'\n{n["titulo"]} ------- {n["hora"]}'
                          '\n'
                         f'\n{n["corpo"]}'
                          '\n'
                         f'\nautor: {n["autor"]} -------- Curtidas: {n["curtidas"]}'
                          '\n+-------------------------------------------------------------------+'
                         f"\nComentario: {f'{lista_de_comentario}'}"
                          '\n')
                    notificar_noticia(logi, comentario)
                else:
                    print("Essa noticia não existe...")

def curtir_noticia(not_lista): #função para comentar na noticia, não sei se está funcionando
    noticia_curtir = input("Digite o titulo da noticia para curtir: ").capitalize()
    for p in not_lista:
        for n in p.values():
            if noticia_curtir == n["titulo"]:
                n["curtidas"] += 1
                print('curtiu!!!')
            elif noticia_curtir != n["titulo"]:
                print('Essa notícia não existe...')
            else:
                print('ERROR...')

def buscar_noticia_usuario(not_lista,lista_de_comentario):
    noticia_pesquisar = input("Digite o titulo da notícia: ").capitalize()
    for p in not_lista:
        for n in p.values():
            if noticia_pesquisar in n["titulo"]:
                noticias_cadastradas(not_lista,lista_de_comentario)
            elif noticia_pesquisar not in n["titulo"]:
                print('\nNoticia não encontrada...\n')
            else:
                print('\nProgram error...\n')