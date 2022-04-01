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

'''
                    FAÇA VOCÊ MESMO
Experimente criar estes programas pequenos para ter um pouco de experiência
própria com listas em Python. Você pode criar uma nova pasta para os
exercícios de cada capítulo a fim de mantê-los organizados.
3.1 – Nomes: Armazene os nomes de alguns de seus amigos em uma lista
chamada names. Exiba o nome de cada pessoa acessando cada elemento da
lista, um de cada vez.

3.2 – Saudações: Comece com a lista usada no Exercício 3.1, mas em vez de
simplesmente exibir o nome de cada pessoa, apresente uma mensagem a elas.
O texto de cada mensagem deve ser o mesmo, porém cada mensagem deve
estar personalizada com o nome da pessoa.

3.3 – Sua própria lista: Pense em seu meio de transporte preferido, como
motocicleta ou carro, e crie uma lista que armazene vários exemplos. Utilize sua
lista para exibir uma série de frases sobre esses itens, como “Gostaria de ter
uma moto Honda”.
'''
# 3.1
names = ['Rhuan', 'Kauan', 'Luciano', 'Anedino', 'Karoline']
print('Resp. 3.1')
print(names[0])
print(names[1])
print(names[2])
print(names[3])
print(names[4])
print('-'*30)


# 3.2
print('Resp. 3.2')
print(names[0] + " Trabalha na Totvs")
print(names[1] + " Trabalha osf Digital")
print(names[2] + " Trabalha empresa de dados")
print(names[3] + " Trabalha na Totvs")
print(names[4] + " Trabalha Avaris")
print('-'*30)

# 3.3
lista = ['Antonov 224', 'Honda', 'Masserat']

print('Resp. 3.3')
print(
    f"O Maior avião do mundo é o {lista[0]}, a moto {lista[1]} é muito rápida e a {lista[2]} é uma marca de carro muito luxuosa.")
print('-'*30)

'''
Alterando, acrescentando e removendo elementos

    A maioria das listas que você criar será dinâmica, o que significa que
você criará uma lista e então adicionará e removerá elementos dela à
medida que seu programa executar. Por exemplo, você poderia criar um
jogo em que um jogador atire em alienígenas que caem do céu. Poderia
armazenar o conjunto inicial de alienígenas em uma lista e então
remover um item da lista sempre que um alienígena for atingido. Sempre
que um novo alienígena aparecer na tela, adicione-o à lista. Sua lista de
alienígenas diminuirá e aumentará de tamanho no decorrer do jogo.
'''

'''
Modificando elementos de uma lista

A sintaxe para modificar um elemento é semelhante à sintaxe para
acessar um elemento de uma lista. Para alterar um elemento, use o nome
da lista seguido do índice do elemento que você quer modificar e, então,
forneça o novo valor que você quer que esse item tenha.
    Por exemplo, vamos supor que temos uma lista de motocicletas, e que
o primeiro item da lista seja 'honda'. Como mudaríamos o valor desse
primeiro item?
'''
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

motorcycles[0] = 'ducati'
print(motorcycles)
'''
O código em u define a lista original, com 'honda'
como o primeiro elemento. O código em v altera o valor do primeiro item
para 'ducati'. A saída mostra que o primeiro item realmente foi
modificado e o restante da lista permaneceu igual: ['honda', 'yamaha',
'suzuki']
['ducati', 'yamaha', 'suzuki']
    Você pode mudar o valor de qualquer item de uma lista, e não apenas
o primeiro.
'''
'''
Acrescentando elementos em uma lista

Você pode acrescentar um novo elemento em uma lista por diversos
motivos. Por exemplo, talvez você queira que novos alienígenas
apareçam no jogo, pode querer acrescentar novos dados em uma
visualização ou adicionar novos usuários registrados em um site que
você criou. Python oferece várias maneiras de acrescentar novos dados
em listas existentes.
'''
'''
Concatenando elementos no final de uma lista

    A maneira mais simples de acrescentar um novo elemento em uma lista é
concatenar o item na lista. Quando concatenamos um item em uma lista,
o novo elemento é acrescentado no final. Usando a mesma lista que
tínhamos no exemplo anterior, adicionaremos o novo elemento 'ducati'
no final da lista:
'''
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
motorcycles.append('ducati')
print(motorcycles)
'''
método append() em u
acrescenta 'ducati' no final da lista sem afetar qualquer outro elemento:
['honda', 'yamaha', 'suzuki']
['honda', 'yamaha', 'suzuki', 'ducati']
    O método append() facilita criar listas dinamicamente. Por exemplo,
podemos começar com uma lista vazia e então acrescentar itens à lista
usando uma série de instruções append(). Usando uma lista vazia, vamos
adicionar os elementos 'honda', 'yamaha' e 'suzuki' à lista:
'''
motorcycles = []
motorcycles.append('honda')
motorcycles.append('yahama')
motorcycles.append('suzuki')

print(motorcycles)

# A lista resultante tem exatamente o mesmo aspecto da
# lista dos exemplos anteriores: ['honda', 'yamaha', 'suzuki']
'''
    Criar listas dessa maneira é bem comum, pois, com frequência, você
não conhecerá os dados que seus usuários querem armazenar em um
programa até que ele esteja executando. Para deixar que seus usuários
tenham o controle, comece definindo uma lista vazia que armazenará os
valores dos usuários. Em seguida, concatene cada novo valor fornecido
à lista que você acabou de criar.

Inserindo elementos em uma lista

Você pode adicionar um novo elemento em qualquer posição de sua
lista usando o método insert(). Faça isso especificando o índice do novo
elemento e o valor do novo item.
'''
motorcycles = ['honda', 'yamaha', 'suzuki']
motorcycles.insert(0, 'ducati')

print(motorcycles)

# Nesse exemplo, o código em u insere o valor 'ducati' no início da lista. O método insert()
# abre um espaço na posição 0 e armazena o valor 'ducati' nesse local. Essa
# operação desloca todos os demais valores da lista uma posição à direita:
# ['ducati', 'honda', 'yamaha', 'suzuki']

'''
Removendo elementos de uma lista

Com frequência, você vai querer remover um item ou um conjunto de
itens de uma lista. Por exemplo, quando um jogador atinge um
alienígena no céu com um tiro, é bem provável que você vá querer
removê-lo da lista de alienígenas ativos. Se um usuário decidir cancelar a
conta em sua aplicação web, você vai querer remover esse usuário da
lista de usuários ativos. Você pode remover um item de acordo com sua
posição na lista ou seu valor.

Removendo um item usando a instrução del
Se a posição do item que você quer remover de uma lista for conhecida,
a instrução del poderá ser usada.
'''
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

del motorcycles[0]

print(motorcycles)

# O código em u usa del para remover o primeiro item,
# 'honda', da lista de motocicletas: ['honda', 'yamaha', 'suzuki']
# ['yamaha', 'suzuki']

'''
Você pode remover um item de qualquer posição em uma lista usando
a instrução del, se souber qual é o seu índice. Por exemplo, eis o modo
de remover o segundo item, 'yamaha', da lista:
'''
motorcycles = ['honda', 'yamaha','suzuki']
print(motorcycles)

del motorcycles[1]

print(motorcycles)

# A segunda motocicleta é apagada da lista: ['honda',
# 'yamaha', 'suzuki']
# ['honda', 'suzuki']

'''
    Nos dois exemplos não podemos mais acessar o valor que foi
removido da lista após a instrução del ter sido usada.

Removendo um item com o método pop()
    Às vezes, você vai querer usar o valor de um item depois de removê-lo
de uma lista. Por exemplo, talvez você queira obter as posições x e y de
um alienígena que acabou de ser atingido para que possa desenhar uma
explosão nessa posição. Em uma aplicação web, você poderia remover
um usuário de uma lista de membros ativos e então adicioná-lo a uma
lista de membros inativos.
    O método pop() remove o último item de uma lista, mas permite que
você trabalhe com esse item depois da remoção. O termo pop deriva de
pensar em uma lista como se fosse uma pilha de itens e remover um item
(fazer um pop) do topo da pilha. Nessa analogia, o topo da pilha
corresponde ao final da lista.
    Vamos fazer um pop de uma motocicleta da lista de motocicletas:
'''
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

popped_motorcycles = motorcycles.pop()

print(motorcycles)
print(popped_motorcycles)

# Começamos definindo e exibindo a lista motorcycles
# em u. Em v fazemos pop de um valor da lista e o armazenamos na variável
# popped_motorcycle. Exibimos a lista em w para mostrar que um valor foi
# removido da lista. Então exibimos o valor removido em x para provar que
# ainda temos acesso ao valor removido.
# A saída mostra que o valor 'suzuki' foi removido do final da lista e
# agora está armazenado na variável popped_motorcycle: ['honda', 'yamaha',
# 'suzuki']
# ['honda', 'yamaha']
# suzuki
'''
    Como esse método pop() poderia ser útil? Suponha que as motocicletas
da lista estejam armazenadas em ordem cronológica, de acordo com a
época em que fomos seus proprietários. Se for esse o caso, podemos
usar o método pop() para exibir uma afirmação sobre a última
motocicleta que compramos:
'''
motorcycles = ['honda', 'yamaha', 'suzuki']
last_owned = motorcycles.pop()
print('The last motorcycle I ownde was a ' + last_owned.title() + '.')

# A saída é uma frase simples sobre a
# motocicleta mais recente que tivemos: The last motorcycle I owned was a
# Suzuki.