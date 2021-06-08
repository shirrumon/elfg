import os
from elfg.main import Elfg
from urls import urlpatterns
from elfg.middleware import middlewares

settings = {
    'BASE_DIR': os.path.dirname(os.path.abspath(__file__)),
    'TEMPLATE_DIR_NAME': 'templates'
}

app = Elfg(
    urls=urlpatterns,
    settings=settings,
    middlewares=middlewares
)