# Generated by Django 3.0.7 on 2020-06-26 21:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('extraactivity', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='extraactivity',
            name='graduation_details',
            field=models.CharField(max_length=400),
        ),
    ]
