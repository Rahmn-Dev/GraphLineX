import matplotlib.pyplot as plt
import numpy as np
from io import BytesIO
import base64

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
    
    fig, ax = plt.subplots()
    ax.plot(x_values, y_values, marker='o', linestyle='-', color='b')
    ax.set_title(f'Line from ({x1}, {y1}) to ({x2}, {y2})')
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.grid(True)

    # Save plot to a BytesIO object
    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    plt.close(fig)
    buffer.seek(0)
    
    # Encode image to base64
    img_str = base64.b64encode(buffer.read()).decode('utf-8')
    
    return img_str