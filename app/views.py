
from django.shortcuts import render
from .algorithm_dda import generate_plot

def draw_line(request):
    img_str = None
    if request.method == 'POST':
        x1 = int(request.POST.get('x1'))
        y1 = int(request.POST.get('y1'))
        x2 = int(request.POST.get('x2'))
        y2 = int(request.POST.get('y2'))

        img_str = generate_plot(x1, y1, x2, y2)
        
    return render(request, 'form.html', {'img_str': img_str})