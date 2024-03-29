# Generated by Django 3.1.2 on 2021-02-04 21:23

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('world', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TestProperty',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=100)),
                ('lon', models.FloatField()),
                ('lat', models.FloatField()),
                ('date_posted', models.DateTimeField(default=django.utils.timezone.now)),
                ('rent', models.IntegerField()),
                ('propertyType', models.CharField(max_length=100)),
            ],
        ),
        migrations.DeleteModel(
            name='Prop',
        ),
    ]
