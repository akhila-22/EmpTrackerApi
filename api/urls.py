
from django.urls import path
from .views import buisnessUnits,buisnessUnit,emps,emp,BuEmps,BuEmp,EmpLogin,EmpLogout
urlpatterns = [
  path('buisnessUnits/',buisnessUnits),
  path('buisnessUnit/<id>/',buisnessUnit),
  path('employees/',emps),
  path('employee/<id>/',emp),
  path('businessUnit/<id>/employee/',BuEmps),
  path('businessUnit/<cid>/employee/<eid>/',BuEmp),
  path('businessUnit/<cid>/employee/<eid>/log/',EmpLogin),
  path('businessUnit/<cid>/employee/<eid>/log/<sessionid>/',EmpLogout)
]
