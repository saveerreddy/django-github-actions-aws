from django.http import HttpResponse

def home(request):
   text = """<h1>our mind blowing home page !! Awsome </h1>"""
   return HttpResponse(text)
