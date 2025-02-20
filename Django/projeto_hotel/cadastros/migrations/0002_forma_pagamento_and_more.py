# Generated by Django 5.1.3 on 2024-12-10 14:05

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cadastros', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Forma_pagamento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
            ],
        ),
        migrations.RenameField(
            model_name='cadastro',
            old_name='CPF',
            new_name='quantidade_pessoas',
        ),
        migrations.RemoveField(
            model_name='cadastro',
            name='data_cadastro',
        ),
        migrations.RemoveField(
            model_name='cadastro',
            name='idade',
        ),
        migrations.AddField(
            model_name='cadastro',
            name='checkin',
            field=models.DateField(auto_now_add=True, default='2024-12-13'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='cadastro',
            name='checkout',
            field=models.DateField(auto_now_add=True, default='2024-12-13'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='cadastro',
            name='cpf',
            field=models.CharField(default='a defini', max_length=11),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='cadastro',
            name='forma_pegamento',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='cadastros.forma_pagamento'),
        ),
    ]
