from django.shortcuts import render,get_object_or_404
from .models import Post
from django.core.paginator import  Paginator,EmptyPage,PageNotAnInteger
from django.views.generic import ListView
from .forms import EmailPostForm,CommentForm
from django.core.mail import send_mail
from webapp.settings import EMAIL_HOST_USER
from taggit.models import Tag
from django.db.models import Count
from  haystack.forms import SearchForm

# Create your views here.


class PostListView(ListView):
    queryset = Post.published.all()
    context_object_name = 'posts'
    paginate_by = 1
    template_name = 'blog/post/list.html'



def post_list(request,tag_slug=None):
    object_list = Post.published.all()
    tag = None


    if tag_slug:
        tag = get_object_or_404(Tag,slug=tag_slug)
        object_list = object_list.filter(tags__in=[tag])


    paginator = Paginator(object_list,1)
    page = request.GET.get('page')

    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = (paginator.page(1))
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    return render(request,'blog/post/list.html',{'page':page,'posts':posts,'tag':tag})


def post_detail(request,post_slug):
    post = Post.object.get(slug=post_slug)
    comments = post.comments.filter(active=True)
    new_comment = None
    post_tags_ids = post.tags.values_list('id',flat=True)
    similar_posts = Post.published.filter(tags__in=post_tags_ids)
    similar_posts = similar_posts.exclude(id=post.id)

    similar_posts = similar_posts.annotate(same_tags=Count('tags'))

    if request.method =='POST':
        comment_from = CommentForm(data=request.POST)
        if comment_from.is_valid():
            new_comment = comment_from.save(commit=False)
            new_comment.post = post
            new_comment.save()
    else:
        comment_from = CommentForm()
    context_dict = {'post':post,'new_comment':new_comment,'comments':comments,
                    'comment_form':comment_from,
                    'similar_posts':similar_posts}
    return render(request,'blog/post/detail.html',context_dict)




def post_search(request):
    form = SearchForm()
    search_dict =None
    if 'q' in request.GET:
        form = SearchForm(request.GET)
        cd = request.GET['q']
        posts = form.search()

        total_results = posts.count()
        search_dict = {'posts': posts, 'keyword': cd, 'total_results': total_results, 'form': form,}


    return render(request, 'blog/post/search.html', search_dict)







def post_share(request,post_id):
    post = get_object_or_404(Post,id=post_id,status='published')

    return render(request,'blog/post/example.html',{'post':post,})






