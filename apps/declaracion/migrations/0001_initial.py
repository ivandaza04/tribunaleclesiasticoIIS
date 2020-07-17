# Generated by Django 2.1.1 on 2020-07-17 20:48

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('proceso', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Declaracion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField(default=django.utils.timezone.now)),
                ('observacion', models.TextField(blank=True, max_length=500, null=True)),
                ('docfile', models.FileField(blank=True, null=True, upload_to='documents/%Y/%m/%d')),
            ],
        ),
        migrations.CreateModel(
            name='Tipo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.CharField(max_length=100, unique=True)),
            ],
            options={
                'ordering': ['tipo'],
            },
        ),
        migrations.AddField(
            model_name='declaracion',
            name='nombre',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='declaracion.Tipo'),
        ),
        migrations.AddField(
            model_name='declaracion',
            name='proceso',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='proceso.Proceso'),
        ),
    ]