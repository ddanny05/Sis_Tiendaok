# Generated by Django 5.1.3 on 2024-11-23 04:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Ventasapp', '0005_alter_factura_cantidad_original'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='factura',
            name='cantidad_original',
        ),
    ]