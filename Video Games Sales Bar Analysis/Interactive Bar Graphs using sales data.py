import pandas as pd
import plotly.graph_objects as go
from ipywidgets import widgets


df = pd.read_csv('/Users/mustafa/Desktop/Coding Projects/Video Games Sales Analysis/cleaned_video_game_sales_withname.csv')

fig = go.FigureWidget()

fig.add_trace(go.Bar(
    x=['NA_Sales', 'EU_Sales', 'JP_Sales', 'Other_Sales'],
    y=[0, 0, 0, 0],
    text=['NA_Sales', 'EU_Sales', 'JP_Sales', 'Other_Sales'],
    textposition='auto',
    marker_color=['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728'],  
    opacity=0.8
))

fig.update_layout(
    title=f"Regional Sales",
    title_x=0.5, 
    xaxis_title="Region",
    yaxis_title="Sales (in millions)",
    font=dict(
        family="Courier New, monospace",  
        size=14,
        color="#7f7f7f"  
    ),
    hovermode="x",
    plot_bgcolor='white', 
    paper_bgcolor='white', 
    showlegend=False,  
)

dropdown = widgets.Dropdown(options=df['Name'].unique())

def update_graph(change):
    game_name = change['new']
    game_data = df[df['Name'] == game_name]

    if not game_data.empty:
        game_data = game_data.iloc[0]
        fig.data[0].y = [game_data['NA_Sales'], game_data['EU_Sales'], game_data['JP_Sales'], game_data['Other_Sales']]
        fig.layout.title.text = f"Regional Sales for {game_name}"
    else:
        print(f"No data found for game: {game_name}")

dropdown.observe(update_graph, names='value')

display(dropdown, fig)
