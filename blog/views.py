from django.shortcuts import render
from django.http import HttpResponse
from blog.models import Atricle

# Create your views here.
def Home(request):
  post_list = Atricle.objects.all()  # 获取全部article 对象
  return render(request, 'home.html', {'post_list': post_list})
  # return HttpResponse("Hello World, Django")

def detail(request, my_args):
  return HttpResponse("You're looking at my_args %s." % my_args)