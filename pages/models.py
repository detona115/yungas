from django.db import models

# Create your models here.

class Pessoa(models.Model):
    gender = models.CharField('gender', max_length=50)
    email = models.EmailField('email', max_length=150)
    regiao = models.CharField('regiao', max_length=50)
    nationality = models.CharField('nationality', max_length=10, default='BR')
    birthday = models.DateTimeField('birthday')
    registered = models.DateTimeField('registered')

    def __str__(self):
        return f"{self.email} {self.regiao} {self.nationality}"

class Name(models.Model):
    title = models.CharField('title', max_length=10)
    first = models.CharField('first', max_length=100)
    last = models.CharField('last', max_length=100)
    pessoa = models.ForeignKey(
        Pessoa,
        null=True,
        on_delete=models.CASCADE,
        related_name='names'
    )

    def __str__(self):
        return f"{self.title} {self.first} {self.last}"


class Location(models.Model):
    street = models.CharField('street', max_length=100)
    city = models.CharField('city', max_length=100)
    state = models.CharField('state', max_length=100)
    postcode = models.CharField('postcode', max_length=15)
    
    pessoa = models.ForeignKey(
        Pessoa,
        null=True,
        on_delete=models.CASCADE,
        related_name='locations'
    )

    def __str__(self):
        return f"{self.street} {self.city} {self.state} {self.postcode}"

class Coordinate(models.Model):
    latitude = models.CharField(max_length=50)
    longitude = models.CharField(max_length=50)
    location = models.ForeignKey(
        Location,
        null=True,
        on_delete=models.CASCADE,
        related_name='coordinates'
    )

    def __str__(self):
        return f"{self.latitude} {self.longitude}"
    
class Timezone(models.Model):
    offset = models.CharField(max_length=10)
    description = models.CharField(max_length=50)
    location = models.ForeignKey(
        Location,
        null=True,
        on_delete=models.CASCADE,
        related_name='timezones'
    )

    def __str__(self):
        return f"{self.offset} {self.description}"

class Picture(models.Model):
    large = models.CharField(max_length=250)
    medium = models.CharField(max_length=250)
    thumbnail = models.CharField(max_length=250)
    pessoa = models.ForeignKey(
        Pessoa,
        null=True,
        on_delete=models.CASCADE,
        related_name='pictures'
    )

    def __str__(self):
        return f"{self.large} {self.medium} {self.thumbnail}" 

class Phone(models.Model):
    phone = models.CharField('telephoneNumbers', max_length=20)
    pessoa = models.ForeignKey(
        Pessoa,
        on_delete=models.CASCADE,
        related_name='phones'
    )

    def __str__(self):
        return f"{self.phone} {self.pessoa}"
    

class Cell(models.Model):
    cell = models.CharField(max_length=20)
    pessoa = models.ForeignKey(
        Pessoa,
        on_delete=models.CASCADE,
        related_name='cells'
    )

    def __str__(self):
        return f"{self.cell} {self.pessoa}"