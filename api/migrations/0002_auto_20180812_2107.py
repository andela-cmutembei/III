# Generated by Django 2.1 on 2018-08-12 21:07

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='bucketlist',
            options={'verbose_name': 'Bucketlist'},
        ),
        migrations.AlterModelOptions(
            name='item',
            options={'verbose_name': 'Bucketlist Item'},
        ),
        migrations.AlterField(
            model_name='bucketlist',
            name='name',
            field=models.CharField(max_length=45),
        ),
        migrations.AlterField(
            model_name='item',
            name='name',
            field=models.CharField(max_length=45),
        ),
        migrations.AlterUniqueTogether(
            name='bucketlist',
            unique_together={('name', 'created_by')},
        ),
        migrations.AlterUniqueTogether(
            name='item',
            unique_together={('name', 'parent_bucketlist')},
        ),
    ]
