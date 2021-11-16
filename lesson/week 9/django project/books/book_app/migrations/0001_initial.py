# Generated by Django 3.2.9 on 2021-11-15 04:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('age', models.IntegerField()),
                ('bio', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Books',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('inn', models.CharField(max_length=13)),
                ('publish_date', models.DateField()),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='book_app.author')),
            ],
        ),
        migrations.CreateModel(
            name='ImageBook',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='image_book')),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='book_app.books')),
            ],
        ),
    ]
