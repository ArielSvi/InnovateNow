from django.db import models

class NavbarItem(models.Model):
    name = models.CharField(max_length=100)
    url = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class HelpedCompany(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    year_founded = models.IntegerField()

    def __str__(self):
        return self.name

class AboutUs(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    mission = models.TextField(default='Nuestra misión es apoyar a los emprendedores.')
    history = models.TextField()
    helped_companies = models.ManyToManyField(HelpedCompany)

    def __str__(self):
        return self.title

class Service(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    


    def __str__(self):
        return self.name
