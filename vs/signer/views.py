from django.shortcuts import render
from django.contrib.auth.models import User
# Create your views here.


def signup(request):
    #request's method in form html tag is equal to POST or not? Else the url will show the input data in the form. So we go through method == post check first.
    if request.method == 'POST':
        #this condition will check if the password entered in both the parameters is equal else throw an error.
        if request.POST['pass1'] == request.POST['pass2']:
            #Try block to give an error if username already taken by some other user.
            try:
                #imported from User module, checks all objects from database using get function and compare them with the form username.
                user =  User.objects.get(username = request.POST['Username'])
                #if tried and found a conflict in username, throw the return, else it goes in except part
                return render(request, 'signer/signup.html', {'error': 'Username Already Taken'})
            #if User does not exist in database
            except User.DoesNotExist:
                #create a user with username and password from POST function
                User.objects.create_user(request.POST['Username'], password = request.POST['pass1'], email=request.POST
                ['emaik'])
                #finally return the signup html after successfull completion
            return render(request, 'signer/signup.html')
        else:
            #if the password doesn't match.
            return render(request, 'signer/signup.html', {'error' : 'Passwords didn\'t match'})
    else:
        #if the request is GET and not POST.
        return render(request, 'signer/signup.html')