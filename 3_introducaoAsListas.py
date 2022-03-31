'''
Neste capítulo e no próximo, veremos o que são listas e
como começar a trabalhar com os elementos de uma
lista. As listas permitem armazenar conjuntos de
informações em um só lugar, independentemente de
termos alguns itens ou milhões deles. As listas são um
dos recursos mais eficazes de Python, prontamente
acessíveis aos novos programadores, e elas agregam
muitos conceitos importantes em programação.
'''
'''
O que é uma lista?
Uma lista é uma coleção de itens em uma ordem em particular. Podemos
criar uma lista que inclua as letras do alfabeto, os dígitos de 0 a 9 ou os
nomes de todas as pessoas de sua família. Você pode colocar qualquer
informação que quiser em uma lista, e os itens de sua lista não precisam
estar relacionados de nenhum modo em particular. Como uma lista
geralmente contém mais de um elemento, é uma boa ideia deixar seu
nome no plural, por exemplo, letters, digits ou names.
    Em Python, colchetes ([]) indicam uma lista, e elementos individuais
da lista são separados por vírgulas. Eis um exemplo simples de uma lista
que contém alguns tipos de bicicleta:
'''

bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles)

'''
Se você pedir a Python que exiba uma lista, ela devolverá
a representação da lista, incluindo os colchetes: ['trek', 'cannondale',
'redline', 'specialized']
    Como essa não é a saída que você quer que seus usuários vejam,
vamos aprender a acessar os elementos individuais de uma lista.
'''
'''
Acessando elementos de uma lista
Listas são coleções ordenadas, portanto você pode acessar qualquer
elemento de uma lista informando a posição – ou índice – do item
desejado ao interpretador Python. Para acessar um elemento de uma
lista, escreva o nome da lista seguido do índice do item entre colchetes.
    Por exemplo, vamos extrair a primeira bicicleta da lista bicycles:
'''
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles[0])
'''
A sintaxe para isso está em u. Quando solicitamos um
item simples de uma lista, Python devolve apenas esse elemento, sem
colchetes ou aspas: trek
'''
'''
    Esse é o resultado que você quer que seus usuários vejam – uma saída
limpa, formatada de modo elegante.
    Também podemos usar os métodos de string do Capítulo 2 em
qualquer elemento de uma lista. Por exemplo, podemos formatar o
elemento 'trek' de modo mais bonito usando o método title():
'''
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles[0].title())
'''
Esse exemplo gera a mesma saída do exemplo
anterior, exceto pelo fato de 'Trek' começar com uma letra maiúscula.
'''
'''
A posição dos índices começa em 0, e não em 1

Python considera que o primeiro item de uma lista está na posição 0, e
não na posição 1. Isso é válido para a maioria das linguagens de
programação, e o motivo tem a ver com o modo como as operações em
lista são implementadas em um nível mais baixo. Se estiver recebendo
resultados inesperados, verifique se você não está cometendo um erro
simples de deslocamento de um.
    O segundo item de uma lista tem índice igual a 1. Usando esse sistema
simples de contagem, podemos obter qualquer elemento que quisermos
de uma lista subtraindo um de sua posição na lista. Por exemplo, para
acessar o quarto item de uma lista, solicite o item no índice 3.
    As instruções a seguir acessam as bicicletas nos índices 1 e 3:
'''
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles[1])
print(bicycles[3])
'''
Esse código devolve a segunda e a
quarta bicicletas da lista: cannondale specialized
'''
'''
Python tem uma sintaxe especial para acessar o último elemento de
uma lista. Ao solicitar o item no índice -1, Python sempre devolve o
último item da lista:
'''
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles[-1])
'''
Esse código devolve o valor 'specialized'. Essa
sintaxe é bem útil, pois, com frequência, você vai querer acessar os
últimos itens de uma lista sem saber exatamente o tamanho dela. Essa
convenção também se estende a outros valores negativos de índice. O
índice -2 devolve o segundo item a partir do final da lista, o índice -3
devolve o terceiro item a partir do final, e assim sucessivamente.
'''

'''
Usando valores individuais de uma lista

Você pode usar valores individuais de uma lista, exatamente como faria
com qualquer outra variável. Por exemplo, podemos usar concatenação
para criar uma mensagem com base em um valor de uma lista.
    Vamos tentar obter a primeira bicicleta da lista e compor uma
mensagem usando esse valor.
'''
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
message = "My first bicycle was a " + bicycles[0].title() + "."
print(message)
'''
Em u, compomos uma frase usando o valor em bicycles[0] e
a armazenamos na variável message. A saída é uma frase simples sobre a
primeira bicicleta da lista: My first bicycle was a Trek.
'''