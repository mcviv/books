from django.shortcuts import render
from django.contrib import messages
from django.shortcuts import render, redirect
from books.forms import newbook


# Create your views here.
def listing(request):
    form = newbook

    if request.method == 'POST':
        form = newbook(request.POST)
    if form.is_valid():
        # print("VALID")
        form.save()
        newbook()
        messages.success(request, 'User Listed Successfully')
        return redirect('register')
    else:
        form = newbook
    return render(request, '', {'form': form})
def upgrading(request):
    form = newbook

    if request.method == 'POST':
        form = newbook(request.POST)
    if form.is_valid():
        # print("VALID")
        form.save()
        newbook()
        messages.success(request, 'User Upgraded Successfully')
        return redirect('register')
    else:
        form = newbook
    return render(request, '', {'form': form})
def creating(request):
    form = newbook

    if request.method == 'POST':
        form = newbook(request.POST)
    if form.is_valid():
        # print("VALID")
        form.save()
        newbook
        messages.success(request, 'User listing Successfully')
        return redirect('register')
    else:
        form = newbook
    return render(request, '', {'form': form})

