# Generated by Django 2.2.2 on 2019-06-07 06:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('example_app', '0003_auto_20190607_0053'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='status',
            field=models.CharField(max_length=5),
        ),
    ]
