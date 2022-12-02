# Generated by Django 4.0.3 on 2022-04-29 08:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Authored',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mm_relation.author')),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('authors', models.ManyToManyField(through='mm_relation.Authored', to='mm_relation.author')),
            ],
        ),
        migrations.AddField(
            model_name='authored',
            name='book',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mm_relation.book'),
        ),
        migrations.AddField(
            model_name='author',
            name='books',
            field=models.ManyToManyField(through='mm_relation.Authored', to='mm_relation.book'),
        ),
    ]
