# Generated by Django 4.1.1 on 2022-12-20 19:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Atendimento', '0041_rename_password_user_senha_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='senha',
            new_name='password',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='usuario',
            new_name='username',
        ),
    ]
