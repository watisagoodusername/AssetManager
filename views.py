from turtle import home
from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime

def index(request):
    now = datetime.now()

    return render(
        request,
        "system/index.html", 
        {
            'title': "Page of a website",
            'message': "Wahoo! It's a me, a website! ",
            'content': "Right now its " + now.strftime("%A, %d %B, %Y at %X")
        }
    )
def about(request):
    return render(
        request,
        "system/about.html",
        {
            'title': "About page of a website",
            'top': "This is what an asset management system is",
            'paragraph': "An asset management system is used to keep track of assets owned by a company or individuals. An asset is defined as: “an item that is considered a resource owned by a company and has economic value that can be measured and expressed in dollars.” (assetpanda.com, 2024). A good asset management system is easy to use, with an easy setup to add assets, and an easy scanning/ entering system so it does not take much time and effort to track each asset. To use the system the person in charge of the asset manager will enter all of the details into the entry, and then users can either scan the asset using a barcode or qr code, or alternatively just select it from a menu. They will then select what they will do with the asset and that information will be sent back to the server (apptricity.com, 2024)."
        }
    )
def qr(request):
    return render(
        request,
        "system/QRcode.html",
        {
            'title': "website qr code generator",
            'message': "qr code to send you to home",
            'onqr': request.build_absolute_uri("/home"),
        }
    )