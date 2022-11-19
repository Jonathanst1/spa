# Generated by Django 4.1.1 on 2022-11-18 20:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Atendimento', '0019_alter_plano_capacitacao'),
    ]

    operations = [
        migrations.AlterField(
            model_name='plano',
            name='capacitacao',
            field=models.CharField(blank=True, choices=[('Sim', 'sim'), ('Nao', 'nao')], default='Sim', max_length=3, null=True),
        ),
    ]