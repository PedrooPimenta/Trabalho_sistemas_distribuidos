# Generated by Django 5.0.4 on 2024-04-25 16:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('monografias', '0002_rename_arquivo_monografia_arquivos'),
    ]

    operations = [
        migrations.AlterField(
            model_name='monografia',
            name='arquivos',
            field=models.FileField(upload_to='arquivos/'),
        ),
    ]