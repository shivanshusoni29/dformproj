from django.shortcuts import render
from .forms import Studentform
from .models import StudentData

# Create your views here.
def index(request):
    if request.method=='GET':
        form=Studentform()
        return render(request,'Register.html',{'form':form})
    else:
        form=Studentform(request.POST)
        if form.is_valid():
            StudentData(
                name=form.cleaned_data['name'],
                age=form.cleaned_data['age'],
                gender=form.cleaned_data['gender'],
                created_at=form.cleaned_data['created_at']
            ).save()
    return render(request,'Register.html',{'form':form})

