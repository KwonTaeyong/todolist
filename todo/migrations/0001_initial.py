# Generated by Django 4.0.2 on 2022-02-24 00:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TodoList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40, verbose_name='할일제목')),
                ('description', models.TextField(max_length=200, verbose_name='할일세부사항')),
                ('date_created', models.DateField(auto_now_add=True, verbose_name='생성날짜')),
                ('date_deadline', models.DateField(verbose_name='데드라인')),
            ],
        ),
        migrations.CreateModel(
            name='TodoList_images',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, upload_to='todo/images/%Y/%m')),
                ('todo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='todo.todolist')),
            ],
        ),
        migrations.CreateModel(
            name='TodoList_files',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('files', models.FileField(blank=True, upload_to='todo/files/%Y/%m')),
                ('todo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='todo.todolist')),
            ],
        ),
    ]
