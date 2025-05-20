import logging

from django.shortcuts import render
from sentry_sdk import capture_exception

logger = logging.getLogger(__name__)


def index(request):
    """
    Display the home page.
    :param request: The HTTP request
    :return: A rendered HTML page displaying the home page.
    """
    return render(request, 'index.html')


def custom_404(request, exception=None):
    """
    Display a custom page for error 404
    :param request: The HTTP request
    :param exception: The exception that caused the 404 error (optional).
    :return:
    """
    logger.warning(f"Custom 404: {request.path} - User: {request.user}")
    capture_exception(exception)
    return render(request, '404.html', status=404)


def custom_500(request, exception=None):
    """
    Display a custom page for error 500
    :param request: The HTTP request
    :param exception: The exception that caused the server error (optional).
    :return:
    """
    logger.error(f"Custom 500: {request.path} - User: {request.user}",
                 extra={'request': request})
    capture_exception(exception)
    return render(request, '500.html', status=500)
