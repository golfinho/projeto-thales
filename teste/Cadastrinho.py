#!/usr/bin/python
#-*- coding: utf8 -*-]
import os, re


def LimparTela():
    os.system('cls||clear')

try:
    LimparTela()

    nome = input('Digite o seu nome: ')
    
    if re.findall('[!@#$%&*1234567890()]', nome):
        print('O nome esta incorreto, Tente outra vez fofissimo(a).')
    else:
        print('O nome esta correto.')

    mail = input('Digite o seu email: ')
    if re.findall(r'^.{1,}@([A-Z|a-z]{1,})\.(com|com.br|br)', mail):
        print('O email esta correto.')
    else:
        print('O email esta incorreto, Tente outra vez fofissimo(a).')

    data = input('Digite sua data de nascimento: ')
    if re.findall(r'^[0-9]{2}/[0-9]{2}/[0-9]{2,4}$', data):
        print('A data de nascimento esta correta.')
    else:
        print('A data de nascimento esta incorreta, Tente outra vez Fofissimo(a).')

    phone = input('Digite seu numero de telefone: ')
    if re.findall(r'^\([0-9]{2}\)[0-9]{5}-[0-9]{4}$', tel):
         print('O telefone esta correto.')
    else:
        print('O telefone esta incorreto, Tente outra vez fofissimo(a).')

    rg = input('Digite o seu RG: ')
    if re.findall(r'^[0-9]{2}(\.[0-9]{3}){2}-[0-9]', rg):
        print('O RG esta correto.')
    else:
         print('O RG esta incorreto, Tente outra vez fofissimo(a).')

    cpf = input('Digite o seu CPF: ')
    if re.findall(r'^([0-9]{3}\.){2}[0-9]{3}-[0-9]{2}$', cpf):
        print('O CPF esta correto.')
    else:
        print('O CPF esta incorreto, Tente outra vez fofissimo(a).')

    ip  = input('Digite o seu IP: ')
    if re.findall(r'^([0-254]{1,3}\.){3}[0-254]{1,3}$', ip):
        print('O IP esta correto.')
    else:
        print('O IP esta incorreto, Tente outra vez fofissimo(a).')

    masc = input('Digite sua mascara de rede: ')
    if re.findall(r'^([0-255]{1,3}\.){3}[0-255]{1,3}$', masc):
         print('a mascara esta correta.')
    else:
        print('A mascara esta incorreta, Tente outra vez fofissimo(a).')

except KeyboardInterrupt:
    print()
