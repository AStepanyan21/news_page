# Generated by Django 3.1.7 on 2021-02-20 15:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0003_auto_20210220_1248'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='categories',
            options={'verbose_name_plural': 'Categories'},
        ),
        migrations.AlterModelOptions(
            name='news',
            options={'verbose_name_plural': 'News'},
        ),
        migrations.AlterField(
            model_name='news',
            name='categories',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='news.categories', verbose_name='News categories'),
        ),
    ]
