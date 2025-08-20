from django.shortcuts import render
from django.http import HttpResponse
from django.core.files.storage import FileSystemStorage
# Create your views here.

def index(request):
    return render(request, 'core/index.html')

def file_upload(request):
    if request.method == 'POST' and request.FILES['myfile']:
        uploaded_file = request.FILES['myfile']
        fs = FileSystemStorage()
        filename = fs.save(uploaded_file.name, uploaded_file)
        file_url = fs.url(filename)
        return render(request, 'blog/upload.html', {'file_url': file_url})
    return render(request, 'core/upload.html')
