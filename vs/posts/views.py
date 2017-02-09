from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.utils import timezone

# Create your views here.
from vs.posts.models import Posts  # model class


def home(request):
    homies = Posts.objects.order_by('pub_date')
    return render(request, 'posts/home.html', {'post_obj_for_html': homies})


@login_required
def create(request):
    if request.method == 'POST':
        if request.POST['title'] and request.POST['u_r_l']:
            post_object = Posts()
            post_object.title = request.POST['title']
            post_object.url = request.POST['u_r_l']
            post_object.author = request.user
            post_object.pub_date = timezone.datetime.now()
            post_object.save(request)
            return redirect('home')
        else:
            return render(request, 'posts/create.html', {'error': 'Enter Title Please, Post not created, try again.'})
    else:
        return render(request, 'posts/create.html')


def __str__(self):
    return '%s' % self.title


def c_up(request, pk):
    if request.method == 'POST':
        #  model's primary key
        counter = Posts.objects.get(pk=pk)
        counter.commends +=1
        counter.save()
        return redirect('home')


def c_down(request, pk):
    #  model's primary key
    if request.method == 'POST':
        counter = Posts.objects.get(pk=pk)
        counter.commends -=1
        counter.save()
        return redirect('home')












