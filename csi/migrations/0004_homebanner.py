# Generated by Django 2.2.5 on 2019-09-18 12:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('csi', '0003_auto_20190918_1134'),
    ]

    operations = [
        migrations.CreateModel(
            name='Homebanner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('banner_id', models.IntegerField(default=0)),
                ('banner', models.ImageField(default='', upload_to='images/banner')),
            ],
        ),
    ]
