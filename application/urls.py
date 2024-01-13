from django.urls import path
from . import views

urlpatterns = [
    path('',views.application_list),
    path('<int:application_id>',views.application_detail, name='application_detail'),
    # path('<slug:slug>',views.application_detail, name='application_detail'),
]