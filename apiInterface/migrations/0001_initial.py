# Generated by Django 3.0.8 on 2020-07-20 18:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='dashboardData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('onroad', models.IntegerField()),
                ('available', models.IntegerField()),
                ('mostInDemandLoc', models.CharField(max_length=40)),
                ('mostInDemandMod', models.CharField(max_length=40)),
            ],
        ),
    ]
