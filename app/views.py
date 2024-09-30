from django.shortcuts import render
from django.http import HttpResponse
from app.models import*
# Create your views here.
 
def insert_Dept(request):
    dno=int(input('enter dept no: '))
    dn=input('enter dept name: ')
    dl=input('enter dept loc: ')
    DO=Dept.objects.get_or_create(deptno=dno, dname=dn, dloc=dl)
    if DO[1]:
        depts=Dept.objects.all()
        d={'depts':depts}
        return render(request, 'displayDept.html', d)
        #return HttpResponse('New object is created')
    else:
        return HttpResponse("Already Exits")
def insert_Emp(request):
    dno=int(input('enter dept no: '))
    dn=input('enter dept name: ')
    dl=input('enter dept loc: ')
    eno=int(input('enter emp no: '))
    en=input('enter emp name: ')
    ej=input('enter emp designation: ')
    es=input('enter emp sal: ')
    hd=input('enter hire date: ')
    c=int(input('enter comm: '))
    m=input('enter manager: ')

    QLDO=Dept.objects.filter(deptno=dno, dname=dn, dloc=dl)

    #DO=Dept.objects.get_or_create(deptno=dno, dname=dn, dloc=dl)[0]
    #EO=Emp.objects.get_or_create(deptno=DO, empno=eno, ename=en, job=ej, sal=es, hiredate=hd,comm=c, mgr=m)
    if QLDO:
        DO=QLDO[0]
        EO=Emp.objects.get_or_create(deptno=DO, empno=eno, ename=en, job=ej, sal=es, hiredate=hd,comm=c, mgr=m)
        emps=Emp.objects.all()
        d={'emps', emps}
        return render(request, 'displayEmp.html', d)
        #return HttpResponse('New object is created')
    else:
        return HttpResponse('Already exits')



def displayDept(request):
    depts=Dept.objects.all()
    d={'depts':depts}
    return render(request, 'displayDept.html', d)
def displayEmp(request):
    emps=Emp.objects.all()
    d={'emps':emps}
    return render(request, 'displayEmp.html', d)