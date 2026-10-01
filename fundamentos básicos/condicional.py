#Uma companhia aérea permite que seus clientes do tipo premium despachem bagagens de até 32kg sem nenhum custo adicional, enquanto os clientes o tipo gold podem levar as malas de até 28kg sem nenhum custo adicional e todos os demais devem pagar por qualquer bagagem despachada.
tipo_cliente = input("Por favor, informe o tipo de cliente: PREMIUM, GOLD ou REGULAR ")
peso_bagagem = float(input("Informe o peso da bagagem que o cliente deseja despachar"))

if tipo_cliente.upper() == "PREMIUM":
    #o que acontece se for Premium
    if peso_bagagem <= 32:
        #Exibir mensagem avisando que pode levar a bagagem
        print(f"Cliente{tipo_cliente}, sua bagagem está dentro do limite permitido! Não é necessário pagar nenhum valor para despacha-la")
    else:
        peso_excedente = peso_bagagem - 32
        #Exibir mensagem avisando sobre peso excedente
        print(f"Os clientes {tipo_cliente} têm direito a despacharem bagagens de até 32kg. A bagagem atual excede este peso em {peso_excedente}kg. Dirija-se ao balcão de cobrança para realizar o pagamento referente ao peso adicional")
elif tipo_cliente.upper() == "GOLD":
    #o que acontece se for Gold
    if peso_bagagem <= 28:
        #Exibir a mensagem avisando que pode levar a bagagem
        print(f"Cliente {tipo_cliente}, sua bagagem está dentro do limite permitido! Não é necessário pagar nenhum valor para despacha-la")
    else:
        peso_excedente = peso_bagagem - 28
        #Exibir a mensagem avisando sobre o excedente
        print(f"Os clientes {tipo_cliente} têm direito a despacharem bagagens de até 28kg. A bagagem atual excede este peso em {peso_excedente}kg, Dirija-se ao balcão de cobrança para realizar o pagamento referente ao peso adicional.")
else:
    #o que acontece se for Regular
    print(f"Os clientes {tipo_cliente} não têm direito à bagagem gratuita. Favor dirigir-se ao balcão de cobranças para realizar o pagamento pela bagagem")
