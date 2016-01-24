from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render
from django.shortcuts import render, get_object_or_404, redirect
from .forms import PostForm
# Create your views here.
from .models import Post

def post_create(request):
    form = PostForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        instance = form.save(commit = False)
        instance.save()
        #mesage success
        messages.success(request, "Successfully Created")
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
    queryset_list = Post.objects.all()
    paginator = Paginator(queryset_list, 10) # Show 25 contacts per page
    page_request_var = 'page'
    page = request.GET.get(page_request_var)
    try:
        queryset = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        queryset = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        queryset = paginator.page(paginator.num_pages)

    context = {
        "object_list" : queryset,
        "title" : "List"
     }
    return render(request, "post_list.html", context)


def post_update(request, id=None):
    instance = get_object_or_404(Post, id =id)
    form = PostForm(request.POST or None, request.FILES or None, instance=instance)
    if form.is_valid():
        instance = form.save(commit = False)
        instance.save()
        messages.success(request, "Item Saved", extra_tags='some-tag')
    return HttpResponseRedirect(instance.get_absolute_url())
    context = {
        "title" : instance.title,
        "instance": instance,
        "form" :form
     }
    return render(request, "post_form.html", context)

def post_delete(request, id=None):
    instance = get_object_or_404(Post, id =id)
    instance.delete()
    messages.success(request, "Successfully Deleted")
    return redirect("posts:list")
