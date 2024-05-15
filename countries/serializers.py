from rest_framework import serializers
from countries.models import Countries

# this is our data model


# this class will manage serialization and deserialization from JSON, it inherits
# from serializers.ModelSerializer
class CountriesSerializer(serializers.ModelSerializer): 

    class Meta: # inner class
        model = Countries
        fields = ('id','name','capital')
