from django.urls import path
from .import views

urlpatterns=[
    path('',views.AddBookView),
    path('addbook/',views.AddBookView,name='add_book'),
    path('showbook/',views.ShowBookView,name='show_book'),
    path('delete/<int:i>/', views.DeleteBookView, name='delete_book'),
    path('update/<int:i>/', views.UpdateBookView, name='update_book'),
    path('studententry/', views.StudentBookView, name='student_entry'),
    path('student/', views.StudentView, name='student_book'),

]