# Módulo `RetaR3`

`RetaR3` representa retas no espaço tridimensional e fornece equações,
verificações de pertencimento, relações entre retas, distâncias e ângulos.
O módulo está em `backend/reta_r3.py` e usa `Vetor` e a classe-base `Reta`.

## Construção

O construtor segue o contrato do projeto e recebe dois pontos distintos:

```python
from backend.reta_r3 import RetaR3
from backend.vetor import Vetor

reta = RetaR3(Vetor((1, 2, 3)), Vetor((3, 2, 7)))
```

O vetor diretor é calculado como `ponto_final - ponto_inicial`. Para informar
diretamente um vetor diretor, use `RetaR3.por_ponto_e_direcao(ponto, direcao)`.
`RetaR3.por_dois_pontos(a, b)` é uma alternativa nomeada ao construtor.
Os pontos e direções devem ser objetos `Vetor` tridimensionais, e o vetor
diretor não pode ser nulo.

## Equações

Para ponto inicial `P₀ = (x₀, y₀, z₀)` e direção `v = (a, b, c)`, a reta é
`P(t) = P₀ + t·v`, com `t ∈ ℝ`.

- `equacao_vetorial()` retorna a representação vetorial herdada de `Reta`.
- `equacao_parametrica()` retorna as três coordenadas em função de `t`.
- `equacao_simetrica()` retorna as razões `(x - x₀)/a = (y - y₀)/b = (z - z₀)/c`.
  Uma coordenada cujo componente diretor seja zero é apresentada como igualdade
  fixa. Exemplo: para ponto `(1, 2, 3)` e direção `(2, 0, 4)`, retorna
  `(x - 1)/2 = (z - 3)/4, y = 2`.

## Pertencimento e operações com pontos

- `obter_ponto(t)` (herdado) retorna um `Vetor` em `P₀ + t·v`.
- `ponto_pertence(ponto, tolerancia=1e-9)` (herdado) retorna `bool`.
- `distancia_ponto(ponto)` retorna `float`, calculado por
  `|AP × v| / |v|`.

## Operações entre retas

Os métodos que recebem outra reta exigem um objeto `RetaR3`.

- `eh_paralela(outra, tolerancia=1e-9)` e
  `eh_ortogonal(outra, tolerancia=1e-9)` retornam `bool`.
- `angulo_com(outra)` retorna o menor ângulo entre as direções, em graus,
  entre `0°` e `90°`.
- `posicao_relativa(outra, tolerancia=1e-9)` retorna `coincidentes`,
  `paralelas`, `concorrentes` ou `reversas`.
- `distancia_reta(outra, tolerancia=1e-9)` retorna `float`; para retas não
  paralelas usa `|w · (u × v)| / |u × v|`, e para paralelas usa a distância
  ponto-reta.
- `ponto_intersecao(outra, tolerancia=1e-9)` retorna um `Vetor` para retas
  concorrentes e `None` quando não há uma interseção única.

Retas coincidentes têm direções proporcionais e ponto inicial compartilhado;
retas paralelas são distintas com direções proporcionais. Retas não paralelas
são concorrentes quando coplanares e reversas quando não são coplanares.

### Exemplo de uso e saídas

```python
reta = RetaR3(Vetor((1, 2, 3)), Vetor((3, 2, 7)))
outra = RetaR3.por_ponto_e_direcao(Vetor((3, 2, 7)), Vetor((-2, 0, -4)))

reta.equacao_vetorial()
# '(x, y, z) = (1, 2, 3) + t(2, 0, 4)'
reta.equacao_parametrica()
# 'x = 1 + 2t\ny = 2 + 0t\nz = 3 + 4t'
reta.equacao_simetrica()
# '(x - 1)/2 = (z - 3)/4, y = 2'
reta.obter_ponto(0.5).coordenadas
# (2.0, 2.0, 5.0)
reta.ponto_pertence(Vetor((2, 2, 5)))
# True
reta.distancia_ponto(Vetor((1, 2, 5)))
# 0.8944271909999159
reta.eh_paralela(outra)
# True
reta.eh_ortogonal(outra)
# False
reta.angulo_com(outra)
# 0.0
reta.posicao_relativa(outra)
# 'coincidentes'
reta.distancia_reta(outra)
# 0.0
reta.ponto_intersecao(outra)
# None (não há uma interseção única)
```

Para duas retas concorrentes, `ponto_intersecao()` retorna o ponto comum como
`Vetor`; por exemplo, as retas `((0, 0, 0), (1, 1, 0))` e
`((2, 0, 0), (-1, 1, 0))` se intersectam em `(1, 1, 0)`.

## Validação e tolerância

O valor padrão das verificações geométricas é `1e-9`. Métodos com tolerância
rejeitam `bool`, valores não reais, valores não finitos e valores negativos.
Dimensões incompatíveis geram `ValueError`; tipos de objeto incompatíveis
geram `TypeError`. Coordenadas seguem as validações de `Vetor`.

## Verificação

Execute a suíte dedicada a partir da raiz do projeto:

```powershell
python -m unittest tests.test_reta_r3 -v
```

Para ver exemplos das quatro posições relativas, equações, pertencimento,
distância e ângulo no terminal:

```powershell
python teste_interativo_r3.py
```
