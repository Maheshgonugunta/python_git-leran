from rest_framework import serializers
from firstapp.models import employee

class Employeeserilizer(serializers.modelserilizers):
    class meta:
        model = employee
        fields=('emp_id','emp_name','mobile_no')



