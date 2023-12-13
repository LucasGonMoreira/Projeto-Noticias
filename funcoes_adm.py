from funcoes_adm import *
from funcoes_usu import *
from usuario import *
from Login import *
from datetime import date
from menu import *
import aspose.words as aw


def add_not(noticias,id_not,logi,not_lista,aux):
    titulo_not = input('Insira um titulo:').capitalize()
    if titulo_not in aux:
        print('\nJá existe uma notícia com esse título\n')
        False
    elif titulo_not not in aux:
        aux.append(titulo_not)
        corpo_not = input('Insira o corpo da noticia:') 
        id = id_not[0] + 1
        id_not[0] = id
        noticias = {
            str(id):{'titulo':titulo_not,'corpo':corpo_not,'autor':logi,'hora':f"{date.today()}", 'curtidas':0, 'comentarios':''}
        }
        not_lista.append(noticias)
        
        with open(f'{logi}.txt','a') as f:
            f.write(f"---------\n{str(id)}\n{titulo_not}\n{corpo_not}\n{date.today()}\n--------\n")
            
        print('\n=======NOTICIA=CRIADA=COM=SUCESSO!!!======\n')
    else:
        print('\nProgram error...\n')

def buscar_noticia(not_lista,logi): #buscar noticia, olha se tem algum bug nela
    pesquisa = input('Digite o ID da notícia que deseja pesquisar: ')
    for p in not_lista:
        if pesquisa in p:    
            if logi == (p[pesquisa]["autor"]):
                print('\n+--------------------------------------------------------------------+'
                        f'\n{p[pesquisa]["titulo"]} ------- {p[pesquisa]["hora"]}'
                        '\n'
                        f'\n{p[pesquisa]["corpo"]}'
                        '\n'
                        f'\nautor: {p[pesquisa]["autor"]} -------- Curtidas: {p[pesquisa]["curtidas"]}'
                        '\n+-------------------------------------------------------------------+'
                        f"\nComentario: {p[pesquisa]['comentarios']}"
                        '\n')
            elif logi != (p[pesquisa]["autor"]):
                print('VOCÊ NÃO TEM ACESSO A ESSA NOTÍCIA...')
            else:
                print('\nProgram error...\n')
        else:
            print('\n-------Notícia-não-encontrada--------\n')



def excluir_noticia(not_lista, logi):  #função para excluir noticia
    print('======EXCLUIR=NOTÍCIA====')
    deletar_noticia = input('Digite o ID da notícia para deletar: ')
    confirm = input('Certeza que deseja excluir? [Y/N]')
    if confirm.lower() == 'y':   
        for p in not_lista:
            if logi == (p[deletar_noticia]["autor"]):
                del p[deletar_noticia]
                print('\n========NOTICIA=EXLUIDA=COM=SUCESSO!!!=========\n')
            else:
                print('VOCÊ NÃO PODE EXCLUIR ESSA NOTÍCIA')
    if confirm.lower() == 'n':
        print('\nFINALIZANDO....\n')
        False



def lista(not_lista, logi): #listar noticias
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
                    f'\nComentario: {n["comentarios"]}'
                    '\n')
            else:
                print('═══════════════════════════════════════════════════════════════════════════')



def editar_noticia(not_lista): #editar noticias
    edit_noti = input('Digite o id da notícia que quer editar: ')
    for p in not_lista:
        print('=========EDITAR=NOTICIA========')
        if edit_noti not in p.keys():
            print('\n---------Notícia-não-encontrada--------\n')
        elif edit_noti in p:
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
                        f"\nComentario: {p[edit_noti]['comentarios']}"
                        '\n')
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
                        f"\nComentario: {p[edit_noti]['comentarios']}"
                        '\n')
            

def salvar_como_pdf(logi):
    doc = aw.Document(f"{logi}.txt")
    doc.save(f"{logi}_pdf.pdf")
    print('\nDocumento salvo com sucesso!!!\n')
    False
