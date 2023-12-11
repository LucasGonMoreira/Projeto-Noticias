#Created by Lucas Gonçalves Moreira

#Funções
from menu import *
from admin import *
from usuario import *
from Login import *
import datetime

#listas/dicionarios
senha_dicionario = {'lucas4904':'adm01','moreira':'0101'}  # dicionario para verificar se a senha é ompativel com o usuario dela
adm_lista = ['lucas4904']         # lista para gravar o nome de usuario
usu_lista = ['moreira']         # lista para gravar o nome de usuario
#not_lista = [{'1': {'titulo': 'Lucas', 'corpo': 'caiu da escada', 'autor': 'lucas4904', 'hora': '2023, 12, 8', 'curtidas': 2, 'comentarios': ''}}, {'2': {'titulo': 'Mateus', 'corpo': 'caiu da escada', 'autor': 'lucas4904', 'hora': '2023, 12, 8', 'curtidas': 5, 'comentarios': ''}}]         # lista para gravar todas as noticias
not_lista = []
noticias = {}          # dicionario para ligar titulos as noticias
id_not = [0]            # dicionario para ligar id a notícias
aux = [] #para gravar o titulo da notícia


# Menu principal do programa 
while True:    
    menu()
    esc = input('Digite a ação escolhida: ')

    if esc != '1234':
        False

    if esc == '4':
        print('\nVolte sempre...\n')
        exit()

    if esc == '1':
       cadastrar_adm(adm_lista, usu_lista, senha_dicionario)
    
    if esc == '2':
       cadastrar_usuario(adm_lista, usu_lista, senha_dicionario)

    if esc == '3':
        login(adm_lista, usu_lista, senha_dicionario, not_lista, noticias, id_not,aux)
    else:
        print('\nProgram error...\n')
        False