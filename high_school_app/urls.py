from django.urls import path
from .views import home, all_streams, one_stream, all_students, one_student, edit_student, delete_student

app_name="high_school_app"

urlpatterns = [
    path('', home, name="home"),
    path('all_streams', all_streams, name="all_streams"),
    path('stream/<id>', one_stream, name='stream'),
    path('all_students', all_students, name="all_students"),
    path('student/<id>', one_student, name='student'),
    path('edit_student/<id>', edit_student, name="edit_student"),
    path('delete_student/<id>', delete_student, name="delete_student"),
]