# svg2ico

Inkscape extension to save image to WinIco file.

## Descrizione del Progetto

**svg2ico** è un'estensione per [Inkscape](https://inkscape.org/) che permette di convertire e esportare disegni vettoriali SVG in file di icone Windows nel formato `.ico`. L'estensione supporta diverse dimensioni standard (16x16, 32x32, 48x48 pixel) e consente di generare facilmente icone professionali direttamente dall'interno di Inkscape senza necessità di software aggiuntivo.

### Caratteristiche
- Conversione diretta da SVG a ICO
- Supporto per multiple dimensioni di icone
- Interfaccia integrata in Inkscape
- Compatibile con Inkscape 0.92 e versioni successive

## Installazione

### Installazione Automatica (Consigliato)

#### Linux / macOS
1. Scaricare il repository o estrarre l'archivio
2. Aprire un terminale nella cartella contenente i file
3. Eseguire lo script di installazione:
   ```bash
   bash install.sh
   ```
4. Seguire le istruzioni a schermo
5. Riavviare Inkscape

#### Windows
1. Scaricare il repository o estrarre l'archivio
2. Fare doppio clic su `install.bat`
3. Se richiesto, fare clic su "Esegui comunque" nel messaggio di sicurezza
4. Seguire le istruzioni a schermo
5. Riavviare Inkscape

---

### Installazione Manuale

#### Linux
1. Individuare la cartella delle estensioni di Inkscape:
   ```bash
   ~/.config/inkscape/extensions/
   ```
2. Copiare i file `svg2ico.py` e `svg2ico.inx` nella cartella delle estensioni
3. Rendere il file `svg2ico.py` eseguibile:
   ```bash
   chmod +x ~/.config/inkscape/extensions/svg2ico.py
   ```
4. Riavviare Inkscape

#### macOS
1. Individuare la cartella delle estensioni di Inkscape:
   ```bash
   ~/Library/Application\ Support/Inkscape/extensions/
   ```
2. Copiare i file `svg2ico.py` e `svg2ico.inx` nella cartella delle estensioni
3. Rendere il file `svg2ico.py` eseguibile:
   ```bash
   chmod +x ~/Library/Application\ Support/Inkscape/extensions/svg2ico.py
   ```
4. Riavviare Inkscape

#### Windows
1. Individuare la cartella delle estensioni di Inkscape (solitamente):
   ```
   C:\Program Files\Inkscape\share\extensions\
   ```
2. Copiare i file `svg2ico.py` e `svg2ico.inx` nella cartella delle estensioni
3. Riavviare Inkscape

## Utilizzo

1. Aprire o creare un disegno SVG in Inkscape
2. Selezionare l'oggetto che si desidera convertire in icona
3. Andare al menu **Estensioni > Esporta** e selezionare **SVG to ICO**
4. Scegliere la dimensione desiderata (16x16, 32x32 o 48x48)
5. Specificare il nome del file di output
6. Fare clic su **Applica**

### Troubleshooting Installazione

#### "Extension non appare nel menu di Inkscape"
- Verificare che i file `svg2ico.py` e `svg2ico.inx` siano nella cartella giusta
- Assicurarsi che `svg2ico.py` sia eseguibile (Linux/macOS): `chmod +x svg2ico.py`
- Riavviare completamente Inkscape
- Controllare i log di Inkscape: Help > System Console

#### "Errore: Pillow not found"
Installare la libreria Pillow:
- **Ubuntu/Debian**: `sudo apt-get install python3-pil`
- **Fedora/RHEL**: `sudo dnf install python3-pillow`
- **macOS**: `pip3 install Pillow`
- **Windows**: `pip install Pillow`

#### "Errore: Python 3 not found"
Installare Python 3:
- **Ubuntu/Debian**: `sudo apt-get install python3`
- **Fedora/RHEL**: `sudo dnf install python3`
- **macOS**: `brew install python3`
- **Windows**: Scaricare da https://www.python.org/downloads/

## Informazioni Tecniche

### Architettura del Plugin

svg2ico è un'estensione nativa di Inkscape che estende la classe `extension.Effect` del framework di Inkscape. L'estensione integra un pannello visuale all'interno dell'editor di Inkscape per permettere all'utente di configurare i parametri di esportazione.

### Flusso di Conversione

1. **Caricamento dei Parametri**: L'utente seleziona la dimensione dell'icona (16x16, 32x32 o 48x48) e specifica il nome del file di output tramite l'interfaccia grafica
2. **Esportazione SVG a PNG**: Il documento SVG aperto in Inkscape viene esportato in formato PNG temporaneo utilizzando il motore di rendering di Inkscape tramite linea di comando
3. **Ridimensionamento**: L'immagine PNG viene ridimensionata alla dimensione richiesta utilizzando l'algoritmo **LANCZOS** per mantenere la qualità
4. **Conversione a ICO**: L'immagine PNG viene convertita nel formato Windows ICO utilizzando la libreria PIL/Pillow
5. **Pulizia**: Il file PNG temporaneo viene eliminato automaticamente

### Configurazione del Plugin

Il plugin è configurato attraverso il file `svg2ico.inx` che definisce:

- **ID**: `org.inkscape.output.svg2ico` - Identificatore univoco del plugin
- **Parametri**:
  - `--s`: Dimensione dell'icona (16, 32 o 48 pixel)
  - `--o`: Nome del file di output (deve terminare con `.ico`)
- **Tipo di Esportazione**: Output in formato ICO (Windows Icon File)
- **Interprete**: Python 3

### Dipendenze

#### Obbligatorie
- **Inkscape 1.0+**: Motore di rendering e framework delle estensioni
- **Python 3.6+**: Interprete Python per eseguire lo script
- **Pillow/PIL**: Libreria Python per la manipolazione delle immagini

#### Facoltative
- **ImageMagick** (convert): Alternativa per la conversione di immagini (fallback)

### Installazione delle Dipendenze

#### Ubuntu/Debian
```bash
sudo apt-get install python3-pil
```

#### Fedora/RHEL
```bash
sudo dnf install python3-pillow
```

#### macOS
```bash
pip3 install Pillow
```

#### Windows
```bash
pip install Pillow
```

### Formati Supportati

**Input**: SVG (Scalable Vector Graphics)
**Output**: ICO (Windows Icon File)

**Modalità colore supportate**:
- RGB (Rosso, Verde, Blu)
- RGBA (RGB + Trasparenza)
- Palette (convertite automaticamente a RGBA)
- Scala di grigi

### Limitazioni Attuali

- Le dimensioni supportate sono limitate a 16x16, 32x32 e 48x48 pixel
- La conversione avviene tramite rasterizzazione (vettoriale → raster)
- Richiede che Inkscape sia correttamente installato sul sistema

## Bug in Lavorazione

### Problemi Noti
- [ ] **Compatibilità con Inkscape 1.0+**: Aggiornamento del supporto per le API di Inkscape 1.0 e versioni successive
- [ ] **Canale alfa**: Miglioramento della gestione della trasparenza (canale alfa) nelle immagini PNG convertite
- [ ] **Dimensioni aggiuntive**: Aggiunta di supporto per altre dimensioni standard di icone (256x256, 512x512)
- [ ] **Conversione batch**: Implementazione della conversione simultanea di più icone
- [ ] **Anteprima**: Aggiunta di un'anteprima dell'icona prima dell'esportazione

## About

* Author: [Maurizio Aru](https://github.com/ginopc)
* License: GNU General Public License v2.0

