from django.contrib import messages
from django.shortcuts import render, redirect

from students.forms import StudentForm, NewStudentComplainForm, NewStudentProposalForm


# Create your views here.
def index(request):
    return render(request, 'index.html')
def about_us(request):
    return render(request, 'about_us.html')
def contact_us(request):
    return render(request, 'contact_us.html')
def gallery(request):
    return render(request, 'gallery.html')

def login(request):
    form = StudentForm()
    return render(request, 'login.html', {'form': form})

def register(request):
    form = NewStudentComplainForm()

    if request.method == 'POST':
        form = NewStudentComplainForm(request.POST)
    if form.is_valid():
        # print("VALID")
        form.save()
        NewStudentComplainForm()
        messages.success(request, 'User Register Successfully')
        return redirect('register')
    else:
        form = NewStudentComplainForm
    return render(request, 'register.html', {'form': form})
def proposal(request):
    form = NewStudentProposalForm()

    if request.method == 'POST':
        form = NewStudentProposalForm(request.POST)
    if form.is_valid():
        # print("VALID")
        form.save()
        NewStudentProposalForm()
        messages.success(request, 'User Register Successfully')
        return redirect('proposal')
    else:
        form = NewStudentProposalForm
    return render(request, 'proposal.html', {'form': form})







