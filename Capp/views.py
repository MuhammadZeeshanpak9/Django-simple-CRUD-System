from django.shortcuts import render, redirect
from .models import Members
from django.shortcuts import render, get_object_or_404, redirect
from .models import Members  # Replace with your actual model
 # Replace with your actual form
from .forms import YourModelForm 

# Create your views here.

def index(request):
    mem=Members.objects.all()
    return render(request,'index.html',{'mem': mem})

def add(request):
    return render(request,'add.html')

def addrec(request):
    x=request.POST['first']
    y=request.POST['last']
    z = request.POST.get('country', 'Default Country')
    mem=Members(firstname=x,lastname=y,country=z)
    mem.save()
    return redirect("/")

def reassign_ids():
    members = Members.objects.all().order_by('id')
    for i, member in enumerate(members, start=1):
        member.id = i
        member.save()

def delete_member(request, pk):
    Members.objects.filter(id=pk).delete()
    reassign_ids()
    return redirect('your_list_view')

def delete(request,id):
    mem=Members.objects.get(id=id)
    mem.delete()
    return redirect("/")

def update(request, id):
    mem = get_object_or_404(Members, id=id)
    return render(request, 'update.html', {'mem': mem})

def uprec(request,id):
    x=request.POST['first']
    y=request.POST['last']
    z=request.POST['country']
    mem=Members.objects.get(id=id)
    mem.firstname=x
    mem.lastname=y
    mem.country=z
    mem.save()
    return redirect("/")