# Generated by Django 4.1.1 on 2023-01-12 17:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Atendimento', '0045_accesscounter'),
    ]

    operations = [
        migrations.CreateModel(
            name='AccessCount',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('count', models.IntegerField()),
            ],
        ),
        migrations.DeleteModel(
            name='AccessCounter',
        ),
    ]
