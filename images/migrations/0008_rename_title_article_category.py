# Generated by Django 4.0.3 on 2022-03-27 20:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('images', '0007_article_remove_category_title'),
    ]

    operations = [
        migrations.RenameField(
            model_name='article',
            old_name='title',
            new_name='category',
        ),
    ]
