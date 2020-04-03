from vuejsform.models import Product
from rest_framework import serializers

# Serializers allow complex data such as querysets and model instances to be converted to native Python datatypes that can then be easily rendered into JSON, XML or other content types.

class ProductSerialiser(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Product
        fields = ['created_time', 'updated_time', 'code', 'factory', 'name', 'origin']