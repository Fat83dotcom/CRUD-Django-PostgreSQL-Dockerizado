# Generated by Django 5.0.6 on 2024-05-22 02:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Core', '0008_cadastrocliente_criado_em_cadastrocliente_criado_por'),
    ]

    operations = [
        migrations.AddField(
            model_name='cadastrocliente',
            name='atualizado_por',
            field=models.DateTimeField(auto_now=True),
        ),
    ]