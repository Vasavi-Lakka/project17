from django.shortcuts import render
from django.http import HttpResponse
from app.models import*
from django.db.models.functions import Length
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
    depts=Dept.objects.all().order_by(Length('dname'))
    #depts=Dept.objects.all()
    depts=Dept.objects.all().order_by('deptno')
    depts=Dept.objects.all().order_by('dname')
    depts=Dept.objects.all().order_by(Length('dloc'))
    depts=Dept.objects.filter(dname__startswith='A')
    depts=Dept.objects.filter(dname__endswith='r')
    depts=Dept.objects.filter(dname__contains='a')
    d={'depts':depts}
    return render(request, 'displayDept.html', d)
def displayEmp(request):
    emps=Emp.objects.all()
    emps=Emp.objects.filter(ename__startswith='V')
    emps=Emp.objects.filter(job__endswith='r')
    emps=Emp.objects.filter(job__contains='j')
    
    
    d={'emps':emps}
    return render(request, 'displayEmp.html', d)
 
 
 
def empdept(request):
    emps=Emp.objects.select_related('deptno').all()
    d={'emps':emps}
    return render(request, 'empdept.html', d)
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
#order_by 
'''
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
    depts=Dept.objects.all().order_by(Length('dname'))
    #depts=Dept.objects.all()
    depts=Dept.objects.all().order_by('deptno')
    depts=Dept.objects.all().order_by('dname')
    depts=Dept.objects.all().order_by(Length('dloc'))
    d={'depts':depts}
    return render(request, 'displayDept.html', d)
def displayEmp(request):
    emps=Emp.objects.all()
    emps=Emp.objects.all().order_by(Length('ename'))
    
    emps=Emps.objects.all().order_by('sal')
    emps=Emps.objects.all().order_by('job')
    emps=Emp.objects.all().order_by(Length('dloc'))
    d={'emps':emps}
    return render(request, 'displayEmp.html', d)'''