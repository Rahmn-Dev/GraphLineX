import plotly.graph_objects as go
import plotly.io as pio

def bresenham_algorithm(x1, y1, x2, y2):
    points = []
    dx = abs(x2 - x1)
    dy = abs(y2 - y1)
    sx = 1 if x1 < x2 else -1
    sy = 1 if y1 < y2 else -1
    err = dx - dy

    while True:
        points.append((x1, y1))
        if x1 == x2 and y1 == y2:
            break
        e2 = 2 * err
        if e2 > -dy:
            err -= dy
            x1 += sx
        if e2 < dx:
            err += dx
            y1 += sy

    return points

def generate_plot(x1, y1, x2, y2):
    points = bresenham_algorithm(x1, y1, x2, y2)
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