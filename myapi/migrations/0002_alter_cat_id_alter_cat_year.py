# Generated by Django 4.1.4 on 2022-12-15 11:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapi', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cat',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='cat',
            name='year',
            field=models.DecimalField(decimal_places=0, max_digits=3),
        ),
    ]
