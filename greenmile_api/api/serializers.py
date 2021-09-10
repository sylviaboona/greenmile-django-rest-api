from rest_framework import serializers
from .models import Loader, Package, Supplier

class LoaderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Loader
        # fields = ['question', 'choice_text', 'votes']
        fields = '__all__'

class SupplierSerializer(serializers.ModelSerializer):
    class Meta:
        model = Supplier
        # fields = ['question', 'choice_text', 'votes']
        fields = '__all__'

class PackageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Package
        # fields = ['question', 'choice_text', 'votes']
        fields = '__all__'