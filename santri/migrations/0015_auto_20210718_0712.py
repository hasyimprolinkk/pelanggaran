# Generated by Django 3.1.3 on 2021-07-18 00:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('santri', '0014_auto_20210718_0637'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pelanggaran',
            name='nama_wali',
        ),
        migrations.RemoveField(
            model_name='pelanggaran',
            name='santri',
        ),
    ]
