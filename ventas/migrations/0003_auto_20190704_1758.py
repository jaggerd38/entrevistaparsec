# Generated by Django 2.2.3 on 2019-07-04 17:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ventas', '0002_auto_20190704_1746'),
    ]

    operations = [
        migrations.AddField(
            model_name='encabezado',
            name='id',
            field=models.AutoField(auto_created=True, default=1, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='encabezado',
            name='no_venta',
            field=models.IntegerField(default=1001, unique=True),
        ),
    ]
