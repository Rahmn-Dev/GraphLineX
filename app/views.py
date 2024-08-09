from django.shortcuts import render
from .algorithm_dda import generate_plot as dda_generate_plot
from .algorithm_bresenham import generate_plot as bresenham_generate_plot
from .algorithm_midpoint import generate_plot as midpoint_generate_plot

def draw_line(request):
    plot_json = None
    if request.method == 'POST':
        x1 = int(request.POST.get('x1'))
        y1 = int(request.POST.get('y1'))
        x2 = int(request.POST.get('x2'))
        y2 = int(request.POST.get('y2'))

        algorithm = request.POST.get('algorithm')

        if algorithm == 'dda':
            plot_json = dda_generate_plot(x1, y1, x2, y2)
            print("ini dda")
        elif algorithm == 'bresenham':
            plot_json = bresenham_generate_plot(x1, y1, x2, y2)
            print("ini bresenham")
        elif algorithm == 'midpoint':
            plot_json = midpoint_generate_plot(x1, y1, x2, y2)
            print("ini midpoint")

    return render(request, 'index.html', {'plot_json': plot_json})