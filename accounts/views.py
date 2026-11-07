from django.shortcuts import render, redirect

from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def register(request):
    # register a new user
    if request.method != "POST":
        # display a blank form
        form = UserCreationForm()
    else:
        # deal with the form
        form = UserCreationForm(data=request.POST)
        if form.is_valid():
            new_user = form.save()
            # let the user login in automatically, then redirect to main page
            login(request, new_user)
            return redirect('learning_logs:index')
    # display the blank form or invalid form
    context = {'form':form}
    return render(request, 'registration/register.html', context)