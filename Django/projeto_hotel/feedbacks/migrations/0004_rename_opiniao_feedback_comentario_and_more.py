# Generated by Django 5.1.3 on 2025-02-08 10:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feedbacks', '0003_delete_contato_remove_feedback_sugestao'),
    ]

    operations = [
        migrations.RenameField(
            model_name='feedback',
            old_name='opiniao',
            new_name='comentario',
        ),
        migrations.AlterField(
            model_name='feedback',
            name='classificar',
            field=models.CharField(choices=[('0', '0'), ('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5')], default='0', max_length=150),
        ),
    ]
