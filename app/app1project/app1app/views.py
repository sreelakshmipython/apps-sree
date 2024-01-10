from django.http import HttpResponse
from django.shortcuts import render, redirect

from .forms import SongForm
from. models import Song

# Create your views here.

def index(request):
    song=Song.objects.all()
    context={'song_list':song}
    return render(request,'index.html',context)
def detail(request,song_id):
    song = Song.objects.get(id=song_id)
    return render(request,"detail.html",{'song':song})
def add_song(request):
    if request.method=='POST':
        song_name=request.POST.get('song_name')
        movie_name=request.POST.get('movie_name')
        singer = request.POST.get('singer')
        year = request.POST.get('year')
        img = request.FILES['img']
        song=Song(song_name=song_name,movie_name=movie_name,singer=singer,year=year,img=img)
    song.save()
    return render(request,'add.html')
def update(request,id):
    song=Song.objects.get(id=id)
    form=SongForm(request.POST or None,request.FILES,instance=song)
    if form.is_valid():
        form.save()

    return render(request,'edit.html',{'form':form,'song':song})
def delete(request,id):
    if request.method=='POST':
        song=Song.objects.get(id=id)
        song.delete()
        return redirect('/')
    return render(request,'delete.html')

