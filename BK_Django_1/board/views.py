from django.shortcuts import render, redirect
from django.http import Http404
from django.core.paginator import Paginator

from bkuser.models import Bkuser
from .models import Board
from .forms import BoardForm
from tag.models import Tag

# Create your views here.

def board_detail(request, pk):
    try:
        board = Board.objects.get(pk=pk)
    except Board.DoesNotExist:
        raise Http404('No content found')


    return render(request, 'board_detail.html', {'board': board})

def board_write(request):
    if not request.session.get('user'):
        return redirect('/bkuser/login')

    if request.method == "POST":
        form = BoardForm(request.POST)
        if form.is_valid():
            user_id = request.session.get('user')
            bkuser = Bkuser.objects.get(pk=user_id)
            board = Board()

            tags = form.cleaned_data['tags'].split(',')

            board.title = form.cleaned_data['title']
            board.contents = form.cleaned_data['content']
            board.writer = bkuser
            board.save()

            for tag in tags:
                if not tag:
                    continue

                _tag, _ = Tag.objects.get_or_create(name=tag)
                board.tags.add(_tag)

            return redirect('/board/list')
    else:
        form = BoardForm()

    return render(request,'board_write.html', {'form': form})

def board_list(request):
    all_boards = Board.objects.all().order_by('-id')
    page = int(request.GET.get('p', 1))
    paginator = Paginator(all_boards, 3)

    boards = paginator.get_page(page)

    return render(request, 'board_list.html', {'boards': boards})