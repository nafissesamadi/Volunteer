from django.shortcuts import render
from .forms import ContactUsForm, ContactUsModelForm
from .models import ContactUs
from django.shortcuts import render, redirect
from django.views import View
from django.views.generic.edit import FormView, CreateView


# Create your views here.


# def contact_us_page(request):
#     if request.method == 'POST':
#         contact_form = ContactUsModelForm(request.POST)
#         if contact_form.is_valid():
#             contact_form.save()
#             return redirect('application_list')
#
#     else:
#         contact_form = ContactUsModelForm()
#     return render(request, 'contact/contact_us_page.html', {'contact_form': contact_form})

# class ContactUsView(View):
#     def get(self,request):
#         contact_form=ContactUsModelForm()
#         return render(request, 'contact/contact_us_page.html', {'contact_form': contact_form})
#     def post(self,request):
#         contact_form=ContactUsModelForm(request.POST)
#         if contact_form.is_valid():
#             contact_form.save()
#             return redirect('application_list')
#         return render(request, 'contact/contact_us_page.html', {'contact_form': contact_form})


# class ContactUsView(FormView):
#     template_name = 'contact/contact_us_page.html'
#     form_class = ContactUsModelForm
#     success_url = '/contact-us'
#
#     def form_valid(self, form):
#         form.save()
#         return super().form_valid(form)

class ContactUsView(CreateView):
    form_class = ContactUsModelForm
    template_name = 'contact/contact_us_page.html'
    success_url = '/contact-us/'



class CreateProfileView(View):
    def get(self, request):
        return render(request, 'contact/create_profile_page.html')

    def post(self, request):
        print(request.FILES)
        return redirect('/contact-us/create-profile')