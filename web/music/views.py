<<<<<<< HEAD

from . models import Album
from django.shortcuts import  render, get_object_or_404





def detail(request,album_id):
    album=get_object_or_404(Album,pk=album_id)

    return render(request,'music/detail.html', {'album':album})
=======
from django.http import HttpResponse
from .models import Album
>>>>>>> c9fea7a820ca18277341452d86b76bb5e343d13a


def index(request):
    all_albums = Album.objects.all()
<<<<<<< HEAD

    context={
        'all_albums': all_albums,
    }
    return render(request, 'music/index.html', context)

=======
    html = ''
    for album in all_albums:
        url='/music/'+ str(album_id)+'/'
        html += '<a href="'+ url +'">' + album.album_title +'</a><br>'
    return HttpResponse(html)

def detail(request,album_id):
    return HttpResponse("<h2> The Details:" + str(album_id)+ "</h2>")
>>>>>>> c9fea7a820ca18277341452d86b76bb5e343d13a



