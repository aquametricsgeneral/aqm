# Generated by Django 2.0.4 on 2018-06-07 14:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EnvHumidity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('datetime', models.DateTimeField()),
                ('value', models.CharField(max_length=10)),
                ('threshold', models.CharField(max_length=10)),
                ('greater', models.CharField(max_length=5)),
                ('less', models.CharField(max_length=5)),
                ('criteria', models.CharField(max_length=10)),
                ('isalert', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='EnvTemp',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('datetime', models.DateTimeField()),
                ('value', models.CharField(max_length=10)),
                ('threshold', models.CharField(max_length=10)),
                ('greater', models.CharField(max_length=5)),
                ('less', models.CharField(max_length=5)),
                ('criteria', models.CharField(max_length=10)),
                ('isalert', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='IsFilling',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('datetime', models.DateTimeField()),
                ('value', models.CharField(max_length=10)),
                ('threshold', models.CharField(max_length=10)),
                ('greater', models.CharField(max_length=5)),
                ('less', models.CharField(max_length=5)),
                ('criteria', models.CharField(max_length=10)),
                ('isalert', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='WaterFlowFishTank',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('datetime', models.DateTimeField()),
                ('value', models.CharField(max_length=10)),
                ('threshold', models.CharField(max_length=10)),
                ('greater', models.CharField(max_length=5)),
                ('less', models.CharField(max_length=5)),
                ('criteria', models.CharField(max_length=10)),
                ('isalert', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='WaterFlowHorizGrow',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('datetime', models.DateTimeField()),
                ('value', models.CharField(max_length=10)),
                ('threshold', models.CharField(max_length=10)),
                ('greater', models.CharField(max_length=5)),
                ('less', models.CharField(max_length=5)),
                ('criteria', models.CharField(max_length=10)),
                ('isalert', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='WaterFlowMain',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('datetime', models.DateTimeField()),
                ('value', models.CharField(max_length=10)),
                ('threshold', models.CharField(max_length=10)),
                ('greater', models.CharField(max_length=5)),
                ('less', models.CharField(max_length=5)),
                ('criteria', models.CharField(max_length=10)),
                ('isalert', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='WaterFlowVertGrow',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('datetime', models.DateTimeField()),
                ('value', models.CharField(max_length=10)),
                ('threshold', models.CharField(max_length=10)),
                ('greater', models.CharField(max_length=5)),
                ('less', models.CharField(max_length=5)),
                ('criteria', models.CharField(max_length=10)),
                ('isalert', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='WaterLevelFull',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('datetime', models.DateTimeField()),
                ('value', models.CharField(max_length=10)),
                ('threshold', models.CharField(max_length=10)),
                ('greater', models.CharField(max_length=5)),
                ('less', models.CharField(max_length=5)),
                ('criteria', models.CharField(max_length=10)),
                ('isalert', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='WaterLevelLow',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('datetime', models.DateTimeField()),
                ('value', models.CharField(max_length=10)),
                ('threshold', models.CharField(max_length=10)),
                ('greater', models.CharField(max_length=5)),
                ('less', models.CharField(max_length=5)),
                ('criteria', models.CharField(max_length=10)),
                ('isalert', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='WaterPH',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('datetime', models.DateTimeField()),
                ('value', models.CharField(max_length=10)),
                ('threshold', models.CharField(max_length=10)),
                ('greater', models.CharField(max_length=5)),
                ('less', models.CharField(max_length=5)),
                ('criteria', models.CharField(max_length=10)),
                ('isalert', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='WaterTempFishTank',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('datetime', models.DateTimeField()),
                ('value', models.CharField(max_length=10)),
                ('threshold', models.CharField(max_length=10)),
                ('greater', models.CharField(max_length=5)),
                ('less', models.CharField(max_length=5)),
                ('criteria', models.CharField(max_length=10)),
                ('isalert', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='WaterTempSumpTank',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('datetime', models.DateTimeField()),
                ('value', models.CharField(max_length=10)),
                ('threshold', models.CharField(max_length=10)),
                ('greater', models.CharField(max_length=5)),
                ('less', models.CharField(max_length=5)),
                ('criteria', models.CharField(max_length=10)),
                ('isalert', models.CharField(max_length=10)),
            ],
        ),
    ]
