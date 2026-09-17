from django.db import models
from datetime import datetime
from Person.models import Person
# Create your models here.
class Event(models.Model):
    category_list=(
        ('M','Musique'),
        ('S','Sport'),
        ('C','Cinema')
    )
    title=models.CharField("Titre",max_length=50)
    description=models.TextField(max_length=50)
    image =models.ImageField(upload_to="images/",null=True,blank=True)
    category =models.CharField(choices=category_list,max_length=8)
    state =models.BooleanField(default=False)
    nbe_participant =models.IntegerField(default=0)
    evt_date = models.DateTimeField()
    creation_date=models.DateField(auto_now_add=True)
    update_date = models.DateField(auto_now=True)
    organizer=models.ForeignKey(
        Person,
        on_delete=models.SET_NULL,
        null=True
    )
    participant=models.ManyToManyField(
        Person,
        through='Participants',
        related_name="participant"
    )
    def __str__(self):
        return f"Le titre de l'evt est: {self.title} et la categorie est : {self.category}"
    class Meta:
        constraints=[
            models.CheckConstraint(check=models.Q(
                evt_date__gt=datetime.now()
            ),name="Please Check event date")
        ]
class Participants(models.Model):
    person=models.ForeignKey(Person,on_delete=models.CASCADE)
    event=models.ForeignKey(Event,on_delete=models.CASCADE)
    participation_date =models.DateTimeField(datetime.now(),auto_now_add=True)
    class Meta:
        unique_together=['person','event']