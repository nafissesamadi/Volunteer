from django.urls import path
from . import views

urlpatterns = [
    # path('',views.application_list, name='application_list'),
    path('',views.ApplicationListView.as_view(), name='application_list'),
    path('<int:pk>', views.ApplicationDetailView.as_view(), name='application_detail'),
    # path('<int:application_id>',views.application_detail, name='application_detail'),

]