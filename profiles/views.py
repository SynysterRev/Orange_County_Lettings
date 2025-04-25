from django.shortcuts import render, get_object_or_404
from sentry_sdk import capture_exception

from profiles.models import Profile


def index(request):
    """
    Display a list of all users profiles.
    :param request: The HTTP request
    :return: A rendered HTML page displaying a list of all users profiles.
    """
    try:
        profiles_list = Profile.objects.all()
    except Exception as e:
        capture_exception(e)
        raise e
    context = {'profiles_list': profiles_list}
    return render(request, 'profiles/index.html', context)


def profile(request, username):
    """
    Display a specific user's profile by ID.
    :param request: The HTTP request
    :param username: The username of the user
    :return: A rendered HTML page displaying a specific user's profile by ID.
    """
    profile = get_object_or_404(Profile, user__username=username)
    context = {'profile': profile}
    return render(request, 'profiles/profile.html', context)
