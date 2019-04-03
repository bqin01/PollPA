# Generated by Django 2.1.7 on 2019-04-03 00:19

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='poll',
            old_name='text',
            new_name='title',
        ),
        migrations.RenameField(
            model_name='vote',
            old_name='year',
            new_name='grade',
        ),
        migrations.AddField(
            model_name='poll',
            name='public',
            field=models.DateTimeField(db_index=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='question',
            name='chart',
            field=models.CharField(choices=[('bar', 'Bar Chart'), ('binary-slider', 'Binary Slider'), ('pie', 'Pie Chart')], default='bar', max_length=20),
        ),
        migrations.AddField(
            model_name='question',
            name='kind',
            field=models.CharField(choices=[('MS', 'Multiple Select (Checkboxes)'), ('SS', 'Single Select (Radio)')], default='SS', max_length=2),
        ),
        migrations.AlterField(
            model_name='poll',
            name='description',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='poll',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='question',
            name='description',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='questionoption',
            name='description',
            field=models.TextField(blank=True),
        ),
    ]
