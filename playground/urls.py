from django.urls import path
from playground import views


app_name = 'playground' 
urlpatterns = [
    path('', views.index, name='home_landing'),
    path('added-title/', views.submitTest, name="test_submit")
]



