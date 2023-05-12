


resposta =0

while resposta!="3":
    print("1 Animar")
    print("2 Calcular")
    print("3 Sortir")
    resposta=input("Que vols fer? ")
    if resposta == "1":
        nom=input("com et dius? ")
        resultat2= ""
        for lletra in nom:
            resultat2 = resultat2 + lletra
            resultat2 = resultat2 + '-'
            resultat = "dame una " + lletra.upper()
            print(resultat)
        print(resultat2[:-1])
    if resposta == "2" :
        operacio = input("Escriu la operació ")
        if '+' in operacio:
            operand1 =  operacio[0:operacio.index('+')]
            operand2 =  operacio[operacio.index('+')+1:]
            print(int(operand2)+int(operand1))
        elif '-' in operacio:
            operand1 = operacio[0:operacio.index('-')]
            operand2 = operacio[operacio.index('-') + 1:]
            print(int(operand1) - int(operand2))
        elif 'x' in operacio:
            operand1 = operacio[0:operacio.index('x')]
            operand2 = operacio[operacio.index('x') + 1:]
            print(int(operand1) * int(operand2))
        elif ':' in operacio:
            operand1 = operacio[0:operacio.index(':')]
            operand2 = operacio[operacio.index(':') + 1:]
            print(int(operand1) / int(operand2))
