# Generated by Django 4.1.7 on 2023-05-17 17:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('imagehub', '0004_alter_post_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='create_date',
            field=models.DateField(auto_now_add=True),
        ),
    ]