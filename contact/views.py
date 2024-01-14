from django.shortcuts import render
from .forms import ContactUsForm, ContactUsModelForm
from .models import ContactUs
from django.shortcuts import render, redirect
from django.views import View


# Create your views here.


def contact_us_page(request):
    if request.method == 'POST':
        contact_form = ContactUsModelForm(request.POST)
        if contact_form.is_valid():
            # contact=ContactUs(title=contact_form.cleaned_data.get('title'),
            #                   full_name=contact_form.cleaned_data.get('full_name'),
            #                   email=contact_form.cleaned_data.get('email'),
            #                   message=contact_form.cleaned_data.get('message'),
            #                   )
            # contact.save()
            contact_form.save()
            return redirect('application_list')

    else:
        contact_form = ContactUsModelForm()
    return render(request, 'contact/contact_us_page.html', {'contact_form': contact_form})

class ContactUsView(View):
    def get(self,request):
        contact_form=ContactUsModelForm()
        return render(request, 'contact/contact_us_page.html', {'contact_form': contact_form})
    def post(self,request):
        contact_form=ContactUsModelForm(request.POST)
        if contact_form.is_valid():
            contact_form.save()
            return redirect('application_list')
        return render(request, 'contact/contact_us_page.html', {'contact_form': contact_form})


