import numpy as np

# >PARÂMETROS
J: float = 1
h: float = 0
T: float = 2.0

# *TAMANHO
L: int = 30
L2: int = L*L


def criaRedeSpins() -> list[list[int]]:
    redeSpins = np.random.randint(0, 2, size=(L, L)) * 2 - 1
    return redeSpins


def probabilidadeInverte(redeSpins: list[list[int]]) -> None:
    si = np.random.randint(0, L2)
    somj = 0

    somj += redeSpins.flat[(si + 1) % L2]
    somj += redeSpins.flat[(si - 1) % L2]
    somj += redeSpins.flat[(si + L) % L2]
    somj += redeSpins.flat[(si - L) % L2]

    deltE = (2 * J * redeSpins.flat[si] * somj) + (2 * h * redeSpins.flat[si])
    P = min(1, np.exp(-deltE/T))

    if np.random.uniform(0.0, 1.0) <= P:
        redeSpins.flat[si] *= -1


def sweep(redeSpins: list[list[int]]) -> None:

    for i in range(L2):
        probabilidadeInverte(redeSpins)
