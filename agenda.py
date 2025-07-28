def adicionar_contato(contatos, nome, telefone, email):
  contato = {"nome": nome, "telefone": telefone, "email": email, "favorito": False}
  contatos.append(contato)
  print(f"O contato {nome} foi adicionado com sucesso!")
  return

def visualizar_lista_contatos(contatos):
  print("\nLista de contatos:")
  for indice, contato in enumerate(contatos, start=1):
    status = "★" if contato["favorito"] else " "
    nome = contato["nome"]
    telefone = contato["telefone"]
    email = contato["email"]
    print(f"{indice}. [{status}] {nome} | {telefone} | {email}")
  return

def editar_contato(contatos, novo_nome, novo_telefone, novo_email, indice_contato):
  indice_ajustado = int(indice_contato) - 1
  contato_nome = contatos[indice_ajustado]["nome"]
  contato_telefone = contatos[indice_ajustado]["telefone"]
  contato_email = contatos[indice_ajustado]["email"]
  if indice_ajustado >= 0 and indice_ajustado < len(contatos):
    contatos[indice_ajustado]["nome"] = novo_nome
    print(f"O nome do contato foi alterado de {contato_nome} para {novo_nome}")
    contatos[indice_ajustado]["telefone"] = novo_telefone
    print(f"O telefone do contato foi alterado de {contato_telefone} para {novo_telefone}")
    contatos[indice_ajustado]["email"] = novo_email
    print(f"O e-mail do contato foi alterado de {contato_email} para {novo_email}")
  return

def favoritar(contatos, indice_contato):
  indice_ajustado = int(indice_contato) - 1
  contato_nome = contatos[indice_ajustado]["nome"]
  if indice_ajustado >= 0 and indice_ajustado < len(contatos):
    contatos[indice_ajustado]["favorito"] = True
    print(f"O contato {contato_nome} foi adicionado como favorito!")
  elif contatos[indice_ajustado]["favorito"]:
    print(f"O contato {contato_nome} já está marcado como favorito.")
  else:
    print("Indice inválido!")
  return

def desfavoritar(contatos, indice_contato):
  indice_ajustado = int(indice_contato) - 1
  contato_nome = contatos[indice_ajustado]["nome"]
  if contatos[indice_ajustado]["favorito"]:
    contatos[indice_ajustado]["favorito"] = False
    print(f"O contato {contato_nome} foi desmarcado como favorito!")
  elif contatos[indice_ajustado]["favorito"] == False:
    print(f"O contato {contato_nome} não está marcado como favorito.")
  else:
    print("Indice inválido.")
  return

def lista_contatos_favoritos(contatos):
  print("\nLista de contatos favoritos:")
  for indice, contato in enumerate(contatos, start=1):
    if contato["favorito"]:
      nome = contato["nome"]
      telefone = contato["telefone"]
      email = contato["email"]
      print(f"{indice}. [★] {nome} | {telefone} | {email}")
  return

def apagar_contato(contatos, indice_contato):
  indice_ajustado = int(indice_contato) - 1
  contato_nome = contatos[indice_ajustado]["nome"]
  if indice_ajustado >= 0 and indice_ajustado < len(contatos):
    contatos.remove(contatos[indice_ajustado])
    print(f"O contato {contato_nome} foi removido da agenda.")
  return

contatos = []
while True:
  print("\n--- AGENDA DE CONTATOS ---")
  print("1 - Adicionar contato")
  print("2 - Visualizar lista de contatos")
  print("3 - Editar um contato")
  print("4 - Marcar/desmarcar contato como favorito")
  print("5 - Visualizar lista de contatos favoritos")
  print("6 - Apagar um contato")
  print("0 - Sair")
  opcao = input("Selecione uma das opcoes acima: ")

  if opcao == "1":
    nome = input("Informe o nome do contato: ")
    telefone = input("Informe o telefone do contato: ")
    email = input("Informe o e-mail do contato: ")
    adicionar_contato(contatos, nome, telefone, email)

  elif opcao == "2":
    visualizar_lista_contatos(contatos)

  elif opcao == "3":
    visualizar_lista_contatos(contatos)
    indice_contato = int(input("Informe o indice do contato que deseja editar: "))
    novo_nome = input("Digite o novo nome do contato: ")
    novo_telefone = input("Digite o novo telefone do contato: ")
    novo_email = input("Digite o novo e-mail do contato: ")
    editar_contato(contatos, novo_nome, novo_telefone, novo_email, indice_contato)


  elif opcao == "4":
    if len(contatos) > 0:
      print("\n1 - Marcar como favorito")
      print("2 - Desmarcar como favorito")
      escolha = input("Escolha uma das opcoes: ")
      if escolha == "1":
        visualizar_lista_contatos(contatos)
        indice_contato = int(input("Informe o indice do contato que deseja favoritar: "))
        favoritar(contatos, indice_contato)
        
      elif escolha == "2":
        visualizar_lista_contatos(contatos)
        indice_contato = int(input("Informe o indice do contato que deseja desfavoritar: "))
        desfavoritar(contatos, indice_contato)
      
      else:
        print("Opção inválida!")

  elif opcao == "5":
    lista_contatos_favoritos(contatos)

  elif opcao == "6":
    visualizar_lista_contatos(contatos)
    indice_contato = int(input("Informe o indice do contato que deseja apagar: "))
    apagar_contato(contatos, indice_contato)

  elif opcao == "0":
    print("Saindo...")
    break

  else:
    print("Opção inválida! Tente novamente.")