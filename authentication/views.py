from django.contrib.auth.models import User, auth
from django.views.generic import TemplateView, CreateView, View, RedirectView
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import Group
from django.contrib import messages
from django.contrib.auth.backends import ModelBackend, UserModel
from django.db.models import Q
from django.core.exceptions import MultipleObjectsReturned
from bookstore.models import BookStore, NewsLetter
from .models import Profile
from django.core.mail import send_mail


def subscription(request):
    subject = 'Book Zone Subscription'
    body = "You Have Been Subscribed to our Newsletter Successfully. \
    Now you will receive updates every time we add a Book"

    subject1 = 'Book Zone Subscription'
    body1 = "You Have Been UnSubscribed to our Newsletter Successfully. \
        Now we will not bother you further"
    if request.method == 'POST':
        profile = Profile.objects.get(user=request.user)
        if request.user.profile.subscribed:
            profile.subscribed = False
            send_mail(subject1, body1, 'shivamrawat829@gmail.com', [request.user.email, ])
            profile.save()
        else:
            profile.subscribed = True
            send_mail(subject, body, 'shivamrawat829@gmail.com', [request.user.email,])
            profile.save()

    return redirect('authentication:index')
    # send_mail('subject', 'body of the message', 'shivamrawat829@gmail.com', ['shivamrawat829@gmail.com',])


class LogoutView(RedirectView):
    def get(self, request, *args, **kwargs):
        auth.logout(request)
        return redirect('authentication:login')


class IndexView(View):
    template_name = 'index.html'

    def get(self, request):
        query = request.GET.get('q', False)
        if query:
            result = BookStore.objects.filter(
                Q(title__icontains=query) |
                Q(description__icontains=query)
            ).order_by('-timestamp')
            all_books = result.filter(availability='available')
        else:
            all_books = BookStore.objects.filter(availability='available').order_by('-timestamp')

        return render(request, self.template_name, {'all_books': all_books,
                                                    }
                      )


class LoginView(View):
    template_name = 'login-page.html'

    def get(self, request):
        if request.user.is_authenticated:
            return redirect('authentication:index')
            # return render(request, self.template_name)
        else:
            # return redirect('authentication:login')
            return render(request, self.template_name)

    def post(self, request):
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('authentication:index')
        else:
            messages.info(request, 'Invalid Credentials')
            return render(request, self.template_name)


class SignUpView(View):
    template_name = 'register.html'

    def get(self, request):
        print("request ", request)
        return render(request, self.template_name)

    def post(self, request):
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        name1 = request.POST['name']

        name = name1.split(" ")
        if len(name) > 1:
            first_name = name[0].capitalize()
            last_name = name[1].capitalize()
        else:
            first_name = name[0].capitalize()
            last_name = ""

        if not username or not email or not password or not confirm_password or not name:
            messages.info(request, 'Please fill all the fields...')
            return render(request, self.template_name, {'email': email, 'name': name1,
         'username': username, 'password': password, 'confirm_password': confirm_password})

        elif password == confirm_password:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'username taken')
                return render(request, self.template_name, {'email': email, 'name': name1, 'username': ""})

            elif User.objects.filter(email=email).exists():
                messages.info(request, 'email taken')
                return render(request, self.template_name, {'email': "", 'username': username,
                                                            'name': name1})
            else:
                user = User.objects.create_user(username=username, email=email, password=password,
                                                first_name=first_name, last_name=last_name)

                # group = Group.objects.get(name='users')
                # user.groups.add(group)
                user.save()
                # profile = Profile(user=user)
                # profile.save()
                return redirect('authentication:index')
        else:
            messages.info(request, 'Not Maching')
            return render(request, self.template_name,{'email': email, 'name': name1, 'username': username})





