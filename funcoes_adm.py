from funcoes_adm import *
from funcoes_usu import *
from usuario import *
from Login import *
from datetime import date


def add_not(noticias,id_not,logi,not_lista):
    for c in not_lista:
        print(c)
        for v in c.values():
            print(v)
            titulo_not = input('Insira um titulo:').capitalize()
            if titulo_not == v["titulo"]:
                print('\nJá existe uma notícia com esse título...\n')
                break
            elif titulo_not != v["titulo"]:
                corpo_not = input('Insira o corpo da noticia:') 
                id = id_not[0] + 1
                id_not[0] = id
                noticias = {
                    str(id):{'titulo':titulo_not,'corpo':corpo_not,'autor':logi,'hora':date.today(), 'curtidas':0, 'comentarios':''}
                }
                not_lista.append(noticias)
                print('\n=======NOTICIA=CRIADA=COM=SUCESSO!!!======\n')
            else:
                print('\nProgram error...\n')


def buscar_noticia(not_lista,logi,lista_de_comentario): #buscar noticia, olha se tem algum bug nela
    pesquisa = input('Digite o ID da notícia que deseja pesquisar: ')
    for p in not_lista:
        if logi == p[pesquisa]["autor"]:
            print('\n+--------------------------------------------------------------------+'
                    f'\n{p[pesquisa]["titulo"]} ------- {p[pesquisa]["hora"]}'
                    '\n'
                    f'\n{p[pesquisa]["corpo"]}'
                    '\n'
                    f'\nautor: {p[pesquisa]["autor"]} -------- Curtidas: {p[pesquisa]["curtidas"]}'
                    '\n+-------------------------------------------------------------------+'
                    f"\nComentario: {f'{lista_de_comentario}'}"
                    '\n')
        elif logi != p[pesquisa]["autor"]:
            print('VOCÊ NÃO TEM ACESSO A ESSA NOTÍCIA...')
        else:
            print('ERROR...')



def excluir_noticia(not_lista, logi):  #função para excluir noticia
    print('======EXCLUIR=NOTÍCIA====')
    deletar_noticia = input('Digite o ID da notícia para deletar: ')
    confirm = input('Certeza que deseja excluir? [Y/N]')
    if confirm.lower() == 'y':   
        for p in not_lista:
            if logi == p[deletar_noticia]["autor"]:
                del p[deletar_noticia]
                print('========NOTICIA=EXLUIDA=COM=SUCESSO!!!==========')
            else:
                print('VOCÊ NÃO PODE EXCLUIR ESSA NOTÍCIA')
    if confirm.lower() == 'n':
        print('FINALIZANDO....')
        False



def lista(not_lista, logi, lista_de_comentario): #listar noticias
    for p in not_lista:
        for n in p.values():
            if logi == n["autor"]:
                print('\n+--------------------------------------------------------------------+'
                    f'\n{n["titulo"]} ------- {n["hora"]}'
                    '\n'
                    f'\n{n["corpo"]}'
                    '\n'
                    f'\nautor: {n["autor"]} -------- Curtidas: {n["curtidas"]}'
                    '\n+-------------------------------------------------------------------+'
                    f"\nComentario: {f'{lista_de_comentario}'}"
                    '\n')
            else:
                print('═══════════════════════════════════════════════════════════════════════════')



def editar_noticia(not_lista,lista_de_comentario): #editar noticias
  while True:
    for p in not_lista:
        print('=========EDITAR=NOTICIA========')
        edit_noti = input('Digite o id da notícia que quer editar: ')
        if edit_noti in p:
            noticia_para_editar = input('Digite qual parte da noticia você quer editar: ')
    
        if noticia_para_editar == 'titulo':
            editar_titulo = input('Digite o novo titulo: ')
            p[edit_noti][noticia_para_editar] = editar_titulo #para pegar a notiicia no id digitado, ir no index do titulo e editar 
            print('\n+--------------------------------------------------------------------+'
                    f'\n{p[edit_noti]["titulo"]} ------- {p[edit_noti]["hora"]}'
                    '\n'
                    f'\n{p[edit_noti]["corpo"]}'
                    '\n'
                    f'\nautor: {p[edit_noti]["autor"]} -------- Curtidas: {p[edit_noti]["curtidas"]}'
                    '\n+-------------------------------------------------------------------+'
                    f"\nComentario: {f'{lista_de_comentario}'}"
                    '\n')

            tentar_novamnete = input('=====Deseja tentar novamente? [S/N]=====')
            if tentar_novamnete.lower() == 'n':
                False
            elif tentar_novamnete.lower() == 's':
                continue
        elif noticia_para_editar == 'corpo':
            editar_corpo = input('Digite o novo corpo da notícia: ')
            p[edit_noti][noticia_para_editar] = editar_corpo #para pegar a notiicia no id digitado, ir no index do corpo e editar
            print('\n+--------------------------------------------------------------------+'
                    f'\n{p[edit_noti]["titulo"]} ------- {p[edit_noti]["hora"]}'
                    '\n'
                    f'\n{p[edit_noti]["corpo"]}'
                    '\n'
                    f'\nautor: {p[edit_noti]["autor"]} -------- Curtidas: {p[edit_noti]["curtidas"]}'
                    '\n+-------------------------------------------------------------------+'
                    f"\nComentario: {f'{lista_de_comentario}'}"
                    '\n')
            
            tentar_novamnete = input('=====Deseja tentar novamente? [S/N]=====')
            if tentar_novamnete.lower() == 'n':
                False
            elif tentar_novamnete.lower() == 's':
                continue
        if edit_noti not in p: #se a o id não estiver no dicionario
            print('----NOTICIA-NÃO-ENCONTRADA!!!----')
            tentar_novamnete = input('Deseja tentar novamente? [S/N]')
            if tentar_novamnete.lower() == 'n':
                False
            elif tentar_novamnete.lower() == 's':
                continue

def listar_por_curtidas(not_lista):
    for p in not_lista:
        for z in p.values():
            lista_noti = list(z["curtidas"].items())
        n = len(lista_noti)
        for i in range (n):
            for j in range (0, n-i-1):
                if lista_noti[j][1] < lista_noti[j+1][1]:
                    aux = lista_noti[j]
                    lista_noti[j] = lista_noti[j + 1]
                    lista_noti[j + 1] = aux

            print(lista_noti)