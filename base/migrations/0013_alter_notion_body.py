# Generated by Django 3.2.3 on 2021-12-24 15:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0012_notion_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notion',
            name='body',
            field=models.TextField(),
        ),
    ]
