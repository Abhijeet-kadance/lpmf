# Generated by Django 4.0 on 2021-12-20 05:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Others', '0006_auto_20211217_1714'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='category_name',
            field=models.CharField(choices=[('Citizen', 'Citizen'), ('Android', 'Android'), ('Developer', 'Developer'), ('Translator', 'Translator')], max_length=50),
        ),
    ]
