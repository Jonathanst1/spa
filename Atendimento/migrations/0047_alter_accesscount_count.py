# Generated by Django 4.1.1 on 2023-01-12 17:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Atendimento', '0046_accesscount_delete_accesscounter'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accesscount',
            name='count',
            field=models.IntegerField(default=0),
        ),
    ]
