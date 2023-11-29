from email.policy import HTTP
import random as rng
from django.shortcuts import render
from django.shortcuts import redirect
from django.shortcuts import HttpResponse
from urllib3 import HTTPResponse
import mdtex2html
from django.http import FileResponse
from . import util
from django.core.files.base import ContentFile
from django.core.files.storage import default_storage
from django.views.decorators.csrf import csrf_exempt
from django.core.files.storage import default_storage


def interractive(request, name):
    return render(request, "encyclopedia/" + name + ".html")
def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def getentry(request, name):
    if name.split('_')[0] == 'edit':
        return render(request, 'encyclopedia/editfile.html',{
        "entry": util.get_entry(name.split('_')[1]),
        "name": name.split('_')[1]
    } )         

    try:
        if name[:2] == 'rs':
            return render(request, 'encyclopedia/rsthing.html',{
                "entry": mdtex2html.convert(util.get_entry(name)),
                "name": name
            })
        else:
            return render(request, 'encyclopedia/thing.html',{
                "entry": mdtex2html.convert(util.get_entry(name)),
                "name": name
            })
    except:
        return HttpResponse('404 Page not found')
def search(request):
    query = (((str(request).split('=')[1]).split()[0])[:-2]).lower()
    se = [x.lower() for x in util.list_entries()]
    if query in se:
        return redirect('/page/'+query)

    else:
        entries = [] 
        for i in se:
            if query in i:
                entries.append(i)
        return render(request, "encyclopedia/index.html", {
            "entries": entries
        })
def edited(request):
    if request.user.is_authenticated:
        util.save_entry(str(request.GET.get('name')), str(request.GET.get('q')))
        return redirect('/page/' + str(request.GET.get('name')))
    else:
        return HttpResponse('not authenticated')        
def add(request):
    if request.user.is_authenticated:
        if str(request.GET.get('name')) in (util.list_entries()):
            return HttpResponse('An article with this name already exists')
        util.save_entry(str(request.GET.get('name')), str(request.GET.get('q')))
        return redirect('/page/' + str(request.GET.get('name')))
    else:
        return HttpResponse('not authenticated')        
def newpage(request):
    return render(request, 'encyclopedia/addpage.html')
def random(request):
    entries = list(util.list_entries())
    entry = rng.choice(entries)
    return redirect(  '/page/' + str(entry))
def whoami(request):
    print(util.list_entries)
    return redirect('/page/landing_page')


def image(request, imgid):
    img = default_storage.open(f"entries/{imgid}")
    response = FileResponse(img)
    return response
@csrf_exempt
def storeAndProcessFile(request):
    if request.method != 'POST':
        return render(request, "encyclopedia/fileupload.html")
    if request.user.is_superuser:   
        file = request.FILES.get('file')
        filename = f"entries/{file.name}"
        if default_storage.exists(filename):
            return HTTPResponse('file already exists')
        default_storage.save(filename, ContentFile(file.read()))
        return HttpResponse('File uploaded')
    else:
        return HttpResponse('not authenticated')
#todo - add save image route