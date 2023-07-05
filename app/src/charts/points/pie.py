import plotly.graph_objects as go
import numpy as np
import pandas as pd

def get():
    # Data for the pizza chart
    labels = ["Pontos usados", "Pontos expirados", "Pontos ativos", "Outros"]
    values = [25, 20, 30, 25]

    # Create the pizza chart figure
    fig = go.Figure(data=[go.Pie(labels=labels, values=values, hole=0.4)])

    # Set the layout options
    fig.update_layout(
        margin=dict(t=40, b=0, l=0, r=0),
        height=200,
        showlegend=True
    )

    return fig