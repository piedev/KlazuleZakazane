from django.http import HttpResponse
from django.template import loader
from .helper import handle_uploaded_text_file, handle_uploaded_pdf_file
from backend import *


def index(request):
    if request.method == 'POST':
        return handlePost(request)
    else:
        template = loader.get_template('Website/index.html')
        return HttpResponse(template.render({'text': ''}, request))


def handlePost(request):
    if request.FILES == {}:
        agreementContent = request.POST.get('pastedAgreement')
    else:
        f = request.FILES['fileToUpload']
        if f.name[-3:] == "pdf":
            agreementContent = handle_uploaded_pdf_file(f)
        else:
            agreementContent = handle_uploaded_text_file(f)
    results = getResults(agreementContent)
    if agreementContent == '':
        template = loader.get_template('Website/index.html')
    else:
        template = loader.get_template('Website/results.html')
    return HttpResponse(template.render({'agreementContent': agreementContent, 'results': results}, request))


def info(request):
    template = loader.get_template('Website/info.html')
    return HttpResponse(template.render({}, request))


def contact(request):
    template = loader.get_template('Website/contact.html')
    return HttpResponse(template.render({}, request))


def getResults(str):
    return odpalSzukanie(str, 1)

def list(request):
    template = loader.get_template('Website/lista.html')
    return HttpResponse(template.render({}, request))

