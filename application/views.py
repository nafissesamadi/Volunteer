from django.shortcuts import render, get_object_or_404
from .models import Application


# Create your views here.
def application_list(request):
    applications = Application.objects.all().order_by('registered_date')
    return render(request, 'application/application_list.html', {'applications': applications})


def application_detail(request, application_id):
    application = get_object_or_404(Application, pk=application_id)
    return render(request, 'application/application_detail.html', {'application': application})
