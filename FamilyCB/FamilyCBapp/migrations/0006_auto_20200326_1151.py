# Generated by Django 3.0.3 on 2020-03-26 16:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('FamilyCBapp', '0005_auto_20200326_1148'),
    ]

    operations = [
        migrations.RenameField(
            model_name='recipe',
            old_name='memberId',
            new_name='member',
        ),
    ]