# Generated by Django 3.1.7 on 2021-03-02 07:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0004_auto_20210302_1017'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ('-id',)},
        ),
        migrations.AlterModelOptions(
            name='genre',
            options={'ordering': ('-id',)},
        ),
    ]