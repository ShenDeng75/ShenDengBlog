# Generated by Django 2.1.7 on 2019-03-17 14:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, unique=True, verbose_name='标签名')),
                ('count', models.IntegerField(blank=True, default=0, max_length=11, verbose_name='包含的数量')),
            ],
            options={
                'verbose_name': '网址标签',
                'db_table': 'category',
            },
        ),
        migrations.CreateModel(
            name='Website',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='名称')),
                ('url', models.URLField(unique=True, verbose_name='链接')),
                ('describe', models.TextField(max_length=150, verbose_name='描述')),
                ('create_date', models.DateField(auto_now_add=True, null=True, verbose_name='创建时间')),
                ('edit_date', models.DateField(auto_now=True, null=True, verbose_name='修改时间')),
                ('belong', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='创建者')),
                ('category', models.ManyToManyField(to='website.Category', verbose_name='标签')),
            ],
            options={
                'verbose_name': '网址',
                'db_table': 'website',
            },
        ),
    ]
