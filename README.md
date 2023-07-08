
![](part0/img/CheemsBanner.png)
# Introduzione
Questo corso comprende tutto il necessario per costruire da zero la componente software CV di un robot a guida autonoma.
Partendo dalla calibrazione della camera fino a riconoscere i Cheems (abitanti della nostra città immaginaria) ed i cartelli stradali.
Per qualsiasi contibuto (ben accetto!!) effettuate un fork e fate pure una pull request.
Sentitevi liberi di usare questo tutorial per ogni scopo educativo.

Saranno necessari come materiali, un Raspberry Pi 4.0 (3.0 può andare bene ma è parecchio lento) ed una PiCamera.
Volendo si può effettuare il tutto anche da PC utilizzando una camera USB, ma per tutorial più avanzati, l'utilizzo del raspberry sarà fondamentale, 
in quanto parte principale del robot.

Il tutorial può essere visionato grazie a [nbviewer](http://nbviewer.jupyter.org), ma per poter runnare il codice in modo ottimale è necessario scaricare la cartella sul proprio PC/raspberry:
* [Parte 0: Introduzione al corso](https://github.com/CheemsCity/CheemsVision/blob/main/CheemsVision-Part0-Introduction.ipynb)
* [Parte 1: Calibrazione della Camera](https://github.com/CheemsCity/CheemsVision/blob/main/CheemsVision-Part1-Calibration.ipynb)
* [Parte 2: Riconoscimento delle linee](https://github.com/CheemsCity/CheemsVision/blob/main/CheemsVision-Part2-LineRecognition.ipynb)
* [Parte 3: Riconoscimento Aruco Markers](https://github.com/CheemsCity/CheemsVision/blob/main/CheemsVision-Part3-ArucoMarkersRecognition.ipynb)
* [Parte 4: Identificazione Colori e Semafori](https://github.com/CheemsCity/CheemsVision/blob/main/CheemsVision-Part4-StreetLightFinder.ipynb)

Alla fine di questi tutorial avrai tutte le competenze per creare una possibile pipeline per l'analisi di immagini per la guida autonoma!

# Installazione
Saranno necessarie un paio di librerie: jupyter, opencv, numpy, pyYAML e matplotlib.  
Sarà anche necessario avere Python installato.

## Creazione Virtual Environment
Creiamo un virtual env, ovvero uno spazio di lavoro python. Questo ci permetterà di installare tutte le librerie che vogliamo senza creare conflitto con  altri programmi.
Il metodo varierà in base al dispositivo che state usando.

### Caso Raspberry 
```bash
pip3 install virtualenv virtualenvwrapper
nano ~/.bashrc
```
aggiungi queste righe alla fine del file che si sarò aperto:  
```bash
#Virtualenvwrapper settings:
export VIRTUALENVWRAPPER_PYTHON=/usr/bin/python3
export WORKON_HOME=$HOME/.virtualenvs
export VIRTUALENVWRAPPER_VIRTUALENV=~/.local/bin/virtualenv
source ~/.local/bin/virtualenvwrapper.sh
export VIRTUALENVWRAPPER_ENV_BIN_DIR=bin
```
ricarica il file
```bash
source ~/.bashrc
```
Creiamo ora il virtual env (i comandi prima erano necessari per l'installazione del gestore dei virtual env):
```bash
mkvirtualenv cv
workon cv
```
ogni volta che vorrai attivare il virtual env creato utilizza il comando **workon nome_env**.  

### Caso Windows 
```bash
pip install virtualenv 
virtualenv cv
 > cv\Scripts\activate
```
l'ultimo comando sarà necessario attivarlo ogni volta che si vorrà andare a lavorare in questo env! è importante trovarsi nella stessa cartella in cui lo si è creato per  poterlo attivare.

## Pacchetti
Per l'installazione di OpenCV su Raspberry linko un tutorial, necessario, in quanto Raspberry sarà il cervello pensante della nostra macchina [Guida installazione su Raspberry](https://robu.in/installing-opencv-using-cmake-in-raspberry-pi/)


Per installare gli altri pacchetti e il contenuto di questo corso potete scrivere questo a terminale
```bash
pip install numpy jupyter PyYAML matplotlib
#la prossima riga solo se sei su PC
pip install opencv-contrib-python
#con il comand git clone andiamo a scaricare questa cartella
git clone https://github.com/CheemsCity/CheemsVision.git
cd CheemsVision
jupyter notebook
```


In caso volessi supportarci nella creazione di altri corsi e robot, puoi offrirci un caffe!

<a href="https://bmc.link/cheemscity" target="_blank"><img src="https://cdn.buymeacoffee.com/buttons/default-orange.png" alt="Buy Me A Coffee" style="height: 41px !important;width: 174px !important;box-shadow: 0px 3px 2px 0px rgba(190, 190, 190, 0.5) !important;-webkit-box-shadow: 0px 3px 2px 0px rgba(190, 190, 190, 0.5) !important;" ></a>

# Supporto

Se avessi bisogno di aiuto scrivici pure su Github o [instagram](https://www.instagram.com/cheems.city/)