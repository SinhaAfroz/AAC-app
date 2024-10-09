# AAC & Protein Properties Web App

This is a web application built with [Streamlit](https://streamlit.io/) that allows users to calculate the Amino Acid Composition (AAC) and several protein properties from a given protein sequence. The app uses the `biopython` library to analyze protein sequences.


## Features

- **Amino Acid Composition (AAC):** Calculates the percentage composition of each amino acid in the input protein sequence.
- **Protein Properties:**
  - Molecular Weight (Da)
  - Isoelectric Point (pI)
  - Instability Index
  - Aromaticity
- **Visualization:** Displays a bar chart showing the amino acid composition.
- **Downloadable Results:** AAC results can be downloaded as a CSV file.

## Live demo
https://aac-app-1.streamlit.app/

### 1. Clone the Repository

```
git clone https://github.com/yourusername/aac-app.git
cd aac-app
```
### 2. Install Dependencies
```
pip install -r requirements.txt
```

### 3. Run the app
```
streamlit run aac_app.py
```
## You can also use colab and run it on ngrok

### 1. Write this before the code it will create a file
%%writefile aac_app.py

### 2. Then run the code written in the file ngrok_run.txt
