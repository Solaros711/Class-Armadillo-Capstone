from django.db import models

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
    ap = models.IntegerField()
    d = models.IntegerField()
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