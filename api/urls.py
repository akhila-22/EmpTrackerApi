
from django.urls import path
from .views import businessUnits,businessUnit,emps,emp,BuEmps,BuEmp,EmpLogin,EmpLogout
urlpatterns = [
  path('businessUnits/',businessUnits),
  path('businessUnit/<id>/',businessUnit),
  path('employees/',emps),
  path('employee/<id>/',emp),
  path('businessUnit/<id>/employee/',BuEmps),
  path('businessUnit/<cid>/employee/<eid>/',BuEmp),
  path('businessUnit/<cid>/employee/<eid>/log/',EmpLogin),
  path('businessUnit/<cid>/employee/<eid>/log/<sessionid>/',EmpLogout)
]
