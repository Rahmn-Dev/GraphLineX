import plotly.graph_objects as go
import plotly.io as pio

def midpoint_algorithm(x1, y1, x2, y2):
    points = []
    dx = x2 - x1
    dy = y2 - y1
    d = dy - (dx / 2)
    x = x1
    y = y1

    points.append((x, y))

    while x < x2:
        x += 1
        if d < 0:
            d = d + dy
        else:
            d = d + (dy - dx)
            y += 1
        points.append((x, y))

    return points

def generate_plot(x1, y1, x2, y2):
    points = midpoint_algorithm(x1, y1, x2, y2)
    x_values, y_values = zip(*points)
    
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=x_values, y=y_values, mode='lines+markers', name='Line'))
    fig.update_layout(
        xaxis_title='X',
        yaxis_title='Y',
        template='plotly_white'
    )

    plot_json = pio.to_json(fig)
    return plot_json