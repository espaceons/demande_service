# Generated by Django 5.2 on 2025-04-16 08:36

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('clients', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True, null=True)),
                ('etat', models.CharField(choices=[('nouveau', 'Nouveau'), ('ancien', 'Ancien')], max_length=50)),
                ('notes', models.TextField(blank=True, null=True)),
                ('longueur', models.IntegerField(blank=True, null=True)),
                ('largeur', models.DecimalField(blank=True, decimal_places=15, max_digits=30, null=True)),
                ('poids', models.IntegerField(blank=True, null=True)),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='clients.client')),
            ],
        ),
    ]
