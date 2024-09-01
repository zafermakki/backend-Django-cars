# Generated by Django 3.2.19 on 2024-01-17 09:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250, unique=True)),
                ('image_path', models.ImageField(upload_to='categories/')),
            ],
            options={
                'db_table': 'categories',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('price', models.DecimalField(decimal_places=4, max_digits=20)),
                ('image_path', models.ImageField(upload_to='categories/')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='products.category')),
            ],
            options={
                'db_table': 'products',
            },
        ),
    ]
