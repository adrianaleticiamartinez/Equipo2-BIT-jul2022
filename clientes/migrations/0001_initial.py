# Generated by Django 4.0.6 on 2022-07-14 03:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('idCliente', models.CharField(max_length=50)),
                ('nombre', models.CharField(max_length=50)),
                ('apellidoPaterno', models.CharField(max_length=50)),
                ('apellidoMaterno', models.CharField(max_length=50)),
                ('fechaNacimiento', models.CharField(max_length=50)),
                ('sexo', models.CharField(max_length=50)),
                ('segmento', models.SmallIntegerField()),
                ('nacionalidad', models.CharField(max_length=50)),
                ('rfc', models.CharField(max_length=50)),
                ('tipoID', models.CharField(max_length=50)),
                ('cuenta', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=50)),
                ('TDD', models.CharField(max_length=50)),
            ],
        ),
    ]
