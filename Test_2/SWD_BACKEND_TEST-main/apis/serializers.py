from rest_framework import serializers
from rest_framework.response import Response
from rest_framework import status
from .models import StudentSubjectsScore, Personnel, Classes, Schools

class StudentSerializer(serializers.ModelSerializer):

    school_class = serializers.StringRelatedField()

    class Meta:
        model = Personnel
        fields = ['id', 'school_class']


class StudentSubjectsScoreSerializer(serializers.ModelSerializer):

    student = serializers.StringRelatedField()
    

    # def validate(self, data):
    #     if(data['score'] < 0 or data['score']  > 100):
    #         raise serializers.ValidationError(status.HTTP_400_BAD_REQUEST)
    #     else:
    #         return data

    class Meta:
        model = StudentSubjectsScore
        fields = ['id', 'student', 'subjects', 'credit', 'score']