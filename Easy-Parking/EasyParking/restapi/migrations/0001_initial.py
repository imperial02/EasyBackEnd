# Generated by Django 2.1.2 on 2018-11-22 07:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Parking',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_parking', models.IntegerField()),
                ('location', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=100)),
                ('total_places', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Place',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('place_status', models.IntegerField()),
                ('device_id', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Section',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('total_places', models.IntegerField()),
                ('parking', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='restapi.Parking')),
            ],
        ),
        migrations.AddField(
            model_name='place',
            name='section',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='restapi.Section'),
        ),
    ]
