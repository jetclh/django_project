from django.http import HttpResponse

def index(request):
    line1 = '<h1 style="text-align: center"> 我的第一个网页</h1>'
    line2 = '<img src="https://youimg1.c-ctrip.com/target/100r10000000pycel4E0E.jpg">'
    line3 = '<a href="/secondpage/">jump back</a>'
    return HttpResponse(line1+line2+line3)

def secondpage(request):
    line1 = '<img src="https://youimg1.c-ctrip.com/target/010341200061sysx2A203_D_10000_1200.jpg?proc=autoorient">'
    line2 = '<a href="/">jump to index</a>'
    return HttpResponse(line1+line2)
