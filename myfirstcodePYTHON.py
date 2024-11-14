# recebendo informação da altura do painel
altura = int(input("Digite a altura do painel: "))
while altura < 1:
    print ("A altura está incorreta! Digite a altura igual ou maior que 1")
    altura = int(input("Digite a altura do painel: "))
# recebendo informação da largura do painel       
largura = int(input("Digite a largura do painel: "))
while largura < 1:
    print ("A largura está incorreta! Digite a largura igual ou maior que 1")
    largura = int(input("Digite a largura do painel: "))
# cálculo do total de LEDS para o painel
calculo_total_leds = (altura +1) * (largura +1)

# resultado apresentado do total de LEDS para o painel
print("O total de LEDS para este painel é de", calculo_total_leds, "LEDS")