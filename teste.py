import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.animation import FuncAnimation

def plot_3d_vectors(ax, velocity, magnetic, force, trajectory, particle_pos=None):
    """
    Atualiza o gráfico 3D com os vetores de velocidade, campo magnético, força e trajetória.
    """
    ax.clear()

    # Plotando vetor de velocidade
    ax.quiver(0, 0, 0, *velocity, color='r', label="v (Velocidade)")
    ax.text(*velocity, "v", color='r')

    # Plotando vetor de campo magnético
    ax.quiver(0, 0, 0, *magnetic, color='b', label="B (Campo Magnético)")
    ax.text(*magnetic, "B", color='b')

    # Plotando vetor de força
    ax.quiver(0, 0, 0, *force, color='g', label="F (Força de Lorentz)")
    ax.text(*force, "F", color='g')

    # Trajetória da partícula
    if trajectory is not None:
        ax.plot3D(trajectory[:, 0], trajectory[:, 1], trajectory[:, 2], color='m', label="Trajetória")

    # Bolinha representando a partícula
    if particle_pos is not None:
        ax.scatter(*particle_pos, color='k', s=50, label="Partícula")

    # Configurando limites e legendas
    max_range = max(abs(np.array([*velocity, *magnetic, *force]).flatten()))
    ax.set_xlim([-max_range, max_range])
    ax.set_ylim([-max_range, max_range])
    ax.set_zlim([-max_range, max_range])

    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    ax.legend()

def calculate_force(q, v, B):
    """
    Calcula a força de Lorentz dada a carga q, vetor velocidade v e vetor campo magnético B.
    """
    return q * np.cross(v, B)

def calculate_trajectory(q, v0, B, t_max=10, dt=0.01, m=1):
    """
    Simula a trajetória de uma partícula carregada em um campo magnético.

    :param q: Carga da partícula.
    :param v0: Velocidade inicial (vetor 3D).
    :param B: Campo magnético (vetor 3D).
    :param t_max: Tempo total de simulação.
    :param dt: Incremento de tempo.
    :param m: Massa da partícula (assumida como 1 por padrão).
    :return: Array Nx3 com as posições ao longo do tempo.
    """
    num_steps = int(t_max / dt)
    trajectory = np.zeros((num_steps, 3))
    velocity = np.array(v0, dtype=np.float64)
    position = np.array([0.0, 0.0, 0.0], dtype=np.float64)  # Posição inicial na origem

    for i in range(num_steps):
        # Calcula a força de Lorentz
        force = q * np.cross(velocity, B)
        # Atualiza a velocidade (F = ma, então a = F/m)
        acceleration = force / m
        velocity += acceleration * dt
        # Atualiza a posição
        position += velocity * dt
        trajectory[i] = position

    return trajectory

def main():
    def update():
        try:
            nonlocal trajectory, anim, v, B, F
            q = float(charge.get())
            vx, vy, vz = float(vx_var.get()), float(vy_var.get()), float(vz_var.get())
            bx, by, bz = float(bx_var.get()), float(by_var.get()), float(bz_var.get())

            v = np.array([vx, vy, vz])
            B = np.array([bx, by, bz])
            F = calculate_force(q, v, B)

            trajectory = calculate_trajectory(q, v, B)
            if anim:
                anim.event_source.stop()
            anim = FuncAnimation(fig, animate, frames=len(trajectory), interval=50, repeat=False)
            canvas.draw()

            # Atualizando o rótulo com o valor da força resultante
            result_label.config(text=f"Força Resultante: ({F[0]:.2f}, {F[1]:.2f}, {F[2]:.2f})")
        except ValueError:
            result_label.config(text="Erro: Insira valores válidos.")

    def animate(frame):
        if trajectory is not None:
            pos = trajectory[frame]
            plot_3d_vectors(ax, v, B, F, trajectory, particle_pos=pos)

    def on_closing():
        if anim:
            anim.event_source.stop()
        root.quit()

    root = tk.Tk()
    root.title("Força de Lorentz")
    root.geometry("1024x728")  # Definindo um tamanho inicial
    root.resizable(True, True)  # Permitindo redimensionamento

    # Adicionando manipulador de evento para fechar a janela
    root.protocol("WM_DELETE_WINDOW", on_closing)

    # Frame principal
    main_frame = tk.Frame(root)
    main_frame.pack(fill=tk.BOTH, expand=True)

    # Label "Força de Lorentz"
    title_label = tk.Label(main_frame, text="Força de Lorentz", font=("Arial", 16))
    title_label.pack(pady=10)

    # Frame para a plotagem e a fórmula
    plot_frame = tk.Frame(main_frame)
    plot_frame.pack(fill=tk.BOTH, expand=True)

    fig = plt.figure(figsize=(6, 6))
    ax = fig.add_subplot(111, projection='3d')

    canvas = FigureCanvasTkAgg(fig, master=plot_frame)
    canvas.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

    # Label com a fórmula da Força de Lorentz
    formula_label = tk.Label(plot_frame, text="F = q * (v x B)", font=("Arial", 14))
    formula_label.pack(side=tk.LEFT, padx=20)

    # Frame para os controles
    control_frame = tk.Frame(main_frame)
    control_frame.pack(fill=tk.X, pady=10)

    tk.Label(control_frame, text="Carga (q):", font=("Arial", 12)).grid(row=0, column=0, padx=5)
    charge = tk.Entry(control_frame, width=10, font=("Arial", 12))
    charge.grid(row=0, column=1, padx=5)

    tk.Label(control_frame, text="Velocidade (v):", font=("Arial", 12)).grid(row=1, column=0, padx=5)
    vx_var, vy_var, vz_var = tk.StringVar(), tk.StringVar(), tk.StringVar()
    tk.Entry(control_frame, textvariable=vx_var, width=10, font=("Arial", 12)).grid(row=1, column=1, padx=5)
    tk.Entry(control_frame, textvariable=vy_var, width=10, font=("Arial", 12)).grid(row=1, column=2, padx=5)
    tk.Entry(control_frame, textvariable=vz_var, width=10, font=("Arial", 12)).grid(row=1, column=3, padx=5)

    tk.Label(control_frame, text="Campo Magnético (B):", font=("Arial", 12)).grid(row=2, column=0, padx=5)
    bx_var, by_var, bz_var = tk.StringVar(), tk.StringVar(), tk.StringVar()
    tk.Entry(control_frame, textvariable=bx_var, width=10, font=("Arial", 12)).grid(row=2, column=1, padx=5)
    tk.Entry(control_frame, textvariable=by_var, width=10, font=("Arial", 12)).grid(row=2, column=2, padx=5)
    tk.Entry(control_frame, textvariable=bz_var, width=10, font=("Arial", 12)).grid(row=2, column=3, padx=5)

    tk.Button(control_frame, text="Atualizar", command=update, font=("Arial", 12)).grid(row=3, column=0, columnspan=4, pady=10)

    result_label = tk.Label(control_frame, text="", font=("Arial", 12))
    result_label.grid(row=4, column=0, columnspan=4)

    trajectory = None
    anim = None
    v = None
    B = None
    F = None

    root.mainloop()

if __name__ == "__main__":
    main()