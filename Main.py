import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider

fig, ax_grafico = plt.subplots()
plt.subplots_adjust(bottom=0.30)

spazio_barra_a = plt.axes([0.25, 0.10, 0.55, 0.025]) 
spazio_barra_b = plt.axes([0.25, 0.04, 0.55, 0.025]) 

posizione_barra = [0,0]
slider_a = Slider(
    ax=spazio_barra_a,
    label='regolatore a',
    valmax=500,
    valmin=1,
    valstep=1.5  # <--- Lascia solo questo, rimuovi valcontinuous
)
slider_b = Slider(
    ax=spazio_barra_b,
    label='regolatore b',
    valmax=500,
    valmin=1,
    valstep=1.5  # <--- Lascia solo questo, rimuovi valcontinuous
)

def perimetro_ellisse (a,b):

    if a < b: a, b = b, a
    e_quadr = (a**2 - b**2) / a**2
    N = 2000
    t = np.linspace(0, np.pi / 2, N)
    dt = (np.pi / 2) / N
    integrando = np.sqrt(1 - e_quadr * (np.sin(t)**2))
    p_semi = np.sum(integrando[:-1] + integrando[1:]) * dt * a / 2
        
    return p_semi * 4

def calcolo_area (a,b):

    return a * b * np.pi

def disegno_ellisse(a,b):
    N = 1000
    x = np.linspace(0,a,N)
    y = b/a * np.sqrt(a**2 - x**2)
    return x,y,-x,-y


def funzioni(val):
    perimetro = perimetro_ellisse(slider_a.val,slider_b.val)
    Area = calcolo_area(slider_a.val,slider_b.val)
    x,y, x_negativa, y_negativa = disegno_ellisse(slider_a.val,slider_b.val)

    ax_grafico.cla() 

    ax_grafico.plot(x, y, linestyle='-', color='r', label='ellisse')
    ax_grafico.plot(x_negativa, y_negativa, linestyle='-', color='r', label='')
    ax_grafico.plot(x_negativa, y, linestyle='-', color='r', label='')
    ax_grafico.plot(x, y_negativa, linestyle='-', color='r', label='')


    # Aggiunta di dettagli
    ax_grafico.set_title(f'ELLISSE\n2p: {perimetro:.2f}\nArea: {Area:.2f}')
    ax_grafico.set_xlabel('x')
    ax_grafico.set_ylabel('y')
    ax_grafico.legend()
    ax_grafico.grid(True)
    ax_grafico.set_xlim(-550, 550)
    ax_grafico.set_ylim(-550, 550)
    ax_grafico.set_aspect('equal')

    plt.draw()

slider_a.on_changed(funzioni)
slider_b.on_changed(funzioni)

plt.show()

