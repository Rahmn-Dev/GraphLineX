from django import forms
from .models import DataSubmission

class DataSubmissionForm(forms.ModelForm):
    class Meta:
        model = DataSubmission
        fields = ['x1', 'x2', 'y1', 'y2', 'x_center', 'y_center', 'radius', 'algorithm']