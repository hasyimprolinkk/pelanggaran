# Generated by Django 3.1.3 on 2021-08-20 17:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('santri', '0027_auto_20210821_0013'),
    ]

    operations = [
        migrations.AddField(
            model_name='santri',
            name='foto',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
