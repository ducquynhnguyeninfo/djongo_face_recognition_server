# Generated by Django 3.0.5 on 2021-03-21 12:30

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Model',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, max_length=200)),
                ('picture', models.CharField(blank=True, max_length=256)),
                ('price', models.FloatField(default=0)),
                ('brand', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='order_manager.Brand')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('client_name', models.CharField(max_length=200)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now, editable=False, verbose_name='created time')),
                ('last_modified_at', models.DateTimeField(verbose_name='last modified time')),
                ('total_money', models.FloatField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Pack',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('price', models.FloatField()),
                ('quantity', models.IntegerField(default=0)),
                ('model', models.ManyToManyField(to='order_manager.Model')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='order_manager.Order')),
            ],
        ),
    ]
