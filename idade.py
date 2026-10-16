#Solicita a idade de uma pessoa e determina se ela é maior de idade (idade maior ou igual a 18 anos) ou menor de idade (idade menor que 18 anos).

idade = int(input("Digite sua idade: "))

if idade >= 18:
    print("Maior de idade")
else:
    print("Menor de idade")