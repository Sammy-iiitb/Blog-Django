from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from .forms import PostForm
# Create your views here.
from .models import Post

def post_create(request):
    form = PostForm(request.POST or None)
    if form.is_valid():
        instance = form.save(commit = False)
        instance.save()
        return HttpResponseRedirect(instance.get_absolute_url())
    #if request.method = "POST"
    #    print request.POST.get("content")
    # setting context to post_form.html
    context = {
        "form" : form,
    }
    return render(request, "post_form.html", context)

def post_detail(request, id=None):
    instance = get_object_or_404(Post, id =id)
    context = {
        "title" : instance.title,
        "instance": instance
     }
    return render(request, "post_detail.html", context)

def post_list(request):
    #return HttpResponse("<h1>List</h1>")
    #if request.user.is_authenticated():
    #    context = {
    #        "title" : "My user List"
    #    }
    #else :

    queryset = Post.objects.all()
    context = {
        "object_list" : queryset,
        "title" : "List"
     }
    return render(request, "index.html", context)

def post_update(request, id=None):
    instance = get_object_or_404(Post, id =id)
    form = PostForm(request.POST or None, instance=instance)
    if form.is_valid():
        instance = form.save(commit = False)
        instance.save()
    return HttpResponseRedirect(instance.get_absolute_url())
    context = {
        "title" : instance.title,
        "instance": instance,
        "form" :form
     }
    return render(request, "post_form.html", context)

def post_delete(request):
    return HttpResponse("<h1>Delete</h1>")
