# Generated by Django 5.0.2 on 2024-02-14 12:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Charger',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(max_length=20)),
                ('power_volt', models.IntegerField()),
                ('charger_type', models.CharField(max_length=5)),
                ('shop_name', models.CharField(max_length=10)),
            ],
        ),
    ]
