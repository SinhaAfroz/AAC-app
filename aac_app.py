import streamlit as st
import Bio
from Bio.SeqUtils.ProtParam import ProteinAnalysis
import pandas as pd
import matplotlib.pyplot as plt

# Function to calculate AAC
def calculate_aac(sequence):
    analysis = ProteinAnalysis(sequence.upper())
    aac = analysis.get_amino_acids_percent()
    return {aa: f"{percent*100:.2f}%" for aa, percent in aac.items()}

# Function to calculate protein properties
def calculate_properties(sequence):
    analysis = ProteinAnalysis(sequence.upper())
    molecular_weight = analysis.molecular_weight()
    isoelectric_point = analysis.isoelectric_point()
    instability_index = analysis.instability_index()
    aromaticity = analysis.aromaticity()

    return {
        "Molecular Weight (Da)": molecular_weight,
        "Isoelectric Point (pI)": isoelectric_point,
        "Instability Index": instability_index,
        "Aromaticity": aromaticity
    }

# Streamlit app
st.set_page_config(page_title="AAC & Protein Properties", layout="wide")
st.title("Amino Acid Composition (AAC) and Protein Properties")

# Sidebar input
with st.sidebar:
    st.header("Input Protein Sequence")
    sequence = st.text_area("Enter Protein Sequence", height=200)

# Ensure the sequence is valid
if sequence:
    if all(aa in "ACDEFGHIKLMNPQRSTVWY" for aa in sequence.upper()):
        # Use tabs to separate different outputs
        tab1, tab2, tab3 = st.tabs(["Amino Acid Composition (AAC)", "AAC Visualization", "Protein Properties"])

        # Calculate AAC and display in tab 1
        with tab1:
            st.subheader("Amino Acid Composition (AAC)")
            aac = calculate_aac(sequence)
            aac_df = pd.DataFrame(list(aac.items()), columns=["Amino Acid", "Percentage"])
            st.dataframe(aac_df)

        # AAC Visualization in tab 2
        with tab2:
            st.subheader("AAC Visualization")
            amino_acids = list(aac.keys())
            percentages = [float(aac[aa].strip('%')) for aa in amino_acids]
            fig, ax = plt.subplots()
            ax.bar(amino_acids, percentages, color='skyblue')
            ax.set_xlabel('Amino Acids')
            ax.set_ylabel('Percentage (%)')
            ax.set_title('Amino Acid Composition')
            st.pyplot(fig)

        # Protein Properties in tab 3
        with tab3:
            st.subheader("Protein Properties")
            properties = calculate_properties(sequence)
            properties_df = pd.DataFrame(list(properties.items()), columns=["Property", "Value"])
            st.dataframe(properties_df)

        # Download option
        st.sidebar.download_button(
            label="Download AAC as CSV",
            data=aac_df.to_csv(index=False),
            file_name="aac_results.csv",
            mime="text/csv"
        )

    else:
        st.sidebar.error("Invalid sequence! Please enter a valid protein sequence.")
else:
    st.sidebar.info("Please enter a protein sequence.")
