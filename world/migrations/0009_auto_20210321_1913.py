# Generated by Django 3.1.2 on 2021-03-21 19:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
        ('world', '0008_userfaves'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userfaves',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.profile'),
        ),
    ]
