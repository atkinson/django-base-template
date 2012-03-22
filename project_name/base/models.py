import uuid

from django.db import models
from django.utils.translation import ugettext_lazy as _

from userena.models import UserenaBaseProfile

class Profile(UserenaBaseProfile):
    user = models.OneToOneField('auth.User',
        unique=True,
        verbose_name=_('user'),
        related_name='profile')
    apps = models.ManyToManyField('saas.App', through='saas.Subscription')


class Subscription(models.Model):
    user = models.ForeignKey('base.Profile')
    app  = models.ForeignKey('base.App')
    plan = models.ForeignKey('base.Plan')


class Plan(models.Model):
    name = models.CharField(max_length=60)
    short_name = models.CharField(max_length=4)
    app = models.ForeignKey('base.App')


def new_uuid():
    return uuid.uuid4().hex

class App(models.Model):
    title = models.CharField(max_length=64)
    uuid = models.CharField(max_length=32, default=new_uuid, editable=False, db_index=True)
    user = models.ForeignKey('auth.User')