from rest_framework import serializers

from info import models


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Student
        fields = ('roll_id', 'email', 'fname', 'lname', 'age', 'standard')