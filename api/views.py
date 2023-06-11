from django.shortcuts import render
from rest_framework import viewsets
from api.models import Company,Employee,LogTable
from api.serializers import CompanySerializer,EmpSerializer,EmpLoginSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.utils import timezone


@api_view(['GET','POST'])
def businessUnits(request):
    if request.method=='GET':
        all_companies=Company.objects.all()
        serializer=CompanySerializer(all_companies,many=True)     #serializing
        print(serializer.data)
        return Response(serializer.data)
    
    elif request.method=='POST':
            deserializer=CompanySerializer(data=request.data)   #deserializing
            if deserializer.is_valid():
                deserializer.save()
                return Response(deserializer.data)
            return Response(deserializer.errors)


@api_view(['PUT','GET','DELETE'])

def businessUnit(request,id):
    if request.method=='GET':

        try:
            company=Company.objects.get(company_id=id)
            serializer=CompanySerializer(company)
            return Response(serializer.data)
        except Exception as e:
            print(e)
            return Response({'message':'invalid id'})
    
    elif request.method=='DELETE':

        try:
            company=Company.objects.get(company_id=id)
            company.delete()
            return Response({'msg':'deleted'})
        except Exception as e:
            print(e)
            return Response({'message':'invalid id'})
    
    elif request.method=='PUT':
        try:
            company=Company.objects.get(company_id=id)
            serializer=CompanySerializer(company,data=request.data,partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors)
        except Exception as e:
            print(e)
            return Response({'message':'invalid id'})


@api_view(['GET','POST'])
def emps(request):
    if request.method=='GET':
        all_emps=Employee.objects.all()
        serializer=EmpSerializer(all_emps,many=True)     #serializing
        print(serializer.data)
        return Response(serializer.data)
    
    elif request.method=='POST':
            deserializer=EmpSerializer(data=request.data)   #deserializing
            if deserializer.is_valid():
                deserializer.save()
                return Response(deserializer.data)
            return Response(deserializer.errors)
    

@api_view(['PUT','GET','DELETE'])

def emp(request,id):
    if request.method=='GET':
        try:
            emp=Employee.objects.get(id=id)
            serializer=EmpSerializer(emp)
            return Response(serializer.data)
        except Exception as e:
            print(e)
            return Response({'message':'invalid id'})
    
    elif request.method=='DELETE':

        try:
            emp=Employee.objects.get(id=id)
            emp.delete()
            return Response({'msg':'deleted'})
        except Exception as e:
            print(e)
            return Response({'message':'invalid id'})
    
    elif request.method=='PUT':
        try:
            emp=Employee.objects.get(id=id)
            deserializer=EmpSerializer(emp,data=request.data,partial=True)
            if deserializer.is_valid():
                deserializer.save()
                return Response(deserializer.data)
            return Response(deserializer.errors)
        except Exception as e:
            print(e)
            return Response({'message':'invalid id'})

@api_view(['GET','POST'])
def BuEmps(request,id):
    if request.method=='GET':
        try:
            company=Company.objects.get(company_id=id)
            employee=Employee.objects.filter(company=company)
            serializer=EmpSerializer(employee,many=True)
            return Response(serializer.data)
        except Exception as e:
                print(e)
                return Response({'message':'invalid id'})

    elif request.method=='POST':
        try:

            comp=request.data['company']
            print(comp)
            try:
                if comp==int(id):
                    print('inside if')
                    deserializer=EmpSerializer(data=request.data)
                    if deserializer.is_valid():
                        deserializer.save()
                        return Response(deserializer.data)
                else:
                    return Response({'message':'invalid id'})
            except Exception as e:
                print(e)
                return Response({'message':'Exception'})
                
        except Exception as e:
            request.data['company']=id
            deserializer=EmpSerializer(data=request.data)
            if deserializer.is_valid():
                deserializer.save()
                return Response(deserializer.data)


            return Response({'message':'invalid msg'})
           


@api_view(['GET','PUT','DELETE'])
def BuEmp(request,cid,eid):
    if request.method=='GET':
        try:
            company=Company.objects.get(company_id=cid)
            employee=Employee.objects.get(id=eid,company=company)
            serializer=EmpSerializer(employee)
            return Response(serializer.data)
        except Exception as e:
                print(e)
                return Response({'message':'invalid id'})
        
    elif request.method=='PUT':
        try:
            comp=request.data['company']
            print(comp)
            try:
                if comp==int(cid):
                    emp=Employee.objects.get(company=comp,id=eid)
                    deserializer=EmpSerializer(emp,data=request.data,partial=True)
                    if deserializer.is_valid():
                        deserializer.save()
                        return Response(deserializer.data)
                else:
                    return Response({'message':'invalid company id'})
            except Exception as e:
                print(e)
                return Response({'message':str(e)})
                
        except Exception as e:
            try:
                request.data['company']=cid
                emp=Employee.objects.get(id=eid)
                deserializer=EmpSerializer(emp,data=request.data,partial=True)
                if deserializer.is_valid():
                    deserializer.save()
                    return Response(deserializer.data)
                return Response(deserializer.errors)
            except Exception as e:
                return Response({'message':str(e)})
           
    

    elif request.method=='DELETE':
        try:
            company=Company.objects.get(company_id=cid)
            emp=Employee.objects.get(id=eid,company=company)
            emp.delete()
            return Response({'msg':'deleted'})
        except Exception as e:
            print(e)
            return Response({'message':str(e)})

@api_view(['GET','POST'])
def EmpLogin(request,cid,eid):
    if request.method=='GET':
        try:
            company=Company.objects.get(company_id=cid)
            employee=Employee.objects.get(id=eid,company=company)
            logdata=LogTable.objects.filter(emp=employee)
            print(logdata)
            serializer=EmpLoginSerializer(logdata,many=True)
            return Response(serializer.data)
        except Exception as e:
            print(e)
            return Response({'message':str(e)})

    elif request.method=='POST':
        try:
            empid=request.data['emp']  # This is the data which we are posting
            print(empid)
            print(eid)
            if(int(eid)==int(empid)):
                cmp=Company.objects.get(company_id=cid)
                emp=Employee.objects.get(id=eid)
                if emp.company.company_id!=cmp.company_id:
                    return Response({'message':'invalid company id for the employee'})
                deserializer=EmpLoginSerializer(data=request.data)   #deserializing
                if deserializer.is_valid():
                    deserializer.save()
                    return Response(deserializer.data)
                return Response(deserializer.errors)
            else:
                return Response({'message':'invalid employee id'})

        except Exception as e:
            try:
                request.data['emp']=eid
                emp=Employee.objects.get(id=eid)
                cmp=Company.objects.get(company_id=cid)
                emp=Employee.objects.get(id=eid)
                if emp.company.company_id!=cmp.company_id:
                    return Response({'message':'invalid company id for the employee'})
                deserializer=EmpLoginSerializer(data=request.data)   #deserializing
                if deserializer.is_valid():
                    deserializer.save()
                    return Response(deserializer.data)
                return Response(deserializer.errors)
            except Exception as e:
                print(e)
                return Response({'message':str(e)})
            

@api_view(['GET','PUT'])
def EmpLogout(request,cid,eid,sessionid):
    if request.method=='GET':
        try:
            company=Company.objects.get(company_id=cid)
            emp=Employee.objects.get(id=eid,company=company)
            logentry=LogTable.objects.get(id=sessionid,emp=emp)
            serializer=EmpLoginSerializer(logentry)
            return Response (serializer.data)
        except Exception as e:
            print(e)
            return Response({'message':str(e)})
    


    if request.method=='PUT':
        try:
            company=Company.objects.get(company_id=cid)
            emp=Employee.objects.get(id=eid,company=company)
            logentry=LogTable.objects.get(id=sessionid,emp=emp)
            if logentry.logout_time:
                return Response({"message": "User already logged out"})
            else:
                deserializer=EmpLoginSerializer(logentry,data={"logout_time": timezone.now()},partial=True)
                if deserializer.is_valid():
                    deserializer.validated_data["logout_time"] = timezone.now()
                    deserializer.save()
                    return Response(deserializer.data)
                else:
                    return Response(deserializer.errors)
        except Exception as e:
            print(e)
            return Response({'message':str(e)})
    