from funcoes_adm import *
from funcoes_usu import *
from usuario import *
from menu import *

def login(adm_lista, usu_lista, senha_dicionario, not_lista, noticias, id_not,lista_de_comentario):
        while True:
            CDS_LOGIN()
            logi = input('Digite seu nome de usuário: ')  # Nome de usuario para login
            senha = input('Digite sua senha: ')  # Senha de usuario para login           
            
            if logi not in (usu_lista or adm_lista) and senha_dicionario.get(logi) != senha:
                print('Nome ou senha do usuário estão incorretos.')
                False


            sn = input('Todos os dados estão corretos?'  # Verificar são para o cliente, caso queira corrigir o cadastro
                '\nse Sim digite S, se Não, digite N:')                                                           
            if sn == 'N' or sn == 'n':
                False            
            elif sn == 'S' or sn == 's':                

                if logi in usu_lista and senha_dicionario.get(logi) == senha:
                    login_usu(logi,not_lista, noticias, id_not, lista_de_comentario)# verifição se login e senha batem com a do usuario      
                    break
                if logi in adm_lista and senha_dicionario.get(logi) == senha:
                    login_adm(logi, not_lista, noticias, id_not,lista_de_comentario)  # verifição se login e senha batem com a do usuario 
                    break



def login_adm(logi, not_lista, noticias, id_not,lista_de_comentario):
        print('------LOGIN EFETUADO COM SUCESSO!!!------'
        f'\nSeja bem vindo(a), {logi}. '
        '\n1- Inserir notícias'
        '\n2- Listar notícias'
        '\n3- Excluir notícia'
        '\n4- Editar notícia'
        '\n5- Buscar notícia'
        '\n6- Listar por curtidas'
        '\n7- Logout')
        opcao = int(input('Digite a opção: '))

        if opcao == 1:
            print('============CRIE=UMA=NOTÍCIA===========')
            add_not(noticias,id_not,logi, not_lista)   #função para criar uma notícia
            login_adm(logi, not_lista, noticias, id_not,lista_de_comentario)

        elif opcao == 2:
            lista(not_lista, logi,lista_de_comentario)
            login_adm(logi, not_lista, noticias, id_not,lista_de_comentario)                    #função para listar todas as notícias

        elif opcao == 3:
            excluir_noticia(not_lista, logi)
            login_adm(logi, not_lista, noticias, id_not,lista_de_comentario)

        elif opcao == 4:
            editar_noticia(not_lista,lista_de_comentario)
            login_adm(logi, not_lista, noticias, id_not,lista_de_comentario)


        elif opcao == 5:
            buscar_noticia(not_lista,logi,lista_de_comentario)
            login_adm(logi, not_lista, noticias, id_not,lista_de_comentario)           #função para buscar uma notícia
            
        elif opcao == 6:
            listar_por_curtidas(not_lista)
            login_adm(logi, not_lista, noticias, id_not,lista_de_comentario)

        elif opcao == 7:
            print('FAZENDO-LOGOUT...')
            False                         #sair do site


def login_usu(logi, not_lista, noticias, titulo_not,lista_de_comentario):
        
        print('-----LOGIN EFETUADO COM SUCESSO!!!-----'
        f'\nSeja bem vindo(a), {logi}.'
        '\n1- Buscar notícia'
        '\n2- Comentar notícia'
        '\n3- Curtir notícia'
        '\n4- Logout')
        opcao = int(input('digite a opção: '))

        if opcao == 1:
            buscar_noticia_usuario(not_lista,lista_de_comentario) 
            login_usu(logi, not_lista, noticias, titulo_not,lista_de_comentario)                #função para listar todas as notícias

        elif opcao == 2:
            comentar_noticia(not_lista,logi,lista_de_comentario,lista_de_comentario)
            login_usu(logi, not_lista, noticias, titulo_not,lista_de_comentario)         #função para buscar uma notícia

        elif opcao == 3:
            curtir_noticia(not_lista)
            login_usu(logi, not_lista, noticias, titulo_not,lista_de_comentario)

        elif opcao == 4:
            False