from django.shortcuts import render,redirect

# Create your views here.
from .forms import BookModelForm,StudentModelForm
from .models import Book,Student
from django.contrib.auth.decorators import login_required


@login_required(login_url='login')
def AddBookView(request):
    form = BookModelForm()
    if request.method == 'POST':
        form = BookModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('show_book')
    template_name = 'Book/addbook.html'
    context={'form':form}
    return render(request,template_name,context)

@login_required(login_url='login')
def ShowBookView(request):
    book_obj=Book.objects.all()
    template_name= 'Book/showbook.html'
    context={'book_obj':book_obj}
    return render(request,template_name,context)

@login_required(login_url='login')
def DeleteBookView(request,i):
    book_obj=Book.objects.get(id=i)
    if request.method == 'POST':
        book_obj.delete()
        return redirect('show_book')
    template_name = 'Book/deletebook.html'
    context={'book_obj':book_obj}
    return render(request,template_name,context)

@login_required(login_url='login')
def UpdateBookView(request,i):
    book_obj= Book.objects.get(id=i)
    form = BookModelForm(instance=book_obj)
    if request.method == 'POST':
        form = BookModelForm(request.POST,instance=book_obj)
        if form.is_valid():
            form.save()
            return  redirect('show_book')
    template_name= 'Book/addbook.html'
    context={'form':form}
    return render(request,template_name,context)

@login_required(login_url='login')
def StudentBookView(request):
    form = StudentModelForm()
    if request.method == 'POST':
        form = StudentModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('student_book')
    template_name = 'Book/entry.html'
    context={'form':form}
    return render(request,template_name,context)

@login_required(login_url='login')
def StudentView(request):
    stud_obj=Student.objects.all()
    template_name= 'Book/student.html'
    context={'stud_obj':stud_obj}
    return render(request,template_name,context)





