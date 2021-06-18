# Generated by Django 3.1.7 on 2021-06-17 10:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('PharmApp', '0003_auto_20210601_2354'),
    ]

    operations = [
        migrations.CreateModel(
            name='Delivery',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('person_name', models.CharField(max_length=255)),
                ('person_email', models.CharField(max_length=255)),
                ('person_tel', models.CharField(max_length=255)),
                ('person_city', models.CharField(max_length=255)),
                ('person_Address', models.CharField(max_length=255)),
                ('person_wish', models.TextField()),
                ('drug_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='PharmApp.drugs')),
            ],
        ),
    ]