# Generated by Django 3.1.3 on 2021-07-16 13:54

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('santri', '0005_auto_20210714_2307'),
    ]

    operations = [
        migrations.AlterField(
            model_name='santri',
            name='nama_santri',
            field=models.CharField(default=django.utils.timezone.now, max_length=200),
            preserve_default=False,
        ),
    ]