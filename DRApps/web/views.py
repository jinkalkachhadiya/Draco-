from django.shortcuts import render

def home_view(request):
    manga_list = [
        {
            'title': 'Solo Leveling',
            'image': 'https://i.etsystatic.com/37268737/r/il/68e56f/5739564279/il_fullxfull.5739564279_42bi.jpg',
            'genre': 'Action, Drama, Fantasy',
            'chapters': 139,
            'read_link': '#'
        },
        {
            'title': 'The end after beginning',
            'image': 'https://i.pinimg.com/550x/33/c4/1e/33c41eced43d1a587e9104fe0115d577.jpg',
            'genre': 'Action, Adventure, Fantasy',
            'chapters': 325,
            'read_link': '#'
        }
    ]
    return render(request, 'web_base.html', {'manga_list': manga_list})
