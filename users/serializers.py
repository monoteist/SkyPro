from rest_framework import serializers

from portfolio.serializers import EducationSerializer, SpecialitySerializer, ExperienceSerializer, PortfolioSerializer

from users.models import User


class UserSerializer(serializers.ModelSerializer):
    speciality = SpecialitySerializer(many=True)
    education = EducationSerializer(many=True)
    portfolio = PortfolioSerializer(many=True)
    experience = ExperienceSerializer(many=True)

    class Meta:
        model = User
        fields = ('status', 'grade', 'speciality', 'salary', 'education',
                  'experience', 'portfolio', 'title', 'phone', 'email',)
