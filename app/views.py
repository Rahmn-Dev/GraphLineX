from django.shortcuts import render
from .algorithm_dda import generate_plot as dda_generate_plot
from .algorithm_bresenham import generate_plot as bresenham_generate_plot
from .algorithm_midpoint import generate_plot as midpoint_generate_plot
from .models import DataSubmission
import re

def parse_query(query):
    midpoint_match = re.match(r'midpoint\((\d+),(\d+)\)\((\d+)\)', query)
    if midpoint_match:
        algorithm = 'midpoint'
        x_center = int(midpoint_match.group(1))
        y_center = int(midpoint_match.group(2))
        radius = int(midpoint_match.group(3))
        return algorithm, x_center, y_center, radius
        
    match = re.match(r'(\w+)\((\d+),(\d+)\)\((\d+),(\d+)\)', query)
    if match:
        algorithm = match.group(1)
        x1 = int(match.group(2))
        y1 = int(match.group(3))
        x2 = int(match.group(4))
        y2 = int(match.group(5))
        return algorithm, x1, y1, x2, y2
    
    return None


def draw_line(request):
    plot_json = None
    submissions = DataSubmission.objects.all().order_by('-created_at')

    show_graph_query = request.GET.get('show_graph')
    if show_graph_query:
        parsed_data = parse_query(show_graph_query)
        if parsed_data:
            if parsed_data[0] == 'midpoint':
                algorithm, x_center, y_center, radius = parsed_data
                plot_json = midpoint_generate_plot(x_center, y_center, radius)
                print(f"Graph generated for {algorithm} algorithm with center ({x_center}, {y_center}) and radius {radius}")
            else:
                algorithm, x1, y1, x2, y2 = parsed_data
                if algorithm == 'dda':
                    plot_json = dda_generate_plot(x1, y1, x2, y2)
                elif algorithm == 'bresenham':
                    plot_json = bresenham_generate_plot(x1, y1, x2, y2)
                print(f"Graph generated for {algorithm} algorithm with coordinates ({x1}, {y1}) and ({x2}, {y2})")


    if request.method == 'POST':
        

        algorithm = request.POST.get('algorithm')

        if algorithm == 'midpoint':
            x_center = int(request.POST.get("x_center"))
            y_center = int(request.POST.get("y_center"))
            radius = int(request.POST.get("radius"))
            plot_json = midpoint_generate_plot(x_center, y_center, radius)
            print("ini midpoint")
        else:
            x1 = int(request.POST.get('x1'))
            y1 = int(request.POST.get('y1'))
            x2 = int(request.POST.get('x2'))
            y2 = int(request.POST.get('y2'))
            if algorithm == 'bresenham':
                plot_json = bresenham_generate_plot(x1, y1, x2, y2)
                print("ini bresenham")
            elif algorithm == 'dda':
                plot_json = dda_generate_plot(x1, y1, x2, y2)
                print("ini dda")

        DataSubmission.objects.create(
            x1=x1 if 'x1' in locals() else None,
            x2=x2 if 'x2' in locals() else None,
            y1=y1 if 'y1' in locals() else None,
            y2=y2 if 'y2' in locals() else None,
            x_center=x_center if 'x_center' in locals() else None,
            y_center=y_center if 'y_center' in locals() else None,
            radius=radius if 'radius' in locals() else None,
            algorithm=algorithm
        )

    return render(request, 'index.html', {'plot_json': plot_json, 'submissions': submissions})