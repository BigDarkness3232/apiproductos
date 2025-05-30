# Generated by Django 5.2.1 on 2025-05-17 17:33

from django.db import migrations, models
import cloudinary.models

class Migration(migrations.Migration):

    dependencies = [
        ('mi_api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imagen', models.ImageField(blank=True, null=True, upload_to='productos')),
                ('nombre_producto', models.CharField(max_length=255)),
                ('descripcion', models.TextField()),
                ('categoria', models.CharField(max_length=100)),
                ('precio', models.DecimalField(decimal_places=2, max_digits=10)),
                ('stock', models.IntegerField()),
            ],
            options={
                'db_table': 'SunnyApp_producto',
                'managed': False,
            },
        ),
        migrations.DeleteModel(
            name='Orden',
        ),
            migrations.AlterField(
            model_name='producto',
            name='imagen',
            field=cloudinary.models.CloudinaryField(blank=True, max_length=255, null=True, verbose_name='imagen'),
        ),
    ]
