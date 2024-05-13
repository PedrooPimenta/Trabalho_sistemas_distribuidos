# Generated by Django 5.0.4 on 2024-05-12 02:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pesquisador',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255, verbose_name='Nome do Pesquisador')),
                ('nivel', models.CharField(choices=[('Graduando', 'Graduando'), ('Graduação', 'Graduacao'), ('Mestrado', 'Mestrado'), ('Doutorado', 'Doutorado')], max_length=10, verbose_name='Titulação')),
                ('lattes', models.URLField(blank=True, null=True, verbose_name='Lattes')),
                ('linkedin', models.URLField(blank=True, null=True, verbose_name='Linkedin')),
                ('researchgate', models.URLField(blank=True, null=True, verbose_name='Research Gate')),
                ('email', models.EmailField(max_length=254, verbose_name='E-mail')),
                ('data_criacao', models.DateTimeField(auto_now_add=True, verbose_name='Data de Criação')),
                ('ativo', models.BooleanField(default=False)),
                ('cargo', models.CharField(choices=[('Aluno', 'Aluno'), ('Professor', 'Professor'), ('Técnico', 'Tecnico')], max_length=10, verbose_name='Cargo')),
            ],
        ),
    ]
