from django.shortcuts import render, HttpResponse
from app01 import models
from app01.forms import PublisherForm

# Create your views here.

def publisher(request):
    data = models.Publisher.objects.all()
    return render(request, "publisher.html", {"publisher_list": data})


def po_publisher(request, edit_id=None):
    obj = models.Publisher.objects.filter(id=edit_id).first()
    form_obj = PublisherForm()
    if request.method == "POST":
        form_obj = PublisherForm(request.POST)
        if form_obj.is_valid():
            print(form_obj.cleaned_data)
            return HttpResponse("ok")
    return render(request, "po_publisher.html", {"form_obj": form_obj,})


