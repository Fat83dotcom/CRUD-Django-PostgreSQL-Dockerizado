# Generated by Django 5.0.6 on 2024-05-19 04:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Core', '0006_cadastrocliente_data_nascimento'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cadastrocliente',
            old_name='data_nascimento',
            new_name='nasc',
        ),
    ]