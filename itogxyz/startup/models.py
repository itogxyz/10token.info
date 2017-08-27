from django.db import models
from django.utils import timezone
# from django.contrib.auth.models import User
from django.conf import settings


class Startup(models.Model):
    name = models.CharField('Startup name', max_length=100)
    description = models.TextField('Description')
    logo = models.ImageField(blank=True,null=True)
    goal = models.IntegerField('Goal')
    vip = models.BooleanField(default=False)
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    wallet = models.CharField('Wallet', max_length=100)

    website = models.CharField('Website', max_length=100)

    created_date = models.DateTimeField(
            default=timezone.now)
    launch_date = models.DateTimeField(
            default=timezone.now, blank=False, null=True)


    def publish(self):
        self.launch_date = timezone.now()
        self.save()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('startups:detail', kwargs={'token_id': self.token_id})


class Investor(models.Model):
    # startup = models.OneToManyField(Startup) #Привязка к Asset (выше) 1 to 1

    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    wallet = models.CharField('Wallet', max_length=100)
    # startups = models.ManyToManyField(Startup)

    passport = models.ImageField(blank=False)

    created_date = models.DateTimeField(
            default=timezone.now)

    def __str__(self):
        return self.user.name


class Order(models.Model):
    investor = models.OneToOneField(Investor)
    startup = models.OneToOneField(Startup)

    amount = models.IntegerField()

    created_date = models.DateTimeField(
            default=timezone.now)
