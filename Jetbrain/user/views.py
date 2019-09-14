from django.contrib import messages
from django.shortcuts import render, redirect

from Jetbrain.blog.models import Post
from . forms.user_forms import SignUp, UpdateUser, UpdateProfile
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


@login_required
def profile(request):
    user = request.user
    posts = Post.objects.filter(author=user)

    if request.method == 'POST':
        u_user = UpdateUser(request.POST, instance=request.user)
        u_profile = UpdateProfile(request.POST, request.FILES, instance=request.user.profile)
        if u_user.is_valid() and u_profile.is_valid():
            u_user.save()
            u_profile.save()
            messages.success(request, f'Your profile has been updated!')
            return redirect('profile')
    else:
        u_user = UpdateUser(instance=request.user)
        u_profile = UpdateProfile(instance=request.user.profile)

    context = {
        'posts': posts,
        'u_user': u_user,
        'u_profile': u_profile
    }
    # raise Exception(context)
    return render(request, 'user/profile.html', context)


def registration(request):
    if request.method == 'POST':
        form = SignUp(request.POST)
        # check whether it's valid:
        if form.is_valid():
            user = form.save(commit=False)

            # Cleaned(normalized) data
            password = form.cleaned_data['password']
            username = form.cleaned_data['username']

            #  Use set_password here
            user.set_password(password)

            user.save()

            user = authenticate(request, username=username, password=password)
            login(request, user)
            return redirect('index-blog')
    else:
        form = SignUp()
    return render(request, 'user/registration.html', {'form': form})


def user_login(request):
    form = {}
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            form['user'] = request.user
            return redirect('index-blog')
        else:
            form['error'] = 'Provide Valid Credentials'
            return render(request, "user/login.html", form)
    else:
        return render(request, "user/login.html", form)


def user_logout(request):
    logout(request)
    return redirect('login')
