from django.contrib import messages
from website.models import  plogdb,clogdb,postdb
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login
from django.contrib.auth.models import User
from django.core.files.storage import FileSystemStorage
from django.utils.datastructures import MultiValueDictKeyError


# Create your views here.
def home1(request):
   return render(request, "home.html")

def mainlog(request):
   return render(request, "mainlog.html")

def loginpartner(request):
   return render(request,"loginpartner.html")

def client_log(request):
   if request.method == "POST":
      na = request.POST.get('cusername')
      pwd = request.POST.get('cpassword')
      if clogdb.objects.filter(cfname=na, cpassword=pwd).exists():
         request.session['cfname'] = na
         request.session['cpassword'] = pwd
         messages.success(request, "Login Successfully")
         return redirect(home1)
      else:
         messages.error(request, "Invalid Password or ID")
         return redirect(loginclient)
   else:
      messages.error(request, "Invalid Password or ID")
      return redirect(loginclient)
def signupclient(request):
   return  render(request,"signupclient.html")

def add_client(request):
   if request.method == "POST":
      cn = request.POST.get('cfname')
      cl = request.POST.get('clname')
      cb = request.POST.get('cbirthday')
      cg = request.POST.get('cgender')
      ce = request.POST.get('cemail')
      cp = request.POST.get('cphone')
      cc = request.POST.get('ccity')
      cpin = request.POST.get('cpincode')
      ci = request.POST.get('cid')
      cpass = request.POST.get('cpassword')
      cf = request.FILES['cfile']
      obj = clogdb(cfname=cn, clname=cl, cbirthday=cb, cgender=cg, cemail=ce,
                   cphone=cp, ccity=cc, cpincode=cpin,
                   cid=ci, cpassword=cpass,cfile=cf)
      obj.save()
      return redirect(loginclient)
def signuppartner(request):
   return  render(request,"signuppartner.html")


def add_partner(request):
   if request.method == "POST":
      pn = request.POST.get('pfname')
      pl = request.POST.get('plname')
      pb = request.POST.get('pbirthday')
      pg = request.POST.get('pgender')
      pe = request.POST.get('pemail')
      pp = request.POST.get('pphone')
      pq = request.POST.get('pqual')
      ps = request.POST.get('pskill')
      pc = request.POST.get('pcity')
      ppin = request.POST.get('ppincode')
      pi = request.POST.get('pid')
      ppass = request.POST.get('ppassword')
      pf = request.FILES['pfile']
      obj = plogdb(pfname=pn, plname=pl, pbirthday=pb, pgender=pg, pemail=pe,
                   pphone=pp, pqual=pq, pskill=ps, pcity=pc, ppincode=ppin,
                   pid=pi, ppassword=ppass,pfile=pf)
      obj.save()
      return redirect(loginpartner)

def loginclient(request):
   return render(request,"loginclient.html")


def client_log(request):
   if request.method == "POST":
      na = request.POST.get('cusername')
      pwd = request.POST.get('cpwd')
      if clogdb.objects.filter(cfname=na, cpassword=pwd).exists():
         request.session['cfname'] = na
         request.session['cpassword'] = pwd
         messages.success(request, "Login Successfully")
         return redirect(home1)
      else:
         messages.error(request, "Invalid Password or ID")
         return redirect(loginclient)
   else:
      messages.error(request, "Invalid Password or ID")
      return redirect(loginclient)

def client_logout(request):
   del request.session['cfname']
   del request.session['cpassword']
   return redirect(loginclient)

def loginpartner(request):
   return render(request,"loginpartner.html")

def partner_log(request):
   if request.method == "POST":
      na = request.POST.get('pusername')
      pwd = request.POST.get('ppwd')
      if plogdb.objects.filter(pfname=na, ppassword=pwd).exists():
         request.session['pfname'] = na
         request.session['ppassword'] = pwd
         messages.success(request, "Login Successfully")
         return redirect(home1)
      else:
         messages.error(request, "Invalid Password or ID")
         return redirect(loginpartner)
   else:
      messages.error(request, "Invalid Password or ID")
      return redirect(loginpartner)


def partner_logout(request):
   del request.session['pfname']
   del request.session['ppassword']
   return redirect(loginpartner)

def clienthome(request):
   return render(request,"clienthome.html")

def postclient(request):
   return render(request,"postclient.html")


def demopage(request):
   return render(request,"demo.html")

def save_post(request):
   if request.method == "POST":
      ac = request.POST.get('acat')
      at = request.POST.get('atitle')
      ad = request.POST.get('adisc')
      ar = request.POST.get('ars')
      al = request.POST.get('aloc')
      ada = request.POST.get('adate')
      ak = request.POST.get('akey')
      ap = request.FILES['aphoto']
      au = request.POST.get('ausername')
      aph= request.POST.get('aphone')
      obj = postdb(acat=ac, atitle=at, adisc=ad, ars=ar, aloc=al,
                   adate=ada, akey=ak, aphoto=ap, ausername=au,aphone=aph)
      obj.save()
      return redirect(postclient)

def view_post(request):
   data = postdb.objects.filter(ausername=request.session['cfname'])
   return render(request,"client_view.html",{'data':data})


def edit_post(request,dataid):
   data=postdb.objects.get(id=dataid)
   return render(request,"edit_post.html",{'data':data})

def update_post(request,postid):
   if request.method == "POST":
      ac = request.POST.get('acat')
      at = request.POST.get('atitle')
      ad = request.POST.get('adisc')
      ar = request.POST.get('ars')
      al = request.POST.get('aloc')
      ada = request.POST.get('adate')
      ak = request.POST.get('akey')
      try:
         ap = request.FILES['aphoto']
         fs = FileSystemStorage()
         file = fs.save(ap.name,ap)
      except MultiValueDictKeyError:
         file=postdb.objects.get(id=postid).aphoto
      postdb.objects.filter(id=postid).update(acat=ac, atitle=at, adisc=ad, ars=ar, aloc=al,adate=ada, akey=ak, aphoto=file)
      return redirect(view_post)

def delete_add(request,dataid):
   data=postdb.objects.filter(id=dataid)
   data.delete()
   return redirect(view_post)

def view_daily(request,cat_name):
   data=postdb.objects.filter(acat=cat_name)

   # # user=clogdb.objects.all()
   #
   # # if clogdb.cfname==postdb.ausername:
   # ausername1 = request.POST.get('ausername1')
   # aphone1 = request.POST.get('aphone1')

   return render(request, "view_daily.html",{'data':data})


# def invoicef(request):
#    # Retrieve the form data from the POST request
#    ausername1 = request.POST.get('ausername1')
#    aphone1 = request.POST.get('aphone1')
#
#
#    # Render the invoice template with the form data as context
#    context = {
#       'ausername1': ausername1,
#       'aphone1': aphone1,
#    }
#    return render(request, 'view_daily.html', context=context)


def view_perminent(request,cat_name):
   data=postdb.objects.filter(acat=cat_name)
   return render(request, "view_perminent.html",{'data':data})

def view_contract(request,cat_name):
   data=postdb.objects.filter(acat=cat_name)
   return render(request, "view_contract.html",{'data':data})

def about(request):
   return render(request,"aboutus.html")

def career(request):
   return render(request,"career.html")

def contactus(request):
   return render(request,"contactus.html")


def search_results(request):
   if request.method == "GET":
      query = request.GET.get('query')

      # Search in cuisinedb and recipedb for matching names and items
      post_result = postdb.objects.filter(atitle__icontains=query)
      # recipe_results = recipedb.objects.filter(recipe_name__icontains=query)
      client = clogdb.objects.all()

      context = {
         'post_result': post_result,
         # 'recipe_results': recipe_results,
         'client': client
      }

      return render(request, 'search1.html', context)