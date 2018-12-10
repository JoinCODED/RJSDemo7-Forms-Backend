# Generated by Django 2.1.4 on 2018-12-10 07:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forms', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='person',
            old_name='first_name',
            new_name='alias',
        ),
        migrations.RenameField(
            model_name='person',
            old_name='last_name',
            new_name='description',
        ),
        migrations.RemoveField(
            model_name='person',
            name='age',
        ),
        migrations.AddField(
            model_name='person',
            name='email',
            field=models.EmailField(default='ll@ugiu.rgred', max_length=254),
            preserve_default=False,
        ),
    ]
