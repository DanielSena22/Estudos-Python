nome = input('Digite seu nome completo: ')

print(nome.upper())
print(nome.lower())
print(len(nome.replace(' ', '')))
primeiroNome = nome.split()
print(len(primeiroNome[0]))
