class RetaR3(Reta):
    """
    Representa uma reta no R³ e analisa suas relações geométricas
    com pontos e com outras retas.

    A reta é definida por um ponto pertencente a ela (ponto inicial)
    e por um vetor diretor não nulo, ambos com três coordenadas.
    Seus pontos são dados por P(t) = P₀ + t·v, com t real.

    CRITÉRIOS DE CLASSIFICAÇÃO (posicao_relativa):

    - Coincidentes: os vetores diretores são proporcionais e o ponto
      inicial de uma das retas pertence à outra. As retas possuem
      infinitos pontos em comum.
    - Paralelas: os vetores diretores são proporcionais, mas as retas
      são distintas, sem pontos em comum.
    - Concorrentes: os vetores diretores não são proporcionais e as
      retas são coplanares, ou seja, o produto misto entre o vetor
      que liga os pontos iniciais e os dois vetores diretores é zero.
      As retas possuem um único ponto em comum.
    - Reversas: os vetores diretores não são proporcionais e as retas
      não são coplanares (produto misto diferente de zero). Não há
      ponto de interseção e a distância entre elas é positiva.

    PERTENCIMENTO DE PONTO:
    Um ponto pertence à reta quando o vetor que liga o ponto inicial
    ao ponto analisado é proporcional ao vetor diretor, considerando
    a tolerância (método herdado de Reta).

    DISTÂNCIAS:
    - Ponto à reta: |AP × v| / |v|, em que A é o ponto inicial, P é o
      ponto analisado e v é o vetor diretor.
    - Reta à reta: |w · (u × v)| / |u × v| para retas não paralelas,
      em que w liga os pontos iniciais e u, v são os vetores diretores.
      Para retas paralelas, é a distância de um ponto de uma à outra.

    ÂNGULO ENTRE RETAS:
    É o menor ângulo entre as direções das retas, de 0° a 90°,
    calculado por cos θ = |u · v| / (|u|·|v|). Retas ortogonais
    têm u · v = 0.

    EXEMPLOS:

    Ponto 1 = (0, 0, 0), direção 1 = (1, 0, 0)
    Ponto 2 = (0, 1, 0), direção 2 = (0, 1, 0)
    Resultado: retas concorrentes, interseção em (0, 0, 0).

    Ponto 1 = (0, 0, 0), direção 1 = (1, 0, 0)
    Ponto 2 = (0, 1, 1), direção 2 = (0, 1, 0)
    Resultado: retas reversas, a distância entre elas é 1.

    Ponto 1 = (0, 0, 0), direção 1 = (1, 1, 1)
    Ponto 2 = (1, 0, 0), direção 2 = (2, 2, 2)
    Resultado: retas paralelas, a distância entre elas é √(2/3) ≈ 0.8165.

    Ponto = (1, 2, 3), direção = (2, 0, 4)
    Equação simétrica: (x - 1)/2 = (z - 3)/4, y = 2
    (componentes nulas do vetor diretor viram igualdades separadas).

    As verificações geométricas usam tolerância numérica relativa de
    1e-9 por padrão, para lidar com aproximações de ponto flutuante.
    """
from math import acos, degrees, isfinite, sqrt
from numbers import Real

from backend.reta import Reta
from backend.vetor import Vetor


def _produto_escalar(a, b):
    return sum(x * y for x, y in zip(a, b))


def _produto_vetorial(a, b):
    return (
        a[1] * b[2] - a[2] * b[1],
        a[2] * b[0] - a[0] * b[2],
        a[0] * b[1] - a[1] * b[0],
    )


def _norma(a):
    return sqrt(_produto_escalar(a, a))


class RetaR3(Reta):
    """Representa uma reta no R³ por um ponto e um vetor diretor."""
    __slots__ = ()

    def __init__(self, ponto_inicial, vetor_diretor):
        super().__init__(ponto_inicial, vetor_diretor)
        if self.dimensao != 3:
            raise ValueError("RetaR3 exige ponto e vetor diretor com dimensão 3.")

    # ------------------------------------------------------------------
    # Construção alternativa
    # ------------------------------------------------------------------
    @classmethod
    def por_dois_pontos(cls, ponto_a, ponto_b):
        """Cria a reta que passa por dois pontos distintos do R³."""
        if not isinstance(ponto_a, Vetor) or not isinstance(ponto_b, Vetor):
            raise TypeError("Os pontos devem ser objetos Vetor.")
        if ponto_a.dimensao != ponto_b.dimensao:
            raise ValueError("Os pontos devem ter a mesma dimensão.")
        return cls(ponto_a, ponto_b.subtrair(ponto_a))

    # ------------------------------------------------------------------
    # Validações internas
    # ------------------------------------------------------------------
    @staticmethod
    def _validar_tolerancia(tolerancia):
        if isinstance(tolerancia, bool) or not isinstance(tolerancia, Real):
            raise TypeError("A tolerância deve ser um número real não negativo.")
        if not isfinite(tolerancia) or tolerancia < 0:
            raise ValueError("A tolerância deve ser finita e não negativa.")

    @staticmethod
    def _validar_reta(outra):
        if not isinstance(outra, RetaR3):
            raise TypeError("O argumento deve ser um objeto RetaR3.")

    # ------------------------------------------------------------------
    # Equações
    # ------------------------------------------------------------------
    def equacao_simetrica(self):
        """Retorna a equação simétrica; componentes nulas viram igualdades."""
        simbolos = ("x", "y", "z")
        fracoes = []
        fixas = []
        for simbolo, p, d in zip(
            simbolos, self.ponto_inicial.coordenadas, self.vetor_diretor.coordenadas
        ):
            if d == 0:
                fixas.append(f"{simbolo} = {p}")
            else:
                fracoes.append(f"({simbolo} - {p})/{d}")
        texto = " = ".join(fracoes)
        if fixas:
            texto += ", " + ", ".join(fixas)
        return texto

    # ------------------------------------------------------------------
    # Relações com pontos
    # ------------------------------------------------------------------
    def distancia_ponto(self, ponto):
        """Distância de um ponto do R³ à reta: |AP × v| / |v|."""
        if not isinstance(ponto, Vetor):
            raise TypeError("ponto deve ser um objeto Vetor.")
        if ponto.dimensao != 3:
            raise ValueError("O ponto deve ter dimensão 3.")
        ap = ponto.subtrair(self.ponto_inicial).coordenadas
        v = self.vetor_diretor.coordenadas
        return _norma(_produto_vetorial(ap, v)) / _norma(v)

    # ------------------------------------------------------------------
    # Relações entre retas
    # ------------------------------------------------------------------
    def eh_paralela(self, outra, tolerancia=1e-9):
        """Indica se os vetores diretores são paralelos (inclui coincidentes)."""
        self._validar_reta(outra)
        self._validar_tolerancia(tolerancia)
        u = self.vetor_diretor.coordenadas
        v = outra.vetor_diretor.coordenadas
        return _norma(_produto_vetorial(u, v)) <= tolerancia * _norma(u) * _norma(v)

    def eh_ortogonal(self, outra, tolerancia=1e-9):
        """Indica se os vetores diretores são ortogonais."""
        self._validar_reta(outra)
        self._validar_tolerancia(tolerancia)
        u = self.vetor_diretor.coordenadas
        v = outra.vetor_diretor.coordenadas
        return abs(_produto_escalar(u, v)) <= tolerancia * _norma(u) * _norma(v)

    def angulo_com(self, outra):
        """Menor ângulo (em graus, entre 0° e 90°) entre duas retas."""
        self._validar_reta(outra)
        u = self.vetor_diretor.coordenadas
        v = outra.vetor_diretor.coordenadas
        cosseno = abs(_produto_escalar(u, v)) / (_norma(u) * _norma(v))
        return degrees(acos(min(1.0, cosseno)))

    def posicao_relativa(self, outra, tolerancia=1e-9):
        """Retorna 'coincidentes', 'paralelas', 'concorrentes' ou 'reversas'."""
        self._validar_reta(outra)
        self._validar_tolerancia(tolerancia)

        if self.eh_paralela(outra, tolerancia):
            if self.ponto_pertence(outra.ponto_inicial, tolerancia):
                return "coincidentes"
            return "paralelas"

        u = self.vetor_diretor.coordenadas
        v = outra.vetor_diretor.coordenadas
        w = outra.ponto_inicial.subtrair(self.ponto_inicial).coordenadas
        normal = _produto_vetorial(u, v)
        misto = abs(_produto_escalar(w, normal))
        if misto <= tolerancia * max(1.0, _norma(w) * _norma(normal)):
            return "concorrentes"
        return "reversas"

    def distancia_reta(self, outra, tolerancia=1e-9):
        """Distância entre duas retas (0 se concorrentes ou coincidentes)."""
        self._validar_reta(outra)
        if self.eh_paralela(outra, tolerancia):
            return self.distancia_ponto(outra.ponto_inicial)
        u = self.vetor_diretor.coordenadas
        v = outra.vetor_diretor.coordenadas
        w = outra.ponto_inicial.subtrair(self.ponto_inicial).coordenadas
        normal = _produto_vetorial(u, v)
        return abs(_produto_escalar(w, normal)) / _norma(normal)

    def ponto_intersecao(self, outra, tolerancia=1e-9):
        """Retorna o ponto de interseção (Vetor) se as retas forem concorrentes.

        Retorna None quando não há um único ponto em comum
        (paralelas, coincidentes ou reversas).
        """
        if self.posicao_relativa(outra, tolerancia) != "concorrentes":
            return None
        u = self.vetor_diretor.coordenadas
        v = outra.vetor_diretor.coordenadas
        w = outra.ponto_inicial.subtrair(self.ponto_inicial).coordenadas
        normal = _produto_vetorial(u, v)
        # P1 + t·u = P2 + s·v  =>  t = ((P2 - P1) × v) · (u × v) / |u × v|²
        t = _produto_escalar(_produto_vetorial(w, v), normal) / _produto_escalar(normal, normal)
        return self.obter_ponto(t)

    def __repr__(self):
        return f"RetaR3({self.ponto_inicial!r}, {self.vetor_diretor!r})"