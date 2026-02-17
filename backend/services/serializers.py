from rest_framework import serializers
from .models import Service, Testimonial, ServiceFeature

class ServiceFeatureSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceFeature
        fields = ['id', 'description', 'order']

class ServiceSerializer(serializers.ModelSerializer):
    features = ServiceFeatureSerializer(many=True)

    class Meta:
        model = Service
        fields = '__all__'

    def create(self, validated_data):
        features_data = validated_data.pop('features', [])
        service = Service.objects.create(**validated_data)
        for feature_data in features_data:
            ServiceFeature.objects.create(service=service, **feature_data)
        return service

    def update(self, instance, validated_data):
        features_data = validated_data.pop('features', None)
        
        # Update service fields
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()

        if features_data is not None:
            # Simple approach: clear and recreation for demo/simplicity
            # In production, you'd match by ID
            instance.features.all().delete()
            for feature_data in features_data:
                ServiceFeature.objects.create(service=instance, **feature_data)
        
        return instance


class TestimonialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Testimonial
        fields = '__all__'
