
#MUDA A PARETE DE RELATORIO EM ALGO SOSTIFICADO

import datetime
import pickle
import os
import random

usuarios = {
  "12345678900": {"nome": "João Silva", "email": "joao.silva@gmail.com", "data": "10/01/2000", "estado": True,},
  "98765432100": {"nome": "Maria Santos", "email": "mariasantos@gmail.com", "data": "15/03/1998", "estado": True},
  "11122233344": {"nome": "Carlos Oliveira", "email": "carlos.oliveira@gmail.com", "data": "22/08/1995", "estado": True},
  "55566677788": {"nome": "Ana Costa", "email": "ana.costa@gmail.com", "data": "30/11/2001", "estado": True},
  "12312445545": {"nome": "Ana Luiza", "email": "analuiza@gmail.com", "data": "12/12/2000", "estado": True},
  "99988877766": {"nome": "Pedro Almeida", "email": "pedro.almeida@gmail.com", "data": "06/04/2002", "estado": True}
}

servicos = {
 "2345": {"tipo":"MANUTENÇÃO","descricao": "Manutenção geral de celulares", "valor": "100.0", "estado": True},
 "5789": {"tipo":"TROCA DE TELA","descricao": "Troca de tela para celulares", "valor": "150.0", "estado": True},
 "2353": {"tipo":"TROCA DE BATERIA","descricao": "Troca de bateria para celulares", "valor": "80.0", "estado": True},
 "1434": {"tipo":"TROCA DE CARCAÇA","descricao": "Troca de carcaça para celulares", "valor": "120.0", "estado": True},
 "0982": {"tipo":"LIMPEZA INTERNA","descricao": "Limpeza interna de celulares", "valor": "50.0", "estado": True},
 "9284": {"tipo":"RECUPERAÇÃO DE DADOS","descricao": "Recuperação de dados para celulares", "valor": "200.0", "estado": False},
 "1242": {"tipo":"FORMATAÇÃO","descricao": "Formatação de celulares", "valor": "70.0", "estado": False}
}

consertos = {
"001": {"cpf": "12345678900","aparelho": "iPhone 12","problema": "Tela quebrada", "desconto": "10", "estado": True},
"002": {"cpf": "98765432100","aparelho": "Samsung Galaxy S21","problema": "Bateria viciada", "desconto": "0", "estado": True},
"003": {"cpf": "11122233344","aparelho": "Xiaomi Redmi Note 10","problema": "Problema no carregamento", "desconto": "0", "estado": True},
"004": {"cpf": "55566677788","aparelho": "Motorola Moto G Power","problema": "Formatação", "desconto": "0", "estado": True},
"005": {"cpf": "99988877766","aparelho": "OnePlus 9 Pro","problema": "Limpeza interna", "desconto": "0", "estado": True}
}

try:
 arqUsuarios = open("Usuarios.dat", "rb")
 arqServicos = open("Servicos.dat", "rb")
 arqConsertos = open("Consertos.dat", "rb")
 usuarios = pickle.load(arqUsuarios)
 servicos = pickle.load(arqServicos)
 consertos = pickle.load(arqConsertos)
 arqUsuarios.close()
 arqServicos.close()
 arqConsertos.close()

except:
 arqUsuarios = open("Usuarios.dat", "wb")
 arqServicos = open("Servicos.dat", "wb")
 arqConsertos = open("Consertos.dat", "wb")
 arqUsuarios.close()
 arqServicos.close()
 arqConsertos.close()

def menu_principal():
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
 return m

def conserta_aparelho_menu():
   consertar = " "
   os.system('cls')
   while consertar != "0":
     print("""
-----------------------------
CONSERTA APARELHO
-----------------------------
1- PROBLEMAS DIVEROS
2- CATÁLOGO DE SERVIÇOS
3- CANCELAR CONSERTO
0- VOLTAR
""")
    consertar=input("ESCOLHA: ")
 return consertar


m= " "
while m!= "0":
 menu_principal()

  if m == "1":
    conserta_aparelho_menu()

    if consertar == "1":
        os.system('cls')
        print("""
-----------------------------
PROBLEMAS DIVERSOS
-----------------------------
1° INFORME A MARCA DO SEU APARELHO
2° INFORME O PROBLEMA DO SEU APARELHO
3° INFORME SEU CPF CASO FOR UM USUÁRIO CADASTADO 
""")
        aparelho=input("MARCA DO APARELHO: ")
        problema=input("PROBLEMA DO APARELHO: ")
        cpf=input("INFORME SEU CPF CASO FOR UM USUÁRIO CADASTADO: ")
        
        if cpf in usuarios:
         os.system('cls')
         print("USUÁRIO ENCONTRADO")
         print()
         cod = "%03d" % (len(consertos) + 1)
        
         if usuarios[cpf]['data'][:5] == datetime.datetime.now().strftime("%d/%m"):
          print("PARABÉNS! VOCÊ GANHOU 10% DE DESCONTO POR SER ANIVERSARIANTE DO MÊS!")
          descinto = "10"
         
         else:
          descinto = "0"
         
         consertos[cod] = { "cpf": cpf, "aparelho": aparelho, "problema": problema, "desconto": descinto, "estado": True }
         print("| %-15s | %-15s | %-20s | %-20s | %-10s |" % ("COD", "CPF", "APARELHO", "PROBLEMA", "DESCONTO"))
         print("| %-15s | %-15s | %-20s | %-20s | %-10s |" % (cod, cpf, aparelho, problema, consertos[cod]["desconto"] + "%"))
         print()
         print("APARELHO CADASTRADO PARA CONSERTO COM SUCESSO!")
         input("PRESSIONE ENTER PARA CONTINUAR...")
        
        else:
         print("USUÁRIO NÃO ENCONTRADO, POR FAVOR CADASTRE-SE ANTES DE SOLICITAR O CONSERTO")
         input("PRESSIONE ENTER PARA CONTINUAR...")
     
    elif consertar == "2":
      print("""
-----------------------------
CATÁLOGO DE SERVIÇOS
-----------------------------
""")
      print("----------------------------------------------------------------------------------------------------")
      print("|%-10s | %-20s | %-37s | %-10s | %-10s|" % ("COD", "NOME", "DESCRIÇÃO", "VALOR", "ESTADO"))
      print("----------------------------------------------------------------------------------------------------")
      for nome in servicos:
        print("|%-10s | %-20s | %-37s | %-10s | %-10s|" % (nome,servicos[nome]["tipo"],servicos[nome]["descricao"],servicos[nome]["valor"],servicos[nome]["estado"]))

      print("----------------------------------------------------------------------------------------------------")
      tipo=input("ESCOLHA UM SERVIÇO PARA SOLICITAR  ")
      
      if tipo in servicos and servicos[tipo]["estado"] == True:
       os.system('cls')
       print("""
---------------------------------
INFORMAÇÃO PARA PRESTAR O SERVIÇO
---------------------------------
1° INFORME A MARCA DO SEU APARELHO
2° INFORME SEU CPF CASO FOR UM USUÁRIO CADASTADO
""")
       
       aparelho=input("MARCA DO APARELHO: ")
       cpf=input("INFORME SEU CPF CASO FOR UM USUÁRIO CADASTADO: ")
       
       if cpf in usuarios:
         os.system('cls')
         print("USUÁRIO ENCONTRADO!")
         cod = "%03d" % (len(consertos) + 1)
         
         if usuarios[cpf]['data'][:5] == datetime.datetime.now().strftime("%d/%m"):
          print("PARABÉNS! VOCÊ GANHOU 10% DE DESCONTO POR SER ANIVERSARIANTE DO MÊS!")
          descinto = "10"
         
         else:         
           
           descinto = "0"
         
         consertos[cod] = { "cpf": cpf, "aparelho": aparelho, "problema": tipo, "desconto": descinto, "estado": True }
         os.system('cls')
         print("| %-15s | %-15s | %-20s | %-20s | %-10s |" % ("COD", "CPF", "APARELHO", "PROBLEMA", "DESCONTO"))
         print("| %-15s | %-15s | %-20s | %-20s | %-10s |" % (cod, cpf, aparelho, tipo, consertos[cod]["desconto"] + "%"))
         
         print("APARELHO CADASTRADO PARA CONSERTO COM SUCESSO!")
         input("PRESSIONE ENTER PARA CONTINUAR...")
        
       else:
          print("USUÁRIO NÃO ENCONTRADO, POR FAVOR CADASTRE-SE ANTES DE SOLICITAR O CONSERTO")
          input("PRESSIONE ENTER PARA CONTINUAR...")
      
      else:
        print("SERVIÇO NÃO ENCONTRADO OU INDISPONÍVEL, POR FAVOR ESCOLHA UM SERVIÇO VÁLIDO E DISPONÍVEL")
        input("PRESSIONE ENTER PARA CONTINUAR...")
    
    elif consertar == "3":
      cod=input("PRIMEIRO, DIGITE O CÓDIGO DO CONSERTO PARA CANCELAR: ")
      
      while cod not in consertos and cod != "0":
        print("CONSERTO NÃO ENCONTRADO, POR FAVOR DIGITE UM CÓDIGO DE CONSERTO VÁLIDO OU DIGITE 0 PARA VOLTAR")
        cod=input("CÓDIGO DO CONSERTO: ")
      
      if cod in consertos:
        
        print("----------------------------------------------------------------------------------------------------------------")
        print("| %-10s | %-15s | %-20s | %-25s | %-10s |" % ("COD", "CPF", "APARELHO", "PROBLEMA", "DESCONTO"))
        print("----------------------------------------------------------------------------------------------------------------")
        for cod in consertos:
         if consertos[cod]["estado"]== True:
          print("| %-10s | %-15s | %-20s | %-25s | %-10s |" % (cod,consertos[cod]["cpf"],consertos[cod]["aparelho"],consertos[cod]["problema"],consertos[cod]["desconto"] + "%"))
        print("----------------------------------------------------------------------------------------------------------------")
        
        desc=input("TEM CERTEZA QUE QUER CANCELAR O CONSERTO COM (S/N): ")
        
        if desc.upper() == "S":
         consertos[cod]['estado'] = False
         print("CONSERTO CANCELADO COM SUCESSO!")
         input("PRESSIONE ENTER PARA CONTINUAR...")
        
        elif desc.upper() == "N":
          print("CANCELAMENTO DO CANCELAMENTO DO CONSERTO")
          input("PRESSIONE ENTER PARA CONTINUAR... ")
        
        else:
          print("OPÇÃO INVÁLIDA, POR FAVOR DIGITE S PARA SIM OU N PARA NÃO")
          input("PRESSIONE ENTER PARA CONTINUAR... ")
    
    
    elif consertar == "0":
      print("VOLTANDO...")
      input("PRESSIONE ENTER PARA CONTINUAR...")
    
    else:
      print("OPÇÃO INVÁLIDA, POR FAVOR ESCOLHA UMA OPÇÃO VÁLIDA")
      input("PRESSIONE ENTER PARA CONTINUAR...")

  elif m == "2" :
    usuario = " "
    os.system('cls')
    
    while usuario != "0":
      print("""
-----------------------------
USUÁRIO
-----------------------------
1- CADASTRAR USUÁRIO
2- DESATIVAR USUÁRIO
3- ATUALIZAR USUÁRIO
4- PESQUISAR USUÁRIO
0- VOLTAR
""")
      usuario=input("ESCOLHA: ")

      if usuario== "1":
       print("""
-----------------------------
CADASTRAR USUÁRIO
-----------------------------
1° INFORME SEU NOME
2° E-MAIL PARA CONTATO
3° SEU CPF
4° SUA DATA DE NASCIMENTO
""")

       nome=input("NOME: ")
       email=input("E-MAIL: ")
       cpf=input("CPF: ")
       date=input("SUA DATA DE NASCIMENTO: ")
       
       if cpf in usuarios:
        print("CPF JÁ CADASTRADO, POR FAVOR DIGITE UM CPF VÁLIDO")
        input("PRESSIONE ENTER PARA CONTINUAR ")
       
       else:
        usuarios[cpf] = {"nome": nome, "email": email, "data": date }

        print("| %-15s | %-15s | %-30s | %-20s | %-10s |" % ("CPF", "NOME", "E-MAIL", "DATA DE NASCIMENTO", "ESTADO"))
        print("| %-15s | %-15s | %-30s | %-20s | %-10s |" % (cpf, nome, email, date, usuarios[cpf]['estado']))
        print("CADASTRO REALIZADO COM SUCESSO!")
        input("PRESSIONE ENTER PARA CONTINUAR ")

      elif usuario == "2":
       usuario_ase=input("PRIMEIRO, DIGITE O CPF DO USUÁRIO QUE QUER DELETAR: ")
      
       while usuario_ase not in usuarios and usuario_ase != "0":
        print("USUÁRIO NÃO ENCONTRADO, POR FAVOR DIGITE UM CPF VÁLIDO OU DIGITE 0 PARA VOLTAR")
        usuario_ase=input("CPF: ")
       
       if usuario_ase in usuarios:
          print("""
-----------------------------
DESATIVAR USUÁRIO
-----------------------------
[1° INFORME SE QUER DESATIVAR O USUÁRIO]
""")
          print("| %-15s | %-15s | %-30s | %-20s | %-10s |" % ("CPF", "NOME", "E-MAIL", "DATA DE NASCIMENTO", "ESTADO"))
          print("| %-15s | %-15s | %-30s | %-20s | %-10s |" % (cpf, nome, email, date, usuarios[cpf]['estado']))
          conf = input("CONFIRME SE QUER DESATIVAR O USUÁRIO (S/N): ")
            
          if conf.upper() == "S":
             usuarios[usuario_ase]['estado'] = False
             print("USUÁRIO DESATIVADO COM SUCESSO!")
            
          elif conf.upper() == "N":
              print("CANCELAMENTO DA DESATIVAÇÃO DO USUÁRIO")
              input("PRESSIONE ENTER PARA CONTINUAR ")

          else:
             print("USUARIO NÃO ENCOTRADO")
             input("PRESSIONE ENTER PARA CONTINUAR...")
    
      elif usuario == "3":
       
        cpf=input("PRIMEIRO, DIGITE SEU CPF: ")
        
        while cpf not in usuarios and cpf != "0":
         print("USUÁRIO NÃO ENCONTRADO, POR FAVOR DIGITE UM CPF VÁLIDO OU DIGITE 0 PARA VOLTAR")
         cpf=input("CPF: ")
       
        if cpf in usuarios:
          m = " "
          
          while m!="0":
              print("""
-----------------------------
ATUALIZAR USUÁRIO
-----------------------------
[QUAIS INFORMÇÔES QUER ATUALIZAR]
1- NOME
2- E-MAIL
3- DATA DE NASCIMENTO
4- TUDO
0- VOLTAR
""")
              m = input("DIGITE: ")
              
              if m == "1":
               nome=input("NOME NOVO: ")
               usuarios[cpf]['nome'] = nome
               print("NOME ATUALIZADO COM SUCESSO!")
               input("PRESSIONE ENTER PARA CONTINUAR ")   
            
              elif m == "2":
               email = input("E-MAIL NOVO: ")
               usuarios[cpf]["email"] = email
               print("E-MAIL ATUALIZADO COM SUCESSO!")
               input("PRESSIONE ENTER PARA CONTINUAR ")
            
              elif m == "3":
               date=input("DATA DE NASCIMENTO NOVA: ")
               usuarios[cpf]['data'] = date
               print("DATA DE NASCIMENTO ATUALIZADA COM SUCESSO!")
               input("PRESSIONE ENTER PARA CONTINUAR ")
          
              elif m == "4":
               nome=input("NOME NOVO: ")
               email=input("E-MAIL NOVO: ")
               date=input("DATA DE NASCIMENTO NOVA: ")
               usuarios[cpf]["nome"] = nome
               usuarios[cpf]["email"] = email
               usuarios[cpf]["data"] = date
               print("INFORMAÇÕES ATUALIZADAS COM SUCESSO!")
               input("PRESSIONE ENTER PARA CONTINUAR ")
              
              elif m == "0":
               print("VOLTANDO...")
               input("PRESSIONE ENTER PARA CONTINUAR ")
              
              else:
               print("OPÇÃO INVÁLIDA, POR FAVOR ESCOLHA UMA OPÇÃO VÁLIDA")
               input("PRESSIONE ENTER PARA CONTINUAR ")
            
      elif usuario == "4":
        
        pesquisar= " "
        os.system('cls')
        while pesquisar != "0":
         print("""
-----------------------------
PESQUISAR USUÁRIO
-----------------------------
1- PRIMEIRO NOME
2- ULTIMO NOME
3- PELO CPF
4- E-MAIL
0- VOLTAR
""")
         pesquisar=input("DIGITE:")
        
         if pesquisar == "1":
           os.system('cls')
           print("""
-----------------------------
PROCURANDO PELO PRIMEIRO NOME
-----------------------------
""")
           nome=input("DIGITE SOMENTE O PRIMEIRO NOME: ")
           
           for nomes in usuarios:
             
             if usuarios[nomes]["nome"].startswith(nome):
               print("CPF: ", nomes)
               print("NOME: ",usuarios[nomes]["nome"])
               print()
           
           input("PRESSIONE ENTER PARA CONTINUAR ")
        
         elif pesquisar == "2":
           os.system('cls')
           print("""
-----------------------------
PROCURANDO PELO ULTIMO NOME
-----------------------------
""")
           nome=input("DIGITE O ULTIMO NOME: ")

           for nomes in usuarios:
             
             if usuarios[nomes]["nome"].endswith(nome):
               print("NOME:", nomes)
               print("CPF:", usuarios[nomes]["nome"])
               print()
           
           input("PRESSIONE ENTER PARA CONTINUAR ")
        
         elif pesquisar == "3":
           os.system('cls')
           print("""
-----------------------------
PROCURANDO PELO CPF
-----------------------------
""")
           cpff=input("DIGITE SOMENTE CPF: ")

           for cpf in usuarios:
             if cpf == cpff:
               print("CPF: ",cpf)

           input("PRESSIONE ENTER PARA CONTINUAR ")
      
         elif pesquisar == "4":
           os.system('cls')
           print("""
-----------------------------
PROCURANDO PELO E-MAIL
-----------------------------
""")
           mail=input("DIGITE SEU E-MAIL: ")

           for mails in usuarios:
             if mail == usuarios[mails]["email"]:
               print("E-MAIL: ",usuarios[mails]["email"])
               print("CPF:", mails) 
          
           input("PRESSIONE ENTER PARA CONTINUAR ")
          

         elif pesquisar == "0":
           print("VOLTANDO...")
           input("PRESSIONE ENTER PARA CONTINUAR ")
        
        else:
         print("OPÇÃO INVÁLIDA, POR FAVOR ESCOLHA UMA OPÇÃO VÁLIDA")
         input("PRESSIONE ENTER PARA CONTINUAR ")

      
      elif usuario == "0":
       print("VOLTANDO...")
       input("PRESSIONE ENTER PARA CONTINUAR ")
      
      else:
       print("OPÇÃO INVÁLIDA, POR FAVOR ESCOLHA UMA OPÇÃO VÁLIDA")
       input("PRESSIONE ENTER PARA CONTINUAR ")

  elif m == "3":
   
   servico = " "
   os.system('cls')
   while servico !="0":
    print("""
-----------------------------
SERVIÇOS
-----------------------------
1- CRIAR SERVIÇO
2- DELETAR/DESATIVAR/ATIVAR SERVIÇO
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
[1° INFORME O NOME DO SERVIÇO
 2° INFORME A DESCRIÇÃO DO SERVIÇO
 3° INFORME O VALOR DO SERVIÇO]
""")

     nome=input("NOME DO SERVIÇO: ")
     descricao=input("DESCRIÇÃO DO SERVIÇO: ")
     valor=(input("VALOR DO SERVIÇO: "))
     cod = "%04d" % random.randint(0, 9999)

     while cod in servicos:
      cod = "%04d" % random.randint(0, 9999)
     
     servicos[cod] = {"tipo": nome ,"descricao": descricao, "valor": valor, "estado": True}
     print("------------------------------------------------------------------------------------------------")
     print("| %-10s | %-20s | %-30s | %-10s | %-10s |" % ("COD", "NOME", "DESCRIÇÃO", "VALOR", "ESTADO"))
     print("------------------------------------------------------------------------------------------------")
     print("| %-10s | %-20s | %-30s | R$ %-7.2f | %-10s |" %(cod,nome,descricao,valor,servicos[cod]["estado"]))
     print("------------------------------------------------------------------------------------------------")

     print("SERVIÇO CRIADO COM SUCESSO!")
     input("PRESSIONE ENTER PARA CONTINUAR ")
   
    elif servico == "2":
     
     cod=input("PRIMEIRO, DIGITE O CÓDIGO DO SERVIÇO PARA DELETAR/DESATIVAR: ")
     while cod not in servicos and cod != "0":
      os.system('cls')
      print("SERVIÇO NÃO ENCONTRADO, POR FAVOR DIGITE UM CÓDIGO DE SERVIÇO VÁLIDO OU DIGITE 0 PARA VOLTAR")
      cod=input("CÓDIGO DO SERVIÇO: ")
     
     if cod in servicos:
      os.system('cls')
      deletar = " "
      
      while deletar != "0":
        print("""
-----------------------------
DELETAR/DESATIVAR/ATIVAR SERVIÇO
-----------------------------
1- DELETAR SERVIÇO
2- DESATIVAR SERVIÇO
3- ATIVAR SERVIÇO
0- VOLTAR
""")
        print("------------------------------------------------------------------------------------------------")
        print("| %-10s | %-20s | %-30s | %-10s | %-10s |" % ("COD", "NOME", "DESCRIÇÃO", "VALOR", "ESTADO"))  
        print("| %-10s | %-20s | %-30s | R$ %-7.2f | %-10s |" %(cod,servicos[cod]['tipo'],servicos[cod]['descricao'],servicos[cod]['valor'],servicos[cod]['estado']))
        print("------------------------------------------------------------------------------------------------")
        deletar = input("ESCOLHA: ")
        
        if deletar == "1":
          desc=input("TEM CERTEZA QUE QUER DELETAR O SERVIÇO COM (S/N): ")
          
          if desc.upper() == "S":
           del servicos[cod]
           print("SERVIÇO DELETADO COM SUCESSO!")
           input("PRESSIONE ENTER PARA CONTINUAR ")
          
          elif desc.upper() == "N":
            print("CANCELAMENTO DA DELETA DO SERVIÇO")
            input("PRESSIONE ENTER PARA CONTINUAR ")
          
          else:
            print("OPÇÃO INVÁLIDA, POR FAVOR DIGITE S PARA SIM OU N PARA NÃO")
            input("PRESSIONE ENTER PARA CONTINUAR ")
        
        elif deletar == "2":
          
          if servicos[cod]['estado'] == True:
            servicos[cod]['estado'] = False
            print("SERVIÇO DESATIVADO COM SUCESSO!")
            input("PRESSIONE ENTER PARA CONTINUAR ")
          
          elif servicos[cod]['estado'] == False:
            print("SERVIÇO JÁ ESTÁ DESATIVADO")
            input("PRESSIONE ENTER PARA CONTINUAR ")
        
        elif deletar == "3":
          
          if servicos[cod]['estado'] == False:
            servicos[cod]['estado'] = True
            print("SERVIÇO ATIVADO COM SUCESSO!")
            input("PRESSIONE ENTER PARA CONTINUAR ")
          
          elif servicos[cod]['estado'] == True:
            print("SERVIÇO JÁ ESTÁ ATIVO")
            input("PRESSIONE ENTER PARA CONTINUAR ")
        
        else:
          print("OPÇÃO INVÁLIDA, POR FAVOR ESCOLHA UMA OPÇÃO VÁLIDA")
          input("PRESSIONE ENTER PARA CONTINUAR ")
        
   
    elif servico == "3":
     cod=input("PRIMEIRO, DIGITE O CÓDIGO DO SERVIÇO QUE QUER ATUALIZAR: ")
     
     while cod not in servicos and cod != "0":
      print("SERVIÇO NÃO ENCONTRADO, POR FAVOR DIGITE UM CÓDIGO DE SERVIÇO VÁLIDO OU DIGITE 0 PARA VOLTAR")
      cod=input("CÓDIGO DO SERVIÇO: ")
     
     if cod in servicos:
      att=' '
      while att != "0":
        os.system('cls')
        print("""
-----------------------------
ATUALIZAR SERVIÇO
-----------------------------
[QUAIS INFORMÇÔES QUER ATUALIZAR]
1- NOME DO SERVIÇO
2- DESCRIÇÃO DO SERVIÇO
3- VALOR DO SERVIÇO
4- TUDO
5- ESTADO DO SERVIÇO
0- VOLTAR
  """)
        print("------------------------------------------------------------------------------------------------")
        print("| %-10s | %-20s | %-30s | %-10s | %-10s |" % ("COD", "NOME", "DESCRIÇÃO", "VALOR", "ESTADO"))  
        print("| %-10s | %-20s | %-30s | R$ %-7.2f | %-10s |" %(cod,servicos[cod]['tipo'],servicos[cod]['descricao'],servicos[cod]['valor'],servicos[cod]['estado']))
        print("------------------------------------------------------------------------------------------------")
        att=input("ESCOLHA: ")

        if att == "1":
         nome=input("NOME DO SERVIÇO NOVO: ")
         servicos[cod]["tipo"] = nome
         print("NOME DO SERVIÇO ATUALIZADO COM SUCESSO!")
         input("PRESSIONE ENTER PARA CONTINUAR ")
       
        elif att == "2":
         descricao=input("DESCRIÇÃO DO SERVIÇO NOVA: ")
         servicos[cod]["descricao"] = descricao
         print("DESCRIÇÃO DO SERVIÇO ATUALIZADA COM SUCESSO!")
         input("PRESSIONE ENTER PARA CONTINUAR ")
        
        elif att == "3":
         valor=float(input("VALOR DO SERVIÇO NOVO: "))
         servicos[cod]["valor"] = valor
         print("VALOR DO SERVIÇO ATUALIZADO COM SUCESSO!")
         input("PRESSIONE ENTER PARA CONTINUAR ")
       
        elif att == "4":
          nome=input("NOME DO SERVIÇO NOVO: ")
          descricao=input("DESCRIÇÃO DO SERVIÇO NOVA: ")
          valor=float(input("VALOR DO SERVIÇO NOVO: "))
          servicos[cod]["tipo"] = nome
          servicos[cod]["descricao"] = descricao
          servicos[cod]["valor"] = valor
          print("INFORMAÇÕES DO SERVIÇO ATUALIZADAS COM SUCESSO!")
          input("PRESSIONE ENTER PARA CONTINUAR ")
        
        elif att == "5":
          estado = input("ESTADO DO SERVIÇO (DISPONÍVEL/INDISPONÍVEL): ")
          
          if estado.upper() == "DISPONÍVEL":
            servicos[cod]["estado"] = True
            print("ESTADO DO SERVIÇO ATUALIZADO PARA DISPONÍVEL COM SUCESSO!")
            input("PRESSIONE ENTER PARA CONTINUAR ")
          
          elif estado.upper() == "INDISPONÍVEL":
            servicos[cod]["estado"] = False
            print("ESTADO DO SERVIÇO ATUALIZADO PARA INDISPONÍVEL COM SUCESSO!")
            input("PRESSIONE ENTER PARA CONTINUAR ")
          
          else:
            print("ESTADO INVÁLIDO, POR FAVOR DIGITE DISPONÍVEL OU INDISPONÍVEL")
            input("PRESSIONE ENTER PARA CONTINUAR ")
        
        elif att == "0":
          print("VOLTANDO...")
          input("PRESSIONE ENTER PARA CONTINUAR ")
          
        else:
          print("OPÇÃO INVÁLIDA, POR FAVOR ESCOLHA UMA OPÇÃO VÁLIDA")
          input("PRESSIONE ENTER PARA CONTINUAR ")


    elif servico == "4":
     P = " "
     os.system('cls')
     
     while P != "0":
      print("""
-----------------------------
MOSTRAR SERVIÇOS 
-----------------------------
1- MOSTRAR SERVIÇOS DISPONÍVEIS
2- MOSTRAR SERVIÇOS INDISPONÍVEIS
3- MOSTRAR TODOS OS SERVIÇOS
0- VOLTAR
""")
      P = input("ESCOLHA: ")
      if P == "1":
        os.system('cls')
        
        print("-------------------------------------------------------------------------------------------------------")
        print("| %-10s | %-20s | %-37s | %-10s | %-10s |" % ("COD", "NOME", "DESCRIÇÃO", "VALOR", "ESTADO"))
        print("-------------------------------------------------------------------------------------------------------")

        for nome in servicos:
         print("| %-10s | %-20s | %-37s | %-10s | %-10s |" % (nome,servicos[nome]["tipo"],servicos[nome]["descricao"],servicos[nome]["valor"],servicos[nome]["estado"]))

        print("-------------------------------------------------------------------------------------------------------")
        input("PRESSIONE ESPAÇO PARA CONTINUAR ")
      
      elif P == "2":
        os.system('cls')
        
        print("-------------------------------------------------------------------------------------------------------")
        print("| %-10s | %-20s | %-37s | %-10s | %-10s |" % ("COD", "NOME", "DESCRIÇÃO", "VALOR", "ESTADO"))
        print("-------------------------------------------------------------------------------------------------------")

        for nome in servicos:
          if servicos[nome]['estado'] == False:
            print("| %-10s | %-20s | %-37s | %-10s | %-10s |" % (nome, servicos[nome]['tipo'], servicos[nome]['descricao'], servicos[nome]['valor'], servicos[nome]['estado']))
        print("-------------------------------------------------------------------------------------------------------")
        input("PRESSIONE ESPAÇO PARA CONTINUAR ")
  
      elif P == "3":
        os.system('cls')
        
        print("-------------------------------------------------------------------------------------------------------")
        print("| %-10s | %-20s | %-37s | %-10s | %-10s |" % ("COD", "NOME", "DESCRIÇÃO", "VALOR", "ESTADO"))
        print("-------------------------------------------------------------------------------------------------------")
        for nome in servicos:
          print("| %-10s | %-20s | %-37s | %-10s | %-10s |" % (nome, servicos[nome]['tipo'], servicos[nome]['descricao'], servicos[nome]['valor'], servicos[nome]['estado']))
        print("-------------------------------------------------------------------------------------------------------")
        input("PRESSIONE ESPAÇO PARA CONTINUAR ")
      
      elif P == "0":
        print("VOLTANDO...")
        input("PRESSIONE ENTER PARA CONTINUAR ")
      
      else:
        print("OPÇÃO INVÁLIDA, POR FAVOR ESCOLHA UMA OPÇÃO VÁLIDA")
        input("PRESSIONE ENTER PARA CONTINUAR ")

  elif m == "4":
   
   relatorio=" "
   while relatorio != "0":
    os.system('cls')
    print("""
-----------------------------
RELATÓRIO
-----------------------------
1- RELATÓRIO DE USUÁRIOS
2- SERVIÇOS/CONSERTO A SER PRESTADOS
0- VOLTAR
""")
    relatorio=input("ESCOLHA: ")

    if relatorio == "1":
     rel_usuario = " "
     
     while rel_usuario !="0":
      os.system('cls')
      print("""
-----------------------------
RELATÓRIO DE USUÁRIOS
-----------------------------
1- USUÁRIOS ATIVOS
2- USUÁRIOS DESATIVOS
3- TODOS OS USUÁRIOS
4- RELATÓRIO COMPLEXA
0- VOLTAR
""")
      rel_usuario=input("DIGITE: ")
      
      if rel_usuario == "1":
        print("----------------------------------------------------------------------------------------------------------------")
        print("| %-15s | %-20s | %-30s | %-12s |" % ("CPF", "NOME", "E-MAIL", "NASCIMENTO"))
        print("----------------------------------------------------------------------------------------------------------------")

        for cpf in usuarios:
         if usuarios[cpf]["estado"] == True:
           print("| %-15s | %-20s | %-30s | %-12s |" % (cpf,usuarios[cpf]["nome"],usuarios[cpf]["email"],usuarios[cpf]["data"]))
        print("----------------------------------------------------------------------------------------------------------------")
        input("PRESSIONE ESPAÇO PARA CONTINUAR ")

      elif rel_usuario == "2":
        print("----------------------------------------------------------------------------------------------------------------")
        print("| %-15s | %-20s | %-30s | %-12s |" % ("CPF", "NOME", "E-MAIL", "NASCIMENTO"))
        print("----------------------------------------------------------------------------------------------------------------")

        for cpf in usuarios:
         if usuarios[cpf]["estado"] == False:
           print("| %-15s | %-20s | %-30s | %-12s |" % (cpf,usuarios[cpf]["nome"],usuarios[cpf]["email"],usuarios[cpf]["data"]))
        print("----------------------------------------------------------------------------------------------------------------")
        input("PRESSIONE ESPAÇO PARA CONTINUAR ")
      
      elif rel_usuario == "3":
        print("----------------------------------------------------------------------------------------------------------------")
        print("| %-15s | %-20s | %-30s | %-12s | %-10s |" % ("CPF", "NOME", "E-MAIL", "NASCIMENTO", "ESTADO"))
        print("----------------------------------------------------------------------------------------------------------------")

        for cpf in usuarios:
         print("| %-15s | %-20s | %-30s | %-12s | %-10s |" % (cpf,usuarios[cpf]["nome"],usuarios[cpf]["email"],usuarios[cpf]["data"],usuarios[cpf]['estado']))
        print("----------------------------------------------------------------------------------------------------------------")
        input("PRESSIONE ESPAÇO PARA CONTINUAR ")

      elif rel_usuario == "4":
        while
           

    elif relatorio == "2":
      relatorio2 = " "
      while relatorio2 != "0":
       os.system('cls')
       print("""
-------------------------------------------------
RELATÓRIO DE SERVIÇOS/CONSERTOS A SEREM PRESTADOS
-------------------------------------------------
1- SERVIÇOS/CONSERTOS ATIVOS
2- SERVIÇOS/CONSERTOS INATIVOS
3- TODOS OS SERVIÇOS/CONSERTOS
4- RELATÓRIO COMPLEXA
0- VOLTAR
""")
      relatorio2=input("DIGITE: ")
      
      if relatorio2 == "1":
        print("------------------------------------------------------------------------------------------------------------------")
        print("| %-10s | %-15s | %-20s | %-25s | %-10s |" % ("COD", "CPF", "APARELHO", "PROBLEMA", "DESCONTO"))
        print("------------------------------------------------------------------------------------------------------------------")

        for cod in consertos:
         if consertos[cod]["estado"] == True:
           print("| %-10s | %-15s | %-20s | %-25s | %-10s |" % (cod,consertos[cod]["cpf"],consertos[cod]["aparelho"],consertos[cod]["problema"],consertos[cod]["desconto"] + "%"))
        print("------------------------------------------------------------------------------------------------------------------")
        input("PRESSIONE ESPAÇO PARA CONTINUAR ")

      elif relatorio2 == "2":
        print("------------------------------------------------------------------------------------------------------------------")
        print("| %-10s | %-15s | %-20s | %-25s | %-10s |" % ("COD", "CPF", "APARELHO", "PROBLEMA", "DESCONTO"))
        print("------------------------------------------------------------------------------------------------------------------")

        for cod in consertos:
         if consertos[cod]["estado"] == False:
           print("| %-10s | %-15s | %-20s | %-25s | %-10s |" % (cod,consertos[cod]["cpf"],consertos[cod]["aparelho"],consertos[cod]["problema"],consertos[cod]["desconto"] + "%"))
        print("------------------------------------------------------------------------------------------------------------------")
        input("PRESSIONE ESPAÇO PARA CONTINUAR ")
      
      elif relatorio2 == "3":
        print("------------------------------------------------------------------------------------------------------------------")
        print("| %-10s | %-15s | %-20s | %-25s | %-10s |" % ("COD", "CPF", "APARELHO", "PROBLEMA", "DESCONTO"))
        print("------------------------------------------------------------------------------------------------------------------")

        for cod in consertos:
         print("| %-10s | %-15s | %-20s | %-25s | %-10s |" % (cod,consertos[cod]["cpf"],consertos[cod]["aparelho"],consertos[cod]["problema"],consertos[cod]["desconto"] + "%"))
        print("------------------------------------------------------------------------------------------------------------------")
        input("PRESSIONE ESPAÇO PARA CONTINUAR ")


    elif relatorio == "0":
      print("VOLTANDO...")
      input("PRESSIONE ENTER PARA CONTINUAR ")

    else:
      print("OPÇÃO INVÁLIDA, POR FAVOR ESCOLHA UMA OPÇÃO VÁLIDA")
      input("PRESSIONE ENTER PARA CONTINUAR...")
  
  elif m == "0":
    arqUsuarios = open("Usuarios.dat", "wb")
    pickle.dump(usuarios, arqUsuarios)
    arqUsuarios.close()

    arqServicos = open("Servicos.dat", "wb")
    pickle.dump(servicos, arqServicos)
    arqServicos.close()

    arqConsertos = open("Consertos.dat", "wb")
    pickle.dump(consertos, arqConsertos)
    arqConsertos.close()

    print("SAINDO DO PROGRAMA...")
    input("PRESSIONE ENTER PARA CONTINUAR...")
  
  else:
    print("OPÇÃO INVÁLIDA, POR FAVOR ESCOLHA UMA OPÇÃO VÁLIDA")
    input("PRESSIONE ENTER PARA CONTINUAR...")
   
    
