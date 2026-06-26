import datetime
import pickle
import os
import random
from validar import validarCPF
from validar import validarEmail

usuarios = {
  "12345678900": {"nome": "João Silva", "email": "joao.silva@gmail.com", "data": "10/01/2000", "cidade": "Recife", "estado": True},
  "98765432100": {"nome": "Maria Santos", "email": "mariasantos@gmail.com", "data": "15/03/1998", "cidade": "Olinda", "estado": True},
  "11122233344": {"nome": "Carlos Oliveira", "email": "carlos.oliveira@gmail.com", "data": "22/08/1995", "cidade": "Caruaru", "estado": True},
  "55566677788": {"nome": "Ana Costa", "email": "ana.costa@gmail.com", "data": "30/11/2001", "cidade": "Petrolina", "estado": True},
  "12312445545": {"nome": "Ana Luiza", "email": "analuiza@gmail.com", "data": "12/12/2000", "cidade": "Garanhuns", "estado": True},
  "99988877766": {"nome": "Pedro Almeida", "email": "pedro.almeida@gmail.com", "data": "06/04/2002", "cidade": "Afogados da Ingazeira", "estado": True},
  "44433322211": {"nome": "Lucas Ferreira", "email": "lucas.ferreira@gmail.com", "data": "25/07/1999", "cidade": "Caicó", "estado": True}
}

meses = {
        "janeiro": "01","fevereiro": "02",
        "março": "03", "abril": "04",
        "maio": "05","junho": "06",
        "julho": "07","agosto": "08",
        "setembro": "09", "outubro": "10",
        "novembro": "11","dezembro": "12"
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
"001": {"cpf": "12345678900", "aparelho": "iPhone 12", "problema": "5789", "desconto": "10", "estado": True}, 
"002": {"cpf": "98765432100", "aparelho": "Samsung Galaxy S21", "problema": "2353", "desconto": "0", "estado": True}, 
"003": {"cpf": "11122233344", "aparelho": "Xiaomi Redmi Note 10", "problema": "2345", "desconto": "0", "estado": True}, 
"004": {"cpf": "55566677788", "aparelho": "Motorola Moto G Power", "problema": "1242", "desconto": "0", "estado": True}, 
"005": {"cpf": "99988877766", "aparelho": "OnePlus 9 Pro", "problema": "0982", "desconto": "0", "estado": True},
"006": {"cpf": "11122233344", "aparelho": "Xiaomi Redmi Note 10", "problema": "Não reconhece o chip", "desconto": "0", "estado": True}, 
}

def limparCPF(cpf):
    cpf = cpf.replace(".", "")
    cpf = cpf.replace("-", "")
    return cpf

def carregar_dados():
  global usuarios, servicos, consertos
  
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
   salvar_dados()

  return usuarios, servicos, consertos

def salvar_dados():
    arqUsuarios = open("Usuarios.dat", "wb")
    pickle.dump(usuarios, arqUsuarios)
    arqUsuarios.close()

    arqServicos = open("Servicos.dat", "wb")
    pickle.dump(servicos, arqServicos)
    arqServicos.close()

    arqConsertos = open("Consertos.dat", "wb")
    pickle.dump(consertos, arqConsertos)
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
     os.system('cls')
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

def problemas_diversos():
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
        
         if usuarios[cpf]['data'][3:5] == datetime.datetime.now().strftime("%m"):
          print("PARABÉNS! VOCÊ GANHOU 10% DE DESCONTO POR SER ANIVERSARIANTE DO MÊS!")
          descinto = "10"
         
         else:
          descinto = "0"
         
         consertos[cod] = { "cpf": cpf, "aparelho": aparelho, "problema": problema, "desconto": descinto, "estado": True }
         print("| %-15s | %-15s | %-20s | %-20s | %-10s |" % ("COD", "CPF", "APARELHO", "PROBLEMA/SERVIÇO", "DESCONTO"))
         print("| %-15s | %-15s | %-20s | %-20s | %-10s |" % (cod, cpf, aparelho, problema, consertos[cod]["desconto"] + "%"))
         salvar_dados()
         print()
         print("APARELHO CADASTRADO PARA CONSERTO COM SUCESSO!")
         input("PRESSIONE ENTER PARA CONTINUAR...")
        
        else:
         print("USUÁRIO NÃO ENCONTRADO, POR FAVOR CADASTRE-SE ANTES DE SOLICITAR O CONSERTO")
         input("PRESSIONE ENTER PARA CONTINUAR...")

def catalogo_servicos ():
      os.system('cls')
      print("""
-----------------------------
CATÁLOGO DE SERVIÇOS
-----------------------------
""")
      print("---------------------------------------------------------------------------------------------------------------")
      print("| %-10s | %-25s | %-40s | %-10s | %-10s |" % ("COD", "NOME", "DESCRIÇÃO", "VALOR", "ESTADO"))
      print("---------------------------------------------------------------------------------------------------------------")
      for nome in servicos:
        print("| %-10s | %-25s | %-40s | %-10s | %-10s |" % (nome,servicos[nome]["tipo"],servicos[nome]["descricao"],servicos[nome]["valor"],servicos[nome]["estado"]))

      print("---------------------------------------------------------------------------------------------------------------")
      tipo=input("ESCOLHA O CÓDIGO DO SERVIÇO PARA SOLICITAR:  ")
      
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
         
         if usuarios[cpf]['data'][3:5] == datetime.datetime.now().strftime("%m"):
          print("PARABÉNS! VOCÊ GANHOU 10% DE DESCONTO POR SER ANIVERSARIANTE DO MÊS!")
          descinto = "10"
         
         else:         
           
           descinto = "0"
         
         consertos[cod] = { "cpf": cpf, "aparelho": aparelho, "problema": tipo, "desconto": descinto, "estado": True }
         os.system('cls')
         print("| %-15s | %-15s | %-20s | %-20s | %-10s |" % ("COD", "CPF", "APARELHO", "PROBLEMA/SERVIÇO", "DESCONTO"))
         print("| %-15s | %-15s | %-20s | %-20s | %-10s |" % (cod, cpf, aparelho, tipo, consertos[cod]["desconto"] + "%"))
         
         print("APARELHO CADASTRADO PARA CONSERTO COM SUCESSO!")
         input("PRESSIONE ENTER PARA CONTINUAR...")
        
       else:
          print("USUÁRIO NÃO ENCONTRADO, POR FAVOR CADASTRE-SE ANTES DE SOLICITAR O CONSERTO")
          input("PRESSIONE ENTER PARA CONTINUAR...")
      
      else:
        print("SERVIÇO NÃO ENCONTRADO OU INDISPONÍVEL, POR FAVOR ESCOLHA UM SERVIÇO VÁLIDO E DISPONÍVEL")
        input("PRESSIONE ENTER PARA CONTINUAR...")

def cancelar_servico ():
      cod=input("PRIMEIRO, DIGITE O CÓDIGO DO CONSERTO PARA CANCELAR: ")
      
      while cod not in consertos and cod != "0":
        print("CONSERTO NÃO ENCONTRADO, POR FAVOR DIGITE UM CÓDIGO DE CONSERTO VÁLIDO OU DIGITE 0 PARA VOLTAR")
        cod=input("CÓDIGO DO CONSERTO: ")
      
      if cod in consertos:
        
        print("----------------------------------------------------------------------------------------------------------------")
        print("| %-10s | %-15s | %-20s | %-25s | %-10s |" % ("COD", "CPF", "APARELHO", "PROBLEMA/SERVIÇO", "DESCONTO"))
        print("----------------------------------------------------------------------------------------------------------------")
        for cod in consertos:
         if consertos[cod]["estado"]== True:
          print("| %-10s | %-15s | %-20s | %-25s | %-10s |" % (cod,consertos[cod]["cpf"],consertos[cod]["aparelho"],consertos[cod]["problema"],consertos[cod]["desconto"] + "%"))
        print("----------------------------------------------------------------------------------------------------------------")
        
        desc=input("TEM CERTEZA QUE QUER CANCELAR O CONSERTO COM (S/N): ")
        
        if desc.upper() == "S":
         consertos[cod]['estado'] = False
         print("CONSERTO CANCELADO COM SUCESSO!")
         salvar_dados()
        
        elif desc.upper() == "N":
          print("CANCELAMENTO DO CANCELAMENTO DO CONSERTO")
        
        else:
          print("OPÇÃO INVÁLIDA, POR FAVOR DIGITE S PARA SIM OU N PARA NÃO")
        
        input("PRESSIONE ENTER PARA CONTINUAR... ")
    
      elif cod == "0":
       print("VOLTANDO...")
    
      else:
       print("OPÇÃO INVÁLIDA, POR FAVOR ESCOLHA UMA OPÇÃO VÁLIDA")
      
      input("PRESSIONE ENTER PARA CONTINUAR...")

def menu_usuario ():
        os.system('cls')
        print("""
-----------------------------
USUÁRIO
-----------------------------
1- CADASTRAR USUÁRIO
2- DESATIVAR/ATIVAR USUÁRIO
3- ATUALIZAR USUÁRIO
4- PESQUISAR USUÁRIO
0- VOLTAR
""")
        usuario=input("ESCOLHA: ")
        return usuario

def cadastrar_usuario():
       os.system('cls')
       print("""
-----------------------------
CADASTRAR USUÁRIO
-----------------------------
1° INFORME SEU NOME
2° E-MAIL PARA CONTATO
3° SEU CPF
4° SUA DATA DE NASCIMENTO
5° SUA CIDADE QUE RESIDE
""")

       nome=input("NOME: ")
       email=input("E-MAIL: ")
       while not validarEmail(email) and email != "0":
        os.system('cls')
        print("E-MAIL INVÁLIDO")
        email = input("DIGITE UM E-MAIL VÁLIDO OU 0 PARA VOLTAR: ")
       
       if email == "0":
        print("VOLTANDO...")
       
       else:
        cpf = input("CPF: ")
        cpf = limparCPF(cpf)

        while (not validarCPF(cpf) or cpf in usuarios) and cpf != "0":
        
         if cpf in usuarios:
           print("CPF JÁ CADASTRADO")
        
         else:
           print("CPF INVÁLIDO")

         cpf = input("DIGITE UM CPF VÁLIDO OU 0 PARA VOLTAR: ")
        
        if cpf == "0":
          print("VOLTANDO...")

        else:
         date = input("SUA DATA DE NASCIMENTO (DD/MM/AAAA): ")
         
         if "/" not in date:
          date = date[:2] + "/" + date[2:4] + "/" + date[4:]
         
         cidade = input("SUA CIDADE QUE RESIDE: ")
         usuarios[cpf] = {"nome": nome, "email": email, "data": date,"cidade": cidade, "estado": True }

         print("| %-15s | %-15s | %-30s | %-20s | %-25s |" % ("CPF", "NOME", "E-MAIL", "DATA DE NASCIMENTO", "CIDADE"))
         print("| %-15s | %-15s | %-30s | %-20s | %-25s |" % (cpf, nome, email, date, usuarios[cpf]['cidade']))
         salvar_dados()
         print("CADASTRO REALIZADO COM SUCESSO!")
      
        input("PRESSIONE ENTER PARA CONTINUAR ")

def desativar_usuario():
       os.system('cls')
       usuario_ase=input("PRIMEIRO, DIGITE O CPF DO USUÁRIO QUE QUER DELETAR: ")
      
       while usuario_ase not in usuarios and usuario_ase != "0":
        print("USUÁRIO NÃO ENCONTRADO, POR FAVOR DIGITE UM CPF VÁLIDO OU DIGITE 0 PARA VOLTAR")
        usuario_ase=input("CPF: ")
       
       if usuario_ase in usuarios:
          desati = " "
          os.system('cls')
          while desati != "0":
            print("""
-----------------------------
DESATIVAR USUÁRIO
-----------------------------
1- DESATIVAR USUÁRIO
2- ATIVAR USUÁRIO
0- SAIR
""")
            print("| %-15s | %-15s | %-30s | %-20s | %-25s | %-10s |" % ("CPF", "NOME", "E-MAIL", "DATA", "CIDADE", "ESTADO"))
            print("| %-15s | %-15s | %-30s | %-20s | %-25s | %-10s |" % (usuario_ase,usuarios[usuario_ase]["nome"],usuarios[usuario_ase]["email"],usuarios[usuario_ase]["data"],usuarios[usuario_ase]["cidade"],usuarios[usuario_ase]["estado"]))
            print()
            conf = input("DIGITE: ")
              
            if conf == "1":
             
             if usuarios[usuario_ase]['estado'] == False:
              print("USUÁRIO JÁ ESTÁ DESATIVADO!")
             
             else:
                usuarios[usuario_ase]['estado'] = False
                print("USUÁRIO DESATIVADO COM SUCESSO!")
             
             input("PRESSIONE ENTER PARA CONTINUAR ")

            elif conf == "2":
             
             if usuarios[usuario_ase]['estado'] == True:
              print("USUÁRIO JÁ ESTÁ ATIVO!")
             
             else:
              usuarios[usuario_ase]['estado'] = True
              print("USUÁRIO REATIVADO COM SUCESSO!")
            
             input("PRESSIONE ENTER PARA CONTINUAR ")

            elif conf == "0":
              salvar_dados()
              print("VOLTANDO...")

            else:
              print("OPÇÃO INVÁLIDA, POR FAVOR ESCOLHA UMA OPÇÃO VÁLIDA")
            
            input("PRESSIONE ENTER PARA CONTINUAR ")

def atualizar_usuario():
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
4- CIDADE
5- TUDO
0- VOLTAR
""")
              m = input("DIGITE: ")
              
              if m == "1":
               nome=input("NOME NOVO: ")
               usuarios[cpf]['nome'] = nome
               print("NOME ATUALIZADO COM SUCESSO!") 
            
              elif m == "2":
               email = input("E-MAIL NOVO: ")
               usuarios[cpf]["email"] = email
               print("E-MAIL ATUALIZADO COM SUCESSO!")
            
              elif m == "3":
               date=input("DATA DE NASCIMENTO NOVA: ")
               usuarios[cpf]['data'] = date
               print("DATA DE NASCIMENTO ATUALIZADA COM SUCESSO!")
          
              elif m == "4":
               cidade=input("NOVA CIDADE: ")
               usuarios[cpf]['cidade'] = cidade
               print("CIDADE ATUALIZADA COM SUCESSO!")

              elif m == "5":
               nome=input("NOME NOVO: ")
               email=input("E-MAIL NOVO: ")
               date=input("DATA DE NASCIMENTO NOVA: ")
               cidade = input("NOVA CIDADE: ")
               usuarios[cpf]["nome"] = nome
               usuarios[cpf]["email"] = email
               usuarios[cpf]["data"] = date
               usuarios[cpf]["cidade"] = cidade
               print("INFORMAÇÕES ATUALIZADAS COM SUCESSO!")
              
              elif m == "0":
               salvar_dados()
               print("VOLTANDO...")
              
              else:
               print("OPÇÃO INVÁLIDA, POR FAVOR ESCOLHA UMA OPÇÃO VÁLIDA")
              
              input("PRESSIONE ENTER PARA CONTINUAR ")

def pesquisar_usuario():
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
5- CIDADE
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
           
           for cpf in usuarios:
             
             if usuarios[cpf]["nome"].startswith(nome):
               print("CPF: ", cpf)
               print("NOME: ",usuarios[cpf]["nome"])
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

           for cpf in usuarios:
             
             if usuarios[cpf]["nome"].endswith(nome):
               print("NOME: ", nome)
               print("CPF: ", usuarios[cpf]["nome"])
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

           for cpf in usuarios:
             if mail == usuarios[cpf]["email"]:
               print("E-MAIL: ",usuarios[cpf]["email"])
               print("CPF: ", cpf) 
          
           input("PRESSIONE ENTER PARA CONTINUAR ")
          
         elif pesquisar == "5":
           os.system('cls')
           print("""
-----------------------------
PROCURANDO PELA CIDADE
-----------------------------
""")
           cida=input("DIGITE A CIDADE: ")
           for cpf in usuarios:
             if cida == usuarios[cida]["cidade"]:
               print("E-MAIL: ",usuarios[cpf]["cidade"])
               print("CPF: ", cpf) 
          
           input("PRESSIONE ENTER PARA CONTINUAR ")
         
         
         elif pesquisar == "0":
           print("VOLTANDO...")
           input("PRESSIONE ENTER PARA CONTINUAR ")
        
        else:
         print("OPÇÃO INVÁLIDA, POR FAVOR ESCOLHA UMA OPÇÃO VÁLIDA")
         input("PRESSIONE ENTER PARA CONTINUAR ")

def menu_servico():
      print("""
-----------------------------
SERVIÇOS
-----------------------------
1- CRIAR SERVIÇO
2- DELETAR/DESATIVAR/ATIVAR SERVIÇO
3- ATUALIZAR SERVIÇO
4- MOSTRAR SERVIÇOS
0- SAIR
""")
      servico = input("ESCOLHA: ")
      return servico

def criar_servico():
     os.system('cls')
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
     valor=(input("VALOR DO SERVIÇO: "))
     cod = "%04d" % random.randint(0, 9999)

     while cod in servicos:
      cod = "%04d" % random.randint(0, 9999)
     
     servicos[cod] = {"tipo": nome ,"descricao": descricao, "valor": valor, "estado": True}
     print("--------------------------------------------------------------------------------------------------")
     print("| %-10s | %-25s | %-40s | %-10s | %-10s |" % ("COD", "NOME", "DESCRIÇÃO", "VALOR", "ESTADO"))
     print("------------------------------------------------------------------------------------------------")
     print("| %-10s | %-25s | %-40s | %-10s | %-10s |" %(cod,nome,descricao,valor,servicos[cod]["estado"]))
     print("--------------------------------------------------------------------------------------------------")

     print("SERVIÇO CRIADO COM SUCESSO!")
     input("PRESSIONE ENTER PARA CONTINUAR ")

def deletar_servico():
     cod=input("PRIMEIRO, DIGITE O CÓDIGO DO SERVIÇO PARA DELETAR/DESATIVAR/ATIVAR: ")
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
        print("--------------------------------------------------------------------------------------------------")
        print("| %-10s | %-25s | %-40s | %-10s | %-10s |" % ("COD", "NOME", "DESCRIÇÃO", "VALOR", "ESTADO"))  
        print("| %-10s | %-25s | %-40s | %-10s | %-10s |" %(cod,servicos[cod]['tipo'],servicos[cod]['descricao'],servicos[cod]['valor'],servicos[cod]['estado']))
        print("--------------------------------------------------------------------------------------------------")
        deletar = input("ESCOLHA: ")
        
        if deletar == "1":
          desc=input("TEM CERTEZA QUE QUER DELETAR O SERVIÇO COM (S/N): ")
          
          if desc.upper() == "S":
           del servicos[cod]
           print("SERVIÇO DELETADO COM SUCESSO!")
          
          elif desc.upper() == "N":
            print("CANCELAMENTO DA DELETA DO SERVIÇO")       
          
          else:
            print("OPÇÃO INVÁLIDA, POR FAVOR DIGITE S PARA SIM OU N PARA NÃO")
          
          input("PRESSIONE ENTER PARA CONTINUAR ")
        
        elif deletar == "2":
          
          if servicos[cod]['estado'] == True:
            servicos[cod]['estado'] = False
            print("SERVIÇO DESATIVADO COM SUCESSO!")
          
          elif servicos[cod]['estado'] == False:
            print("SERVIÇO JÁ ESTÁ DESATIVADO")
          
          input("PRESSIONE ENTER PARA CONTINUAR ")
        
        elif deletar == "3":
          
          if servicos[cod]['estado'] == False:
            servicos[cod]['estado'] = True
            print("SERVIÇO ATIVADO COM SUCESSO!")
          
          elif servicos[cod]['estado'] == True:
            print("SERVIÇO JÁ ESTÁ ATIVO")
          
          input("PRESSIONE ENTER PARA CONTINUAR ")
        
        elif deletar == "0":
          print("VOLTANDO...")

        else:
          print("OPÇÃO INVÁLIDA, POR FAVOR ESCOLHA UMA OPÇÃO VÁLIDA")
        
        input("PRESSIONE ENTER PARA CONTINUAR ")

def atualizar_servico():
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
0- VOLTAR
  """)
        print("--------------------------------------------------------------------------------------------------")
        print("| %-10s | %-25s | %-40s | %-10s | %-10s |" % ("COD", "NOME", "DESCRIÇÃO", "VALOR", "ESTADO"))  
        print("| %-10s | %-25s | %-40s | %-10s | %-10s |" %(cod,servicos[cod]['tipo'],servicos[cod]['descricao'],servicos[cod]['valor'],servicos[cod]['estado']))
        print("--------------------------------------------------------------------------------------------------")
        att=input("ESCOLHA: ")

        if att == "1":
         nome=input("NOME DO SERVIÇO NOVO: ")
         servicos[cod]["tipo"] = nome
         salvar_dados()
         print("NOME DO SERVIÇO ATUALIZADO COM SUCESSO!")
       
        elif att == "2":
         descricao=input("DESCRIÇÃO DO SERVIÇO NOVA: ")
         servicos[cod]["descricao"] = descricao
         salvar_dados()
         print("DESCRIÇÃO DO SERVIÇO ATUALIZADA COM SUCESSO!")

        elif att == "3":
         valor=input("VALOR DO SERVIÇO NOVO: ")
         servicos[cod]["valor"] = valor
         salvar_dados()
         print("VALOR DO SERVIÇO ATUALIZADO COM SUCESSO!")
       
        elif att == "4":
          nome=input("NOME DO SERVIÇO NOVO: ")
          descricao=input("DESCRIÇÃO DO SERVIÇO NOVA: ")
          valor=input("VALOR DO SERVIÇO NOVO: ")
          servicos[cod]["tipo"] = nome
          servicos[cod]["descricao"] = descricao
          servicos[cod]["valor"] = valor
          salvar_dados()
          print("INFORMAÇÕES DO SERVIÇO ATUALIZADAS COM SUCESSO!")
        
        elif att == "0":
          print("VOLTANDO...")
          
        else:
          print("OPÇÃO INVÁLIDA, POR FAVOR ESCOLHA UMA OPÇÃO VÁLIDA")
        
        input("PRESSIONE ENTER PARA CONTINUAR ")

def menu_mostart_servico():
        print("""
-----------------------------
MOSTRAR SERVIÇOS 
-----------------------------
1- MOSTRAR SERVIÇOS ATIVOS
2- MOSTRAR SERVIÇOS DESATIVADOS
3- MOSTRAR TODOS OS SERVIÇOS
0- VOLTAR
""")
        P = input("ESCOLHA: ")
        return P

def mostrar_servicos(estado):
    print("--------------------------------------------------------------------------------------------------")
    print("| %-10s | %-25s | %-40s | %-10s |" % ("COD", "NOME", "DESCRIÇÃO", "VALOR"))
    print("--------------------------------------------------------------------------------------------------")

    for codigo in servicos:
        if estado == "todos" or servicos[codigo]["estado"] == estado:
            print("| %-10s | %-25s | %-40s | %-10s |" % (codigo,servicos[codigo]["tipo"],servicos[codigo]["descricao"],servicos[codigo]["valor"]))

    print("--------------------------------------------------------------------------------------------------")
    input("PRESSIONE ENTER PARA CONTINUAR ")

def menu_relatorio():
  print("""
-----------------------------
RELATÓRIO
-----------------------------
1- RELATÓRIO DE USUÁRIOS
2- SERVIÇOS/CONSERTO A SER PRESTADOS
3- RELATÓRIO COMPLEXO
0- VOLTAR
""")
  relatorio=input("ESCOLHA: ")
  return relatorio

def relatorio_usuario():
      print("""
-----------------------------
RELATÓRIO DE USUÁRIOS
-----------------------------
1- USUÁRIOS ATIVOS
2- USUÁRIOS DESATIVOS
3- TODOS OS USUÁRIOS
0- VOLTAR
""")
      rel_usuario=input("DIGITE: ")
      return rel_usuario

def menu_consetos():
      print("""
-------------------------------------------------
RELATÓRIO DE SERVIÇOS/CONSERTOS A SEREM PRESTADOS
-------------------------------------------------
1- SERVIÇOS/CONSERTOS ATIVOS
2- SERVIÇOS/CONSERTOS INATIVOS
3- TODOS OS SERVIÇOS/CONSERTOS
0- VOLTAR
""")
      relatorio2=input("DIGITE: ")
      return relatorio2

def mostrar_usuarios(estado):
    os.system('cls')
    print("----------------------------------------------------------------------------------------------------------------------")
    print("| %-15s | %-20s | %-30s | %-12s | %-25s |" % ("CPF", "NOME", "E-MAIL", "NASCIMENTO", "CIDADE"))
    print("----------------------------------------------------------------------------------------------------------------------")

    for cpf in usuarios:
        if estado == "todos" or usuarios[cpf]["estado"] == estado:
            print("| %-15s | %-20s | %-30s | %-12s | %-25s |" % (cpf,usuarios[cpf]["nome"],usuarios[cpf]["email"],usuarios[cpf]["data"],usuarios[cpf]["cidade"]))

    print("----------------------------------------------------------------------------------------------------------------------")
    input("PRESSIONE ENTER PARA CONTINUAR ")

def mostrar_consertos(estado):
    os.system('cls')
    print("-----------------------------------------------------------------------------------------------------")
    print("| %-10s | %-15s | %-25s | %-25s | %-10s |" % ("COD", "CPF", "APARELHO", "PROBLEMA", "DESCONTO"))
    print("-----------------------------------------------------------------------------------------------------")

    for cod in consertos:
        if estado == "todos" or consertos[cod]["estado"] == estado:
            print("| %-10s | %-15s | %-25s | %-25s | %-10s |" % (cod,consertos[cod]["cpf"],consertos[cod]["aparelho"],consertos[cod]["problema"],consertos[cod]["desconto"] + "%"))

    print("-----------------------------------------------------------------------------------------------------")
    input("PRESSIONE ENTER PARA CONTINUAR ")

def menu_complexo():
       print("""
-----------------------------
RELATÓRIOS COMPLEXOS
-----------------------------
1- RELATÓRIO POR IDADE
2- RELATÓRIO POR ANIVERSARIANTES
3- RELATÓRIO POR CIDADES DE USUÁRIOS
4- RELATÓRIO DETALHADO DOS SERVÇOS/CONSERTOS
0- SAIR
""")
       relatorio3 = input("DIGITE: ")
       return relatorio3

def mostrar_relatorio_idade(opcao, idadepes):
    os.system('cls')
    print("---------------------------------------------------------------------------------------------")
    print("| %-15s | %-20s | %-40s | %-5s |" % ("CPF", "NOME", "E-MAIL", "IDADE"))
    print("---------------------------------------------------------------------------------------------")

    for cpf in usuarios:
        ano = int(usuarios[cpf]["data"][6:])
        idade = datetime.datetime.now().year - ano

        if opcao == "1" and idade >= idadepes:
            print("| %-15s | %-20s | %-40s | %-5d |" % (cpf, usuarios[cpf]["nome"], usuarios[cpf]["email"], idade))

        elif opcao == "2" and idade <= idadepes:
            print("| %-15s | %-20s | %-40s | %-5d |" % (cpf, usuarios[cpf]["nome"], usuarios[cpf]["email"], idade))

        elif opcao == "3" and idade == idadepes:
            print("| %-15s | %-20s | %-40s | %-5d |" % (cpf, usuarios[cpf]["nome"], usuarios[cpf]["email"], idade))

    print("---------------------------------------------------------------------------------------------")

def relatorio_aniversariantes():
    os.system('cls')
    aniver = input("DIGITE O MÊS: ").lower()
    achou = ""

    if aniver in meses:

        print("--------------------------------------------------------------------------------------------------")
        print("| %-15s | %-20s | %-40s | %-10s |" % ("CPF", "NOME", "E-MAIL", "NASCIMENTO"))
        print("--------------------------------------------------------------------------------------------------")

        for cpf in usuarios:
            if usuarios[cpf]["data"][3:5] == meses[aniver]:
                achou = "sim"
                print("| %-15s | %-20s | %-40s | %-10s |" % (cpf,usuarios[cpf]["nome"],usuarios[cpf]["email"],usuarios[cpf]["data"]))

        if achou == "":
            print("NENHUM USUÁRIO FAZ ANIVERSÁRIO NESSE MÊS.")

        print("--------------------------------------------------------------------------------------------------")

    else:
        print("MÊS INVÁLIDO!")

    input("PRESSIONE ENTER PARA CONTINUAR ")

def relatorio_cidade():
    os.system('cls')
    cidadepro = input("DIGITE A CIDADE PARA MOSTRAR: ").lower()
    achou = ""

    print("------------------------------------------------------------------------------------------------------------")
    print("| %-15s | %-20s | %-40s | %-20s |" % ("CPF", "NOME", "E-MAIL", "CIDADE"))
    print("------------------------------------------------------------------------------------------------------------")

    for cpf in usuarios:
        cidade = usuarios[cpf]["cidade"].lower()

        if cidade == cidadepro:
            achou = "sim"

            print("| %-15s | %-20s | %-40s | %-20s |" % (cpf,usuarios[cpf]["nome"],usuarios[cpf]["email"],usuarios[cpf]["cidade"]))

    if achou == "":
        print("NENHUM USUÁRIO ENCONTRADO NESSA CIDADE.")

    print("------------------------------------------------------------------------------------------------------------")
    input("PRESSIONE ENTER PARA CONTINUAR ")

def relatorio_detalhado_servicos():
    os.system('cls')
    print("--------------------------------------------------------------------------------------------------------------------")
    print("| %-5s | %-25s | %-25s | %-35s | %-10s |" % ("COD", "CLIENTE", "APARELHO", "SERVIÇO/PROBLEMA", "DESCONTO"))
    print("--------------------------------------------------------------------------------------------------------------------")

    for cod in consertos:

        cpf = consertos[cod]["cpf"]
        nome = usuarios[cpf]["nome"]
        problema = consertos[cod]["problema"]

        if problema in servicos:
            servico = servicos[problema]["tipo"]
        else:
            servico = problema

        desconto = consertos[cod]["desconto"]

        print("| %-5s | %-25s | %-25s | %-35s | %-10s |" % (cod,nome,consertos[cod]["aparelho"],servico,desconto + "%"))

    print("--------------------------------------------------------------------------------------------------------------------")
    input("PRESSIONE ENTER PARA CONTINUAR ")

def relatorio_idade():
         print("""
-----------------------------
RELATÓRIO POR IDADE
-----------------------------
1- MAIOR OU IGUAL À IDADE
2- MENOR OU IGUAL À IDADE
3- IGUAL À IDADE
0- VOLTAR
""")
         opcao = input("ESCOLHA: ")
         return opcao

#menu principal
m= " "
usuarios, servicos, consertos = carregar_dados()
while m!= "0":
  m=menu_principal()

  if m == "1":
   consertar = " "
   os.system('cls')
   while consertar != "0":
    consertar = conserta_aparelho_menu()

    if consertar == "1":
     problemas_diversos()
     
    elif consertar == "2":
     catalogo_servicos()
    
    elif consertar == "3":
     cancelar_servico ()
    
    elif consertar == "0":
       print("VOLTANDO...")
       input("PRESSIONE ENTER PARA CONTINUAR ")
    
    else:
       print("OPÇÃO INVÁLIDA, POR FAVOR ESCOLHA UMA OPÇÃO VÁLIDA")
       input("PRESSIONE ENTER PARA CONTINUAR ")


  elif m == "2" :
    usuario = " "
    os.system('cls') 
    while usuario != "0":
      usuario = menu_usuario()

      if usuario== "1":
       cadastrar_usuario()

      elif usuario == "2":
       desativar_usuario()
    
      elif usuario == "3":
       atualizar_usuario()

      elif usuario == "4":
       pesquisar_usuario()
      
      elif usuario == "0":
       print("VOLTANDO...")
       input("PRESSIONE ENTER PARA CONTINUAR ")
      
      else:
       print("OPÇÃO INVÁLIDA, POR FAVOR ESCOLHA UMA OPÇÃO VÁLIDA")
       input("PRESSIONE ENTER PARA CONTINUAR ")

  elif m == "3": 
   servico = " "
   while servico !="0":
    os.system('cls')
    servico = menu_servico()
    
    if servico == "1":
     criar_servico()
   
    elif servico == "2":
     deletar_servico()
   
    elif servico == "3":
     atualizar_servico()

    elif servico == "4":
     P = " "
     while P != "0":
      os.system('cls')
      P = menu_mostart_servico()
      
      if P == "1":
        os.system('cls')
        mostrar_servicos(True)
      
      elif P == "2":
        os.system('cls')
        mostrar_servicos(False)
  
      elif P == "3":
        os.system('cls')
        mostrar_servicos("todos")
      
      elif P == "0":
        print("VOLTANDO...")
        input("PRESSIONE ENTER PARA CONTINUAR ")
      
      else:
        print("OPÇÃO INVÁLIDA, POR FAVOR ESCOLHA UMA OPÇÃO VÁLIDA")
        input("PRESSIONE ENTER PARA CONTINUAR ")

    elif servico == "0":
      print("VOLTANDO...")
      input("PRESSIONE ENTER PARA CONTINUAR ")
      
    else:
      print("OPÇÃO INVÁLIDA, POR FAVOR ESCOLHA UMA OPÇÃO VÁLIDA")
      input("PRESSIONE ENTER PARA CONTINUAR ")

  elif m == "4":
   relatorio=" "
   
   while relatorio != "0":
    os.system('cls')
    relatorio = menu_relatorio()

    if relatorio == "1":
     
     rel_usuario = " "
     while rel_usuario !="0":
      os.system('cls')
      rel_usuario = relatorio_usuario()
      
      if rel_usuario == "1":
         mostrar_usuarios(True)

      elif rel_usuario == "2":
        mostrar_usuarios(False)
      
      elif rel_usuario == "3":
       mostrar_usuarios("todos")

      elif rel_usuario == "0":
       print("VOLTANDO...")
       input("PRESSIONE ESPAÇO PARA CONTINUAR ")
      
      else:
       print("OPÇÃO INVÁLIDA, POR FAVOR ESCOLHA UMA OPÇÃO VÁLIDA")
       input("PRESSIONE ESPAÇO PARA CONTINUAR ")
           

    elif relatorio == "2":
      relatorio2 = " "
      
      while relatorio2 != "0":
       os.system('cls')
       relatorio2 =  menu_consetos()
      
       if relatorio2 == "1":
        mostrar_consertos(True)

       elif relatorio2 == "2":
        mostrar_consertos(False)
      
       elif relatorio2 == "3":
        mostrar_consertos("todos")

       elif relatorio2 == "0":
        print("VOLTANDO...")
        input("PRESSIONE ESPAÇO PARA CONTINUAR ")

       else:
        print("OPÇÃO INVÁLIDA, POR FAVOR ESCOLHA UMA OPÇÃO VÁLIDA")
        input("PRESSIONE ESPAÇO PARA CONTINUAR ")
  
    elif relatorio == "3":
      relatorio3 = " "
      
      while relatorio3 != "0":
       os.system('cls')
       relatorio3=menu_complexo()
      
       if relatorio3 == "1":
        
        opcao = " "
        while opcao != "0":
         os.system('cls')
         opcao= relatorio_idade()
         
         if opcao == "1" or opcao == "2" or opcao == "3":
          idadepes = int(input("DIGITE A IDADE: "))
          mostrar_relatorio_idade(opcao, idadepes)
         
         elif opcao == "0":
          print("VOLTANDO...")
        
         else:
          print("OPÇÃO INVÁLIDA, POR FAVOR ESCOLHA UMA OPÇÃO VÁLIDA")
        
         input("PRESSIONE ENTER PARA CONTINUAR ")

       elif relatorio3 == "2":
          relatorio_aniversariantes()

       elif relatorio3 == "3":
        relatorio_cidade()
    
       elif relatorio3 == "4":
         relatorio_detalhado_servicos()

       elif relatorio3 == "0":
         print("SAINDO DO PROGRAMA...")
         input("PRESSIONE ENTER PARA CONTINUAR...")
  
       else:
         print("OPÇÃO INVÁLIDA, POR FAVOR ESCOLHA UMA OPÇÃO VÁLIDA")
         input("PRESSIONE ENTER PARA CONTINUAR...")

    
    elif relatorio == "0":
      print("VOLTANDO...")
      input("PRESSIONE ENTER PARA CONTINUAR ")

    else:
      print("OPÇÃO INVÁLIDA, POR FAVOR ESCOLHA UMA OPÇÃO VÁLIDA")
      input("PRESSIONE ENTER PARA CONTINUAR...")
  
  elif m == "0":
    salvar_dados()
    print("SAINDO DO PROGRAMA...")
    input("PRESSIONE ENTER PARA CONTINUAR...")
  
  else:
    print("OPÇÃO INVÁLIDA, POR FAVOR ESCOLHA UMA OPÇÃO VÁLIDA")
    input("PRESSIONE ENTER PARA CONTINUAR...")
