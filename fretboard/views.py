from django.shortcuts import render
from django.shortcuts import HttpResponse

# Create your views here.
def index(request):
    #return HttpResponse("hey")
    return render(request, "fretboard/fretboard.html")

def flextest(request):
    #return HttpResponse("hey")
    return render(request, "fretboard/flextest.html")