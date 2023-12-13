#funções
from funcoes_adm import *
from funcoes_usu import *
from usuario import *
from Login import *
from datetime import date
from sms import *

def comentar_noticia(not_lista,logi): #função para comentar na noticia, não sei se está funcionando
    noticia_para_comentar = input('Digite o título da notícia para comentar: ').capitalize()
    for p in not_lista:
        for n in p.values():
                print('════════════COMENTARIOS════════════')
                if noticia_para_comentar == n["titulo"]:
                    comentario = input('Digite o comentario: ')
                    n["comentarios"] = f"|{logi} - {comentario} - {date.today()}|"

                    print('\n+--------------------------------------------------------------------+'
                         f'\n{n["titulo"]} ------- {n["hora"]}'
                          '\n'
                         f'\n{n["corpo"]}'
                          '\n'
                         f'\nautor: {n["autor"]} -------- Curtidas: {n["curtidas"]}'
                          '\n+-------------------------------------------------------------------+'
                         f'\nComentario: {n["comentarios"]}'
                          '\n')
                    #notificar_comentario(logi, comentario)
                else:
                    print("\nEssa noticia não existe...\n")

def curtir_noticia(not_lista): #função para comentar na noticia, não sei se está funcionando
    noticia_curtir = input("Digite o titulo da noticia para curtir: ").capitalize()
    for p in not_lista:
        for n in p.values():
            if noticia_curtir == n["titulo"]:
                n["curtidas"] += 1
                print('curtiu!!!')
                notificar_curtida()
            elif noticia_curtir != n["titulo"]:
                print('\nEssa notícia não existe...\n')
            else:
                print('\nERROR...\n')

def buscar_noticia_usuario(not_lista):
    noticia_pesquisar = input("Digite o titulo da notícia: ").capitalize()
    for p in not_lista:
        for n in p.values():
            if noticia_pesquisar in n["titulo"]:
                print('\n+--------------------------------------------------------------------+'
                        f'\n{p["titulo"]} ------- {p["hora"]}'
                        '\n'
                        f'\n{p["corpo"]}'
                        '\n'
                        f'\nautor: {p["autor"]} -------- Curtidas: {p["curtidas"]}'
                        '\n+-------------------------------------------------------------------+'
                        f'\nComentario: {p["comentarios"]}'
                        '\n')
                print('════════════════════════════════════════════════════════════════════════════')
                
            elif noticia_pesquisar not in n["titulo"]:
                print('\nNoticia não encontrada...\n')
            else:
                print('\nProgram error...\n')