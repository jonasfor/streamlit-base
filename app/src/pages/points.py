import streamlit as st
from ..utils import Page
from ..charts.points import pie, area
import pandas as pd
import numpy as np
import plotly.graph_objects as go


class Points(Page):
    def __init__(self, state):
        self.state = state

    def write(self):

        tab1, tab2, tab3 = st.tabs(["Programa de pontos", "Média de consumo de pontos", "Recorrência no programa"])

        with tab1:
            col1, col2 = st.columns(spec=[2, 3], gap='large')

            with col1:
                st.subheader("Acumulo de pontos")
                st.plotly_chart(pie.get(), use_container_width=True)
                
            with col2:
                st.subheader("Histórico de pontos")
                st.area_chart(area.get())

        with tab2:
            st.header("A dog")
            st.image("https://static.streamlit.io/examples/dog.jpg", width=200)

        with tab3:
            st.header("An owl")
            st.image("https://static.streamlit.io/examples/owl.jpg", width=200)

        # st.title("Análise do programa de pontos")
        
        # self.state.client_config["slider_value"] = 98
