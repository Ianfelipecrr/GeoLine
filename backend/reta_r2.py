import backend.reta as Reta

class RetaR2(Reta):

    __slots__ = ("_ponto_inicial", "_ponto_final")

    def __init__(self, ponto_inicial, ponto_final):
        self.ponto_inicial = ponto_inicial
        self.ponto_final = ponto_final

    @Reta.ponto_inicial.setter
    def ponto_inicial(self, ponto_inicial):
        try:
            ponto_inicial = float(ponto_inicial)
            self._ponto_inicial = ponto_inicial

        except ValueError:
            raise("O ponto inicial deve ser um número real.")

    @property
    def ponto_final(self):
        return self._ponto_final

    @ponto_final.setter
    def ponto_final(self, ponto_final):
        try:
            x_final, y_final = ponto_final
            x_final = float(x_final)
            y_final = float(y_final)

            if len(ponto_final) == 2:
                self._ponto_final = (x_final, y_final)

            else:
                raise("O ponto deve ter uma coordenada X e uma coordenada Y.")

        except ValueError:
            raise("O ponto inicial deve ser um número real.")
        
    @property
    def vetor_diretor(self):
        return self._ponto_final - self._ponto_inicial

    def equacao_reduzida(self):
        x_inicial, y_inicial = self.ponto_inicial
        
        x_final, y_final = self.ponto_final
        
        #m = 

    def equacao_simetrica(self):
        pass
    
