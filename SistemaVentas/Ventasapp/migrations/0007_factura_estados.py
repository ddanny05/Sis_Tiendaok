# Generated by Django 5.1.3 on 2024-11-27 04:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Ventasapp', '0006_remove_factura_cantidad_original'),
    ]

    operations = [
        migrations.AddField(
            model_name='factura',
            name='estados',
            field=models.CharField(choices=[('V', 'Vendida'), ('A', 'Anulada')], default=1, max_length=40),
            preserve_default=False,
        ),
    ]