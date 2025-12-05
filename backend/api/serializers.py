from rest_framework import serializers
from api.models import Employee

class EmployeeSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(
        read_only=True,
        default=serializers.CurrentUserDefault()
    )
    department = serializers.ChoiceField(choices=Employee.DEPARTMENT_CHOICES)

    class Meta:
        model = Employee
        fields = ('id', 'user', 'name', 'department', 'salary')
        
        
class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(required=True)
    passwrod = serializers.CharField(required=True)
    

class SignupSerializer(serializers.Serializer):
    username = serializers.CharField(required=True)
    email = serializers.EmailField(required=False)
    passwrod = serializers.CharField(required=True)