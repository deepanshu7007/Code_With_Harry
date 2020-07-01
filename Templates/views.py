from django.http import HttpResponse;
from django.shortcuts import render;

def index(request):
    return render(request,'index.html');

def analyze(request):
    operations="";
    djtext=request.GET.get("text","default text");
    puncremover=request.GET.get('removepunc','off');
    capitalized=request.GET.get('capitalized','off');
    newlineremover=request.GET.get('newlineremover','off');
    extraspaceremover=request.GET.get('extraspaceremover','off');

    if(puncremover=='on'):
        values="";
        punctuations='''!()-[]{};:'"\,<>./?@#$%^&*_~''';
        for char in djtext:
            if char not in punctuations:
                values=values+char;
        operations=operations+"Punctuation Remover";
        djtext=values;
    if(capitalized=='on'):
        values="";
        for char in djtext:
            values=values+char.upper();
        operations=operations+", Capitalized";
        djtext=values;
    if(extraspaceremover=="on"):
        x=0;
        y=len(djtext);
        while(x<y):
            if djtext[x] == ' ' and djtext[x+1] == " ":
                mod=djtext[:x]+djtext[x:].lstrip();
                djtext=mod;
                y=len(djtext);
            x=x+1;
        operations=operations+", extraspaceremover";
    if(newlineremover=="on"):
        values="";
        for char in djtext:
            if char != "\n" and char!="\r":
                values=values+char;
        operations=operations+", newlineremover";
        djtext=values;

    if(newlineremover=="off" and extraspaceremover=="off" and capitalized=="off" and puncremover=="off"):
        return render(request,'Error404.html');

    params={"Operations":operations,'analyzed_text':djtext};
    return render(request,"analyze.html",params)