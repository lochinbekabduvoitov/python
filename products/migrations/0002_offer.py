# Generated by Django 3.2.19 on 2023-06-16 11:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Offer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=255)),
                ('desciption', models.CharField(max_length=522)),
                ('discount', models.FloatField()),
            ],
        ),
    ]