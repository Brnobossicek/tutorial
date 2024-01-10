from rest_framework import serializers
from EmployeeApp.models import Department, Employees

class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = ('DepartmentID',
                  'DepartmentName')
        
class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employees
        fields = ('EmployeeID',
                  'EmployeeName',
                  'Departmnet',
                  'DateOfJoin',
                  'PhotoFileName')