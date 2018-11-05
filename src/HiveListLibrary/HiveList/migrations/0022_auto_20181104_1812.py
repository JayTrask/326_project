# Generated by Django 2.1.1 on 2018-11-04 18:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('HiveList', '0021_remove_contributor_playlist_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contributors',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.RemoveField(
            model_name='voteinstance',
            name='contributor_id',
        ),
        migrations.RemoveField(
            model_name='voteinstance',
            name='playlist_id',
        ),
        migrations.RemoveField(
            model_name='voteinstance',
            name='song_id',
        ),
        migrations.RemoveField(
            model_name='playlist',
            name='playlist_creator_id',
        ),
        migrations.RemoveField(
            model_name='songinstance',
            name='contributor_id',
        ),
        migrations.DeleteModel(
            name='Contributor',
        ),
        migrations.DeleteModel(
            name='VoteInstance',
        ),
        migrations.AddField(
            model_name='contributors',
            name='playlist_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='HiveList.Playlist'),
        ),
    ]