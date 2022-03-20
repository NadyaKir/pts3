# Generated by Django 3.2.7 on 2022-01-25 08:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Заголовок')),
                ('slug', models.SlugField(max_length=255, unique=True, verbose_name='URL(slug)')),
                ('brief', models.TextField(verbose_name='Краткое описание')),
                ('content', models.TextField(verbose_name='Контент')),
                ('photo', models.ImageField(upload_to='photos/%Y-%m-%d', verbose_name='Фото')),
                ('time_create', models.DateTimeField(auto_now_add=True, verbose_name='Время создания')),
                ('time_update', models.DateTimeField(auto_now=True, verbose_name='Время изменения')),
                ('is_published', models.BooleanField(default=True, verbose_name='Публикация')),
            ],
            options={
                'verbose_name': 'Новость',
                'verbose_name_plural': 'Новости',
                'ordering': ['time_create', 'title'],
            },
        ),
    ]
