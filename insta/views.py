from django.shortcuts import render,redirect
from django.http  import HttpResponse,Http404
import datetime as dt
from .models import Post

# Create your views here.

def posts_today(request):
    date = dt.date.today()
    posts = Post.todays_posts()
    return render(request, 'insta-posts/today-posts.html', {"date": date,"posts":posts})


def past_days_posts(request, past_date):
    try:
        # Converts data from the string Url
        date = dt.datetime.strptime(past_date, '%Y-%m-%d').date()
    except ValueError:
        # Raise 404 error when ValueError is thrown
        raise Http404()
        assert False

    if date == dt.date.today():
        return redirect(posts_today)

    posts = Post.days_posts(date)
    return render(request, 'insta-posts/past-posts.html',{"date": date,"posts":posts})


def search_results(request):

    if 'post' in request.GET and request.GET["post"]:
        search_term = request.GET.get("post")
        searched_postss = Post.search_by_title(search_term)
        message = f"{search_term}"

        return render(request, 'insta-posts/search.html',{"message":message,"postss": searched_postss})

    else:
        message = "You haven't searched for any term"
        return render(request, 'insta-postss/search.html',{"message":message})

def post(request,post_id):
    try:
        post = Post.objects.get(id = post_id)
    except DoesNotExist:
        raise Http404()
    return render(request,"insta-posts/post.html", {"post":post})