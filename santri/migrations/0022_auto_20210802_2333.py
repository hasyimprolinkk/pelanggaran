# Generated by Django 3.1.2 on 2021-08-02 16:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('santri', '0021_auto_20210802_2328'),
    ]

    operations = [
        migrations.AlterField(
            model_name='santri',
            name='nama_wali',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='walisantris', to='santri.walisantri'),
        ),
    ]
