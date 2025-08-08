
import streamlit as st
from PIL import Image

st.image('./catsci-logo.svg', width=400)
st.subheader("Links for Data Processing and Visualisation", divider="orange")
st.write("")


#-- GRAPH VISUALISATION --
st.markdown("""
<style>
#a {
    background-color: #F0F2F6;
    color: #444352;
    padding: 10px 20px;
    margin: 15px;
    font-size: 18px;
    border: none;
    border-radius: 5px;
    cursor: pointer;
    transition: background-color .2s ease;
    text-decoration: none;
    display: inline-block;
}
#a:hover {
    background-color: #5DE2E7;
}
</style>

<a href="https://graph-visualisation.streamlit.app/" target="_blank">
    <div id="a">
        Data Visualisation
    </div>
</a>
""", unsafe_allow_html=True)

# --- Crystal 16 Processing ---

st.markdown("""
<style>
#b {
    background-color: #F0F2F6;
    color: #444352;
    padding: 10px 20px;
    margin: 15px;
    font-size: 18px;
    border: none;
    border-radius: 5px;
    cursor: pointer;
    transition: background-color .2s ease;
    text-decoration: none;
    display: inline-block;
}
#b:hover {
    background-color: #faaf4c;
}
</style>

<a href="https://crystal-16-processing.streamlit.app" target="_blank">
    <div id="b">
        Crystal16 Processing
    </div>
</a>
""", unsafe_allow_html=True)


#-- PE's LC TABLE GENERATOR --
st.markdown("""<a href="https://lc-data.streamlit.app/" target="_blank">
    <div id="a">
        LC Processor and Table Generator
    </div>
</a>
""", unsafe_allow_html=True)

# --- PM's RT predictor ---

st.markdown("""<a href="https://rt-predict.streamlit.app/" target="_blank">
    <div id="b">
        RT Prediction Tool
    </div>
</a>
""", unsafe_allow_html=True)


# --LABLYNX --

st.markdown("""


<a href="https://portaointeligente2.azurewebsites.net/records/" target="_blank">
    <div id="a">
        LabLynx
    </div>
</a>
""", unsafe_allow_html=True)


