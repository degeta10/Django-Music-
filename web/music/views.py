from django.http import HttpResponse

def index(request):
    return(HttpResponse("<h1> This is Music</h1>"))

def rock(request):
    return(HttpResponse("<h1> This is Rock Music</h1>"))
def detail(request, album_id):
	return(HttpResponse("<h2>Details of album id:"+str(album_id)+"</h2>"))



