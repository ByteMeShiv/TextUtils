from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(request):
    return render(request, "index.html")


def analyze(request):
    # Get the text
    djtext = request.POST.get("text", "default")
    # Create the dictionary that will have all the data
    upper = request.POST.get("upper", "off")

    xsRemover = request.POST.get("xsRemover", "off")

    nlMover = request.POST.get("nlMover", "off")

    removepunc = request.POST.get("removepunc", "off")

    if removepunc == "on":
        punctuations = """!()-[]{};:'"\,<>./?@#$%^&*_~"""
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        params = {"purpose": "Removed Punctuations", "analyzed_text": analyzed}
        return render(request, "analyze.html", params)

    if xsRemover == "on":
        analyzed = ""
        for i, char in enumerate(djtext):
            if not (djtext[i] == " " and djtext[i + 1] == " "):
                analyzed = analyzed + char
        params = {"purpose": "Removed Xtra Space", "analyzed_text": analyzed}
        return render(request, "analyze.html", params)

    if upper == "on":
        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char.upper()
        params = {"purpose": "UpperCase", "analyzed_text": analyzed}
        return render(request, "analyze.html", params)

    if nlMover == "on":
        analyzed = ""
        for char in djtext:
            if char != "\n" or char != "\r":
                analyzed = analyzed + char
        print(analyzed)
        params = {"purpose": "Removed Newlines", "analyzed_text": "analyzed"}
        return render(request, "analyze.html", params)
    else:
        return render(request, "analyze.html")
