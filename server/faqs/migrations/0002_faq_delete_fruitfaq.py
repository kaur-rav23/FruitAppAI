# Generated by Django 5.1.1 on 2024-09-14 18:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('faqs', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='FAQ',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fruit_name', models.CharField(max_length=100)),
                ('question', models.TextField()),
                ('answer', models.TextField()),
            ],
        ),
        migrations.DeleteModel(
            name='FruitFAQ',
        ),
    ]
