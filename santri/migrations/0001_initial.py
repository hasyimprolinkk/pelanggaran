# Generated by Django 3.1.3 on 2021-07-13 09:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pengguna',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama_pengguna', models.CharField(blank=True, max_length=200)),
                ('staff', models.CharField(blank=True, choices=[('Kepala Pondok', 'Kepala Pondok'), ('Keamanan', 'Keamanan'), ('Pendidikan', 'Pendidikan'), ('Sekertaris', 'Sekertaris')], max_length=200)),
                ('no_telpon', models.CharField(blank=True, max_length=200)),
            ],
            options={
                'verbose_name_plural': 'Pengguna',
            },
        ),
        migrations.CreateModel(
            name='WaliSantri',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama_wali', models.CharField(blank=True, max_length=200, null=True)),
                ('alamat', models.CharField(blank=True, max_length=200, null=True)),
                ('no_telpon', models.CharField(blank=True, max_length=200, null=True)),
            ],
            options={
                'verbose_name_plural': 'Wali Santri',
            },
        ),
        migrations.CreateModel(
            name='Santri',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('no_induk', models.CharField(max_length=10, unique=True)),
                ('nama_santri', models.CharField(blank=True, max_length=200, null=True)),
                ('tgl_lahir', models.DateField()),
                ('alamat', models.CharField(blank=True, max_length=200, null=True)),
                ('pendidikan', models.CharField(blank=True, choices=[('UNIVERSITAS ZAINUL HASAN', 'UNIVERSITAS ZAINUL HASAN'), ('SMA Zainul Hasan', 'SMA Zainul Hasan'), ('MA Zainul Hasan', 'MA Zainul Hasan'), ('SMP Zainul Hasan', 'SMP Zainul Hasan'), ('MTS Zainul Hasan', 'MTS Zainul Hasan')], max_length=150, null=True)),
                ('id_wali', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='santri.walisantri')),
            ],
            options={
                'verbose_name_plural': 'Santri',
            },
        ),
    ]