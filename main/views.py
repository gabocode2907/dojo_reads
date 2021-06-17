from django.shortcuts import redirect, render
from django.contrib import messages
from .models import User

# Create your views here.
def index(request):
    return render(request, 'index.html')

#localhost:8000/user/create_user
def create_user(request):
    if request.method == "POST":
        # Validation chech before safe in our DB
        errors = User.objects.registration_validator(request.POST)
        if len(errors) > 0:
            for key,value in errors.items():
                messages.error(request, value)
            return redirect('/')

