import streamlit as st
import py3Dmol
import requests
import biotite.structure.io as bsio

st.set_page_config(layout = 'wide')
st.sidebar.title('🧪 ProteinWise')
st.sidebar.write('[*ProteinWise*](https://esmatlas.com/about) is an end-to-end single sequence protein structure predictor based on the ESM-2 language model. For more information, read the [research article](https://www.biorxiv.org/content/10.1101/2022.07.20.500902v2) and the [news article](https://www.nature.com/articles/d41586-022-03539-1) published in *Nature*.')
