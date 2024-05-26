#jogo da velha
class Jogo:
    def __init__(self):
        self.tabuleiro = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
        self.jogador1 = "X"
        self.jogador2 = "O"

    def printTabuleiro(self):
        print(f"{self.tabuleiro[0]}|{self.tabuleiro[1]}|{self.tabuleiro[2]}\n"
              f"{self.tabuleiro[3]}|{self.tabuleiro[4]}|{self.tabuleiro[5]}\n"
              f"{self.tabuleiro[6]}|{self.tabuleiro[7]}|{self.tabuleiro[8]}")

    def jogar(self):
        for i in range(9):
            if i % 2 == 0:
                jogador = self.jogador1
            else:
                jogador = self.jogador2

            jogada = int(input(f"Jogador {jogador} - Escolha a casa que deseja jogar, com base no teclado numérico: ")) - 1
            if self.tabuleiro[jogada] == " ":
                self.tabuleiro[jogada] = jogador
                self.printTabuleiro()
            else:
                while self.tabuleiro[jogada] != " ":
                    jogada=int(input("Escolha outra casa, esta ja esta ocupada")) -1
                self.tabuleiro[jogada] = jogador
                self.printTabuleiro()


            if ((self.tabuleiro[0] == self.tabuleiro[1] == self.tabuleiro[2] == jogador) or
                    (self.tabuleiro[3] == self.tabuleiro[4] == self.tabuleiro[5] == jogador) or
                    (self.tabuleiro[6] == self.tabuleiro[7] == self.tabuleiro[8] == jogador) or
                    (self.tabuleiro[0] == self.tabuleiro[3] == self.tabuleiro[6] == jogador) or
                    (self.tabuleiro[1] == self.tabuleiro[4] == self.tabuleiro[7] == jogador) or
                    (self.tabuleiro[2] == self.tabuleiro[5] == self.tabuleiro[8] == jogador) or
                    (self.tabuleiro[0] == self.tabuleiro[4] == self.tabuleiro[8] == jogador) or
                    (self.tabuleiro[2] == self.tabuleiro[4] == self.tabuleiro[6] == jogador)):
                print(f"Jogador {jogador} Venceu!")
                break
        else:
            print("Empate!")

jogo = Jogo()
jogo.printTabuleiro()
jogo.jogar()
