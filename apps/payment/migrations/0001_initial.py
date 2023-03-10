# Generated by Django 4.1.7 on 2023-03-09 11:54
from __future__ import annotations

import django.db.models.deletion
from django.conf import settings
from django.db import migrations
from django.db import models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('courses', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Payment',
            fields=[
                (
                    'id', models.BigAutoField(
                        auto_created=True,
                        primary_key=True, serialize=False, verbose_name='ID',
                    ),
                ),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                (
                    'price', models.DecimalField(
                        decimal_places=2,
                        max_digits=10, verbose_name='Price',
                    ),
                ),
                (
                    'payment_type', models.CharField(
                        choices=[
                            ('Click', 'Click'), ('Payme', 'Payme'), (
                                'Paynet', 'Paynet',
                            ), ('Visa', 'Visa'),
                        ], max_length=255, verbose_name='Payment Type',
                    ),
                ),
                (
                    'payment_status', models.CharField(
                        choices=[
                            ('Pending', 'Pending'), ('Success', 'Success'), (
                                'Failed', 'Failed',
                            ),
                        ], max_length=255, verbose_name='Payment Status',
                    ),
                ),
                (
                    'course', models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to='courses.course', verbose_name='Course',
                    ),
                ),
                (
                    'user', models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL, verbose_name='User',
                    ),
                ),
            ],
            options={
                'verbose_name': 'Payment',
                'verbose_name_plural': 'Payments',
            },
        ),
    ]