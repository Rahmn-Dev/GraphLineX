# Generated by Django 5.1 on 2024-08-10 01:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DataSubmission',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('x1', models.FloatField(null=True)),
                ('x2', models.FloatField(null=True)),
                ('y1', models.FloatField(null=True)),
                ('y2', models.FloatField(null=True)),
                ('x_center', models.FloatField(null=True)),
                ('y_center', models.FloatField(null=True)),
                ('radius', models.FloatField(null=True)),
                ('algorithm', models.CharField(max_length=50)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
