# Força de Lorentz

Este projeto é uma aplicação gráfica interativa que simula a trajetória de uma partícula carregada em um campo magnético, utilizando a força de Lorentz. A interface gráfica é construída com Tkinter e a visualização 3D é feita com Matplotlib.

## Requisitos

- Python 3.x
- Bibliotecas: `matplotlib`, `numpy`, `tkinter`

## Configuração do Ambiente Virtual

1. Crie um ambiente virtual:
    ```sh
    python -m venv venv
    ```

2. Ative o ambiente virtual:
    - No Windows:
        ```sh
        .\venv\Scripts\activate
        ```
    - No macOS/Linux:
        ```sh
        source venv/bin/activate
        ```

3. Instale as dependências necessárias:
    ```sh
    pip install matplotlib numpy
    ```

## Executando o Programa

1. Certifique-se de que o ambiente virtual está ativado.
2. Execute o script [teste.py](http://_vscodecontentref_/0):
    ```sh
    python teste.py
    ```

## Uso da Interface Gráfica

1. **Carga (q)**: Insira o valor da carga da partícula.
2. **Velocidade (v)**: Insira os componentes x, y e z da velocidade inicial da partícula.
3. **Campo Magnético (B)**: Insira os componentes x, y e z do campo magnético.
4. Clique no botão **Atualizar** para calcular e visualizar a trajetória da partícula e a força de Lorentz resultante.

## Documentação do Código

### Funções Principais

- **plot_3d_vectors(ax, velocity, magnetic, force, trajectory, particle_pos=None)**:
  Atualiza o gráfico 3D com os vetores de velocidade, campo magnético, força e trajetória da partícula.

- **calculate_force(q, v, B)**:
  Calcula a força de Lorentz dada a carga [q](http://_vscodecontentref_/1), vetor velocidade [v](http://_vscodecontentref_/2) e vetor campo magnético [B](http://_vscodecontentref_/3).

- **calculate_trajectory(q, v0, B, t_max=10, dt=0.01, m=1)**:
  Simula a trajetória de uma partícula carregada em um campo magnético.

### Função Principal

- **main()**:
  Configura a interface gráfica com Tkinter, inicializa os componentes e define as funções de atualização e animação.

### Estrutura da Interface Gráfica

- **Título**: "Força de Lorentz"
- **Fórmula**: Exibe a fórmula da força de Lorentz [F = q * (v x B)](http://_vscodecontentref_/4)
- **Controles**: Entradas para carga, velocidade e campo magnético, e botão para atualizar a simulação.
- **Resultado**: Exibe a força resultante calculada.

### Eventos e Animações

- **update()**:
  Atualiza os valores de entrada, calcula a força de Lorentz e a trajetória, e inicia a animação.
- **animate(frame)**:
  Atualiza a posição da partícula na animação.
- **on_closing()**:
  Para a animação e fecha a aplicação quando a janela é fechada.

## Observações

- Certifique-se de inserir valores válidos nos campos de entrada para evitar erros.
- A aplicação permite redimensionamento da janela para melhor visualização do gráfico 3D.
