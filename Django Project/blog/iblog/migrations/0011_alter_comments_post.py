# Generated by Django 4.2.1 on 2023-05-22 11:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('iblog', '0010_alter_comments_post'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comments',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='text', to='iblog.post'),
        ),
    ]
