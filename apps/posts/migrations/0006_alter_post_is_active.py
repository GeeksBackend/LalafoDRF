# Generated by Django 4.2 on 2023-05-18 14:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0005_post_is_active'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='is_active',
            field=models.BooleanField(default=True, verbose_name='Статус поста'),
        ),
    ]
