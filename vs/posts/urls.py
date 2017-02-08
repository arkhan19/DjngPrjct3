from django.conf.urls import url
from vs.posts.views import *

#this url is for singer application
app_name = 'posts'


urlpatterns = [
    url(r'^create/', create, name='create'),
    #url(r'^login/', log_in, name='log_in'),
]
