'''

Variáveis
    Vamos experimentar usar uma variável em hello_world.py. Acrescente
uma nova linha no início do arquivo e modifique a segunda linha:
message = "Hello Python world!"
print(message) Execute esse programa para ver o que acontece. Você deverá
ver a mesma saída vista anteriormente: Hello Python world!
    Acrescentamos uma variável chamada message. Toda variável armazena
um valor, que é a informação associada a essa variável. Nesse caso, o
valor é o texto “Hello Python world!”.
Acrescentar uma variável implica um pouco mais de trabalho para o
interpretador Python. Quando processa a primeira linha, ele associa o
texto “Hello Python world!” à variável message. Quando chega à segunda
linha, o interpretador exibe o valor associado à message na tela.
Vamos expandir esse programa modificando hello_world.py para que
exiba uma segunda mensagem. Acrescente uma linha em branco em
hello_world.py e, em seguida, adicione duas novas linhas de código:
message = "Hello Python world!"
print(message)
message = "Hello Python Crash Course world!"
print(message) Ao executar hello_world.py agora você deverá ver duas
linhas na saída: Hello Python world!
Hello Python Crash Course world!
Podemos mudar o valor de uma variável em nosso programa a
qualquer momento, e Python sempre manterá o controle do valor atual.

Nomeando e usando variáveis
Ao usar variáveis em Python, é preciso seguir algumas regras e diretrizes.
Quebrar algumas dessas regras provocará erros; outras diretrizes
simplesmente ajudam a escrever um código mais fácil de ler e de
entender. Lembre-se de ter as seguintes regras em mente: • Nomes de
variáveis podem conter apenas letras, números e underscores. Podem
começar com uma letra ou um underscore, mas não com um número.
Por exemplo, podemos chamar uma variável de message_1, mas não de
1_message.
• Espaços não são permitidos em nomes de variáveis, mas
underscores podem ser usados para separar palavras em nomes de
variáveis. Por exemplo, greeting_message funciona, mas greeting
message causará erros.
• Evite usar palavras reservadas e nomes de funções em Python como
nomes de variáveis, ou seja, não use palavras que Python reservou
para um propósito particular de programação, por exemplo, a
palavra print. (Veja a seção “Palavras reservadas e funções
embutidas de Python”.) • Nomes de variáveis devem ser concisos,
porém descritivos. Por exemplo, name é melhor que n, student_name

é melhor que s_n e name_length é melhor que
length_of_persons_name.
• Tome cuidado ao usar a letra minúscula l e a letra maiúscula O, pois
elas podem ser confundidas com os números 1 e 0.
Aprender a criar bons nomes de variáveis, em especial quando seus
programas se tornarem mais interessantes e complicados, pode exigir
um pouco de prática. À medida que escrever mais programas e começar
a ler códigos de outras pessoas, você se tornará mais habilidoso na
criação de nomes significativos.
NOTA As variáveis Python que você está usando no momento devem utilizar
letras minúsculas. Você não terá erros se usar letras maiúsculas, mas é
uma boa ideia evitá-las por enquanto.

Evitando errosemnomesao usar variáveis
Todo programador comete erros, e a maioria comete erros todos os
dias. Embora bons programadores possam criar erros, eles também
sabem responder a esses erros de modo eficiente. Vamos observar um
erro que você provavelmente cometerá no início e vamos aprender a
corrigi-lo.
Escreveremos um código que gera um erro propositadamente. Digite o
código a seguir, incluindo a palavra mesage com um erro de ortografia,
conforme mostrada em negrito: message = "Hello Python Crash Course
reader!"

É claro que, nesse exemplo, omitimos a letra s do nome da variável
message na segunda linha. O interpretador Python não faz uma
verificação de ortografia em seu código, mas garante que os nomes das
variáveis estejam escritos de forma consistente. Por exemplo, observe o
que acontece quando escrevemos message incorretamente em outro
ponto do código também: mesage = "Hello Python Crash Course
reader!"

print(mesage) Nesse caso, o programa executa com sucesso!
Hello Python Crash Course reader!

Os computadores são exigentes, mas não se preocupam com uma
ortografia correta ou incorreta. Como resultado, você não precisa levar
em consideração a ortografia ou as regras gramaticais do inglês (ou de
português) quando tentar criar nomes de variáveis e escrever código.
Muitos erros de programação são apenas erros de digitação de um
caractere em uma linha de um programa. Se você gasta muito tempo
procurando um desses erros, saiba que está em boa companhia. Muitos
programadores experientes e talentosos passam horam caçando esses
tipos de pequenos erros. Tente rir da situação e siga em frente, sabendo
que isso acontecerá com frequência durante sua vida de programador.


NOTA: A melhor maneira de entender novos conceitos de programação é
tentar usá-los em seus programas. Se não souber o que fazer quando
estiver trabalhando em um exercício deste livro, procure dedicar-se a
outra tarefa por um tempo. Se continuar sem conseguir avançar, analise a
parte relevante do capítulo. Se ainda precisar de ajuda, veja as sugestões
no Apêndice C.

FAÇA VOCÊ MESMO
Escreva um programa separado para resolver cada um destes exercícios. Salve
cada programa com um nome de arquivo que siga as convenções-padrão de
Python, com letras minúsculas e underscores, por exemplo, simple_message.py e
simple_messages.py.
2.1 – Mensagem simples: Armazene uma mensagem em uma variável e, em
seguida, exiba essa mensagem.
2.2 – Mensagens simples: Armazene uma mensagem em uma variável e, em
seguida, exiba essa mensagem. Então altere o valor de sua variável para uma
nova mensagem e mostre essa nova mensagem.
'''
# 2.1
texto = "2.1 Teste de print"
print(texto)

# 2.2
texto = "2.2 Outro teste"
print(texto)

texto = "2.2 Mais um teste"
print(texto)

'''
Strings
Como a maior parte dos programas define e reúne algum tipo de dado e
então faz algo útil com eles, classificar diferentes tipos de dados é
conveniente. O primeiro tipo de dado que veremos é a string. As strings,
à primeira vista, são bem simples, mas você pode usá-las de vários
modos diferentes.
Uma string é simplesmente uma série de caracteres. Tudo que estiver
entre aspas é considerada uma string em Python, e você pode usar aspas
simples ou duplas em torno de suas strings, assim: "This is a string."
'This is also a string.'
Essa flexibilidade permite usar aspas e apóstrofos em suas strings: 'I
told my friend, "Python is my favorite language!"'
"The language 'Python' is named after Monty Python, not the snake."
"One of Python's strengths is its diverse and supportive community."
Vamos explorar algumas das maneiras de usar strings.

Mudando para letras maiúsculas e minúsculas em uma string usando
métodos

Uma das tarefas mais simples que podemos fazer com strings é mudar o
tipo de letra, isto é, minúscula ou maiúscula, das palavras de uma string.
Observe o código a seguir e tente determinar o que está acontecendo:
'''
name = "ada lovelace"
print(name.title())

'''
Salve esse arquivo como name.py e então execute-o.
Você deverá ver esta saída: Ada Lovelace Nesse exemplo, a string com
letras minúsculas "ada lovelace" é armazenada na variável name. O método
title() aparece depois da variável na instrução print(). Um método é uma
ação que Python pode executar em um dado. O ponto (.) após name em
name.title() informa a Python que o método title() deve atuar na variável
name. Todo método é seguido de um conjunto de parênteses, pois os
métodos, com frequência, precisam de informações adicionais para realizar
sua tarefa. Essas informações são fornecidas entre os parênteses. A
função title() não precisa de nenhuma informação adicional, portanto seus
parênteses estão vazios.
title() exibe cada palavra com uma letra maiúscula no início. Isso é
útil, pois, muitas vezes, você vai querer pensar em um nome como uma
informação. Por exemplo, você pode querer que seu programa
reconheça os valores de entrada Ada, ADA e ada como o mesmo nome e
exiba todos eles como Ada.
Vários outros métodos úteis estão disponíveis para tratar letras
maiúsculas e minúsculas também. Por exemplo, você pode mudar uma
string para que tenha somente letras maiúsculas ou somente letras
minúsculas, assim:

'''
name = "Ada Lovelace"
print(name.upper())
print(name.lower())

'''Essas instruções exibirão o
seguinte: ADA LOVELACE
ada lovelace O método lower() é particularmente útil para armazenar
dados. Muitas vezes, você não vai querer confiar no fato de seus usuários
fornecerem letras maiúsculas ou minúsculas, portanto fará a conversão das
strings para letras minúsculas antes de armazená-las. Então, quando
quiser exibir a informação, usará o tipo de letra que fizer mais sentido
para cada string.

Combinando ou concatenando strings

Muitas vezes, será conveniente combinar strings. Por exemplo, você
pode querer armazenar um primeiro nome e um sobrenome em variáveis
separadas e, então, combiná-las quando quiser exibir o nome completo
de alguém: first_name = "ada"
'''
first_name = "ada"
last_name = "lovelace"
full_name = first_name + " " + last_name
print(full_name)
'''
Python usa o símbolo de adição (+) para combinar
strings. Nesse exemplo, usamos + para criar um nome completo combinando
first_name, um espaço e last_name u, o que resultou em: ada lovelace
Esse método de combinar strings se chama concatenação. Podemos usar
concatenação para compor mensagens completas usando informações
armazenadas em uma variável. Vamos observar um exemplo:
'''
first_name = "ada"
last_name = "lovelace"
full_name = first_name + " " + last_name
print("Hello, " + full_name.title() + "!")
'''
Nesse caso, o nome completo é usado em u, em uma sentença que saúda o usuário, e o método title() é
utilizado para formatar o nome de forma apropriada. Esse código devolve uma
saudação simples, porém formatada de modo elegante: Hello, Ada Lovelace!
    Podemos usar concatenação para compor uma mensagem e então
armazenar a mensagem completa em uma variável:
'''
first_name = 'ada'
last_name = 'lovelace'
full_name = first_name + ' ' + last_name
message = "Hello, " + full_name.title() + "!"
print(message)

'''
Esse código também exibe a mensagem “Hello, Ada
Lovelace!”, mas armazenar a mensagem em uma variável em u deixa a
instrução print final em v muito mais simples.

'''
'''
Acrescentando espaços em branco em strings com tabulações ou
quebras delinha
    Em programação, espaços em branco se referem a qualquer caractere que
não é mostrado, como espaços, tabulações e símbolos de fim de linha.
Podemos usar espaços em branco para organizar a saída de modo que
ela seja mais legível aos usuários.
    Para acrescentar uma tabulação em seu texto, utilize a combinação de
caracteres \t como mostrado em:
'''
print("\tPython")

'''
Para acrescentar uma quebra de linha em uma
string, utilize a combinação de caracteres \n:
'''
print("Languages:\nPython\nC\nJavaScript")

'''
Também podemos combinar tabulações e quebras de linha em uma
única string. A string "\n\t" diz a Python para passar para uma nova
linha e iniciar a próxima com uma tabulação. O exemplo a seguir mostra
como usar uma string de uma só linha para gerar quatro linhas na saída:
'''
print("Languages:\n\tPython\n\tC\n\tJavaScript")

'''
Quebras de linha e tabulações serão muito úteis nos próximos
dois capítulos, quando começaremos a gerar muitas linhas de saída usando
apenas algumas linhas de código.
'''

'''
Removendo espaços em branco
Espaços em branco extras podem ser confusos em seus programas. Para
os programadores, 'python' e 'python ' parecem praticamente iguais.
Contudo, para um programa, são duas strings diferentes. Python
identifica o espaço extra em 'python ' e o considera significativo, a
menos que você informe o contrário.
    É importante pensar em espaços em branco, pois, com frequência,
você vai querer comparar duas strings para determinar se são iguais. Por
exemplo, uma situação importante pode envolver a verificação dos
nomes de usuário das pessoas quando elas fizerem login em um site.
Espaços em branco extras podem ser confusos em situações muito mais
simples também. Felizmente, Python facilita eliminar espaços em branco
extras dos dados fornecidos pelas pessoas.
    Python é capaz de encontrar espaços em branco dos lados direito e
esquerdo de uma string. Para garantir que não haja espaços em branco
do lado direito de uma string, utilize o método rstrip().
'''
favorite_language = 'python '
print(favorite_language)
print(favorite_language.rstrip())

'''
    O valor armazenado em favorite_language em u contém um espaço em
branco extra no final da string. Quando solicitamos esse valor a Python
em uma sessão de terminal, podemos ver o espaço no final do valor v.
Quando o método rstrip() atua na variável favorite_language em w, esse
espaço extra é removido. Entretanto, a remoção é temporária. Se
solicitar o valor de favorite_language novamente, você poderá ver que a
string é a mesma que foi fornecida, incluindo o espaço em branco extra
x.
    Para remover o espaço em branco da string de modo permanente, você
deve armazenar o valor com o caractere removido de volta na variável:

'''
favorite_language = 'python '
favorite_language = favorite_language.rstrip()
print(favorite_language)

'''
Para remover o espaço em branco da string, você deve remover o
espaço em branco do lado direito da string e então armazenar esse valor
de volta na variável original, como mostrado em u. Alterar o valor de
uma variável e então armazenar o novo valor de volta na variável original
é uma operação frequente em programação. É assim que o valor de uma
variável pode mudar à medida que um programa é executado ou em
resposta à entrada de usuário.
    Também podemos remover espaços em branco do lado esquerdo de
uma string usando o método lstrip(), ou remover espaços em branco
dos dois lados ao mesmo tempo com strip():
'''
favorite_language = ' python '
favorite_language.rstrip()
favorite_language.lstrip()
favorite_language.strip()
'''
    Nesse exemplo, começamos com um valor que tem espaços em
branco no início e no fim u. Então removemos os espaços extras do
lado direito em v, do lado esquerdo em w e de ambos os lados em x.
Fazer experimentos com essas funções de remoção pode ajudar você a
ter familiaridade com a manipulação de strings. No mundo real, essas
funções de remoção são usadas com mais frequência para limpar
entradas de usuário antes de armazená-las em um programa.
'''
'''
Evitando erros desintaxe com strings

Um tipo de erro que você poderá ver com certa regularidade é um erro
de sintaxe. Um erro de sintaxe ocorre quando Python não reconhece uma
seção de seu programa como um código Python válido. Por exemplo, se
usar um apóstrofo entre aspas simples, você produzirá um erro. Isso
acontece porque Python interpreta tudo que estiver entre a primeira aspa
simples e o apóstrofo como uma string. Ele então tenta interpretar o
restante do texto como código Python, o que causa erros.
    Eis o modo de usar aspas simples e duplas corretamente. Salve este
programa como apostrophe.py e então execute-o: apostrophe.py message
= "One of Python's strengths is its diverse community."

'''
message = "One of Python's strengths is its diverse community."
print(message)
'''
O apóstrofo aparece entre um conjunto de aspas duplas,
portanto o interpretador Python não terá nenhum problema para ler a
string corretamente: One of Python's strengths is its diverse community.
    No entanto, se você usar aspas simples, o interpretador Python não
será capaz de identificar em que ponto a string deve terminar:

message = 'One of Python's strengths is its diverse community.'
print(message)

message = 'One of Python's strengths is its diverse community.'
^u SyntaxError: invalid syntax

 logo depois da segunda aspa simples. Esse erro de sintaxe informa
que o interpretador não reconheceu algo como código Python válido. Os
erros podem ter origens variadas, e destacarei alguns erros comuns à
medida que surgirem. Você poderá ver erros de sintaxe com frequência
enquanto aprende a escrever código Python apropriado. Erros de sintaxe
também são o tipo menos específico de erro, portanto podem ser difíceis e
frustrantes para identificar e corrigir. Se você não souber o que fazer
quanto a um erro particularmente persistente, consulte as sugestões no
Apêndice C.

NOTA
    O recurso de destaque de sintaxe de seu editor deve ajudar você a
identificar alguns erros de sintaxe rapidamente quando escrever seus
programas. Se você vir código Python em destaque como se fosse inglês,
ou inglês destacado como se fosse código Python, é provável que haja
uma aspa sem correspondente em algum ponto de seu arquivo.
'''
'''
                        FAÇA VOCÊ MESMO
Salve cada um dos exercícios a seguir em um arquivo separado com um nome
como name_cases.py. Se não souber o que fazer, descase um pouco ou
consulte as sugestões que estão no Apêndice C.

2.3 Mensagem pessoal: Armazene o nome de uma pessoa em uma variável e
apresente uma mensagem a essa pessoa. Sua mensagem deve ser simples,
como “Alô Eric, você gostaria de aprender um pouco de Python hoje?”.

2.4 – Letras maiúsculas e minúsculas em nomes: Armazene o nome de uma
pessoa em uma variável e então apresente o nome dessa pessoa em letras
minúsculas, em letras maiúsculas e somente com a primeira letra maiúscula.

2.5 – Citação famosa: Encontre uma citação de uma pessoa famosa que você
admire. Exiba a citação e o nome do autor. Sua saída deverá ter a aparência
a seguir, incluindo as aspas: Albert Einstein certa vez disse: “Uma pessoa que
nunca cometeu um erro jamais tentou nada novo.”

2.6 – Citação famosa 2: Repita o Exercício 2.5, porém, desta vez, armazene o
nome da pessoa famosa em uma variável chamada famous_person. Em
seguida, componha sua mensagem e armazene-a em uma nova variável
chamada message. Exiba sua mensagem.


2.7 – Removendo caracteres em branco de nomes: Armazene o nome de uma
pessoa e inclua alguns caracteres em branco no início e no final do nome.
Lembre-se de usar cada combinação de caracteres, "\t" e "\n", pelo menos
uma vez.

Exiba o nome uma vez, de modo que os espaços em branco em torno do
nome sejam mostrados. Em seguida, exiba o nome usando cada uma das três
funções de remoção de espaços: lstrip(), rstrip() e strip()
'''
#2.3
pessoa  = 'rafael'
mensagem = ', você gostaria de aprender um pouco de Python hoje?'
print(pessoa + mensagem)

#2.4
print(pessoa.lower())
print(pessoa.upper())
print(pessoa.title())

#2.5 / #2.6
famoso = 'maya angelou '
layout = "certa vez disse: "
citacao = '"Você enfrentará muitas derrotas na vida, mas nunca se deixe ser derrotado."'
print(famoso.title() + layout + citacao)

#2.7
nome = ' rhuan '
print(nome.rstrip())
print(nome.lstrip())
print(nome.strip())

'''
Números
    Os números são usados com muita frequência em programação para
armazenar pontuações em jogos, representar dados em visualizações,
guardar informações em aplicações web e assim por diante. Python trata
números de várias maneiras diferentes, de acordo com o modo como
são usados. Vamos analisar inicialmente como Python trata inteiros,
pois eles são os dados mais simples para trabalhar.
'''
'''
Inteiros
Você pode somar (+), subtrair (-), multiplicar (*) e dividir (/) inteiros em
Python.
>>> 2 + 3
5
>>> 3 - 2
1
>>> 2 * 3
6
>>> 3 / 2
1.5
    
    Em uma sessão de terminal, Python simplesmente devolve o resultado
da operação. Dois símbolos de multiplicação são usados em Python
para representar exponenciais: >>> 3 ** 2
9
>>> 3 ** 3
27
>>> 10 ** 6
1000000

    A linguagem Python também aceita a ordem das operações, portanto
você pode fazer várias operações em uma expressão. Também podemos
usar parênteses para modificar a ordem das operações para que Python
possa avaliar sua expressão na ordem que você especificar. 

Por exemplo:
>>> 2 + 3*4
14
>>> (2 + 3) * 4
20

    Os espaços nesses exemplos não têm nenhum efeito no modo como
Python avalia as expressões: eles simplesmente ajudam a identificar mais
rapidamente as operações que têm prioridade quando lemos o código.
'''
'''
Números de ponto flutuante

Python chama qualquer número com um ponto decimal de número de
ponto flutuante (float). Esse termo é usado na maioria das linguagens de
programação e refere-se ao fato de um ponto decimal poder aparecer em
qualquer posição em um número. Toda linguagem de programação
deve ser cuidadosamente projetada para lidar de modo adequado com
números decimais de modo que eles se comportem de forma
apropriada, não importa em que lugar o ponto decimal apareça.
    Na maioria das ocasiões, podemos usar decimais sem nos preocupar
com o modo como eles se comportam. Basta fornecer os números que
você quer usar, e Python provavelmente fará o que você espera:
>>> 0.1 + 0.1
0.2
>>> 0.2 + 0.2
0.4
>>> 2 * 0.1
0.2
>>> 2 * 0.2
0.4
    No entanto, tome cuidado, pois, às vezes, você poderá obter um
número arbitrário de casas decimais em sua resposta:
>>> 0.2 + 0.1
0.30000000000000004
>>> 3 * 0.1
0.30000000000000004

    Isso acontece em todas as linguagens e não é motivo para muita
preocupação. Python tenta encontrar uma forma de representar o
resultado do modo mais exato possível, o que, às vezes, é difícil,
considerando a maneira como os computadores devem representar os
números internamente. Basta ignorar as casas decimais extras por
enquanto; você aprenderá a lidar com casas extras quando for
necessário nos projetos da Parte II.
'''
'''
Evitando erros detipo comafunção str()
Com frequência, você vai querer usar o valor de uma variável em uma
mensagem. Por exemplo, suponha que você queira desejar feliz
aniversário a alguém. Você poderia escrever um código como este:
'''
#age = 23
#message = "Happy " + age + "rd Birthday!"
#print(message)

'''
Você esperaria que esse código exibisse a seguinte
saudação simples de feliz aniversário: Happy 23rd birthday!. Contudo, se
executar esse código, verá que ele gera um erro: Traceback (most recent
call last): File "birthday.py", line 2, in <module> message = "Happy " +
age + "rd Birthday!"...

 TypeError: Can't convert 'int' object to str implicitly É um erro de
tipo. Significa que Python não é capaz de reconhecer o tipo de informação
que você está usando. Nesse exemplo, Python vê que você está usando uma
variável em u cujo valor é um inteiro (int), mas não tem certeza de como
interpretar esse valor. O interpretador sabe que a variável poderia
representar um valor numérico 23 ou os caracteres 2 e 3. Quando usar
inteiros em strings desse modo, você precisará especificar explicitamente
que quer que Python utilize o inteiro como uma string de caracteres.
Podemos fazer isso envolvendo a variável com a função str(); essa função
diz a Python para representar valores que não são strings como strings: 
'''
age = 23
message = "Happy " + str(age) + "rd Birthday!"
print(message)

'''
Com isso, Python sabe que você quer converter o valor
numérico 23 em uma string e exibir os caracteres 2 e 3 como parte da
mensagem de feliz aniversário. Agora você obterá a mensagem esperada, sem
erros: Happy 23rd Birthday!
    Trabalhar com números em Python é simples na maior parte do
tempo. Se você estiver obtendo resultados inesperados, verifique se
Python está interpretando seus números da forma desejada, seja como
um valor numérico, seja como um valor de string.
'''

'''
                                FAÇA VOCÊ MESMO
2.8 – Número oito: Escreva operações de adição, subtração, multiplicação e
divisão que resultem no número 8. Lembre-se de colocar suas operações em
instruções print para ver os resultados. Você deve criar quatro linhas como esta:
print(5 + 3) Sua saída deve simplesmente ser composta de quatro linhas, com o
número 8 em cada uma das linhas.

2.9 – Número favorito: Armazene seu número favorito em uma variável. Em
seguida, usando essa variável, crie uma mensagem que revele o seu número
favorito. Exiba essa mensagem.

'''
#2.8
print(5 + 3)
print(16 / 2)
print(10 - 2)
print(2 * 4)

#2.9
numero_favorito = 40
mensagem = " é o meu número favorito!"
print(str(numero_favorito) + mensagem)

'''
Comentários

Comentários são um recurso extremamente útil na maioria das
linguagens de programação. Tudo que você escreveu em seus
programas até agora é código Python. À medida que seus programas se
tornarem mais longos e complicados, você deve acrescentar notas que
descrevam a abordagem geral adotada para o problema que você está
resolvendo. Um comentário permite escrever notas em seus programas
em linguagem natural.

Como escrevercomentários?
Em Python, o caractere sustenido (#) indica um comentário. Tudo que
vier depois de um caractere sustenido em seu código será ignorado pelo
interpretador Python. Por exemplo: comment.py # Diga olá a todos
print("Hello Python people!") Python ignora a primeira linha e executa a
segunda.
Hello Python people!

Quetipos decomentário você deve escrever?

O principal motivo para escrever comentários é explicar o que seu
código deve fazer e como você o faz funcionar. Quando estiver no meio
do trabalho de um projeto, você entenderá como todas as partes se
encaixam. Porém, quando retomar um projeto depois de passar um
tempo afastado, é provável que você vá esquecer alguns detalhes. É
sempre possível estudar seu código por um tempo e descobrir como os
segmentos deveriam funcionar, mas escrever bons comentários pode
fazer você economizar tempo ao sintetizar sua abordagem geral em
linguagem natural clara.
    Se quiser se tornar um programador profissional ou colaborar com
outros programadores, escreva comentários significativos. Atualmente, a
maior parte dos softwares é escrita de modo colaborativo, seja por um
grupo de funcionários em uma empresa, seja por um grupo de pessoas
que trabalham juntas em um projeto de código aberto. Programadores
habilidosos esperam ver comentários no código, portanto é melhor
começar a adicionar comentários descritivos em seus programas agora.
Escrever comentários claros e concisos em seu código é um dos hábitos
mais benéficos que você pode desenvolver como um novo programador.
    Quando estiver decidindo se deve escrever um comentário, pergunte a
si mesmo se você precisou considerar várias abordagens antes de definir
uma maneira razoável de fazer algo funcionar; em caso afirmativo,
escreva um comentário sobre sua solução. É muito mais fácil apagar
comentários extras depois que retornar e escrever comentários em um
programa pouco comentado. A partir de agora, usarei comentários em
exemplos deste livro para ajudar a explicar algumas seções de código.
'''
'''
Zen de Python
Durante muito tempo, a linguagem de programação Perl foi o principal
sustentáculo da internet. A maioria dos primeiros sites interativos usava
scripts Perl. O lema da comunidade Perl na época era: “Há mais de uma
maneira de fazer algo”. As pessoas gostaram dessa postura por um
tempo porque a flexibilidade inscrita na linguagem possibilitava resolver
a maior parte dos problemas de várias maneiras. Essa abordagem era
aceitável enquanto trabalhávamos em nossos próprios projetos, mas, em
algum momento, as pessoas perceberam que a ênfase na flexibilidade
dificultava a manutenção de projetos grandes em longo prazo. Revisar
código e tentar descobrir o que outra pessoa pensou quando resolvia
um problema complexo era difícil, tedioso e consumia bastante tempo.
    Programadores Python experientes incentivarão você a evitar a
complexidade e buscar a simplicidade sempre que for possível. A
filosofia da comunidade Python está contida no “Zen de Python” de Tim
Peters. Você pode acessar esse conjunto resumido de princípios para
escrever um bom código Python fornecendo import this ao seu
interpretador. Não reproduzirei todo o “Zen de Python” aqui, mas
compartilharei algumas linhas para ajudar a entender por que elas devem
ser importantes para você como um programador Python iniciante.

>>> import this The Zen of Python, by Tim Peters

Beautiful is better than ugly.

(Bonito é melhor que feio) Os programadores Python adotam a noção
de que o código pode ser bonito e elegante. Em programação, as
pessoas resolvem problemas. Os programadores sempre respeitaram
soluções bem projetadas, eficientes e até mesmo bonitas para os
problemas. À medida que conhecer mais a linguagem Python e usá-la
para escrever mais códigos, uma pessoa poderá espiar por sobre seu
ombro um dia e dizer: “Uau, que código bonito!”.

Simple is better than complex.

(Simples é melhor que complexo) Se você puder escolher entre uma
solução simples e outra complexa, e as duas funcionarem, utilize a
solução simples. Seu código será mais fácil de manter, e será mais
simples para você e para outras pessoas desenvolverem com base nesse
código posteriormente.

Complex is better than complicated.

(Complexo é melhor que complicado) A vida real é confusa e, às
vezes, uma solução simples para um problema não é viável. Nesse caso,
utilize a solução mais simples possível que funcione.

Readability counts.

(Legibilidade conta) Mesmo quando seu código for complexo,
procure deixá-lo legível. Quando trabalhar com um projeto que envolva
códigos complexos, procure escrever comentários informativos para
esse código.

There should be one-- and preferably only one --obvious way to do it.

(Deve haver uma – e, de preferência, apenas uma – maneira óbvia de
fazer algo) Se for solicitado a dois programadores Python que resolvam
o mesmo problema, eles deverão apresentar soluções razoavelmente
compatíveis. Isso não quer dizer que não haja espaço para a criatividade
em programação. Pelo contrário! No entanto, boa parte da programação
consiste em usar abordagens pequenas e comuns para situações simples
em um projeto maior e mais criativo. Os detalhes de funcionamento de
seus programas devem fazer sentido para outros programadores Python.

Now is better than never.

(Agora é melhor que nunca) Você poderia passar o resto de sua vida
conhecendo todas as complexidades de Python e da programação em
geral, mas, nesse caso, jamais concluiria qualquer projeto. Não tente
escrever um código perfeito; escreva um código que funcione e, então,
decida se deve aperfeiçoá-lo nesse projeto ou passar para algo novo

'''
'''
Resumo
Neste capítulo aprendemos a trabalhar com variáveis. Aprendemos a
usar nomes descritivos para as variáveis e a resolver erros de nomes e de
sintaxe quando surgirem. Vimos o que são strings e como exibi-las
usando letras minúsculas, letras maiúsculas e iniciais maiúsculas. No
início, utilizamos espaços em branco para organizar a saída e
aprendemos a remover caracteres em branco desnecessários de
diferentes partes de uma string. Começamos a trabalhar com inteiros e
números de ponto flutuante, e lemos a respeito de alguns
comportamentos inesperados com os quais devemos tomar cuidado
quando trabalharmos com dados numéricos. Também aprendemos a
escrever comentários explicativos para que você e outras pessoas leiam
seu código com mais facilidade. Por fim, lemos a respeito da filosofia de
manter seu código o mais simples possível, sempre que puder.
No Capítulo 3 aprenderemos a armazenar coleções de informações em
variáveis chamadas listas. Veremos como percorrer uma lista,
manipulando qualquer informação que ela tiver.

'''
'''
Ao prosseguir para o próximo capítulo e começar a explorar tópicos
mais sofisticados, procure ter em mente essa filosofia de simplicidade e
clareza. Programadores experientes respeitarão mais o seu código e
ficarão felizes em oferecer feedback e colaborar com você em projetos
interessantes
'''