# Generated by Django 5.0.6 on 2024-06-25 22:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_alter_cover_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cover',
            name='name',
            field=models.TextField(verbose_name='Title (underline)'),
        ),
    ]