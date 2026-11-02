import matplotlib.pyplot as plt
import numpy as np
import nucleo

#nucleo.T = 1.5
#nucleo.J = 1

# criando rede 
rede_inicial = nucleo.criaRedeSpins()


# Fazemos uma cópia exata para evoluir no "Depois"
rede_final = rede_inicial.copy()


# Executa os 300 sweeps na rede final
numero_sweeps = 300
for _ in range(numero_sweeps):
  nucleo.sweep(rede_final)


# Antes VS Depois
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 5))


# Configuração visual comum para retirar os eixos numéricos
for ax in (ax1, ax2):
  ax.tick_params(
      left=False, bottom=False, labelleft=False, labelbottom=False
  )


# G1
im1 = ax1.imshow(rede_inicial, cmap="Spectral")
ax1.set_title("Configuração inicial (aleatória)", fontsize=12)

# G2 
im2 = ax2.imshow(rede_final, cmap="Spectral")
ax2.set_title(f"Depois de {numero_sweeps} sweeps (T = {nucleo.T})", fontsize=12)


#Titulo
fig.suptitle(
    f"Modelo de Ising {nucleo.L}x{nucleo.L} — J = {nucleo.J}, T = {nucleo.T}",
    fontsize=14,
    fontweight="bold",
)

plt.tight_layout()
plt.show()