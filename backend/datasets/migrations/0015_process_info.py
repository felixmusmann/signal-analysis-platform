# Generated by Django 2.2.5 on 2019-09-30 09:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('datasets', '0014_auto_20190930_0922'),
    ]

    operations = [
        migrations.AddField(
            model_name='process',
            name='info',
            field=models.TextField(blank=True),
        ),
    ]