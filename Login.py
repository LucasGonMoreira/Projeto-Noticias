from funcoes_adm import *
from funcoes_usu import *
from usuario import *
from menu import *

def login(adm_lista, usu_lista, senha_dicionario, not_lista, noticias, id_not,aux):
        while True:
            CDS_LOGIN()
            logi = input('Digite seu nome de usuário: ')  # Nome de usuario para login
            senha = input('Digite sua senha: ')  # Senha de usuario para login           
            
            if logi not in (usu_lista or adm_lista) and senha_dicionario.get(logi) != senha:
                print('Nome ou senha do usuário estão incorretos.')
                break


            sn = input('Todos os dados estão corretos?'
                '\nse Sim digite S, se Não, digite N:')                                                           
            if sn == 'N' or sn == 'n':
                False            
            elif sn == 'S' or sn == 's':                

                if logi in usu_lista and senha_dicionario.get(logi) == senha:
                    login_usu(logi,not_lista, noticias, id_not)
                    break
                if logi in adm_lista and senha_dicionario.get(logi) == senha:
                    login_adm(logi, not_lista, noticias, id_not,aux)
                    break



def login_adm(logi, not_lista, noticias, id_not,aux):
        print('------LOGIN EFETUADO COM SUCESSO!!!------'
        f'\nSeja bem vindo(a), {logi}. '
        '\n[1] - Inserir notícias'
        '\n[2] - Listar notícias'
        '\n[3] - Excluir notícia'
        '\n[4] - Editar notícia'
        '\n[5] - Buscar notícia'
        '\n[6] - Salvar backup como pdf'
        '\n[7] - Logout')
        
        opcao = int(input('Digite a opção: '))
        if opcao == 1:
            print('============CRIE=UMA=NOTÍCIA===========')
            add_not(noticias,id_not,logi,not_lista,aux)   #função para criar uma notícia
            login_adm(logi, not_lista, noticias, id_not,aux)

        elif opcao == 2:
            lista(not_lista, logi)
            login_adm(logi, not_lista, noticias, id_not,aux)                   #função para listar todas as notícias

        elif opcao == 3:
            excluir_noticia(not_lista, logi)
            login_adm(logi, not_lista, noticias, id_not,aux)

        elif opcao == 4:
            editar_noticia(not_lista,logi)
            login_adm(logi, not_lista, noticias, id_not,aux)


        elif opcao == 5:
            buscar_noticia(not_lista,logi)
            login_adm(logi, not_lista, noticias, id_not,aux)

        elif opcao == 6:
            salvar_como_pdf(logi)

        elif opcao == 7:
            print('FAZENDO-LOGOUT...')
            False                         #sair do site

        else:
            print('\nProgram error...\n')
            False
        

def login_usu(logi, not_lista, noticias, titulo_not):
        
        print('-----LOGIN EFETUADO COM SUCESSO!!!-----'
        f'\nSeja bem vindo(a), {logi}.'
        '\n[1] - Buscar notícia'
        '\n[2] - Comentar notícia'
        '\n[3] - Curtir notícia'
        '\n[4] - Logout')
        opcao = int(input('digite a opção: '))

        if opcao == 1:
            buscar_noticia_usuario(not_lista) 
            login_usu(logi, not_lista, noticias, titulo_not)                #função para listar todas as notícias

        elif opcao == 2:
            comentar_noticia(not_lista,logi)
            login_usu(logi, not_lista, noticias, titulo_not)         #função para buscar uma notícia

        elif opcao == 3:
            curtir_noticia(not_lista)
            login_usu(logi, not_lista, noticias, titulo_not)

        elif opcao == 4:
            print('\nFazendo Logout...')
            False
        else:
            print('\nProgram error...\n')