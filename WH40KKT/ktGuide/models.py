from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class Army(models.Model):
    name = models.CharField(max_length=50)
    bio = models.CharField(max_length=1000)

    def __str__(self):
        return self.name

class Ability(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=1000)
    
    def __str__(self):
        return self.name

class Specialist(models.Model):
    name = models.CharField(max_length=50)

class Weapon(models.Model):
    army = models.ForeignKey(Army, on_delete=models.PROTECT) 
    name = models.CharField(max_length=50)
    weapon_range = models.CharField(max_length=50)
    weapon_type = models.CharField(max_length=50)
    s = models.CharField(max_length=50)
    ap = models.CharField(max_length=50)
    d = models.CharField(max_length=50)
    abilities = models.CharField(max_length=1000)
    pts = models.IntegerField()

    def __str__(self):
        return self.name

class Unit(models.Model):
    army = models.ForeignKey(Army, on_delete=models.PROTECT)
    name = models.CharField(max_length=50)
    m = models.IntegerField()
    ws = models.IntegerField()
    bs = models.IntegerField()
    s = models.IntegerField()
    t = models.IntegerField()
    w = models.IntegerField()
    a = models.IntegerField()
    ld = models.IntegerField()
    sv = models.IntegerField()
    max_units = models.CharField(max_length=50)
    weapons_list = models.ManyToManyField(Weapon, related_name='weapon')
    ability_list = models.ManyToManyField(Ability, related_name='ability')
    specialist_list = models.ManyToManyField(Specialist, related_name='specialist')
    point_value = models.IntegerField()

    def __str__(self):
        return self.name

class User(AbstractUser):
    username = models.CharField(max_length=26, unique=True)
    email = models.EmailField(
        verbose_name='email address',
        max_length=100,
        unique=True
    )
    admin = models.BooleanField(default=False)
    bio = models.CharField(max_length=800, default="Bio goes here")

    @property
    def is_admin(self):
        return self.admin

class GuideUnit(models.Model):
    name = models.CharField(max_length=50)
    unit = models.ForeignKey(Unit, on_delete=models.PROTECT)
    weapon = models.ForeignKey(Weapon, on_delete=models.PROTECT)
    role = models.ForeignKey(Specialist, on_delete=models.PROTECT)


class Guide(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    army = models.ForeignKey(Army, on_delete=models.CASCADE)
    units = models.ManyToManyField(Unit, related_name='units')
    weapons = models.ManyToManyField(Weapon, related_name='weapons')
    title = models.CharField(max_length=100)
    guide_desc = models.CharField(max_length=10000)
    point_value = models.IntegerField()
    votes = models.IntegerField()
    date_created = models.DateTimeField()

class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    guide = models.ForeignKey(Guide, on_delete=models.CASCADE)
    content = models.CharField(max_length=500)
    date_created = models.DateTimeField()