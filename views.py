from urllib import request
from django.shortcuts import render, HttpResponse
from django.shortcuts import redirect, render
from django.contrib import messages
from .models import *


# Create your views here.
def index(request):
    return render(request, 'index.html')

# Insert a New Educator with Course
def insert_Educator(request):
    print("0")

    if request.method == "POST":

        print("1")
        #Access Data from HTML
        educator_name = request.POST.get('educator_name')
        course_name = request.POST.get('course_name')

        #check Educator Name already exist or not
        if Educator.objects.filter(educator_name=educator_name.lower()):
            print("educator_name check")
            messages.error(request, "Educator Name already exist!")
            return render(request, 'insert_details.html')
            #return redirect('insert_details.html')

        print("2")
        #Store a Educator Data into Database
        educator_new = Educator.objects.create(educator_name=educator_name)
        educator_new.save()

        print("3")        
        #Store a Course Data into Database
        course_new = Course.objects.create(course_name=course_name)
        course_new.save()

        #Add Course to Educator
        edu_courses_new = educator_new.courses.add(course_new)
        

        # After Insert render on view_details.html
        print("4")
        return redirect('view_details')

    return render(request, 'insert_details.html')

# View Educator
def view_Educator(request):
    #Data view from Database 
    #educator_name = request.POST.get('educator_name')
    educator_list = list(Educator.objects.all())
    #course_list = list(educator_list.courses.all())
    print(educator_list)

    #educator_list = {'educator_list':  educator_list}

    return render(request, 'view_details.html', {'educator_list':  educator_list})

# Update Course
def update_Course(request, pk):
    get_data = Course.objects.get(id=pk)
    return render(request,'update_course.html',{'key1': get_data})

    #return render(request, 'edu_form.html')

# Update Course View
def update_View(request, pk):
    print("update_View - 1")
    update_data = Course.objects.get(id=pk)
    update_data.course_name = request.POST['course_name']

    print("update_View - 2")
    
    # Query for Update
    update_data.save()
    print("update_View - 3")

    # Showing a Updated Data
    #update_data = {'update_data':  update_data}
    #return render(request, 'view_details.html', update_data)
    return redirect('view_details')

def delete_View(request, name):
    delete_data = Course.objects.filter(course_name = name)
    print(delete_data)
    #Query for Delete 
    delete_data.delete()

    # Showing a Updated Data
    return redirect('view_details')
"""


    for educator in educator_list:
        for course in educator.courses.all():
            print(educator, course)
"""
"""  3:23 PM, 12_6_2022
    for educator in educator_list:
        print(educator)
    
    for course in educator.courses.all():
        print(course)


    # Creating Object of Model Class

    # Inserting Data into a Table
    educator_new = Educator.objects.create(educator_name=educator_name)
    educator_new.save()
    print(educator_name)

   
    # After Insert render on show.html
    return redirect('show')



def index(request):
    return render(request, 'index.html')

def InsertPageView(request):
    return render(request, 'insert.html')

def Educator_InsertData(request):
    # Data from HTML to View
    educator_name = request.POST.get('educator_name')
    course_name = re
    

    # Creating Object of Model Class

    # Inserting Data into a Table
    educator_new = Educator.objects.create(educator_name=educator_name)
    educator_new.save()
    print(educator_name)

   
    # After Insert render on show.html
    return redirect('show')

def Course_InsertData(request):
    # Data from HTML to View
    course_name = request.POST.get('course_name')
    

    # Creating Object of Model Class

    # Inserting Data into a Table
    course_new = Course.objects.create(course_name=course_name)
    course_new.save()
    print(course_name)


    # After Insert render on show.html
    return redirect('show')

# Educator Show Page View
def Educator_ShowPage(request):
    #SELECT * FROM table_name;
    educator_data = Educator.objects.all()
    
    return render(request, 'show.html',{'show_1':educator_data})
    #key1= show_1 and show_2 is New

# Educator Show Page View
def Course_ShowPage(request):
    #SELECT * FROM table_name;
    course_data = Course.objects.all()

    return render(request, 'show.html',{'show_2':course_data})
    #key1= show_1 and show_2 is New



# Update Page
def UpdatePage(request, pk):
    get_data = Educator.objects.get(id=pk)
    return render(request,'update.html',{'key2': get_data})

    #return render(request, 'edu_form.html')

# Update Data View
def UpdateData(request, pk):
    update_data = Educator.objects.get(id=pk)
    update_data.edu_name = request.POST['edu_name']
    update_data.edu_major = request.POST['edu_major']
    update_data.edu_exp = request.POST['edu_exp']
    update_data.edu_course_1 = request.POST['edu_course_1']
    update_data.edu_course_2 = request.POST['edu_course_2']

    # Query for Update
    update_data.save()

    # Showing a Updated Data
    return redirect('show')

# Delete Data View
def DeleteData(request, pk):
    delete_data = Educator.objects.get(id=pk)

    #Query for Delete 
    delete_data.delete()

    # Showing a Updated Data
    return redirect('show')
"""
    