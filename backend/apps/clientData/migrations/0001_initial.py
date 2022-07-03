# Generated by Django 4.0.4 on 2022-07-02 17:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('procedure', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ClientData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mail', models.EmailField(max_length=50, unique=True)),
                ('password', models.CharField(max_length=100)),
                ('telephone', models.CharField(max_length=10)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('procedure', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='client_data', to='procedure.generalprocedure')),
            ],
            options={
                'verbose_name': 'Datos del cliente',
                'verbose_name_plural': 'Datos de los clientes',
            },
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dni', models.CharField(max_length=10, unique=True)),
                ('type_identification_document', models.CharField(default='cedula', max_length=10)),
                ('fisrt_name', models.CharField(max_length=25)),
                ('second_name', models.CharField(blank=True, max_length=25)),
                ('father_surname', models.CharField(max_length=25)),
                ('mother_surname', models.CharField(blank=True, max_length=25)),
                ('mobile', models.CharField(blank=True, max_length=10)),
                ('is_principal', models.BooleanField(default=False)),
                ('client_data', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='person_identification', to='clientData.clientdata')),
            ],
            options={
                'verbose_name': 'Datos de la persona',
                'verbose_name_plural': 'Datos de las personas',
            },
        ),
        migrations.CreateModel(
            name='MunicipalAccount',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(max_length=10)),
                ('password', models.CharField(max_length=50)),
                ('client_data', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='municipal_account', to='clientData.clientdata')),
            ],
        ),
        migrations.CreateModel(
            name='HousesClient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country', models.CharField(blank=True, default='Ecuador', max_length=50)),
                ('province', models.CharField(default='Guayas', max_length=50)),
                ('town', models.CharField(blank=True, default='Guayaquil', max_length=50)),
                ('parish', models.CharField(blank=True, max_length=100)),
                ('district', models.CharField(blank=True, max_length=100)),
                ('main_road_name', models.CharField(max_length=100)),
                ('cross_road_name', models.CharField(blank=True, max_length=100)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('client_data', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='houses_customer', to='clientData.clientdata')),
            ],
            options={
                'verbose_name': 'Casa del cliente',
                'verbose_name_plural': 'Casas del cliente',
            },
        ),
        migrations.CreateModel(
            name='Cadastral',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sector', models.CharField(max_length=3)),
                ('apple', models.CharField(max_length=4)),
                ('lot', models.CharField(max_length=3)),
                ('div1', models.CharField(blank=True, default='0', max_length=1)),
                ('div2', models.CharField(blank=True, default='0', max_length=1)),
                ('div3', models.CharField(blank=True, default='0', max_length=1)),
                ('div4', models.CharField(blank=True, default='1', max_length=1)),
                ('home_client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='house_cadastral', to='clientData.housesclient')),
            ],
        ),
    ]
