# Generated by Django 4.1.1 on 2022-11-18 21:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Atendimento', '0028_plano_capacitacao2'),
    ]

    operations = [
        migrations.AlterField(
            model_name='plano',
            name='capacitacao2',
            field=models.CharField(choices=[('Sim', 'sim'), ('Nao', 'nao')], max_length=3),
        ),
    ]