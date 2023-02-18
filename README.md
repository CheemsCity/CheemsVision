# Introduzione
Questo corso comprende tutto il necessario per costruire da zero la componente software CV di un robot a guida autonoma.
Partendo dalla calibrazione della camera fino a riconoscere i Cheems (abitanti della nostra città immaginaria) ed i cartelli stradali.
Per qualsiasi contibuto (ben accetto!!) effettuate un fork e fate pure una pull request.
Sentitevi liberi di usare questo tutorial per ogni scopo educativo.

Saranno necessari come materiali, un Raspberry Pi 4.0 (3.0 può andare bene ma è parecchio lento) ed una PiCamera.

Il tutorial può essere visionato grazie a [nbviewer](http://nbviewer.jupyter.org):
* [Parte 0: Introduzione al corso](http://nbviewer.jupyter.org/github/CheemsCity/CheemsVision/CheemsVision-Part0-Introduction.ipynb)

# Installazione
Saranno necessarie un paio di libreria: jupyter, opencv, numpy.
Per l'installazione di OpenCV su Raspberry linko un tutorial, necessario, in quanto Raspberry sarà il cervello pensante della nostra macchina [Guida installazione su Raspberry](https://robu.in/installing-opencv-using-cmake-in-raspberry-pi/)


Per installare gli altri pacchetti e il contenuto di questo corso potete scrivere questo a terminale
```bash
pip install numpy jupyter
git clone https://github.com/CheemsCity/CheemsVision.git
cd CheemsVision
jupyter notebook
```
