from django.shortcuts import render

# Create your views here.

from django.template import loader
from django.http import HttpResponse, HttpResponseNotFound
from myapps.functions import handle_uploaded_file
from django.views.decorators.http import require_http_methods
from myapps.forms import EmpForm


def index(request):
    if request.method == "POST":
        form = EmpForm(request.POST, request.FILES)
        if form.is_valid():
            handle_uploaded_file(request.FILES['file'])
            return HttpResponse("File uploaded successfuly")
            try:
                return redirect('/')
            except:
                pass
    else:
        form=EmpForm()



    return render(request,"index.html",{'forms':form})

