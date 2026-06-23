# Ellipse-Python-calculator
An interactive and precise ellipse perimeter and surface calculator 
#  Ellipse Simulator

Un simulatore interattivo in Python per il calcolo geometrico e la visualizzazione grafica di un'ellisse in tempo reale.

##  Caratteristiche
- **Calcolo del Perimetro**: Implementato tramite integrazione numerica autonoma (metodo dei trapezi) per risolvere gli integrali ellittici.
- **Calcolo dell'Area**: Calcolo immediato basato sui semiassi.
- **Interfaccia Interattiva**: Dynamic aggiornamento del grafico tramite gli slider di `matplotlib`.
- **Ottimizzazione**: Gestione efficiente dei vettori di dati tramite `NumPy`.

## Tecnologie Utilizzate
- **Python 3**
- **NumPy** (Calcolo scientifico e vettorizzazione)
- **Matplotlib** (Visualizzazione grafica e widget interattivi)

##  Come Eseguirlo
1. Assicurati di avere le librerie installate:
   ```bash
   pip install numpy matplotlib
   ```
2. Esegui lo script:
   ```bash
   python nome_del_file.py
   ```

##  Concetti Matematici Applicati
Il simulatore non usa formule standard per il perimetro, ma approssima l'integrale della funzione dell'eccentricità:
$$E(e) = \int_{0}^{\pi/2} \sqrt{1 - e^2 \sin^2(t)} \ dt$$
Divisore della curva in segmenti ad alta precisione per aggirare l'assenza di una formula elementare per il perimetro dell'ellisse.
