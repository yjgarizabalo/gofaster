from rest_framework import serializers
from .models import Persona

class PersonaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Persona
        # fields = ('id', 'primer_nombre', 'x', 'xx')
        fields = '__all__'