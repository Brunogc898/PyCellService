
#fazer a parte de relatorio, para mostrar os usuarios cadastrados, os serviços prestados e os aparelhos consertados

import os

usuarios = {}

servicos = {}

consertos = []

m= " "
while m!= "0":
  os.system('clear')
  print("""
-----------------------------
CONSERTA CELULAR DA PRINCIPAL
-----------------------------
-INFORME SEU INTERESSE-
1- CONSERTA APARELHO
2- USUÁRIO
3- SERVIÇOS
4- RELATÓRIO
0- SAIR
""")
  m=input("ESCOLHA: ")

  if m == "1":
   consertar = " "
   while consertar != "0":
    print("""
-----------------------------
CONSERTA APARELHO
-----------------------------
1- PARA PROBLEMAS DIVEROS
2- CATÁLOGO DE SERVIÇOS
0- VOLTAR
""")
    consertar=input("ESCOLHA: ")

    if consertar == "1":
        print("""
 -----------------------------
INFORMAÇÃO DO APARELHO
-----------------------------
1° INFORME O NOME DO SEU APARELHO
2° INFORME O PROBLEMA DO SEU APARELHO
3° INFORME SEU CPF CASO FOR UM USUARIO CADASTADO 
""")
        aparelho=input("NOME DO APARELHO: ")
        problema=input("PROBLEMA DO APARELHO: ")
        cpf=input("INFORME SEU CPF CASO FOR UM USUARIO CADASTADO :")
        if cpf in usuarios:
         print("USUÁRIO ENCONTRADO")
         consertos.append({"aparelho": aparelho, "problema": problema, "cpf": cpf})
         print("APARELHO CADASTRADO PARA CONSERTO COM SUCESSO!")
         input("PRESSIONE ENTER PARA CONTINUAR...")
        else:
         print("USUÁRIO NÃO ENCONTRADO, POR FAVOR CADASTRE-SE ANTES DE SOLICITAR O CONSERTO")
         input("PRESSIONE ENTER PARA CONTINUAR...")
     
    elif consertar == "2":
      print("""
-----------------------------
SERVIÇOS DISPONÍVEIS
-----------------------------
""")
      print("MANUTENÇÃO")
      input("PRESSIONE ENTER PARA CONTINUAR...")
  
  elif m == "2" :
    usuario = " "
    while usuario != "0":
      print("""
-----------------------------
USUARIO
-----------------------------
1- CADASTRAR USUARIO
2- DELETAR USUARIO
3- ATUALIZAR USUARIO
0- VOLTAR
""")
      usuario=input("ESCOLHA: ")

      if usuario== "1":
       print("""
-----------------------------
CADASTRAR USUARIO
-----------------------------
1° INFORME SEU NOME
2° E-MAIL PARA CONTATO
3° SEU CPF
""")

       nome=input("NOME: ")
       email=input("E-MAIL: ")
       cpf=(input("CPF: "))
       usuarios[cpf] = {"nome": nome, "email": email}

       print("CADASTRO REALIZADO COM SUCESSO!")
       input("PRESSIONE ENTER PARA CONTINUAR ")

      elif usuario == "2":
       print("""
-----------------------------
DELETAR USUARIO
-----------------------------
1° INFORME SEU CPF PARA DELETAR
2° CONFIRME SE QUER REALMENTE QUER DELETAR
""")
       cpf=input("CPF: ")
       
       if cpf in usuarios:
        print("USUARIO ENCONTRADO")
        conf=input("CONFIRME SE QUER DELETAR O USUARIO COM (S/N): ")
        
        if conf == "S":
         del usuarios[cpf]
        
        else:
         print("CANCELAMENTO DA DELETA DE USUARIO")
         input("PRESSIONE ENTER PARA CONTINUAR ")
       
       else:
        print("USUARIO NÃO ENCOTRADO")
        input("PRESSIONE ENTER PARA CONTINUAR...")
    
      elif usuario == "3":
       print("""
-----------------------------
ATUALIZAR USUARIO
-----------------------------
1° INFORME NOVAMENTE SEU NOME, E-MAIL E CPF
""")
       nome=input("NOME: ")
       email=input("E-MAIL:")
       cpf=input("CPF: ")
       usuarios[cpf] = {"nome": nome, "email": email}

  elif m == "3":
   
   servico = " "
   while servico !="0":
    print("""
-----------------------------
TIPO DE SERVIÇO
-----------------------------
1- CRIAR SERVIÇO
2- DELETAR SERVIÇO
3- ATUALIZAR SERVIÇO
4- MOSTRAR TODOS OS SERVIÇOS
0- SAIR
""")
    servico = input("ESCOLHA: ")
    if servico == "1":
     print("""
-----------------------------
CRIAR SERVIÇO
-----------------------------
1° INFORME O NOME DO SERVIÇO
2° INFORME A DESCRIÇÃO DO SERVIÇO
3° INFORME O VALOR DO SERVIÇO
""")

     nome=input("NOME DO SERVIÇO: ")
     descricao=input("DESCRIÇÃO DO SERVIÇO: ")
     valor=float(input("VALOR DO SERVIÇO: "))
     servicos[nome] = {"descricao": descricao, "valor": valor}

     print("SERVIÇO CRIADO COM SUCESSO!")
     input("PRESSIONE ENTER PARA CONTINUAR ")
   
    elif servico == "2":
     print("""
-----------------------------
DELETAR SERVIÇO
-----------------------------
1° INFORME O NOME DO SERVIÇO PARA DELETAR
2° CONFIRME SE QUER REALMENTE DELETAR O SERVIÇO
""")
     nome=input("NOME DO SERVIÇO: ")
     if nome in servicos:
      print("SERVIÇO ENCONTRADO")
      conf=input("CONFIRME SE QUER DELETAR O SERVIÇO COM (S/N): ")
      
      if conf == "S":
        del servicos[nome]
        print("SERVIÇO DELETADO COM SUCESSO!")
        input("PRESSIONE ENTER PARA CONTINUAR ")
      
      else:
        print("CANCELAMENTO DA DELETA DE SERVIÇO")
        input("PRESSIONE ENTER PARA CONTINUAR...")
    
     else:
      print("SERVIÇO NÃO ENCOTRADO")
      input("PRESSIONE ENTER PARA CONTINUAR...")
   
    elif servico == "3":
     print("""
-----------------------------
ATUALIZAR SERVIÇO
-----------------------------
1° INFORME O NOME DO SERVIÇO PARA ATUALIZAR
2° INFORME NOVAMENTE A DESCRIÇÃO E O VALOR DO SERVIÇO
""")
     nome=input("NOME DO SERVIÇO: ")
     descricao=input("DESCRIÇÃO DO SERVIÇO: ")
     valor=float(input("VALOR DO SERVIÇO: "))
     
     if nome in servicos:
      print("SERVIÇO ENCONTRADO")
      servicos[nome] = {"descricao": descricao, "valor": valor}
      print("SERVIÇO ATUALIZADO COM SUCESSO!")
      input("PRESSIONE ENTER PARA CONTINUAR ")
    
     else:
      print("SERVIÇO NÃO ENCOTRADO")
      input("PRESSIONE ENTER PARA CONTINUAR...")

    elif servico == "4":
     print("""
-----------------------------
SERVIÇOS DISPONÍVEIS
-----------------------------
""")
    print("MANUTENÇÃO")
    input("PRESSIONE ESPAÇO PARA CONTINUAR ")

  elif m =="4":
   
   relatorio=" "
   while relatorio != "0":
    print("""
-----------------------------
RELATORIO
-----------------------------
1- RELATORIO DE USUARIOS
2- SERVIÇOS PRESTADOOS
3- APARELHOS CONSETADOS
0- VOLTAR
""")
    relatorio=input("ESCOLHA: ")

    if relatorio == "1":
     print("""
-----------------------------
RELATORIO DE USUARIOS
-----------------------------
""")
     print("MANUTENÇÃO")
     input("PRESSIONE ESPAÇO PARA CONTINUAR ")

    elif relatorio == "2":
      print("""
-----------------------------
RELATORIO DE SERVIÇOS PRESTADOS
-----------------------------
""")
      print("MANUTENÇÃO")
      input("PRESSIONE ESPAÇO PARA CONTINUAR " )
    
    elif relatorio == "3":
      print("""
-----------------------------
RELATORIO DE APARELHOS CONSERTADOS
-----------------------------
""")
      print("MANUTENÇÃO")
      input("PRESSIONE ESPAÇO PARA CONTINUAR ")
  
  elif m == "0":
    print("SAINDO DO PROGRAMA...")
    input("PRESSIONE ENTER PARA CONTINUAR...")
  
  else:
    print("OPÇÃO INVÁLIDA, POR FAVOR ESCOLHA UMA OPÇÃO VÁLIDA")
    input("PRESSIONE ENTER PARA CONTINUAR...")
   