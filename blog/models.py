# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.utils import timezone
from django.db import models
# Create your models here.

class Category(models.Model):
    baslik = models.CharField(max_length=250)
    aciklama = models.CharField(max_length=500)

    def __str__(self):
        return self.baslik

class Post(models.Model):
    baslik = models.CharField(max_length=250)
    govde = models.TextField()
    kategory = models.ForeignKey(Category)
    ekleme_tarihi = models.DateField(default=timezone.now)
    yayinda_mi = models.BooleanField(default=1)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.baslik

    def __unicode__(self):
        return self.slug

class etiket(models.Model):
    yazi = models.CharField(max_length=250, unique=True)

    def __str__(self):
        return self.yazi