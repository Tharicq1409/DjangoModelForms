from django.shortcuts import render,redirect
from . forms import user_reg_form

def formpage(request):
    if request.method == 'POST':
        form = user_reg_form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = user_reg_form()
    return render(request,"index.html",{'form': form})