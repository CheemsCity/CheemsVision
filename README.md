# Introduzione
Questo corso comprende tutto il necessario per costruire da zero la componente software CV di un robot a guida autonoma.
Partendo dalla calibrazione della camera fino a riconoscere i Cheems (abitanti della nostra città immaginaria) ed i cartelli stradali.
Per qualsiasi contibuto (ben accetto!!) effettuate un fork e fate pure una pull request.
Sentitevi liberi di usare questo tutorial per ogni scopo educativo.

Saranno necessari come materiali, un Raspberry Pi 4.0 (3.0 può andare bene ma è parecchio lento) ed una PiCamera.
Volendo si può effettuare il tutto anche da PC ma quest'ultimo non permetterà di effettuare l'ultimo step di tracciamento del percorso.

Il tutorial può essere visionato grazie a [nbviewer](http://nbviewer.jupyter.org):
* [Parte 0: Introduzione al corso](https://github.com/CheemsCity/CheemsVision/blob/main/CheemsVision-Part0-Introduction.ipynb)
* [Parte 1: Calibrazione della Camera](https://github.com/CheemsCity/CheemsVision/blob/main/CheemsVision-Part1-Calibration.ipynb)
* [Parte 3: Riconoscimento Aruco Markers](https://github.com/CheemsCity/CheemsVision/blob/main/CheemsVision-Part3-ArucoMarkersRecognition.ipynb)
* [Parte 4: Identificazione Colori e Semafori](https://github.com/CheemsCity/CheemsVision/blob/main/CheemsVision-Part4-StreetLightFinder.ipynb)

# Installazione
Saranno necessarie un paio di libreria: jupyter, opencv, numpy.
Per l'installazione di OpenCV su Raspberry linko un tutorial, necessario, in quanto Raspberry sarà il cervello pensante della nostra macchina [Guida installazione su Raspberry](https://robu.in/installing-opencv-using-cmake-in-raspberry-pi/)


Per installare gli altri pacchetti e il contenuto di questo corso potete scrivere questo a terminale
```bash
pip install numpy jupyter
#la prossima riga solo se sei su PC
pip install opencv-contrib-python
git clone https://github.com/CheemsCity/CheemsVision.git
cd CheemsVision
jupyter notebook
```
