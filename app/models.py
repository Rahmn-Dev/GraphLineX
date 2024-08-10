from django.db import models

class DataSubmission(models.Model):
    x1 = models.FloatField(null=True)
    x2 = models.FloatField(null=True)
    y1 = models.FloatField(null=True)
    y2 = models.FloatField(null=True)
    x_center = models.FloatField(null=True)
    y_center = models.FloatField(null=True)
    radius = models.FloatField(null=True)
    algorithm = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Submission {self.id} - {self.algorithm}"