print('') #print para dar espaço
print('* Calculadora Simples *') #printando o título do programa na tela
print('') #print para dar espaço

n1 = float(input('Informe o primeiro número: ')) # Pedindo o n1 para o usuário, float para poder aceitar qualquer número real.

while True: #Se o usuário escrever alguma coisa, é true, então segue o código.
    op = input('Informe a operação (+, - , * , /): ') #Pedindo a operação que ele quer.
    if op == '+' or op == '-' or op == '*' or op == '/': #Se a operação for uma dessas. quebra e continua o código.
        break

n2 = float(input('Informe o segundo número: ')) #Pedindo o segundo número

if op == '+': #Se for +
    print('Resultado =', n1+n2) #Printando +
elif op == '-': #Se for -
    print('Resultado =', n1-n2 ) #Printando -
elif op == '*': #Se for *
    print('Resultado =', n1*n2) #Printando *
elif op == '/': #Se for /
    print('Resultado = ', n1/n2) #Printando /