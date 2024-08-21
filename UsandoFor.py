def imprimeAndares(totalAndares):

  for andar in range (1, totalAndares + 1):
    if andar == 13:
        continue
    else:
      print(f"Andar{andar}")

imprimeAndares(20)