"""Demonstração manual das operações da classe RetaR3.

Execute na raiz do projeto com ``python teste_interativo_r3.py``.
"""

from backend.reta_r3 import RetaR3
from backend.vetor import Vetor


def reta(ponto, direcao):
    return RetaR3.por_ponto_e_direcao(Vetor(ponto), Vetor(direcao))


def descrever_par(nome, primeira, segunda):
    print(f"\n{nome}")
    print(f"  posição: {primeira.posicao_relativa(segunda)}")
    print(f"  ângulo: {primeira.angulo_com(segunda):.6g}°")
    print(f"  distância: {primeira.distancia_reta(segunda):.6g}")
    intersecao = primeira.ponto_intersecao(segunda)
    descricao_intersecao = (
        intersecao.coordenadas if intersecao is not None else "sem ponto único"
    )
    print(f"  interseção única: {descricao_intersecao}")


def demonstrar():
    print("=== Demonstração de retas no R³ ===")

    r = RetaR3(Vetor((1, 2, 3)), Vetor((3, 2, 7)))
    print("\nReta principal (construída por dois pontos):")
    print(f"  vetorial: {r.equacao_vetorial()}")
    print(f"  paramétrica:\n{r.equacao_parametrica()}")
    print(f"  simétrica: {r.equacao_simetrica()}")
    print(f"  ponto (2, 2, 5) pertence: {r.ponto_pertence(Vetor((2, 2, 5)))}")
    print(f"  distância de (1, 2, 5): {r.distancia_ponto(Vetor((1, 2, 5))):.6g}")

    descrever_par("Retas coincidentes", r, reta((3, 2, 7), (-2, 0, -4)))
    descrever_par("Retas paralelas distintas", reta((0, 0, 0), (0, 0, 1)), reta((3, 4, 0), (0, 0, 2)))
    descrever_par("Retas concorrentes", reta((0, 0, 0), (1, 1, 0)), reta((2, 0, 0), (-1, 1, 0)))
    descrever_par("Retas reversas", reta((0, 0, 0), (1, 0, 0)), reta((0, 0, 1), (0, 1, 0)))


if __name__ == "__main__":
    demonstrar()
