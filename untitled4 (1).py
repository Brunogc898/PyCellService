
import os

usuarios = {}

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
   print("""
-----------------------------
INFORMAÇÃO DO APARELHO
-----------------------------
1° INFORME O NOME DO SEU APARELHO
2° INFORME O PROBLEMA DO SEU APARELHO
3° INFORME SEU CPF CASO POR UM USUARIO CADASTADO :")

""")

   aparelho=input("NOME DO APARELHO: ")
   problema=input("PROBLEMA DO APARELHO: ")
   nome=input("INFORME SEU CPF CASO POR UM USUARIO CADASTADO :")

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
0- SAIR
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
       cpf=int(input("CPF: "))
       usuarios[cpf] = {"nome": nome, "email": email}

       print("CADASTRO REALIZADO COM SUCESSO!")
       input("PRESSIONE ENTER PARA CONTINUAR...")

      elif usuario == "2":
       print("""
-----------------------------
DELETAR USUARIO
-----------------------------
1° INFORME SEU CPF PARA DELETAR
2° CONFIRME SE QUER REALMENTE QUER DELETAR
""")
       cpf=int("CPF: ")
       if cpf in usuarios:
        print("USUARIO ENCONTRADO")
        conf=("CONFIRME SE QUER DELETAR O USUARIO COM (S/N): ")
        if conf == "S":
         del usuarios[cpf]
        else:
         print("CANCELAMENTO DA DELETA DE USUARIO")
       else:
        print("USUARIO NÃO ENCOTRADO")
    
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

  if m == "3":
   servico= " "
   while servico !="0":
    print("""
-----------------------------
TIPO DE SERVIÇO
-----------------------------
1- CONSERTO
2- MANUTENÇÃO
3- REPARO
4- TROCA DE PEÇA
5- FORMATAÇÃO
0- SAIR
""")
   servico = input("ESCOLHA: ")

   if servico == "1":
    print("""
-----------------------------
CONSERTO
-----------------------------
1- O CONSERTO É REALIZADO QUANDO O APARELHO ESTÁ COM DEFEITO DE FABRICAÇÃO, OU SEJA, O PROBLEMA EXISTE DESDE O MOMENTO DA COMPRA DO APARELHO.
2- O PRAZO PARA O CONSERTO É DE 30 DIAS, CONTADOS A PARTIR DA DATA DE COMPRA DO APARELHO.
3- O CONSERTO É GRATUITO, OU SEJA, NÃO HÁ CUSTO PARA O CLIENTE.
4- O CLIENTE DEVE APRESENTAR A NOTA FISCAL DE COMPRA DO APARELHO PARA REALIZAR O CONSERTO.
""") 
    tipo = "Conserto"
    input("PRESSIONE ENTER PARA CONTINUAR...")

   elif servico == "2":
    print("""
-----------------------------
MANUTENÇÃO
-----------------------------
1- A MANUTENÇÃO É REALIZADA PARA PREVENIR PROBLEMAS NO APARELHO E GARANTIR SEU BOM FUNCIONAMENTO.
2- O PRAZO PARA A MANUTENÇÃO É DE 15 DIAS, CONTADOS A PARTIR DA DATA DE SOLICITAÇÃO.
3- A MANUTENÇÃO TEM UM CUSTO, QUE VARIA DE ACORDO COM O TIPO DE SERVIÇO NECESSÁRIO.
4- O CLIENTE DEVE APRESENTAR A NOTA FISCAL DE COMPRA DO APARELHO PARA REALIZAR A MANUTENÇÃO.
""")
    tipo = "Manutenção"
    input("PRESSIONE ENTER PARA CONTINUAR...") 

   elif servico == "3":
    print("""
-----------------------------
REPARO
-----------------------------
1- O REPARO É REALIZADO QUANDO O APARELHO ESTÁ COM DEFEITO QUE NÃO PODE SER RESOLVIDO COM MANUTENÇÃO.
2- O PRAZO PARA O REPARO É DE 30 DIAS, CONTADOS A PARTIR DA DATA DE SOLICITAÇÃO.
3- O REPARO TEM UM CUSTO, QUE VARIA DE ACORDO COM O TIPO DE SERVIÇO NECESSÁRIO.
4- O CLIENTE DEVE APRESENTAR A NOTA FISCAL DE COMPRA DO APARELHO PARA REALIZAR O REPARO.
""")
    tipo = "Reparo"
    input("PRESSIONE ENTER PARA CONTINUAR...")

   elif servico == "4":
    print("""
-----------------------------
TROCA DE PEÇA
-----------------------------
1- A TROCA DE PEÇA É REALIZADA QUANDO UMA PEÇA DO APARELHO ESTÁ DANIFICADA E NÃO PODE SER REPARADA.
2- O PRAZO PARA A TROCA DE PEÇA É DE 30 DIAS, CONTADOS A PARTIR DA DATA DE SOLICITAÇÃO.
3- A TROCA DE PEÇA TEM UM CUSTO, QUE VARIA DE ACORDO COM O TIPO DE PEÇA NECESSÁRIA.
4- O CLIENTE DEVE APRESENTAR A NOTA FISCAL DE COMPRA DO APARELHO PARA REALIZAR A TROCA DE PEÇA.
""")
    tipo = "Troca de Peça"
    input("PRESSIONE ENTER PARA CONTINUAR...")

   elif servico == "5":
    print("""
-----------------------------
FORMATAÇÃO
-----------------------------
1- A FORMATAÇÃO É REALIZADA PARA LIMPAR OS DADOS DO APARELHO E RESTAURAR SEU FUNCIONAMENTO PADRÃO.
2- O PRAZO PARA A FORMATAÇÃO É DE 15 DIAS, CONTADOS A PARTIR DA DATA DE SOLICITAÇÃO.
3- A FORMATAÇÃO TEM UM CUSTO, QUE VARIA DE ACORDO COM O TIPO DE SERVIÇO NECESSÁRIO.
4- O CLIENTE DEVE APRESENTAR A NOTA FISCAL DE COMPRA DO APARELHO PARA REALIZAR A FORMATAÇÃO.
""")
    tipo = "Formatação"
    input("PRESSIONE ENTER PARA CONTINUAR...")

  if m =="4":
   
   relatorio=" "
   while relatorio != "0":
    print("""
-----------------------------
RELATORIO
-----------------------------
1- RELATORIO DE USUARIOS
2- SERVIÇOS PRESTADOOS
3- APARELHOS CONSETADOS
4- SAIR
""")
    servico=input("ESCOLHA: ")

    if servico == "1":
     print("""
-----------------------------
RELATORIO DE USUARIOS
-----------------------------
""")
print("MANUTENÇÃO")
input("PRESSIONE ESPAÇO PARA CONTINUAR")

    elif servico == "2":
     print("asdasdas")
     