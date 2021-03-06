# Generated by Django 2.0.4 on 2018-06-11 00:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('monitor', '0014_auto_20180611_0851'),
    ]

    operations = [
        migrations.AlterField(
            model_name='envtemp',
            name='alert',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='envtemp',
            name='lowerlimit',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=5),
        ),
        migrations.AlterField(
            model_name='envtemp',
            name='upperlimit',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=5),
        ),
        migrations.AlterField(
            model_name='envtemp',
            name='value',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=5),
        ),
        migrations.AlterField(
            model_name='envtemp',
            name='withinlimit',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='isfilling',
            name='alert',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='isfilling',
            name='lowerlimit',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=5),
        ),
        migrations.AlterField(
            model_name='isfilling',
            name='upperlimit',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=5),
        ),
        migrations.AlterField(
            model_name='isfilling',
            name='value',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=5),
        ),
        migrations.AlterField(
            model_name='isfilling',
            name='withinlimit',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='waterflowfishtank',
            name='alert',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='waterflowfishtank',
            name='lowerlimit',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=5),
        ),
        migrations.AlterField(
            model_name='waterflowfishtank',
            name='upperlimit',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=5),
        ),
        migrations.AlterField(
            model_name='waterflowfishtank',
            name='value',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=5),
        ),
        migrations.AlterField(
            model_name='waterflowfishtank',
            name='withinlimit',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='waterflowhorizgrow',
            name='alert',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='waterflowhorizgrow',
            name='lowerlimit',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=5),
        ),
        migrations.AlterField(
            model_name='waterflowhorizgrow',
            name='upperlimit',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=5),
        ),
        migrations.AlterField(
            model_name='waterflowhorizgrow',
            name='value',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=5),
        ),
        migrations.AlterField(
            model_name='waterflowhorizgrow',
            name='withinlimit',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='waterflowmain',
            name='alert',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='waterflowmain',
            name='lowerlimit',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=5),
        ),
        migrations.AlterField(
            model_name='waterflowmain',
            name='upperlimit',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=5),
        ),
        migrations.AlterField(
            model_name='waterflowmain',
            name='value',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=5),
        ),
        migrations.AlterField(
            model_name='waterflowmain',
            name='withinlimit',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='waterflowvertgrow',
            name='alert',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='waterflowvertgrow',
            name='lowerlimit',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=5),
        ),
        migrations.AlterField(
            model_name='waterflowvertgrow',
            name='upperlimit',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=5),
        ),
        migrations.AlterField(
            model_name='waterflowvertgrow',
            name='value',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=5),
        ),
        migrations.AlterField(
            model_name='waterflowvertgrow',
            name='withinlimit',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='waterlevelfull',
            name='alert',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='waterlevelfull',
            name='lowerlimit',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=5),
        ),
        migrations.AlterField(
            model_name='waterlevelfull',
            name='upperlimit',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=5),
        ),
        migrations.AlterField(
            model_name='waterlevelfull',
            name='value',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=5),
        ),
        migrations.AlterField(
            model_name='waterlevelfull',
            name='withinlimit',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='waterlevellow',
            name='alert',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='waterlevellow',
            name='lowerlimit',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=5),
        ),
        migrations.AlterField(
            model_name='waterlevellow',
            name='upperlimit',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=5),
        ),
        migrations.AlterField(
            model_name='waterlevellow',
            name='value',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=5),
        ),
        migrations.AlterField(
            model_name='waterlevellow',
            name='withinlimit',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='waterph',
            name='alert',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='waterph',
            name='lowerlimit',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=5),
        ),
        migrations.AlterField(
            model_name='waterph',
            name='upperlimit',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=5),
        ),
        migrations.AlterField(
            model_name='waterph',
            name='value',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=5),
        ),
        migrations.AlterField(
            model_name='waterph',
            name='withinlimit',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='watertempfishtank',
            name='alert',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='watertempfishtank',
            name='lowerlimit',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=5),
        ),
        migrations.AlterField(
            model_name='watertempfishtank',
            name='upperlimit',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=5),
        ),
        migrations.AlterField(
            model_name='watertempfishtank',
            name='value',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=5),
        ),
        migrations.AlterField(
            model_name='watertempfishtank',
            name='withinlimit',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='watertempsumptank',
            name='alert',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='watertempsumptank',
            name='lowerlimit',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=5),
        ),
        migrations.AlterField(
            model_name='watertempsumptank',
            name='upperlimit',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=5),
        ),
        migrations.AlterField(
            model_name='watertempsumptank',
            name='value',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=5),
        ),
        migrations.AlterField(
            model_name='watertempsumptank',
            name='withinlimit',
            field=models.BooleanField(default=True),
        ),
    ]
