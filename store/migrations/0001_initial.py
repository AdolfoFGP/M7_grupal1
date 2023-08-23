# Generated by Django 4.2.4 on 2023-08-09 01:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=70)),
                ('descripcion', models.TextField()),
                ('precio', models.IntegerField()),
                ('imagen', models.ImageField(default='store/img/default_image.jpg', null=True, upload_to='store/img')),
            ],
        ),
    ]
