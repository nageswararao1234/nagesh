from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from .api import TestView, UserView

urlpatterns = [
    url(r'^test/$', TestView.as_view()),
    url(r'^user/$', UserView.as_view()),
    url('user/<int:pk>/', UserView.as_view()),

]

urlpatterns = format_suffix_patterns(urlpatterns)