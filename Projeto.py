#TROCAR AS CHAVES DOS SERVIÇOS POR NUMEROES E A PARTE DO CONSERTO TROCA PRA DICIONARIO E TB POR DATA DE NASCIMENTO

import os

usuarios = {
  "12345678900": {"nome": "João Silva", "email": "joao.silva@gmail.com"},
  "98765432100": {"nome": "Maria Santos", "email": "mariasantos@gmail.com"},
  "11122233344": {"nome": "Carlos Oliveira", "email": "carlos.oliveira@gmail.com"},
  "55566677788": {"nome": "Ana Costa", "email": "ana.costa@gmail.com"},
  "99988877766": {"nome": "Pedro Almeida", "email": "pedro.almeida@gmail.com"}
}

servicos = {
 "MANUTENÇÃO": {"descricao": "Manutenção geral de celulares", "valor": 100.0},
 "TROCA DE TELA": {"descricao": "Troca de tela para celulares", "valor": 150.0},
 "TROCA DE BATERIA": {"descricao": "Troca de bateria para celulares", "valor": 80.0},
 "TROCA DE CARCAÇA": {"descricao": "Troca de carcaça para celulares", "valor": 120.0},
 "LIMPEZA INTERNA": {"descricao": "Limpeza interna de celulares", "valor": 50.0},
 "RECUPERAÇÃO DE DADOS": {"descricao": "Recuperação de dados para celulares", "valor": 200.0},
 "FORMATAÇÃO": {"descricao": "Formatação de celulares", "valor": 70.0}
}

consertos = [
["12345678900", "iPhone 12", "Tela quebrada"],
["98765432100", "Samsung Galaxy S21", "Bateria viciada"],
["11122233344", "Xiaomi Redmi Note 10", "Problema no carregamento"],
["55566677788", "Motorola Moto G Power", "FORMATAÇÃO"],
["99988877766", "OnePlus 9 Pro", "LIMPEZA INTERNA"]
]

m= " "
while m!= "0":
  os.system('cls')
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
PROBLEMAS DIVERSOS
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
         consertos.append([cpf, aparelho, problema])
         
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
      for nome in servicos:
       print("----------------------------------------------------------------------------")
       print(f"NOME DO SERVIÇO: {nome} - DESCRIÇÃO: {servicos[nome]['descricao']} - VALOR: R${servicos[nome]['valor']}")
      
      print("----------------------------------------------------------------------------")
      tipo=input("ESCOLHA UM SERVIÇO PARA SOLICITAR  ")
      
      if tipo in servicos:
       print("""
---------------------------------
INFORMAÇÃO PARA PRESTAR O SERVIÇO
---------------------------------
1° INFORME O NOME DO SEU APARELHO
2° INFORME SEU CPF CASO FOR UM USUARIO CADASTADO""")
       
       aparelho=input("NOME DO APARELHO: ")
       cpf=input("INFORME SEU CPF CASO FOR UM USUARIO CADASTADO :")
       
       if cpf in usuarios:
           print("USUÁRIO ENCONTRADO")
           consertos.append([cpf, aparelho, tipo])
          
           print("SERVIÇO SOLICITADO COM SUCESSO!")
           input("PRESSIONE ENTER PARA CONTINUAR...")
        
       else:
          print("USUÁRIO NÃO ENCONTRADO, POR FAVOR CADASTRE-SE ANTES DE SOLICITAR O CONSERTO")
          input("PRESSIONE ENTER PARA CONTINUAR...")
  
  elif m == "2" :
    usuario = " "
    os.system('cls')
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
   os.system('cls')
   while servico !="0":
    print("""
-----------------------------
SERVIÇOS
-----------------------------
1- CRIAR SERVIÇO
2- DELETAR SERVIÇO
3- ATUALIZAR SERVIÇO
4- MOSTRAR TODOS OS SERVIÇOS
0- SAIR
""")
    servico = input("ESCOLHA: ")
    os.system('cls')
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
     os.system('cls')
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
     os.system('cls')
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
     for nome in servicos:
      print("--------------------------------------------------------------------------------------------")
      print(f"NOME: {nome} - DESCRIÇÃO: {servicos[nome]['descricao']} - VALOR: {servicos[nome]['valor']}")
     print("--------------------------------------------------------------------------------------------")
     input("PRESSIONE ESPAÇO PARA CONTINUAR ")

  elif m == "4":
   
   relatorio=" "
   while relatorio != "0":
    os.system('cls')
    print("""
-----------------------------
RELATORIO
-----------------------------
1- RELATORIO DE USUARIOS
2- SERVIÇOS/CONSERTO Á SER PRESTADOS
0- VOLTAR
""")
    relatorio=input("ESCOLHA: ")

    if relatorio == "1":
     os.system('cls')
     print("""
-----------------------------
RELATORIO DE USUARIOS
-----------------------------
""")
     for cpf in usuarios:
      print("----------------------------------------------------------------------------")
      print(f"CPF: {cpf} - NOME: {usuarios[cpf]['nome']} - E-MAIL: {usuarios[cpf]['email']}")
     
     print("----------------------------------------------------------------------------")
     input("PRESSIONE ESPAÇO PARA CONTINUAR ")

    elif relatorio == "2":
      os.system('cls')
      print("""
-----------------------------
RELATORIO DE SERVIÇOS PRESTADOS
-----------------------------
""")
      for cpf in consertos:
        print("---------------------------------------------------------------------------------------------------")
        print(f"CPF: {cpf[0]} - APARELHO: {cpf[1]} - PROBLEMA/SERVIÇO: {cpf[2]}")
      print("---------------------------------------------------------------------------------------------------")
      input("PRESSIONE ESPAÇO PARA CONTINUAR ")
        
  
  elif m == "0":
    print("SAINDO DO PROGRAMA...")
    input("PRESSIONE ENTER PARA CONTINUAR...")
  
  else:
    print("OPÇÃO INVÁLIDA, POR FAVOR ESCOLHA UMA OPÇÃO VÁLIDA")
    input("PRESSIONE ENTER PARA CONTINUAR...")
   
