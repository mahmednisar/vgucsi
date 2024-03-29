# Generated by Django 2.2.4 on 2019-09-05 08:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blogpost',
            fields=[
                ('post_id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=50)),
                ('head0', models.CharField(default='', max_length=500)),
                ('chead0', models.CharField(default='', max_length=5000)),
                ('head1', models.CharField(default='', max_length=500)),
                ('chead1', models.CharField(default='', max_length=5000)),
                ('head2', models.CharField(default='', max_length=500)),
                ('chead2', models.CharField(default='', max_length=5000)),
                ('pub_date', models.DateField(auto_now=True)),
                ('thumbnail', models.ImageField(default='', upload_to='images/blog')),
            ],
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('msg_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('email', models.CharField(default='', max_length=70)),
                ('phone', models.CharField(default='', max_length=70)),
                ('desc', models.CharField(default='', max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('event_id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=50)),
                ('event_date', models.DateField()),
                ('subtitle', models.CharField(default='', max_length=50)),
                ('content', models.TextField()),
                ('image', models.ImageField(default='', upload_to='images/events')),
            ],
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('member_id', models.IntegerField(default=0)),
                ('member_name', models.CharField(max_length=50)),
                ('member_class', models.CharField(choices=[('Faculty Coordinator', 'Faculty Coordinator'), ('President', 'President'), ('Vice-President', 'Vice-President'), ('Secretary', 'Secretary'), ('TECHNICAL HEAD', 'Technical Head'), ('Chief-Treasurer', 'Chief-Treasurer'), ('Treasurer', 'Treasurer'), ('Reception Incharge', 'Reception Incharge'), ('Event Coordinator', 'Event Coordinator'), ('Coordinator', 'Coordinator'), ('Chief Editor', 'Chief Editor'), ('Editor', 'Editor'), ('Discipline Coordinator', 'Discipline Coordinator'), ('Refreshment Incharge', 'Refreshment Incharge'), ('Class Representative', 'Class Representative')], max_length=50)),
                ('csi', models.IntegerField(blank=True, default=0)),
                ('member_url', models.CharField(blank=True, default='', max_length=50)),
                ('ln', models.CharField(default='', max_length=50)),
                ('github', models.CharField(blank=True, default='', max_length=50)),
                ('ins', models.CharField(default='', max_length=50)),
                ('mail', models.CharField(default='', max_length=50)),
                ('twitter', models.CharField(default='', max_length=50)),
                ('facebook', models.CharField(default='', max_length=50)),
                ('telegram', models.CharField(blank=True, default='', max_length=50)),
                ('whatsapp', models.CharField(default='', max_length=50)),
                ('member_image', models.ImageField(default='', upload_to='images/team')),
            ],
        ),
    ]
