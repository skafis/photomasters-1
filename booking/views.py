from django.shortcuts import render, get_object_or_404

# Create your views here.
def home_page(request):
    return render(request, 'booking/home.html')