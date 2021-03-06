# Generated by Django 2.2.7 on 2020-01-02 17:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0006_auto_20191225_0502'),
    ]

    operations = [
        migrations.RenameField(
            model_name='entry',
            old_name='week',
            new_name='day',
        ),
        migrations.RenameField(
            model_name='entry',
            old_name='Fri',
            new_name='done',
        ),
        migrations.RemoveField(
            model_name='entry',
            name='Mon',
        ),
        migrations.RemoveField(
            model_name='entry',
            name='Sat',
        ),
        migrations.RemoveField(
            model_name='entry',
            name='Sun',
        ),
        migrations.RemoveField(
            model_name='entry',
            name='Thu',
        ),
        migrations.RemoveField(
            model_name='entry',
            name='Tue',
        ),
        migrations.RemoveField(
            model_name='entry',
            name='Wed',
        ),
        migrations.AlterField(
            model_name='entry',
            name='mood',
            field=models.CharField(choices=[('Fantastic', '😄'), ('Meh', '😐'), ('Lamentable', '😔 ')], default='Meh', max_length=30),
        ),
        migrations.AlterField(
            model_name='entry',
            name='notes',
            field=models.CharField(max_length=800, verbose_name='Entry'),
        ),
    ]
