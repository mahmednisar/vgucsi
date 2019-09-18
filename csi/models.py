from django.db import models
from django import forms

CLASS_CHOICES = (
    ('Dean Engineering','Dean Engineering'),
    ('Head of Department-CSE', 'Head of Department-CSE '),
    ('Faculty Coordinator','Faculty Coordinator' ),
    ('President','President' ),
    ( 'Vice-President', 'Vice-President'),
    ('Secretary', 'Secretary'),
    ('Technical Head', 'Technical Head'),
    ('Chief-Treasurer', 'Chief-Treasurer'),
    ('Treasurer','Treasurer'),
    ('Reception Incharge', 'Reception Incharge'),
    ('Event Coordinator', 'Event Coordinator'),
    ('Coordinator','Coordinator'),
    ('Chief Editor','Chief Editor'),
    ('Editor','Editor'),
    ('Discipline Coordinator', 'Discipline Coordinator'),
    ('Refreshment Incharge','Refreshment Incharge'),
    ('Class Representative','Class Representative')
)

# Create your models here.
class Blogpost(models.Model):
    post_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    sub_head = models.CharField(max_length=5000,blank=True,null=True, default="")
    content = models.TextField(blank=True,null=True)
    pub_date = models.DateField(auto_now=True)
    thumbnail = models.ImageField(upload_to='images/blog', default="")

    def __str__(self):
        return self.title


class Team(models.Model):
    member_id = models.IntegerField(default=0)
    member_name = models.CharField(max_length=50)
    member_class = models.CharField(max_length=50, choices=CLASS_CHOICES)
    csi=models.IntegerField(blank=True, default=0)
    member_url = models.CharField(max_length=50,blank=True, default="#")
    ln = models.CharField(max_length=50, blank=True, default="")
    ins = models.CharField(max_length=50, blank=True, default="")
    mail = models.CharField(max_length=100, blank=True, default="")
    whatsapp = models.CharField(max_length=50, blank=True, default="")
    member_image = models.ImageField(upload_to='images/team', default="")

    def __str__(self):
        return self.member_class


class Homebanner(models.Model):
    banner_id = models.AutoField(primary_key=True)
    banner_name = models.CharField(max_length=500, blank=True, default="")
    banner = models.ImageField(upload_to='images/banner', default="")

    def __str__(self):
        return self.banner_name


class Event(models.Model):
    event_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=500)
    event_date = models.DateField()
    subtitle = models.CharField(max_length=500, default="")
    content = models.TextField()
    image = models.ImageField(upload_to='images/events', default="")

    def __str__(self):
        return self.title


class Contact(models.Model):
    msg_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=70, default="")
    phone = models.CharField(max_length=70, default="")
    desc = models.TextField(null=True)

    def __str__(self):
        return self.name



