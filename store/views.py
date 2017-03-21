from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from django.template import loader
from django.http import Http404
from .models import bijou,sub_bijou



def store_page(request):
    all_bijou = bijou.objects.all()
    context={
        'all_bijou':all_bijou,
    }
    return render(request,'store/index.html',context)

def bijou_details(request,bijou_name):
    """
    try:
        one_bijou = bijou.objects.get(name=bijou_name)
    except bijou.DoesNotExist:
        raise Http404("Bijou does not exist")
    """
    one_bijou = get_object_or_404(bijou,name=bijou_name)
    return render(request,'store/detail.html',{'one_bijou':one_bijou})

def bijou_favorite(request,bijou_name):
    one_bijou = get_object_or_404(bijou, name=bijou_name)
    try:
        one_sub_bijou = one_bijou.sub_bijou_set.get(name=request.POST["sub_bijou"])
    except (KeyError,sub_bijou.DoesNotExist):
        return render(request,"store/detail.html",{
            'one_bijou':one_bijou,
            'error_message':'Your choice is invalid !!'
        })
    else:
        try:
            if(request.POST["favor_done"]):
                one_sub_bijou.favorite = True
                one_sub_bijou.save()
                return render(request,"store/detail.html",{'one_bijou':one_bijou})
        except:
            if (request.POST["favor_undone"]):
                one_sub_bijou.favorite = False
                one_sub_bijou.save()
                return render(request, "store/detail.html", {'one_bijou': one_bijou})
