import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import nucleo

# PARÂMETROS
redeSpins: list[list[int]] = nucleo.criaRedeSpins()


# FUNÇÕES
def update(frame):
    axes.set_title(
            f" (Ising = {nucleo.L}x{nucleo.L} — T = {nucleo.T}) Sweep: {frame+1}",
            fontsize=20
    )
    nucleo.sweep(redeSpins)  # Atualiza a redeSpins por 1 sweep
    img.set_data(redeSpins)  # Atualiza o heatmap com o novo redeSpins
    return img,


# PLOT
fig, axes = plt.subplots()

img = axes.imshow(redeSpins, cmap="Spectral")

axes.tick_params(
        left=False,
        bottom=False,
        labelleft=False,
        labelbottom=False
)


# ANIMAÇÃO
anim = FuncAnimation(
                fig=fig,
                func=update,
                frames=300,
                interval=100,
                repeat=False,
                cache_frame_data=False,
                )

# VISUALIZAÇÃO
plt.show()
anim.save(
        filename=f"Animacoes/L{nucleo.L}_T{nucleo.T}.mp4",
        writer="ffmpeg",
        fps=10
)
