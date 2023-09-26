from rest_framework import serializers
from .models import Employee


class EmployeeSerializer(serializers.ModelSerializer):
	password = serializers.CharField(write_only=True)  # Include 'password' field for write-only

	class Meta:
		model = Employee
		fields = ('id', 'first_name', 'last_name', 'email', 'employee_id', 'password')

	def create(self, validated_data):
		# Extract and hash the 'password' field before saving
		password = validated_data.pop('password')
		user = Employee(**validated_data)
		user.set_password(password)  # Hash the password
		user.save()
		return user
