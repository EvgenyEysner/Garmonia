from django.urls import path
from .views import IndexView, AboutUs, Contact, Treatments


urlpatterns = [
    path('', IndexView.as_view(), name='home'),
    path('ueber-uns/', AboutUs.as_view(), name='about'),
    path('kontakt/', Contact.as_view(), name='contact'),
    path('behandlungen/', Treatments.as_view(), name='treatments'),
]