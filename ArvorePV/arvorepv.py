class RbNode:
    def __init__(self, data):
        self.data = data
        self.pai = None
        self.left = None
        self.right = None
        self.cor = None

    def __str__(self):
        return str(self.data)

class RbTree:
    def __init__(self, data):
        nulo = RbNode(None)
        node = RbNode(data)
        self.root = node
        self.null = nulo
        self.null.cor = 'Black'
        self.root.left = nulo
        self.root.right = nulo
        node.pai = nulo
        node.cor = 'Black'



def Inorder_Tree_Walk(node):
    if node != None and node.data != None:
        Inorder_Tree_Walk(node.left)
        print((str(node), node.cor), end=" ")
        Inorder_Tree_Walk(node.right)


def Tree_Search(nodo, k):
    while nodo != None and k != nodo.data:
        if k < nodo.data:
            nodo = nodo.left
        else:
            nodo = nodo.right
    return nodo


def Tree_Minimum(nodo):
    while nodo.left != None and nodo.left.data != None:
        nodo = nodo.left
    return nodo


def Tree_Maximum(nodo):
    while nodo.right != None and nodo.right.data != None:
        nodo = nodo.right
    return nodo


def Tree_Successor(nodo):
    if nodo.right != None:
        return Tree_Minimum(nodo.right)
    y = nodo.pai
    while y != None and nodo == y.right:
        nodo = y
        y = Tree_Minimum(y)
    return y


def Tree_Predecessor(nodo):
    while nodo.left != None and nodo.left.data != None:
        return Tree_Maximum(nodo.left)
    y = nodo.pai
    while y != None and nodo == y.left:
        nodo = y
        y = Tree_Maximum(y)
    return y


def Left_Rotate(Tree, node):
    y = node.right
    node.right = y.left
    if y.left != Tree.null:
        y.left.pai = node
    y.pai = node.pai
    if node.pai == Tree.null:
        Tree.root = y
    elif node == node.pai.left:
        node.pai.left = y
    else:
        node.pai.right = y
    y.left = node
    node.pai = y


def Right_Rotate(Tree, node):
    y = node.left
    node.left = y.right
    if y.right != Tree.null:
        y.right.pai = node
    y.pai = node.pai
    if node.pai == Tree.null:
        Tree.root = y
    elif node == node.pai.right:
        node.pai.right = y
    else:
        node.pai.left = y
    y.right = node
    node.pai = y


def RB_Insert_Fixup(Tree, node):
    while node.pai.cor == 'Red':
        if node.pai == node.pai.pai.left:
            y = node.pai.pai.right
            if y.cor == 'Red':
                node.pai.cor = 'Black'
                y.cor = 'Black'
                node.pai.pai.cor = 'Red'
                node = node.pai.pai
            else:
                if node == node.pai.right:
                    node = node.pai
                    Left_Rotate(Tree, node)
                node.pai.cor = 'Black'
                node.pai.pai.cor = 'Red'
                Right_Rotate(Tree, node.pai.pai)
        else:
            y = node.pai.pai.left
            if y.cor == 'Red':
                node.pai.cor = 'Black'
                y.cor = 'Black'
                node.pai.pai.cor = 'Red'
                node = node.pai.pai
            else:
                if node == node.pai.left:
                    node = node.pai
                    Right_Rotate(Tree, node)
                node.pai.cor = 'Black'
                node.pai.pai.cor = 'Red'
                Left_Rotate(Tree, node.pai.pai)
    Tree.root.cor = 'Black'


def RB_Insert(Tree, node):
    y = Tree.null
    x = Tree.root
    while x != Tree.null:
        y = x
        if node.data < x.data:
            x = x.left
        else:
            x = x.right
    node.pai = y
    if y == Tree.null:
        Tree.root = node
    elif node.data < y.data:
        y.left = node
    else:
        y.right = node
    node.left = Tree.null
    node.right = Tree.null
    node.cor = 'Red'
    RB_Insert_Fixup(Tree, node)


def RB_Transplant(Tree, u, v):
    if u.pai == Tree.null:
        Tree.root = v
    elif u == u.pai.left:
        u.pai.left = v
    else:
        u.pai.right = v
        v.pai = u.pai


def RB_Delete_Fixup(Tree, node):
    while node != Tree.root and node.cor == 'Black':
        if node == node.pai.right:
            w = node.pai.right
            if w.cor == 'Red':
                w.cor = 'Black'
                node.pai.cor = 'Red'
                Left_Rotate(Tree, node.pai)
                w = node.pai.right
            if w.left.cor == 'Black' and w.right.cor == 'Black':
                w.cor = 'Red'
                node = node.pai
            else:
                if w.right.cor == 'Black':
                    w.left.cor = 'Black'
                    w.cor = 'Red'
                    Right_Rotate(Tree, w)
                    w = node.pai.right
                w.cor = node.pai.cor
                node.pai.cor = "Black"
                w.right.cor = "Black"
                Left_Rotate(Tree, node.pai)
                node = Tree.root
        else:
            w = node.pai.left
            if w.cor == 'Red':
                w.cor = 'Black'
                node.pai.cor = 'Red'
                Right_Rotate(Tree, node.pai)
                w = node.pai.left
            if w.right.cor == 'Black' and w.left.cor == 'Black':
                w.cor = 'Red'
                node = node.pai
            else:
                if w.left.cor == 'Black':
                    w.right.cor = 'Black'
                    w.cor = 'Red'
                    Left_Rotate(Tree, w)
                    w = node.pai.left
                w.cor = node.pai.cor
                node.pai.cor = "Black"
                w.left.cor = "Black"
                Right_Rotate(Tree, node.pai)
                node = Tree.rootRight
    node.cor = 'Black'


def RB_Delete(Tree, node):
    y = node
    y_cor_original = y.cor
    if node.left == Tree.null:
        x = node.right
        RB_Transplant(Tree, node, node.right)
    elif node.right == Tree.null:
        x = node.left
        RB_Transplant(Tree, node, node.left)
    else:
        y = Tree_Minimum(node.right)
        y = y.right
        if y.pai == node:
            x.pai = y
        else:
            RB_Transplant(Tree, y, y.right)
            y.right = node.right
            y.right.pai = y
        RB_Transplant(Tree, node, y)
        y.left = node.left
        y.left.pai = y
        y.cor = node.cor
    if y_cor_original == 'Black':
        RB_Delete_Fixup(Tree, x)


if __name__ == '__main__':

    idlist = {}

    while True:
        print('_-' * 40)
        print('''Digite a operação desejada:
0 - Criar Árvore
1 - Inserir Nós
2 - Deletar Nós
3 - Verificar o Predecessor de um Nó
4 - Verificar o Sucessor de um Nó
5 - Verificar o nó mínimo de uma árvore
6 - Verificar o nó máximo de uma árvore
7 - Andar em ordem por uma árvore
8 - Exibir Relatório
9 - Fechar o Programa.''')
        select = int(input('Alternativa: '))
        print('_-' * 40)

        if select == 0:
            ide = int(input("\nDigite um número de identificação para a árvore: "))
            if ide not in idlist.keys():
                raiz = int(input("Digite o valor da Raiz: "))
                tree = RbTree(raiz)
                idlist[ide] = tree
                print('\n' + ('-OK-' * 20))
                print('ARVORE CRIADA')
                print(('-OK-' * 20) + '\n')

            elif not ide:
                print("\n" + ("#" * 80))
                print("Você não digitou nenhum número de identificação, Por favor insira um número de identificação!")
                print(("#" * 80) + "\n")
            else:
                print("\n" + ("#" * 80))
                print("Esse número de identificação já está sendo utilizado, Tente Outro!")
                print(("#" * 80) + "\n")

        if idlist:

            if select == 1:

                print("NÚMEROS DE IDENTIFICAÇÃO DAS ÁRVORES NO SISTEMA:")
                for j in idlist.keys():
                    print(j, end='/ ')
                print(' ')
                chave = int(input("Digite o número de identificação da árvore que você quer alterar: "))
                if chave in idlist.keys():
                    arv = idlist[chave]
                    vezes = int(input("Digite quantos Nós você deseja adcionar à Árvore {}: ".format(chave)))
                    if not vezes or vezes < 1:
                        print("\n" + ("#" * 80))
                        print("VALOR INVÁLIDO")
                        print(("#" * 80) + "\n")
                    else:
                        for i in range(vezes):
                            dado = int(input("Digite o valor do Nó: "))
                            RB_Insert(arv, RbNode(dado))
                        print("\n" + ("-OK-" * 20))
                        print("NÓ(S) ADCIONADO(S)")
                        print(("-OK-" * 20) + "\n")
                else:
                    print("\n" + ("#" * 80))
                    print("Esse número de identificação não está cadastrado, Verifique se você o digitou corretamente!")
                    print(("#" * 80) + "\n")

            elif select == 2:

                print("NÚMEROS DE IDENTIFICAÇÃO DAS ÁRVORES NO SISTEMA:")
                for j in idlist.keys():
                    print(j, end='/ ')
                print(' ')
                chave = int(input("Digite o número de identificação da árvore que você quer alterar: "))
                if chave in idlist.keys():
                    arv = idlist[chave]
                    vezes = int(input("Digite quantos Nós você deseja remover da Árvore {}: ".format(chave)))
                    if not vezes or vezes < 1:
                        print("\n" + ("#" * 80))
                        print("VALOR INVÁLIDO")
                        print(("#" * 80) + "\n")
                    else:
                        for i in range(vezes):
                            dado = int(input("Digite o valor do Nó a ser Removido : "))
                            RB_Delete(arv, Tree_Search(arv.root, dado))
                        print("\n" + ("-OK-" * 20))
                        print("NÓ(S) REMOVIDO(S)")
                        print(("-OK-" * 20) + "\n")
                else:
                    print("\n" + ("#" * 80))
                    print("Esse número de identificação não está cadastrado, Verifique se você o digitou corretamente!")
                    print(("#" * 80) + "\n")

            elif select == 3:

                print("NÚMEROS DE IDENTIFICAÇÃO DAS ÁRVORES NO SISTEMA:")
                for j in idlist.keys():
                    print(j, end='/ ')
                print(' ')
                chave = int(input("Digite o número de identificação da árvore da qual você deseja selecionar o nó: "))
                if chave in idlist.keys():
                    arv = idlist[chave]
                    valor = int(input("Digite o valor do nó do qual você deseja verificar o Predecessor: "))
                    no = Tree_Predecessor(Tree_Search(arv.root, valor))
                    print("\n" + ("-OK-" * 20))
                    print("O Predecessor do nó de valor {} na árvore {} é o nodo de valor {}".format(valor, chave, no))
                    print(("-OK-" * 20) + "\n")
                else:
                    print("\n" + ("#" * 80))
                    print("Esse número de identificação não está cadastrado, Verifique se você o digitou corretamente!")
                    print(("#" * 80) + "\n")

            elif select == 4:

                print("NÚMEROS DE IDENTIFICAÇÃO DAS ÁRVORES NO SISTEMA:")
                for j in idlist.keys():
                    print(j, end='/ ')
                print(' ')
                chave = int(input("Digite o número de identificação da árvore da qual você deseja selecionar o nó: "))
                if chave in idlist.keys():
                    arv = idlist[chave]
                    valor = int(input("Digite o valor do nó do qual você deseja verificar o Sucessor: "))
                    no = Tree_Successor(Tree_Search(arv.root, valor))
                    print("\n" + ("-OK-" * 20))
                    print("O Sucessor do nó de valor {} na árvore {} é o nodo de valor {}".format(valor, chave, no))
                    print(("-OK-" * 20) + "\n")
                else:
                    print("\n" + ("#" * 80))
                    print("Esse número de identificação não está cadastrado, Verifique se você o digitou corretamente!")
                    print(("#" * 80) + "\n")

            elif select == 5:

                print("NÚMEROS DE IDENTIFICAÇÃO DAS ÁRVORES NO SISTEMA:")
                for j in idlist.keys():
                    print(j, end='/ ')
                print(' ')
                chave = int(input("Digite o número de identificação da árvore da qual você deseja verificar o nó mínimo: "))
                if chave in idlist.keys():
                    arv = idlist[chave]
                    no = Tree_Minimum(arv.root)
                    print("\n" + ("-OK-" * 20))
                    print("O nó mínimo da árvore {} é o nó de valor {}".format(chave, no))
                    print(("-OK-" * 20) + "\n")
                else:
                    print("\n" + ("#" * 80))
                    print("Esse número de identificação não está cadastrado, Verifique se você o digitou corretamente!")
                    print(("#" * 80) + "\n")

            elif select == 6:

                print("NÚMEROS DE IDENTIFICAÇÃO DAS ÁRVORES NO SISTEMA:")
                for j in idlist.keys():
                    print(j, end='/ ')
                print(' ')
                chave = int(input("Digite o número de identificação da árvore da qual você deseja verificar o nó máximo: "))
                if chave in idlist.keys():
                    arv = idlist[chave]
                    no = Tree_Maximum(arv.root)
                    print("\n" + ("-OK-" * 20))
                    print("O nó máximo da árvore {} é o nó de valor {}".format(chave, no))
                    print(("-OK-" * 20) + "\n")
                else:
                    print("\n" + ("#" * 80))
                    print("Esse número de identificação não está cadastrado, Verifique se você o digitou corretamente!")
                    print(("#" * 80) + "\n")

            elif select == 7:

                print("NÚMEROS DE IDENTIFICAÇÃO DAS ÁRVORES NO SISTEMA:")
                for j in idlist.keys():
                    print(j, end='/ ')
                print(' ')
                chave = int(input("Digite o número de identificação da árvore da qual você deseja verificar: "))
                if chave in idlist.keys():
                    arv = idlist[chave]
                    print("\n" + ("-OK-" * 20))
                    print("ARVORE {}:" .format(chave))
                    Inorder_Tree_Walk(arv.root)
                    print(' ')
                    print(("-OK-" * 20) + "\n")

        elif select == 8:
            break

        if select == 8:
            break

"""  RELATÓRIO

	A estrutura de dados utilizada no projeto foi construida através de programação orientada à objeto.
Primeiramente foi definida uma classe que representa um nó (ou vértice) com os seguintes atributos:

[RbNode]

'self.data' => o atributo que recebe um argumento de classe, esse argumento recebe o dado que será armazenado
		no nó.
'self.pai' => este ponteiro a princípio não aponta para dado algum mas no processo de inserção apontará para o pai
		deste nó.
'self.left' => este ponteiro também não aponta para dado algum mas no mesmo processo de inserção apontará para o
		filho esquerdo deste nó.
'self.right' => este ponteiro segue a mesma estrutura de 'self.left' porém aponta para o nó filho direito do nó
		em questão.
'self.cor' => este atributo armazena um string (no processo de inserção) que definirá se a cor do nó sera preta ("Black") ou vermelha ("Red").

//Também foi implementado uma função que retorna um tipo string do dado armazenado no nó, para facilitar a função que caminhará pela árvore em ordem.//

Em seguida, a estrutura da árvore em sí foi construída para não violar as cláusulas das árvores vermelhas e pretas
sendo implementada meticulosamente pelas definições do livro "Algorítmos - Teoria e Prática" (Cormen).

//1.Todo nó é vermelho ou preto.
  2.A raiz é preta.
  3.Toda folha (NIL) é preta.
  4.Se um nó é vermelho, então os seus filhos são pretos.
  5.Para cada nó, todos os caminhos simples do nó até folhas descendentes contêm o mesmo número de nós pretos.//

Segue aqui a orientação:

[RbTree]

'nulo = RbNode(None)' => Aqui constroi-se um nó de valor nulo para facilitar a construsão do nó "T.nil" mais a frente no __init__.
'node = RbNode(data)' => Recebe o argumento que se passa pela construção da classe que será utilizado para definir qual nó na árvore será a raiz.
'self.root = node' => ponteiro que a ponta para o "node" que definirá a raiz da árvore.
'self.null = nulo' => ponteiro que define o "T.nil" deste projeto.

'self.null.cor = 'Black'' => "Para uma árvore vermelho-preto T, a sentinela T.nil é um
			      objeto com os mesmos atributos que um nó comum na árvore. Seu atributo cor é PRETO."
'self.root.left = nulo' => "seus outros atributos — p, esquerda, 
'self.root.right = nulo' => direita e chave — podem adotar valores arbitrários."
'node.pai = nulo' => já que a raiz não tem pai, este ponteiro aponta para um nodo nulo de cor preta.
'node.cor = 'Black'' => a cor da raiz sempre é preta, então esse ponteiro sempre aponta para a cor 'Black'

A partir de agora serão descritas as funções que constroem, destroem e processam certas particularidades na árvore,
algumas dessas funções não foram retiradas do livro do cormem mas do canal "Programação Dinâmica" (https://www.youtube.com/channel/UC70mr11REaCqgKke7DPJoLg) e "MichaelSambol" (https://www.youtube.com/user/mikeysambol).

A primeira função em ordem crescente das linhas de código é Inorder_Tree_Walk() que recebe a raiz da árvore e exibe
na tela os nós em ordem, a função em questão foi adaptada para não só exibir o valor dos nós mas também sua cor.
Nesta função percorrer uma árvore de n nós demora o tempo Q(n) e custa O(n).

A função seguinte é Tree_Search() que recebe a raiz da árvore e um valor que será procurado na árvore, e retornará o
nó que contém um valor igual ao valor inserido ná função. O procedimento começa sua busca na raiz e traça um caminho simples descendo a árvore, para cada nó x que encontra, ele compara a chave k com a x.chave. Se as duas chaves são iguais, a busca termina. O caso nó programa é uma função iterativa, está função terá tempo de execução = O(h) sendo h a altura da árvore em questão.

As duas funções seguintes são Tree_Maximum() e Tree_Minimum() estás funções percorrem a árvore em busca dos vértices
de maior ou menor valor, respectivamente, nesta árvore em questão. Ambos os procedimentos são executados no tempo O(h) em uma árvore de altura h já que, como em Tree_Search(), a sequência de nós encontrados forma um caminho simples descendente partindo da raiz.

As duas funções seguintes são Tree_Successor() e Tree_Predecessor() essas funções procuram e retornam um nó sucessor
(ou predecessor) imediato de um outro nó que for passado por estas função.O tempo de execução de Tree_Successor em uma árvore de altura h é O(h), já que seguimos um caminho simples para cima na árvore ou, então, um caminho simples para baixo na árvore. O procedimento Tree_Predecessor(), que é simétrico de Tree_Successor(), também é executado no tempo O(h).

As proximas duas funções são partes das rotações, esses processos são importantes para o processo de balanceamento da estrutura de dados da classe árvore. As operações de árvores de busca RB_Insert() e RB_Delete, quando executadas em uma árvore vermelho-preto com n chaves, demoram o tempo O(lg n). Como elas modificam a árvore, o resultado pode violar as propriedades vermelho-preto portanto usamos as rotações para garantir o balanceamento e estas propriedades
Quando fazemos uma rotação para a esquerda em um nó x, supomos que seu filho à direita y não é T.nil; x pode ser qualquer nó na árvore cujo filho à direita não é T.nil. A rotação para a esquerda “pivota” ao redor da ligação de x para y. Transforma y na nova raiz da subárvore, com x como filho à esquerda de y e o filho à esquerda de y como filho à direita de x. Left_Rotate() e Right_Rotate são executados no tempo O(1). Somente ponteiros são alterados por uma rotação; todos os outros atributos em um nó permanecem os mesmos. Foi usado o vídeo "Red-black trees in 3 minutes - Rotations" (https://www.youtube.com/watch?v=95s3ndZRGbk) para descrever a lógica das rotações.

As Proximas cinco funções fazem parte dos processos de Inserção e Eliminação. As primeiras duas funções deste grupo são RB_Insert() e RB_Insert_Fixup() que pretendem inserir um nó em uma árvore e, no processo de inserção, consertar a árvore para as propriedades das árvores vermelha e preta. Podemos inserir um nó em uma árvore vermelho-preto de n nós no tempo O(lg n). para inserir o nó z na árvore T como se ela fosse uma árvore de busca binária comum e depois colorimos z de vermelho, usamos a cor vermelha porque sabemos que devemos respeitar as seguintes propriedades das árvores vermelha e preta:

////1. Um nó é vermelho ou preto.
    2. A raiz e folhas(NIL) são pretas.
    3. Se um nó é vermelho, então seus filhos são pretos.
    4. Todos os caminhos de um nó até seus descendentes NIL contêm o mesmo número de nós pretos.////

Ao inserir um nó vermelho podemos violar a propriedade 2 e 3 mas através do RB_Insert_Fixup() podemos facilmente consertar essas violações.

O mesmo acontece ao deletar um nó, alguma propriedade da arvore pode ser violada por isso usa-se metodos de RB_Transplant() e RB_Delete_Fixup() para não haver nenhuma violação. Como as outras operações básicas em uma árvore vermelho-preto de n nós, a eliminação de um nó demora o
tempo O(lg n).

Lógo após as definições das funções temos os menus e o dicionário idlist, que permite através de um número de identificação permite que o usuário faça alterações em múltiplas árvores.
Ao ser identificado um número de identificação o dicionário irá salvar em seus valores a árvore que aquele número representa e também retornará a arvore sempre que for chamado para fazer alguma alteração."""