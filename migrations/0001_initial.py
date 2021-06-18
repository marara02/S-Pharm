# Generated by Django 3.1.7 on 2021-05-30 12:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Drugs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='')),
                ('name', models.CharField(max_length=255)),
                ('cost', models.CharField(max_length=200)),
                ('pharmacy', models.CharField(max_length=255)),
                ('address', models.TextField()),
                ('number', models.CharField(max_length=255)),
            ],
        ),
    ]