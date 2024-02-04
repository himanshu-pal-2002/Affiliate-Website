from django.shortcuts import render

# Views for Homepage.
def Home(request):
    return render(request,'home.html')
