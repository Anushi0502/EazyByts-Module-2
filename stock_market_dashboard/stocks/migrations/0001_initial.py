# Generated by Django 3.2.25 on 2025-02-22 10:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Portfolio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Stock',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('symbol', models.CharField(max_length=10, unique=True)),
                ('name', models.CharField(max_length=100)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('last_updated', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='StockHolding',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField()),
                ('purchase_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('portfolio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stocks.portfolio')),
                ('stock', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stocks.stock')),
            ],
        ),
        migrations.AddField(
            model_name='portfolio',
            name='stocks',
            field=models.ManyToManyField(through='stocks.StockHolding', to='stocks.Stock'),
        ),
        migrations.AddField(
            model_name='portfolio',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
