def calcular_velocidade_media():
    #Codigo da nossa função
    velocidade_media = distancia / tempo
    #exibir o resultado
    print(f"A velocidade média é {velocidade_media}")


#solicitar distancia e tempo
distancia = float(input("Digite a distancia percorrida: "))
tempo = float(input("Digite o tempo da viagem: "))
calcular_velocidade_media()