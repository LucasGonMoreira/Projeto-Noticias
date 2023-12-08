from menu import *

def cadastrar_usuario(adm_lista, usu_lista, senha_dicionario):
    while True:
        while True:
            print('==========CADASTRO=USUÁRIO===========')
            usu_usu = input('Digite seu nome de usuário: ')
            
            if usu_usu in adm_lista or usu_usu in usu_lista:  # Verificação para identificar
                # se o username ja esta em uso
                print('Nome de usuário já está em uso. Escolha outro nome de usuário.')
                continue
            
            else:
                break

        while True:
            usu_senha = input('Digite sua senha: ')
            
            if len(usu_senha) < 6:
                print('Senha tem que ter mais de 6 digitos.')
                continue
            
            else:
                break


        sn = input('Todos os dados estão corretos?'  # Verificar são para o cliente, caso queira corrigir o cadastro
                '\nse Sim digite S, se Não, digite N:')
        
        if sn == 'N' or sn == 'n':
            continue
        
        elif sn == 'S' or sn == 's':
            usu_lista.append(usu_usu)  # Salvar nome de usuario
            senha_dicionario[f'{usu_usu}'] = usu_senha  # Salvar senha e designar senha para determinado user
            break