#JOGO PEDRA,PAPEL E TESOURA
import random
from random import randint
class jogo():

    def jogar(self,escolha):
        itens = ['pedra', 'papel', 'tesoura']
        computador = random.choice(itens)

        if escolha == computador:
            return 'Empate!!! Você escolheu:' + escolha + ' e o computador escolheu: ' + computador

        elif (escolha == 'papel' and computador =='pedra') or\
             (escolha == 'tesoura' and computador == 'papel') or\
             (escolha == 'pedra' and computador == 'tesoura'):
             return 'Você venceu!!! Você escolheu:' + escolha + ' e o computador escolheu: ' + computador

        else:
            return 'Você perdeu!!! Você escolheu:' + escolha + ' e o computador escolheu: ' + computador
