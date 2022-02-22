from django.shortcuts import render
from .forms import ImageUploadForm

#Uploaded photos will save here
def handle_uploaded_file(f):
    with open('img.jpg', 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)



# Create your views here.
def home(request):
    return render(request,'home.html')

def imageprocess(request):

    form = ImageUploadForm(request.POST, request.FILES)
    if form.is_valid():
        handle_uploaded_file(request.FILES['image'])

        #integration of OCR NER WEB SCRAPING MODELS
    

    return render(request,'result.html')