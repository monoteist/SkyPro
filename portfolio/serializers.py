from rest_framework import serializers

from portfolio.models import Education, Experience, Portfolio, Speciality

class EducationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Education
        fields = ('title',)

class PortfolioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Portfolio
        fields = ('title',)

class SpecialitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Speciality
        fields = ('title',)

class ExperienceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Experience
        fields = ('title',)