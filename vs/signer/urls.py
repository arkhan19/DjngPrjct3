from django.conf.urls import url
from vs.signer.views import *

#this url is for singer application
app_name = 'signer'


urlpatterns = [
    url(r'^signup/', signup, name='signup'),
    url(r'^login/', log_in, name='log_in'),
]
