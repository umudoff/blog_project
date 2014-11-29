from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from blog.forms import UserForm, UserProfileForm, PostForm, CommentForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User

from django.template import RequestContext
from django.shortcuts import render_to_response
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout

from models import Post, Comment, UserProfile


# View glavnoy stranici
def index(request):
    # kontekst zaprosa, soderjit takuyu informaciyu kak detali klienta
    context = RequestContext(request)

    # struktura dlya otpravleniya dannix v shabloni
    context_dict = {'boldmessage': "Welcome to the blog"}

    return render_to_response('blog/index.html', context_dict, context)

def register(request):
    context = RequestContext(request)
    registered=False

    if request.method == 'POST':
       user_form= UserForm(data=request.POST)
       if user_form.is_valid():
          user=user_form.save()
          user.set_password((user.password))
          registered=True
          # login
          user.backend="django.contrib.auth.backends.ModelBackend"
          login(request, user)
       else:
           print user_form.errors
    else:
        user_form=UserForm()
    return render_to_response('blog/register.html',
                          {'user_form':user_form, 'registered':registered},
                          context)



def user_login(request):

    context = RequestContext(request)


    if request.method == 'POST':

        username = request.POST['username']
        password = request.POST['password']


        user = authenticate(username=username, password=password)


        if user is not None:

            if user.is_active:
                #   authenticate()
                login(request, user)
                return HttpResponseRedirect('/') #/blog/
            else:

                return HttpResponse("Your Rango account is disabled.")
        else:

            print "Invalid login details: {0}, {1}".format(username, password)
            return HttpResponse("Invalid login details supplied.")

    else:

         return render_to_response('blog/login.html', {}, context)



@login_required
def restricted(request):
    return HttpResponse("Since you're logged in, you can see this text!")



@login_required
def user_logout(request):

    logout(request)


    return HttpResponseRedirect('/blog/')



def posts(request):
    context = RequestContext(request)
    p_list = Post.objects.all()
    c_list = Comment.objects.all()
    
    

    context_dict = {
        'posts_list': p_list,
         'comments_list':c_list,
     }



    return render_to_response('blog/posts.html',
                          context_dict, context)


def add_post(request):
    context = RequestContext(request)
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
             form.save(commit=True)
             return added(request)
        else:
            print form.errors
    else:

        nn=request.META.__getitem__("USER")
        print request
        form = PostForm({'fk_CreatedBy': User.objects.get(username=request.user.username)} )

    return render_to_response('blog/add_post.html', {'form':form}, context)

def added(request):
    print "added"
    return HttpResponseRedirect('/blog/posts/')


def add_comment(request, posid):
    context= RequestContext(request)
    pos=Post.objects.get(pk=posid)
    pid=posid
    if request.method == 'POST':
        form = CommentForm(data=request.POST)
        if form.is_valid():
           comm= form.save(commit=True)
           return added(request)
        else:
            print form.errors
    else:
        nn = request.META.__getitem__("USER")
        print request
        form = CommentForm(
                           {'fk_UserID': User.objects.get(username=request.user.username), 'postID':pid})

    return render_to_response('blog/add_comment.html', {'comment_form':form,'pos_id':pid}, context)





#
def edit_post(request, posid):
    context=RequestContext(request)
    pos=Post.objects.get(pk=posid)
    form = PostForm(request.POST or None, instance=pos)
    if form.is_valid():
       form.save()
       return added(request)
    

    return render_to_response('blog/edit_post.html', {'form':form, 'pos_id':posid}, context)


def edit_comment(request, comid):
    context=RequestContext(request)
    com=Comment.objects.get(pk=comid)
    form= CommentForm(request.POST or None, instance=com)
    if form.is_valid():
       form.save()
       return added(request)

    return render_to_response('blog/edit_comment.html', {'form':form, 'comid':comid}, context)



