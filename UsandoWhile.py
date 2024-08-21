def impAndares(numeroAndares):
    andarAtual = 0
    while (andarAtual <= numeroAndares):
      if andarAtual ==13:
          andarAtual = andarAtual+1
          continue
      print(f"Andar {andarAtual}")
      andarAtual += 1
        
      
impAndares(20)