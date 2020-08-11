from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404, HttpResponseRedirect
import datetime as dt
from .models import Post
from .forms import NewsLetterForm
from .email import send_welcome_email
from django.contrib.auth.decorators import login_required.


@login_required(login_url='/accounts/login/')
def article(request, article_id):

    # Create your views here.


def posts_today(request):
    posts = Post.todays_posts()
    if request.method == 'POST':
        form = NewsLetterForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['your_name']
            email = form.cleaned_data['email']
            recipient = NewsLetterRecipients(name=name, email=email)
            recipient.save()
            send_welcome_email(name, email)
            HttpResponseRedirect('posts_today')
        else:
            form = NewsLetterForm()
        return render(request, 'insta-posts/today-posts.html', {"date": date, "posts": posts, "letterForm": form})


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
    return render(request, 'insta-posts/past-posts.html', {"date": date, "posts": posts})


def search_results(request):

    if 'post' in request.GET and request.GET["post"]:
        search_term = request.GET.get("post")
        searched_postss = Post.search_by_title(search_term)
        message = f"{search_term}"

        return render(request, 'insta-posts/search.html', {"message": message, "postss": searched_postss})

    else:
        message = "You haven't searched for any term"
        return render(request, 'insta-postss/search.html', {"message": message})


def post(request, post_id):
    try:
        post = Post.objects.get(id=post_id)
    except DoesNotExist:
        raise Http404()
    return render(request, "insta-posts/post.html", {"post": post})
