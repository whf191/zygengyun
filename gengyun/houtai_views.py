#coding=utf-8
from  __future__ import unicode_literals
from django.shortcuts import render_to_response,HttpResponse,HttpResponseRedirect
from django.contrib.auth.models import User
from django.forms import ModelForm
from suit_ckeditor.widgets import CKEditorWidget
from django.template import RequestContext
from django.contrib.auth import authenticate,login,logout
from  django.contrib.auth.decorators import  login_required
from  .models import  gengyuns ,zhongzi
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger  #导入django自带的分页工具
from .houtai_caidan import caidan
import datetime


class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ["username","password","first_name","email"]



def gengyun_login(request):
    if request.method == "GET":
        if request.user.is_authenticated():

            return  HttpResponseRedirect("/gengyun_index/")

        else:
            return render_to_response("zhuce.html",{'form':UserForm()},context_instance=RequestContext(request))

    else:
        form = UserForm(request.POST)
        if form.is_valid():
            print request.POST
            User.objects.create_user(username=request.POST.get("username",None),password=request.POST.get("password",None),first_name=request.POST.get("first_name",None),email=request.POST.get("email",None))
            return HttpResponseRedirect("/gengyun_denglu/")
        else:
            return render_to_response("zhuce.html", {'form': form},context_instance=RequestContext(request))

def gengyun_denglu(request):
    if request.method == "GET":
        if request.user.is_authenticated():
            return HttpResponseRedirect("/gengyun_index/")
        else:
            return  render_to_response("denglu.html",context_instance=RequestContext(request))

    else:
        username = request.POST.get("username",None)
        password = request.POST.get("password",None)
        if username and password:
            user = authenticate(username=username,password=password)
            if user is not None:
                print login(request,user)
                return HttpResponseRedirect("/gengyun_login/")

        return  HttpResponseRedirect('/gengyun_denglu/')


def gengyun_logout(request):
    logout(request)
    return HttpResponseRedirect("/gengyun_index/")

@login_required
def houtai_admin(request):
    cd = caidan()
    request.caidan = cd

    return render_to_response("houtai_admin.html",{"request":request})

@login_required
def houtai_admin_grxx(request):
    t =  request.GET.get("t",None)
    if request.method == "GET":
        cd = caidan()
        request.caidan = cd
        return render_to_response("houtai_admin_grxx.html", context_instance=RequestContext(request))

    else:
        if t == "yonghu":
            first_name = request.POST.get("first_name",None)
            email = request.POST.get("email",None)
            user_obj = request.user
            if first_name and email:
                user_obj.first_name = first_name
                user_obj.email = email
                try:
                    user_obj.save()
                    return HttpResponse("0|修改成功.")
                except Exception,e:
                    print e
                    return HttpResponse("2|修改失败")
            return HttpResponse("3|参数不符")

        elif t == "password":
            old_password = request.POST.get("old_password",None)
            xin_password1 =  request.POST.get("xin_password1",None)
            xin_password2 = request.POST.get("xin_password2", None)

            if old_password and xin_password1 and xin_password2:
                user = authenticate(username=request.user.username,password=old_password)
                if user is None:
                    return HttpResponse("2|老密码认证失败")
                if xin_password1 != xin_password2:
                    return HttpResponse("3|两次密码输入不一样")

                user_obj = request.user
                user_obj.set_password(xin_password1)
                user_obj.save()
                return HttpResponse("0|用户密码修改成功")


        return HttpResponse("3|参数不符")

#我的耕耘分页
def get_gengyuns(pk,limit=10):
    try:
        pk = int(pk)
    except Exception,e:
        print e
        return False

    dhl_list = gengyuns.objects.filter(user_id=pk).order_by('-pk')
    print dhl_list
    p = Paginator(dhl_list,limit)

    return p

#我的种子分页
def get_zhongzis(pk,limit=10):
    try:
        pk = int(pk)
    except Exception,e:
        print e
        return False

    dhl_list = zhongzi.objects.filter(user_id=pk).order_by('-pk')

    p = Paginator(dhl_list,limit)

    return p


@login_required
def houtai_admin_wdgy(request):
    cd = caidan()
    request.caidan = cd

    fenye_duixiang =  get_gengyuns(pk=request.user.pk)
    page = request.GET.get('page', None)

    if not page:
        page = 1
    try:
        huoqu_mouye_jilu = fenye_duixiang.page(page)
    except PageNotAnInteger:
        huoqu_mouye_jilu = fenye_duixiang.page(1)
    except EmptyPage:
        huoqu_mouye_jilu = fenye_duixiang.page(fenye_duixiang.num_pages)  # 取最后一条记录


    return render_to_response("houtai_admin_wdgy.html", {"request": request,'huoqu_mouye_jilu':huoqu_mouye_jilu}   )

@login_required
def houtai_admin_gyzz(request):
    cd = caidan()
    request.caidan = cd
    userid_pk = request.user.pk
    fenye_duixiang =  get_zhongzis(pk=request.user.pk)
    page = request.GET.get('page', None)

    if not page:
        page = 1
    try:
        huoqu_mouye_jilu = fenye_duixiang.page(page)
    except PageNotAnInteger:
        huoqu_mouye_jilu = fenye_duixiang.page(1)
    except EmptyPage:
        huoqu_mouye_jilu = fenye_duixiang.page(fenye_duixiang.num_pages)  # 取最后一条记录


    return render_to_response("houtai_admin_zz.html", {"request": request,'huoqu_mouye_jilu':huoqu_mouye_jilu}   )





@login_required
def houtai_fayan(request):

    print request.POST


    if request.method == "GET":
        #context_instance csrf需要
        return render_to_response("houtai_admin_fayan.html",context_instance=RequestContext(request))

    else:

        t = request.GET.get("t",None)
        name =  request.POST.get("name","")
        text = request.POST.get("editor1","")

        if len(name.strip()) == 0:
            return HttpResponse("1|标题为空,不允许发表")

        try:

            gys = gengyuns(user_id=request.user, name=name, text=text,create_date=datetime.datetime.today())
            gys.save()

        except Exception, e:
            print e
            return HttpResponse("2|保存失败，联系管理员")

        if t == "ajax":
            return HttpResponse("0|/houtai_admin_wdgy/")

        else:
            return HttpResponseRedirect("/houtai_admin_wdgy/")

@login_required
def zhongzi_fayan(request):
    print request.POST
    gengyuns_pk = request.GET.get("pk",None)
    if  not gengyuns_pk:
        return HttpResponse("2|不合理的请求")

    request.gengyuns_pk = gengyuns_pk

    if request .method == "GET":
        return render_to_response("houtai_admin_zhongzi_fayan.html",context_instance=RequestContext(request))

    else:
        t = request.GET.get("t",None)
        name =  request.POST.get("name","")
        text = request.POST.get("editor1","")

        if len(name.strip()) == 0:
            return HttpResponse("1|标题为空,不允许发表")

        try:

            gy_pk = gengyuns.objects.get(pk=gengyuns_pk)

            gys = zhongzi(user_id=request.user, gengyuns_id=gy_pk,name=name, text=text,create_date=datetime.datetime.today())
            gys.save()

        except Exception, e:
            print e
            return HttpResponse("2|保存失败，联系管理员")

        if t == "ajax":
            return HttpResponse("0|/gengyun_zhongzi/?pk=%s" % gengyuns_pk)

        else:
            return HttpResponseRedirect("/gengyun_zhongzi/?pk=%s" % gengyuns_pk)


