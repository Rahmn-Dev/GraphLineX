import plotly.graph_objects as go
import plotly.io as pio
import json

def dda_algorithm(x1, y1, x2, y2):
    dx = x2 - x1
    dy = y2 - y1
    steps = max(abs(dx), abs(dy))

    x_increment = dx / steps
    y_increment = dy / steps

    x = x1
    y = y1
    points = []

    for _ in range(steps + 1):
        points.append((round(x), round(y)))
        x += x_increment
        y += y_increment

    return points

def generate_plot(x1, y1, x2, y2):
    points = dda_algorithm(x1, y1, x2, y2)
    x_values, y_values = zip(*points)
    
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=x_values, y=y_values, mode='lines+markers', name='Line'))
    fig.update_layout(
                      xaxis_title='X',
                      yaxis_title='Y',
                      template='plotly_white')

    plot_json = pio.to_json(fig)
    
    return plot_json