from django.urls import path
from app import views as v

app_name = 'app'

urlpatterns = [
    path('', v.index, name='index'), 
    path('form/', v.form, name='form'),  
    path('edit/<int:id>/', v.edit, name='edit'),
    path('delete/<int:id>/', v.delete, name='delete'),
]
 