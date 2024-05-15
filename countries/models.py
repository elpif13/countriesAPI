from django.db import models

# This is a django model.


class Countries(models.Model): # for using all the properties of Model class
    # this class is going to inherit from the Model base class which belongs to the models module
    name = models.CharField(max_length=50, blank=False, default='')
    #default is empty
    capital = models.CharField(max_length=50, blank=False, default='')

    def __str__(self):
        return self.name

    class Meta: #inner class
        ordering = ('id',) #ordered by id
        verbose_name = "Country" # table name
        verbose_name_plural = "Countries" # plural form of table name
        db_table = "Country"


        # for applying changes first makemigrations then migrate

    
    
