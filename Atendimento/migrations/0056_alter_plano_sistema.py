# Generated by Django 4.1.1 on 2023-01-31 18:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Atendimento', '0055_alter_plano_identificacao_area_solicitante_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='plano',
            name='sistema',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
