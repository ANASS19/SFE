# Generated by Django 3.1.6 on 2021-05-21 20:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='historique',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Centre_livree', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='main_app.souscentre')),
                ('Livraison_historique', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='main_app.livraison')),
                ('Materiel_historique', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='main_app.materielmodel')),
            ],
        ),
    ]
