# Generated by Django 4.1.1 on 2022-11-18 19:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Atendimento', '0011_rename_capacitacao1_plano_capacitacao_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='plano',
            name='capacitacao',
            field=models.CharField(choices=[('Sim', 'sim'), ('Nao', 'nao')], default='Sim', max_length=3),
        ),
    ]
