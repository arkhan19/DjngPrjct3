from django.conf.urls import url,include
from vs.signer.views import *

#this url is for singer application
app_name = 'signer'


urlpatterns = [
    url(r'^signup/', signup, name='signup'),
    url(r'^login/', log_in, name='log_in'),
    url(r'^signout/', signout, name='log_out'),
]
