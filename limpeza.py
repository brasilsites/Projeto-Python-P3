import os
import sys

class LimpaTela():
    def __init__(self,so=sys.platform):
        so_clear=''
        if (so == 'linux'):
            so_clear = 'clear'
        elif (so[:3] == 'win'):
            so_clear = 'cls'

        if so_clear:
            limpar = lambda l: os.system(l)
        else:
            limpar = lambda l: l
        limpar(so_clear)

def voltar():
    input(' pressione qualquer tecla para voltar:')
    LimpaTela()

