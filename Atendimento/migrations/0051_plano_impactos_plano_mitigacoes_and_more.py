# Generated by Django 4.1.1 on 2023-01-24 18:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Atendimento', '0050_plano_n1area_plano_n2area_alter_plano_volumetrias_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='plano',
            name='impactos',
            field=models.TextField(blank=True, max_length=1000),
        ),
        migrations.AddField(
            model_name='plano',
            name='mitigacoes',
            field=models.TextField(blank=True, max_length=1000),
        ),
        migrations.AlterField(
            model_name='plano',
            name='riscos_identificados',
            field=models.TextField(blank=True, max_length=1000),
        ),
    ]