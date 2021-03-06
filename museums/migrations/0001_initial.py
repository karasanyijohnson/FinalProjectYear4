# Generated by Django 3.1.4 on 2020-12-19 19:19

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
            name='Museum',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(choices=[('CAMPAIGN AGAINST GENOCIDE', 'CAMPAIGN AGAINST GENOCIDE'), ('RWANDA ART', 'RWANDA ART'), ("KING'S PALACE", "KING'S PALACE"), ('NATIONAL LIBERATION', 'NATIONAL LIBERATION'), ('ENVIRONMENT', 'ENVIRONMENT'), ('KWIGIRA', 'KWIGIRA'), ("KANDT'S HOUSE", "KANDT'S HOUSE")], max_length=50)),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('image', models.ImageField(upload_to='media/museums')),
                ('location', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('check_in', models.DateTimeField()),
                ('check_out', models.DateTimeField()),
                ('museum', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='museums.museum')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
