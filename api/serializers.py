from rest_framework import serializers
from api.models import Company,Employee,LogTable


class CompanySerializer(serializers.ModelSerializer):
    
    class Meta:
        model=Company
        fields=('name','location','about','type','added_date','active')
        
class EmpSerializer(serializers.ModelSerializer):
      
    class Meta:
        model=Employee
        fields="__all__"

class EmpLoginSerializer(serializers.ModelSerializer):     
    class Meta:
        model=LogTable
        fields="__all__"