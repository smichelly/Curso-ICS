# Generated by Django 5.1 on 2024-09-16 13:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0003_cliente_escolaridade'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='escolaridade',
            field=models.CharField(max_length=50),
        ),
    ]
