# Generated by Django 3.2.4 on 2021-06-17 20:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PharmApp', '0008_auto_20210617_2159'),
    ]

    operations = [
        migrations.CreateModel(
            name='Apteks',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pharm_name', models.CharField(max_length=255)),
                ('pharm_city', models.CharField(max_length=255)),
                ('pharm_working_schedule', models.CharField(max_length=255)),
                ('url', models.CharField(max_length=255)),
                ('pharm_telephone', models.CharField(max_length=255)),
            ],
        ),
    ]
