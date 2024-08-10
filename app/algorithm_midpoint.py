import plotly.graph_objects as go
import plotly.io as pio

def midpoint_circle_algorithm(x_center, y_center, radius):
    x = radius
    y = 0
    points = []

    points.append((x + x_center, y + y_center))

    if radius > 0:
        points.append((x + x_center, -y + y_center))
        points.append((y + x_center, x + y_center))
        points.append((-y + x_center, x + y_center))

    P = 1 - radius

    while x > y:
        y += 1

        if P <= 0:
            P = P + 2 * y + 1
        else:
            x -= 1
            P = P + 2 * y - 2 * x + 1

        if x < y:
            break

        points.append((x + x_center, y + y_center))
        points.append((-x + x_center, y + y_center))
        points.append((x + x_center, -y + y_center))
        points.append((-x + x_center, -y + y_center))

        if x != y:
            points.append((y + x_center, x + y_center))
            points.append((-y + x_center, x + y_center))
            points.append((y + x_center, -x + y_center))
            points.append((-y + x_center, -x + y_center))

    return points

def generate_plot(x_center, y_center, radius):
    points = midpoint_circle_algorithm(x_center, y_center, radius)
    x_values, y_values = zip(*points)
    
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=x_values, y=y_values, mode='markers', name='Circle'))
    fig.update_layout(
        xaxis_title='X',
        yaxis_title='Y',
        template='plotly_white',
        xaxis=dict(scaleanchor="y", scaleratio=1), 
    )

    plot_json = pio.to_json(fig)
    
    return plot_json