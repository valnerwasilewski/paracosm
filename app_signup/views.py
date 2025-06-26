from django.http import HttpResponseBadRequest, HttpResponseNotAllowed
from django.shortcuts import redirect, render

from .models import User, UserType


def home(request):
    return render(request, 'users/home.html')


def home2(request):
    return render(request, 'users/home2.html')


def signup_view(request):
    """
    Show sign up page
    """
    return render(request, 'users/sign_up.html')


def signin_view(request):
    return render(request, 'users/sign_in.html')


def registration_completed_view(request):
    return render(request, 'users/registration_completed.html')


def userslist_view(request):
    users = User.objects.all()
    return render(request, 'users/users_list.html', {'users': users})


def register_user(request):
    """
    Process data and register a new user
    """

    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        user_type_id = 3

        print(f'user_type_id padrão: {user_type_id}')

        if not username or not email or not password:
            return HttpResponseNotAllowed('All fiedls are mandatory!')

        try:
            user_type_id = int(user_type_id)
            print(f'user_type_id recebido: {user_type_id}')

            user_type = UserType.objects.get(user_type_id=user_type_id)

        except (ValueError, UserType.DoesNotExist):
            return HttpResponseBadRequest('Invalid User Type')

        new_user = User.create_user(
            username=username, email=email, password=password
        )
        new_user.save()

        return redirect('registration_completed')

    return HttpResponseNotAllowed(['POST'])
