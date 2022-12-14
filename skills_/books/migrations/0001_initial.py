# Generated by Django 4.0.3 on 2022-03-21 01:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, verbose_name='Nombre')),
                ('isbn', models.IntegerField(default=0, verbose_name='ISBN')),
                ('publisher_date', models.DateField(verbose_name='Fecha publicación')),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='Fecha creación')),
            ],
            options={
                'db_table': 'books',
            },
        ),
    ]
