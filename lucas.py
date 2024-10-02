altura = float(input('Entre com sua altura:'))  
peso = float(input('Entre com seu peso:'))  
imc = peso/(altura * altura)  
print('Seu índice de massa corporal é {:.2f}'.format(imc))


if imc<17: 
    print("  Muito abaixo do peso")
elif imc>17 and imc<18.49:
    print("Abaixo do peso")
elif imc>18.50 and imc<24.99:
    print("Peso normal")
elif imc>25 and imc<29.99:
    print("Acima do peso")
elif imc>30 and imc<34.99:
    print("Obesidade I")
else:
    print("Obesidade II")
