# Generated by Django 2.1.2 on 2018-10-21 06:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('unravel', '0004_documentversion'),
    ]

    operations = [
        migrations.CreateModel(
            name='DocumentResult',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(auto_now=True)),
                ('archived_date', models.DateTimeField(blank=True, null=True)),
                ('archived_user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='unravel_documentresult_archived', related_query_name='unravel_documentresult_archivers', to=settings.AUTH_USER_MODEL)),
                ('created_user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='unravel_documentresult_created', related_query_name='unravel_documentresult_creators', to=settings.AUTH_USER_MODEL)),
                ('documents', models.ManyToManyField(help_text='Documents that were analysed.', related_name='results', to='unravel.Document')),
                ('updated_user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='unravel_documentresult_updated', related_query_name='unravel_documentresult_updaters', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Document Result',
                'verbose_name_plural': 'Document Results',
            },
        ),
    ]
