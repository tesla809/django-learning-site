"""Views."""
from django.http import HttpResponse


def hello_world(request):
    """Hello world View."""
    return HttpResponse('Hello, World!')
