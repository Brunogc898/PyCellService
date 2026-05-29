
usuarios = {}


m= " "
while m!= "0":
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
  m=input(" ")

  if m == "1":
   print("""
-----------------------------
INFORMAÇÃO DO APARELHO
-----------------------------
1° INFORME O NOME DO SEU APARELHO
2° INFORME O PROBLEMA DO SEU APARELHO
""")

   aparelho=input("NOME DO APARELHO: ")
   problema=input("PROBLEMA DO APARELHO: ")

   print("""
-----------------------------
TIPO DE SERVIÇO
-----------------------------
1- CONSERTO
2- MANUTENÇÃO
3- REPARO
4- TROCA DE PEÇA
5- FORMATAÇÃO
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


   print("""
-----------------------------
DADOS DO SERVIÇO
-----------------------------
APARELHO: %s
PROBLEMA: %s
SERVIÇO: %s
""" % (aparelho, problema, tipo))

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
      usuario=input(" ")

      if usuario== "1":
       print("""
-----------------------------
CADASTRAR USUARIO
-----------------------------
1° INFORME SEU NOME
2° E-MAIL PARA CONTATO
3° SEU CPF
4° (OPCIONAL) TELEFONE DE AMIGO PARA CONTATO
""")

      nome=input("NOME: ")
      email=input("E-MAIL: ")
      cpf=input("CPF: ")
      perm=input("DESEJA ADICIONAR TELEFONE DE AMIGO? (S/N)")
      tele= " "
      if perm == "S":
       tele=input("TELEFONE DE AMIGO: ")
      usuarios[cpf] = {"nome": nome, "email": email, "telefone": tele}

      print("CADASTRO REALIZADO COM SUCESSO!")
      input("PRESSIONE ENTER PARA CONTINUAR...")
      