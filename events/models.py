from django.db import models

class Event(models.Model):
    title= models.CharField(max_length=100)
    image = models.ImageField(upload_to='events/images/')
    url = models.URLField(blank=True)
    datestart = models.DateField(auto_now=False, auto_now_add=False)
    datefinish = models.DateField(auto_now=False, auto_now_add=False)
    ROAD = 'RD'
    TRACK = 'TR'
    CYCLO = 'CX'
    MTB = 'MTB'
    GRAVEL = 'GR'
    discipine_choice = [(ROAD, 'Road'),
                        (TRACK, 'Track'),
                        (CYCLO, 'Cyclo-Cross'),
                        (MTB, 'Mountain-Bike'),
                        (GRAVEL, 'Gravel Bike'),
                        ]
    discipline = models.CharField(
        max_length=3,
        choices=discipine_choice,
        default=ROAD,
    )
    stages = models.IntegerField(blank=True, default=0)
    stage0 = models.BooleanField(default=False)
    raceresult = models.CharField(max_length=7, blank=True)
    startlist =  models.BooleanField(default=True)


    def __str__(self):
        return self.title
