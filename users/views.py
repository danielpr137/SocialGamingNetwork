from django.shortcuts import render, redirect
from .forms import UserProfileForm
from .models import UserProfile

def user_profile_view(request):
    if request.method == 'POST':
        form = UserProfileForm(request.POST)
        if form.is_valid():
            user_profile = form.save(commit=False)
            user_profile.user = request.user
            user_profile.save()
            return redirect('profile')
    else:
        form = UserProfileForm()

    return render(request, 'users/profile_form.html', {'form': form})