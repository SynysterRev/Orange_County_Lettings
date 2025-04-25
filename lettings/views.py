from django.shortcuts import render, get_object_or_404
from sentry_sdk import capture_exception

from lettings.models import Letting


def index(request):
    """
    Display a list of all available lettings.
    :param request: The HTTP request
    :return: A rendered HTML page displaying the list of all available Lettings.
    """
    try:
        lettings_list = Letting.objects.all()
    except Exception as e:
        capture_exception(e)
        raise e
    context = {'lettings_list': lettings_list}
    return render(request, 'lettings/index.html', context)


def letting(request, letting_id):
    """
    Display a specific letting by ID.
    :param request: The HTTP request
    :param letting_id: The ID of the letting
    :return: A rendered HTML page displaying a specific letting by ID.
    """
    letting = get_object_or_404(Letting, id=letting_id)
    context = {
        'title': letting.title,
        'address': letting.address,
    }
    return render(request, 'lettings/letting.html', context)
