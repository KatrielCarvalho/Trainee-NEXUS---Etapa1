import matplotlib.pyplot as plt
import numpy as np
import nucleo
print("Iniciando a simulação do Modelo de Ising...")
#Se quiser testar outras temperaturas sem mexer no nucleo.py, descomente abaixo:
#nucleo.T = 1.5
#nucleo.J = 1

print(f"Temperatura atual (T): {nucleo.T}")
print("Gerando a rede inicial aleatória...")
# criando rede 
rede_inicial = nucleo.criaRedeSpins()


# Fazemos uma cópia exata para evoluir no "Depois"

rede_final = rede_inicial.copy()


# Executa os 300 sweeps na rede final
numero_sweeps = 300
print(f"Rodando {numero_sweeps} sweeps com o algoritmo de Metropolis. Aguarde...")
for _ in range(numero_sweeps):
  nucleo.sweep(rede_final)
  
print("Cálculos concluídos! Montando a visualização...")

# Antes VS Depois. Cria uma figura com 2 gráficos lado a lado (1 linha, 2 colunas)
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 5))

#removendo os números das bordas
# Configuração visual
for ax in (ax1, ax2):
  ax.tick_params(
      left=False, bottom=False, labelleft=False, labelbottom=False
  )


# G1 vmin e vmax garantem que as cores não "buguem" se a rede ficar toda de uma cor só
im1 = ax1.imshow(rede_inicial, cmap="Spectral", vmin=-1, vmax=1)
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
#Ajusta os espaços para os textos não ficarem sobrepostos
plt.tight_layout()

print("Pronto! Exibindo o gráfico na tela.")
plt.show()
