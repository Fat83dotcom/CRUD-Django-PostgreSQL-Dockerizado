# Generated by Django 5.0.6 on 2024-05-18 05:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Core', '0003_alter_cadastrocliente_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cadastrocliente',
            name='email',
            field=models.EmailField(max_length=512),
        ),
    ]