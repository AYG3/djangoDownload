from django.shortcuts import render, HttpResponse
from django.urls import reverse
import pdfkit


config = pdfkit.configuration(wkhtmltopdf=r"C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe")


def home(request):
    return render(request, 'core/home.html')

def generatePDF(request):
    pdf = pdfkit.from_url(request.build_absolute_uri(reverse('core:home')), False, configuration=config)
    response = HttpResponse(pdf, content_type='application/pdf') # content_toe?
    response['Content-Dispositon'] = 'attachment; filename="file_name.pdf"'

    return response