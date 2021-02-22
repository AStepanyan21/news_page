# Generated by Django 3.1.7 on 2021-02-20 12:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categories',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(db_index=True, max_length=50, verbose_name='News title')),
                ('text', models.TextField(verbose_name='News text')),
                ('categories', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='news.categories', verbose_name='News categories')),
                ('sub_categories', models.ManyToManyField(null=True, related_name='provider', to='news.Categories', verbose_name='List for sub categories')),
            ],
        ),
    ]
