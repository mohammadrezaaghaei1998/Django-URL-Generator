from django.shortcuts import render,redirect
import uuid
from django.http import HttpResponse
from .models import url
from django.contrib import messages





def index(request):
    return render(request,'index.html')



def generator(request):
    if request.method == 'POST':
        link = request.POST.get('link', '')
        if link:
            uid = str(uuid.uuid4())[:5]
            new_url = url(link=link, uuid=uid)
            new_url.save()
            return HttpResponse(uid)
        else:
            return HttpResponse("Plese enter your link")
    else:
        None


    

def url_redirect(request, pk):
    try:
        url_obj = url.objects.get(uuid=pk)
        return redirect(url_obj.link)
    except url.DoesNotExist:
        return render(request, '404.html')
