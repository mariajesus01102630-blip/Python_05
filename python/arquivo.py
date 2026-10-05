# 1- Crie uma variavel mensagem e exiba uma mensagen na tela
# 2- Crie uma variavel numero e exiba esse numero na tela
# 3- Crie duas variaveis numéricas e faça as 4 operações matematicas com esses números> Faça tambem a exponenciação e o resto da divisão
# 4- CRie duas variaveis de texto e faça a concatenação dessas mensagens
# 5- Faça um programa que receba um texto e faça-o repetir 5 vezes
# 6- Crie uma variavel de texto em minúsculo e deixo-o com todas as letras maiúsculas
# 7- Crie um programa que receba um texto do usuario e exiba na tela 
# 8- CRie um programa que receba do usuario nome, idade, altura, cidade e  estado e exiba a seguinte frase na tela: "Olá, meu nome é ____, tenho ____ anos de idade. Moro na cidade de ______/__". Use printf
# 9- Crie um programa com uma variavel numero qualquerl. Depois, crie uma variavel chute pedindo para o usuario digitar um numero. Na sequencia, crie uma condição para saber se o chute é igual a variavel. Caso seja igual exiba uma mensagem "Voce acertou", se for diferente exiba a mensagem "voce errou"1 

mensagem = ' meu nome é Maria'
print(mensagem)

numero = 7
print(numero)

numero2 = 2
soma = numero + numero2
print(soma)

numero3 = 10
numero4 = 20
soma = numero3 + numero4
div = numero3 / numero4
sub = numero3 - numero4
multi = numero3 * numero4
print(soma)
print(div)
print(sub)
print(multi)

expo = numero3 ** numero4
Resto_dive = numero4 % numero3
Divi_Inteira = numero // numero2
print(expo)
print(Resto_dive)
print(Divi_Inteira)

texto1 = "batata"
texto2 = "banana"
c = texto1 + " " + texto2
print(c)

text = "aula"
repeticao = text * 5
print (repeticao)

text2 = 'bom dia'
#text2.upper()
print(text2.upper())

texto = input("Coloque sua mensagem")
print(texto)

nome2 = input (" digite seu nome") 
idade = int (input("digite sua idade"))
altura = float (input("digite sua altura"))
cidade = input(" digite sua cidade")
estado = input ("digite seu estado")

print (f'meu nome é {nome2}, tenho {idade} anos de idade. Moro na cidade de {cidade} do estado de {estado}. minha altura é {altura}') 