from django.shortcuts import render

# Create your views here.
def index_page(request):
    return render(request,'home/index_page.html')

def header_partial(request):
    return render(request, 'shared/header_partial.html')

def footer_partial(request):
    return render(request, 'shared/footer_partial.html')

def canvas_partial(request):
    return render(request, 'shared/canvas_partial.html')