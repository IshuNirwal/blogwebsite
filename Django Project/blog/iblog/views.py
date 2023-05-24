from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from .models import *
from django.core.paginator import Paginator
from django.core.mail import EmailMessage,send_mail
from django.conf import settings
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate,login
from django.contrib.auth.models import User
# Create your views here.

def home(request):
    CategoryData=Category.objects.all()
    PostData=Post.objects.all()
    paginator=Paginator(PostData,2)
    page_number=request.GET.get('page')
    Postdatafinal=paginator.get_page(page_number)
    totalpage=Postdatafinal.paginator.num_pages
    # if request.method=="GET":
    #     st=request.GET.get('postname')
    #     if st!=None:
    #         POST=Post.objects.filter(title=st)
    data={
        'CategoryData':CategoryData,
        'PostData':PostData,
        'PostData':Postdatafinal,
        'lastpage':totalpage,
        'totalpagelist':[n+1 for n in range(totalpage)],
        
    }
    return render(request,'home.html',data)
def search(request):
    st=request.GET.get('postname')
    POST=Post.objects.filter(title__icontains=st)
    data={
        'POST':POST
    }
    return render(request,'search.html',data)
     
def post(request, url):
    post= Post.objects.get(url=url)
    cats=Category.objects.all()
    if request.method=='POST':
        name=request.POST.get('name')
        email=request.POST.get('email')
        commentt=request.POST.get('comment')
        if name != "" and email !="":
           en = Comment(name=name,email=email,comment=commentt,post=post)
           en.save()
    comment=Comment.objects.filter(post=post)
    return render(request, 'posts.html',{'post':post,'cats':cats,'comment':comment})
def category(request,url):
    cat=Category.objects.get(url=url)
    posts=Post.objects.filter(cat=cat)
    return render(request,'category.html',{'cat':cat,'posts':posts})
def contact(request):
    if request.method=="POST":
        name_1=request.POST.get('fullname')
        email1=request.POST.get('email')
        message1=request.POST.get('message')
        en=ContactEnquiry(name=name_1,email=email1,message=message1)
        en.save()
        subject=" Regarding Registration"
        #htmly=get_template('email.html')
        from_email=settings.EMAIL_HOST_USER
        recipent_list=[email1]
        context={'name_1':name_1,'email':email1,'message':message1}
        html=render_to_string('email.html',context)
        #html_content=htmly.render(context)
        send_mail(
            subject,
            'message',
            from_email,
            recipent_list,
            html_message=html,
            
           )
        # msg.content_subtype='html'
        # msg.attach_file('email.html')
        # msg.send()
        return render(request,'thanks.html')
    return render(request,'contact.html')

@csrf_exempt
def handlerequest(request):
    if request.method=="POST":
        name=request.POST.get('fullname')
        cardnumber=request.POST.get('cardnum')
        date1=request.POST.get('date1')
        date2=request.POST.get('date2')
        cvc=request.POST.get('cvc')
        en=ContactEnquiry(name=name,cardnumber=cardnumber,date1=date1,date2=date2,cvc=cvc)
        en.save()
    return render(request,'payment.html')




def sign(request):
    if request.method=='POST':
        username=request.POST.get('username')
        
        password=request.POST.get('password')
        user=authenticate(username=username,password=password)
        if username!=None:
            if User.objects.filter(username=username):
               login(request,user)
               
               return redirect("/home")
           
           
    return render(request,'login.html')



def signup(request):
    if request.method=='POST':
        username=request.POST.get('username')
        email=request.POST.get('email')
        password=request.POST.get('password')
        myuser=User.objects.create_user(username=username,email=email,password=password)
        myuser.save()
        print(username,email,password)
        return render(request,'login.html')
    return render(request,'signup.html')
def About(request):
    return render(request,"aboutus.html")
