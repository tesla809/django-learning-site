"""Views for course app."""
from django.http import HttpResponse
from django.shortcuts import render

from courses.models import Course


# Create your views here.
def course_list(request):
    """Return simple course list."""
    courses = Course.objects.all()
    output = ', '.join([str(course) for course in courses])
    return HttpResponse(output)
