# Generated by Django 3.1.2 on 2021-02-08 19:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('world', '0004_testproperty'),
    ]

    operations = [
        migrations.AlterField(
            model_name='testproperty',
            name='rent',
            field=models.CharField(max_length=100),
        ),
    ]
