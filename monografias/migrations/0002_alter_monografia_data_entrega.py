# Generated by Django 5.0.4 on 2024-05-18 18:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('monografias', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='monografia',
            name='data_entrega',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
