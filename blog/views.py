from django.shortcuts import render
from django.http import HttpResponse
from blog.models import Atricle

# Create your views here.
def home(request):
  post_list = Atricle.objects.all()  # 获取全部article 对象
  return render(request, 'home.html', {'post_list': post_list})
  # return HttpResponse("Hello World, Django")

def detail(request, id):
  try:
    post = Atricle.objects.get(id=str(id))
  except Atricle.DoseNotExist:
    raise Http404
  
  return render(request, 'post.html', {'post': post})

def archives(request):
  try:
    post_list = Atricle.objects.all()
  except Atricle.DoseNotExist:
    raise Http404
  return render(request, 'archives.html', {'post_list' : post_list, 
                                            'error' : False})
                                  
def about_me(request) :
    return render(request, 'aboutme.html')

def search_tag(request, tag) :
    try:
        post_list = Atricle.objects.filter(category__iexact = tag) #contains
    except Article.DoesNotExist :
        raise Http404
    return render(request, 'tag.html', {'post_list' : post_list})

def blog_search(request):
    if 's' in request.GET:
        s = request.GET['s']
        if not s:
            return render(request,'home.html')
        else:
            post_list = Atricle.objects.filter(title__icontains = s)
            if len(post_list) == 0 :
                return render(request,'archives.html', {'post_list' : post_list,
                                                    'error' : True})
            else :
                return render(request,'archives.html', {'post_list' : post_list,
                                                    'error' : False})
    return redirect('/')