# Generated by Django 3.2 on 2023-01-20 17:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_remision_clie_fecha_remision'),
    ]

    operations = [
        migrations.AlterField(
            model_name='remision_clie',
            name='fecha_remision',
            field=models.DateField(auto_now_add=True),
        ),
    ]
