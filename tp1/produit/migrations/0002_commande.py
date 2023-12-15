# Generated by Django 4.2.7 on 2023-11-15 20:43

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('produit', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Commande',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Description_cmd', models.CharField(max_length=50)),
                ('Date_cmd', models.DateTimeField(default=datetime.datetime.now)),
                ('Produit_cmd', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='produit.produit')),
            ],
        ),
    ]
