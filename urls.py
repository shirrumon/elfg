from elfg.urls import Url
from view import *

urlpatterns = [
    Url('^$', Homepage),
    Url('^/math$', EpicMath),
    Url('^/hello$', Hello),
]