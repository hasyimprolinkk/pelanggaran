# Generated by Django 3.1.3 on 2021-07-23 01:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('santri', '0016_auto_20210720_2200'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True)),
                ('start_date', models.DateField()),
            ],
        ),
    ]
