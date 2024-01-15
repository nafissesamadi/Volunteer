from django.shortcuts import render, get_object_or_404
from .models import Application
from django.views.generic.base import TemplateView
from django.views.generic import ListView, DetailView

# region Application_List
# Create your views here.
# def application_list(request):
#     applications = Application.objects.all().order_by('registered_date')
#     return render(request, 'application/application_list.html', {'applications': applications})


# class ApplicationListView(TemplateView):
#     template_name = 'application/application_list.html'
#     def get_context_data(self, **kwargs):
#         applications=Application.objects.all().order_by('rating')
#         context=super(ApplicationListView,self).get_context_data()
#         context['applications'] = applications
#         return context

class ApplicationListView(ListView):
    template_name='application/application_list.html'
    model=Application
    context_object_name = 'applications'
    def get_queryset(self):
        base_query=super(ApplicationListView,self).get_queryset()
        data=base_query.filter(is_active=True)
        return data

# endregion

# region Application_detail

# def application_detail(request, application_id):
#     application = get_object_or_404(Application, pk=application_id)
#     return render(request, 'application/application_detail.html', {'application': application})

# class ApplicationDetailView(TemplateView):
#     template_name = 'application/application_detail.html'
#
#     def get_context_data(self, **kwargs):
#         context = super(ApplicationDetailView, self).get_context_data()
#         application_id = kwargs['application_id']
#         application = get_object_or_404(Application, pk=application_id)
#         context['application'] = application
#         return context

class ApplicationDetailView(DetailView):
    template_name ='application/application_detail.html'
    model= Application


# endregion