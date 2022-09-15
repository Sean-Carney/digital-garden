# Generated by Django 4.1 on 2022-09-15 02:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0002_alter_note_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='notelink',
            name='note',
        ),
        migrations.RemoveField(
            model_name='notelink',
            name='url',
        ),
        migrations.AddField(
            model_name='notelink',
            name='reference',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='reference', to='notes.note'),
        ),
        migrations.AddField(
            model_name='notelink',
            name='source',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='source', to='notes.note'),
        ),
    ]
