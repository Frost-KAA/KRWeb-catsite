# Generated by Django 4.1.4 on 2022-12-15 11:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapi', '0002_alter_cat_id_alter_cat_year'),
    ]

    operations = [
        migrations.AddField(
            model_name='cat',
            name='upload',
            field=models.ImageField(default=' ', upload_to='uploads/'),
            preserve_default=False,
        ),
    ]
