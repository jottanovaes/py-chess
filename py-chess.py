import numpy as np
########## Xadrez da Ale e do Kayola ##########

#### A estrutura do jogo do xadrez será dividida em: ####
#### Peça: Menor elemento que conterá os métodos posição (para guardar a própria posição no tabuleiro) ####
#### Tipos de Peça: Classes que serão uma extensão das peças, herdará seus métodos e terá seus próprios ####
#### Posição: cada casa do tabuleiro, na questão, serão 64 unidades dessa classe para o jogo, guardando informações como: ####
#### conteudo: vazio ou peça, disponível: indica se tem peça ou não, capturavel: indica se a posição indica uma captura ####

###### Definição da classe peças #####
class IntervaloError(Exception):
    """Posição informada está fora do intervalo (0, 7)"""

class Peca:
    def __init__(self, posXPeca, posYPeca, corDaPeca, nomeDaPeca):
        self.posXPeca = posXPeca
        self.posYPeca = posYPeca
        self.nomeDaPeca = nomeDaPeca
        self.corDaPeca = corDaPeca

    def nome(self):
        return self.nomeDaPeca


###### Definição das peças do jogo, que extende a classe Peça #####


class Rei(Peca):
    def __init__(self, posXPeca, posYPeca, corDaPeca):
        Peca.__init__(self, posXPeca, posYPeca, corDaPeca, "Rei")

    def __str__(self):
        return 'R'+self.corDaPeca[0].upper()

    def movimentacao(self, tabuleiro):
        # Movimento Rei Norte
        if int(self.posXPeca) - 1 >= 0:
            if tabuleiro.tabuleiro[int(self.posXPeca) - 1][int(self.posYPeca)].conteudo is None:
                tabuleiro.tabuleiro[int(self.posXPeca) - 1][int(
                    self.posYPeca)].disponivel = True

        # Movimento Rei Nordeste
        if int(self.posXPeca) - 1 >= 0 and int(self.posYPeca) - 1 >= 0:
            if tabuleiro.tabuleiro[int(self.posXPeca)-1][int(self.posYPeca) - 1].conteudo is None:
                tabuleiro.tabuleiro[int(self.posXPeca)-1][int(
                    self.posYPeca) - 1].disponivel = True

        # Movimento Rei Este
        if int(self.posYPeca) + 1 < 7 :
            if tabuleiro.tabuleiro[int(self.posXPeca)][int(self.posYPeca) + 1].conteudo is None:
                tabuleiro.tabuleiro[int(self.posXPeca)][int(
                self.posYPeca) + 1].disponivel = True

        # Movimento Rei Sudeste
        if int(self.posXPeca) + 1 < 7 and int(self.posYPeca) + 1 < 7:
            if tabuleiro.tabuleiro[int(self.posXPeca)+1][int(self.posYPeca) + 1].conteudo is None:
                tabuleiro.tabuleiro[int(self.posXPeca)+1][int(
                    self.posYPeca) + 1].disponivel = True

        # Movimento Rei Sul
        if int(self.posXPeca) + 1 < 7 and tabuleiro.tabuleiro[int(self.posXPeca) + 1][int(self.posYPeca)].conteudo is None:
            tabuleiro.tabuleiro[int(self.posXPeca) +
                                1][int(self.posYPeca)].disponivel = True

        # Movimento Rei Sudoeste
        if int(self.posXPeca) + 1 < 7 and int(self.posYPeca) - 1 >= 0:
            if tabuleiro.tabuleiro[int(self.posXPeca)+1][int(self.posYPeca) - 1].conteudo is None:
                tabuleiro.tabuleiro[int(self.posXPeca)+1][int(
                    self.posYPeca) - 1].disponivel = True

        # Movimento Rei Oeste
        if int(self.posYPeca) - 1 >= 0 and tabuleiro.tabuleiro[int(self.posXPeca)][int(self.posYPeca) - 1].conteudo is None:
            tabuleiro.tabuleiro[int(self.posXPeca)][int(
                self.posYPeca) - 1].disponivel = True

        # Movimento Rei Noroeste
        if int(self.posXPeca) - 1 >= 0 and int(self.posYPeca) - 1 >= 0:
            if tabuleiro.tabuleiro[int(self.posXPeca)-1][int(self.posYPeca) - 1].conteudo is None:
                tabuleiro.tabuleiro[int(self.posXPeca)-1][int(
                    self.posYPeca) - 1].disponivel = True

        print('\n? Indica onde a peça pode se mover\n! Indica movimento de captura:\n')
        tabuleiro.imprimirTabuleiro()
        movX, movY = tabuleiro.moverPeca()
        if int(movX) not in range(8) or int(movY) not in range(8):
            raise IntervaloError
        else:
            if tabuleiro.tabuleiro[int(movX)][int(movY)].disponivel:
                tabuleiro.tabuleiro[int(movX)][int(movY)].conteudo = Rei(
                    int(movX), int(movY), self.corDaPeca)
                tabuleiro.tabuleiro[self.posXPeca][self.posYPeca].conteudo = None
                tabuleiro.cancelarEscolha()

class Dama(Peca):
    def __init__(self, posXPeca, posYPeca, corDaPeca):
        Peca.__init__(self, posXPeca, posYPeca, corDaPeca, "Dama")

    def __str__(self):
        return 'D'+self.corDaPeca[0].upper()

    def movimentacao(self, tabuleiro):
        # Movimento Dama sudeste
        for i in range(8):
            if self.posXPeca + i < 7 and self.posYPeca + i < 7:
                if tabuleiro.tabuleiro[int(self.posXPeca) + i + 1][int(self.posYPeca) + i + 1].conteudo is None:
                    tabuleiro.tabuleiro[int(
                        self.posXPeca) + i + 1][int(self.posYPeca) + i + 1].disponivel = True
                else:
                    break

        # Movimento Dama sudoeste
        for i in range(8):
            if self.posXPeca + i < 7 and self.posYPeca - i >= 0:
                if tabuleiro.tabuleiro[int(self.posXPeca) + i + 1][int(self.posYPeca) - i - 1].conteudo is None:
                    tabuleiro.tabuleiro[int(
                        self.posXPeca) + i + 1][int(self.posYPeca) - i - 1].disponivel = True
                else:
                    break

        # Movimento Dama Nordeste
        for i in range(8):
            if self.posXPeca - i >= 0 and self.posYPeca + i < 7:
                if tabuleiro.tabuleiro[int(self.posXPeca) - i - 1][int(self.posYPeca) + i + 1].conteudo is None:
                    tabuleiro.tabuleiro[int(
                        self.posXPeca) - i - 1][int(self.posYPeca) + i + 1].disponivel = True
                else:
                    break

        # Movimento Dama Noroeste
        for i in range(8):
            if self.posXPeca - i >= 0 and self.posYPeca - i >= 0:
                if tabuleiro.tabuleiro[int(self.posXPeca) - i - 1][int(self.posYPeca) - i - 1].conteudo is None:
                    tabuleiro.tabuleiro[int(
                        self.posXPeca) - i - 1][int(self.posYPeca) - i - 1].disponivel = True
                else:
                    break

         # Movimento Dama Sul
        for i in range(8):
            if int(self.posXPeca) + i < 7:
                if tabuleiro.tabuleiro[int(self.posXPeca) + i + 1][self.posYPeca].conteudo is None:
                    tabuleiro.tabuleiro[int(
                        self.posXPeca) + i + 1][self.posYPeca].disponivel = True
                else:
                    break

        # Movimento Dama Norte
        for i in range(8):
            if int(self.posXPeca) - i > 0:
                if tabuleiro.tabuleiro[int(self.posXPeca) - i - 1][self.posYPeca].conteudo is None:
                    tabuleiro.tabuleiro[int(
                        self.posXPeca) - i - 1][self.posYPeca].disponivel = True
                else:
                    break

        # Movimento Dama Esquerda
        for i in range(8):
            if int(self.posYPeca) - i > 0:
                if tabuleiro.tabuleiro[int(self.posXPeca)][self.posYPeca - i - 1].conteudo is None:
                    tabuleiro.tabuleiro[int(
                        self.posXPeca)][self.posYPeca - i - 1].disponivel = True
                else:
                    break

        # Movimento Dama Direita
        for i in range(8):
            if int(self.posYPeca) + i < 7:
                if tabuleiro.tabuleiro[int(self.posXPeca)][self.posYPeca + i + 1].conteudo is None:
                    tabuleiro.tabuleiro[int(
                        self.posXPeca)][self.posYPeca + i + 1].disponivel = True
                else:
                    break

        print('\n? Indica onde a peça pode se mover\n! Indica movimento de captura:\n')
        tabuleiro.imprimirTabuleiro()
        movX, movY = tabuleiro.moverPeca()
        if int(movX) not in range(8) or int(movY) not in range(8):
            raise IntervaloError
        else:
            if tabuleiro.tabuleiro[int(movX)][int(movY)].disponivel:
                tabuleiro.tabuleiro[int(movX)][int(movY)].conteudo = Dama(
                    int(movX), int(movY), self.corDaPeca)
                tabuleiro.tabuleiro[int(movX)][int(
                    movY)].conteudo.primeiroMovimento = False
                tabuleiro.tabuleiro[self.posXPeca][self.posYPeca].conteudo = None
                tabuleiro.cancelarEscolha()

class Bispo(Peca):
    def __init__(self, posXPeca, posYPeca, corDaPeca):
        Peca.__init__(self, posXPeca, posYPeca, corDaPeca, "Bispo")

    def __str__(self):
        return 'B'+self.corDaPeca[0].upper()

    def movimentacao(self, tabuleiro):
        # Movimento Bispo Sudeste
        for i in range(8):
            if self.posXPeca + i < 7 and self.posYPeca + i < 7:
                if tabuleiro.tabuleiro[int(self.posXPeca) + i + 1][int(self.posYPeca) + i + 1].conteudo is None:
                    tabuleiro.tabuleiro[int(
                        self.posXPeca) + i + 1][int(self.posYPeca) + i + 1].disponivel = True
                else:
                    break

        # Movimento Bispo Sudoeste
        for i in range(8):
            if self.posXPeca + i < 7 and self.posYPeca - i >= 0:
                if tabuleiro.tabuleiro[int(self.posXPeca) + i + 1][int(self.posYPeca) - i - 1].conteudo is None:
                    tabuleiro.tabuleiro[int(
                        self.posXPeca) + i + 1][int(self.posYPeca) - i - 1].disponivel = True
                else:
                    break

        # Movimento Bispo Nordeste
        for i in range(8):
            if self.posXPeca - i >= 0 and self.posYPeca + i < 7:
                if tabuleiro.tabuleiro[int(self.posXPeca) - i - 1][int(self.posYPeca) + i + 1].conteudo is None:
                    tabuleiro.tabuleiro[int(
                        self.posXPeca) - i - 1][int(self.posYPeca) + i + 1].disponivel = True
                else:
                    break

        # Movimento Bispo Noroeste
        for i in range(8):
            if self.posXPeca - i >= 0 and self.posYPeca - i >= 0:
                if tabuleiro.tabuleiro[int(self.posXPeca) - i - 1][int(self.posYPeca) - i - 1].conteudo is None:
                    tabuleiro.tabuleiro[int(
                        self.posXPeca) - i - 1][int(self.posYPeca) - i - 1].disponivel = True
                else:
                    break

        print('\n? Indica onde a peça pode se mover\n! Indica movimento de captura:\n')
        tabuleiro.imprimirTabuleiro()
        movX, movY = tabuleiro.moverPeca()
        if int(movX) not in range(8) or int(movY) not in range(8):
            raise IntervaloError
        else:
            if tabuleiro.tabuleiro[int(movX)][int(movY)].disponivel:
                tabuleiro.tabuleiro[int(movX)][int(movY)].conteudo = Bispo(
                    int(movX), int(movY), self.corDaPeca)
                tabuleiro.tabuleiro[int(movX)][int(
                    movY)].conteudo.primeiroMovimento = False
                tabuleiro.tabuleiro[self.posXPeca][self.posYPeca].conteudo = None
                tabuleiro.cancelarEscolha()

class Cavalo(Peca):
    def __init__(self, posXPeca, posYPeca, corDaPeca):
        Peca.__init__(self, posXPeca, posYPeca, corDaPeca, "Cavalo")

    def __str__(self):
        return 'C'+self.corDaPeca[0].upper()

    def movimentacao(self, tabuleiro):
        # Movimento Cavalo
        if int(self.posXPeca) + 2 < 7:
            if int(self.posYPeca) + 1 <= 7:
                if tabuleiro.tabuleiro[int(self.posXPeca)+2][int(self.posYPeca) + 1].conteudo is None:
                    tabuleiro.tabuleiro[int(
                        self.posXPeca)+2][int(self.posYPeca) + 1].disponivel = True
            if int(self.posYPeca) - 1 >= 0:
                if tabuleiro.tabuleiro[int(self.posXPeca)+2][int(self.posYPeca) - 1].conteudo is None:
                    tabuleiro.tabuleiro[int(
                        self.posXPeca)+2][int(self.posYPeca) - 1].disponivel = True

        if int(self.posXPeca) - 2 >= 0:
            if int(self.posYPeca) + 1 <= 7:
                if tabuleiro.tabuleiro[int(self.posXPeca)-2][int(self.posYPeca) + 1].conteudo is None:
                    tabuleiro.tabuleiro[int(
                        self.posXPeca)-2][int(self.posYPeca) + 1].disponivel = True
            if int(self.posYPeca) - 1 >= 0:
                if tabuleiro.tabuleiro[int(self.posXPeca)-2][int(self.posYPeca) - 1].conteudo is None:
                    tabuleiro.tabuleiro[int(
                        self.posXPeca)-2][int(self.posYPeca) - 1].disponivel = True

        if int(self.posYPeca) + 2 < 7:
            if int(self.posXPeca) + 1 <= 7:
                if tabuleiro.tabuleiro[int(self.posXPeca)+1][int(self.posYPeca) + 2].conteudo is None:
                    tabuleiro.tabuleiro[int(
                        self.posXPeca)+1][int(self.posYPeca) + 2].disponivel = True
            if int(self.posXPeca) - 1 >= 0:
                if tabuleiro.tabuleiro[int(self.posXPeca)-1][int(self.posYPeca) + 2].conteudo is None:
                    tabuleiro.tabuleiro[int(
                        self.posXPeca)-1][int(self.posYPeca) + 2].disponivel = True

        if int(self.posYPeca) - 2 >= 0:
            if int(self.posXPeca) + 1 <= 7:
                if tabuleiro.tabuleiro[int(self.posXPeca)+1][int(self.posYPeca) - 2].conteudo is None:
                    tabuleiro.tabuleiro[int(
                        self.posXPeca)+1][int(self.posYPeca) - 2].disponivel = True
            if int(self.posXPeca) - 1 >= 0:
                if tabuleiro.tabuleiro[int(self.posXPeca)-1][int(self.posYPeca) - 2].conteudo is None:
                    tabuleiro.tabuleiro[int(
                        self.posXPeca)-1][int(self.posYPeca) - 2].disponivel = True

        print('\n? Indica onde a peça pode se mover\n! Indica movimento de captura:\n')
        tabuleiro.imprimirTabuleiro()
        movX, movY = tabuleiro.moverPeca()
        if int(movX) not in range(8) or int(movY) not in range(8):
            raise IntervaloError
        else:
            if tabuleiro.tabuleiro[int(movX)][int(movY)].disponivel:
                tabuleiro.tabuleiro[int(movX)][int(movY)].conteudo = Cavalo(
                    int(movX), int(movY), self.corDaPeca)
                tabuleiro.tabuleiro[self.posXPeca][self.posYPeca].conteudo = None
                tabuleiro.cancelarEscolha()

class Torre(Peca):
    def __init__(self, posXPeca, posYPeca, corDaPeca):
        Peca.__init__(self, posXPeca, posYPeca, corDaPeca, "Torre")

    def __str__(self):
        return 'T'+self.corDaPeca[0].upper()

    def movimentacao(self, tabuleiro):
        # Movimento Cavalo Sul
        for i in range(8):
            if int(self.posXPeca) + i < 7:
                if tabuleiro.tabuleiro[int(self.posXPeca) + i + 1][self.posYPeca].conteudo is None:
                    tabuleiro.tabuleiro[int(
                        self.posXPeca) + i + 1][self.posYPeca].disponivel = True
                elif not tabuleiro.tabuleiro[int(self.posXPeca) + i + 1][self.posYPeca].conteudo.corDaPeca != self.corDaPeca:
                    tabuleiro.tabuleiro[int(self.posXPeca) + i + 1][self.posYPeca].capturavel = True
                else:
                    break

        # Movimento Cavalo Norte
        for i in range(8):
            if int(self.posXPeca) - i > 0:
                if tabuleiro.tabuleiro[int(self.posXPeca) - i - 1][self.posYPeca].conteudo is None:
                    tabuleiro.tabuleiro[int(
                        self.posXPeca) - i - 1][self.posYPeca].disponivel = True
                else:
                    break

        # Movimento Cavalo Oeste
        for i in range(8):
            if int(self.posYPeca) - i > 0:
                if tabuleiro.tabuleiro[int(self.posXPeca)][self.posYPeca - i - 1].conteudo is None:
                    tabuleiro.tabuleiro[int(
                        self.posXPeca)][self.posYPeca - i - 1].disponivel = True
                else:
                    break

        # Movimento Cavalo Este
        for i in range(8):
            if int(self.posYPeca) + i < 7:
                if tabuleiro.tabuleiro[int(self.posXPeca)][self.posYPeca + i + 1].conteudo is None:
                    tabuleiro.tabuleiro[int(
                        self.posXPeca)][self.posYPeca + i + 1].disponivel = True
                else:
                    break

        print('\n? Indica onde a peça pode se mover\n! Indica movimento de captura:\n')
        tabuleiro.imprimirTabuleiro()
        movX, movY = tabuleiro.moverPeca()
        if int(movX) not in range(8) or int(movY) not in range(8):
            raise IntervaloError
        else:
            if tabuleiro.tabuleiro[int(movX)][int(movY)].disponivel:
                tabuleiro.tabuleiro[int(movX)][int(movY)].conteudo = Torre(
                    int(movX), int(movY), self.corDaPeca)
                tabuleiro.tabuleiro[self.posXPeca][self.posYPeca].conteudo = None
                tabuleiro.cancelarEscolha()

class Peao(Peca):
    def __init__(self, posXPeca, posYPeca, corDaPeca):
        Peca.__init__(self, posXPeca, posYPeca, corDaPeca, "Peao")
        self.primeiroMovimento = True
        self.direcao = 1 if corDaPeca == 'branca' else -1

    def __str__(self):
        return 'P'+self.corDaPeca[0].upper()

    #### Método de movimento do Peão ###
    def movimentacao(self, tabuleiro):
        if self.primeiroMovimento and tabuleiro.tabuleiro[self.posXPeca + 2*self.direcao][self.posYPeca].conteudo is None:
            tabuleiro.tabuleiro[self.posXPeca + 2 *
                                self.direcao][self.posYPeca].disponivel = True
        if tabuleiro.tabuleiro[self.posXPeca + self.direcao][self.posYPeca].conteudo is None:
            tabuleiro.tabuleiro[self.posXPeca +
                                self.direcao][self.posYPeca].disponivel = True
        try:
            if not tabuleiro.tabuleiro[self.posXPeca + self.direcao][self.posYPeca+self.direcao].conteudo is None and tabuleiro.tabuleiro[self.posXPeca + self.direcao][self.posYPeca+self.direcao].conteudo.corDaPeca != self.corDaPeca:
                tabuleiro.tabuleiro[self.posXPeca + self.direcao][self.posYPeca +
                                                                  self.direcao].capturavel = True
        except:
            print('Peão não possui nenhuma peça para capturar.')
            pass
        try:
            if not tabuleiro.tabuleiro[self.posXPeca + self.direcao][self.posYPeca-self.direcao].conteudo is None and tabuleiro.tabuleiro[self.posXPeca + self.direcao][self.posYPeca-self.direcao].conteudo.corDaPeca != self.corDaPeca:
                tabuleiro.tabuleiro[self.posXPeca + self.direcao][self.posYPeca -
                                                                  self.direcao].capturavel = True
        except:
            print('Peão não possui nenhuma peça para capturar.')
            pass

        print('\n? Indica onde a peça pode se mover\n! Indica movimento de captura:\n')
        tabuleiro.imprimirTabuleiro()
        movX, movY = tabuleiro.moverPeca()
        if int(movX) not in range(8) or int(movY) not in range(8):
            raise IntervaloError
        else:
            if tabuleiro.tabuleiro[int(movX)][int(movY)].disponivel:
                tabuleiro.tabuleiro[int(movX)][int(movY)].conteudo = Peao(
                    int(movX), int(movY), self.corDaPeca)
                tabuleiro.tabuleiro[int(movX)][int(
                    movY)].conteudo.primeiroMovimento = False
                tabuleiro.tabuleiro[self.posXPeca][self.posYPeca].conteudo = None
                tabuleiro.cancelarEscolha()


class Posicao:
    def __init__(self, x, y, conteudo=None):
        self.conteudo = conteudo
        self.x = x
        self.y = y
        self.selecionada = False
        self.disponivel = False
        self.capturavel = False


###### Definição do tabuleiro do jogo #####
class Tabuleiro:
    def __init__(self):
        self.tabuleiro = []
        self.iniciaTabuleiro()

    def iniciaTabuleiro(self):
        for i in range(8):
            self.tabuleiro.append([])
            for j in range(8):
                self.tabuleiro[i].append(Posicao(i, j))
                if i == 7:
                    if j == 0 or j == 7:
                        self.tabuleiro[i][j].conteudo = Torre(i, j, "branca")
                    elif j == 1 or j == 6:
                        self.tabuleiro[i][j].conteudo = Cavalo(i, j, "branca")
                    elif j == 2 or j == 5:
                        self.tabuleiro[i][j].conteudo = Bispo(i, j, "branca")
                    elif j == 3:
                        self.tabuleiro[i][j].conteudo = Dama(i, j, "branca")
                    elif j == 4:
                        self.tabuleiro[i][j].conteudo = Rei(i, j, "branca")
                elif i == 6:
                    self.tabuleiro[i][j].conteudo = Peao(i, j, "branca")
                elif i == 1:
                    self.tabuleiro[i][j].conteudo = Peao(i, j, "preta")
                elif i == 0:
                    if j == 0 or j == 7:
                        self.tabuleiro[i][j].conteudo = Torre(i, j, "preta")
                    elif j == 1 or j == 6:
                        self.tabuleiro[i][j].conteudo = Cavalo(i, j, "preta")
                    elif j == 2 or j == 5:
                        self.tabuleiro[i][j].conteudo = Bispo(i, j, "preta")
                    elif j == 3:
                        self.tabuleiro[i][j].conteudo = Dama(i, j, "preta")
                    elif j == 4:
                        self.tabuleiro[i][j].conteudo = Rei(i, j, "preta")

    def imprimirTabuleiro(self):
        print('Tabuleiro: \n')
        for linha in self.tabuleiro:
            for posicao in linha:
                if posicao.conteudo is None:
                    if posicao.disponivel:
                        print(' ?? ', end='')
                    else:
                        print(' ** ', end='')
                elif posicao.selecionada:
                    print('[' + str(posicao.conteudo) + ']', end='')
                elif posicao.capturavel:
                        print(' !! ', end='')
                else:
                    print(' ' + str(posicao.conteudo) + ' ', end='')
            print()
        print('\n')

    def escolherPeca(self):
        posX, posY = input("Selecione uma posicao: ").split(',')
        
        self.tabuleiro[int(posX)][int(posY)].selecionada = True

        decisao = int(input('1 - Mover peça\n2 - Cancelar seleção\n'))

        if decisao == 1:
            self.tabuleiro[int(posX)][int(posY)].conteudo.movimentacao(self)
        else:
            self.cancelarEscolha()
        

    def cancelarEscolha(self):
        for i in range(8):
            for j in range(8):
                self.tabuleiro[i][j].selecionada = False
                self.tabuleiro[i][j].disponivel = False

    def moverPeca(self):
        return input("Selecione o destino: ").split(',')
        
    def salvarTabuleiro(self):
        jogo = open('jogo-tabuleiro.tb', 'wb')
        np.save(jogo, self.tabuleiro)
        jogo.close()
        print('\n Jogo Salvo!')

    def carregarTabuleiro(self):
        try:
            jogo = open('jogo-tabuleiro.tb', 'rb')
            self.tabuleiro = np.load(jogo, allow_pickle=True)
        except FileNotFoundError:
            print('Verifique se existe arquivo de jogo e tente novamente.')
        finally:
            jogo.close()

    def gerarEstatisticas(self):
        pass


def main():
   jogo = Tabuleiro()
   jogo.imprimirTabuleiro()

   ''' script captura peão'''
   jogo.escolherPeca()
   



if __name__ == "__main__":
   main()
