# Generated by Django 2.2 on 2019-10-27 17:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_auto_20191027_0817'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserComment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(default='guest@gmail.com', max_length=254)),
                ('firstname', models.CharField(max_length=200, null=True)),
                ('lastname', models.CharField(max_length=200, null=True)),
                ('comment', models.TextField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('blogpost', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.BlogPost')),
            ],
        ),
    ]
