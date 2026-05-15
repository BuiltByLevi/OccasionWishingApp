from django.shortcuts import render, redirect
from .models import OccasionMessage, FriendWish

def home(request):
    # Get parameters from URL
    occasion = request.GET.get('occasion', 'birthday')
    name = request.GET.get('to', 'Friend')
    
    # Check for custom message in URL
    custom_title = request.GET.get('title', None)
    custom_message = request.GET.get('message', None)
    custom_color = request.GET.get('color', None)
    custom_emojis = request.GET.get('emojis', None)
    
    # If custom parameters exist, use them
    if custom_title and custom_message:
        context = {
            'name': name,
            'occasion': occasion,
            'title': custom_title,
            'message': custom_message,
            'theme_color': custom_color if custom_color else '#ff4d6d',
            'emojis': custom_emojis if custom_emojis else '✨🎉✨',
        }
    else:
        # Try to get from database
        msg = OccasionMessage.objects.filter(occasion=occasion).first()
        if msg:
            context = {
                'name': name,
                'occasion': occasion,
                'title': msg.title,
                'message': msg.message,
                'theme_color': msg.theme_color or '#ff4d6d',
                'emojis': msg.emojis,
            }
        else:
            # Default messages if no database entry is available
            defaults = {
                'birthday': {
                    'title': '🎉 Happy Birthday',
                    'message': (
                        "You are truly one of the most special people in my life. Your friendship is a treasure that I'll always be grateful for. "
                        "No matter how much time passes, the memories we created together still bring a smile to my face. I really miss those beautiful days, "
                        "the laughter, the fun, and all the moments we shared.\n\n"
                        "May your life always be filled with happiness, success, love, and endless smiles. Stay the amazing, kind-hearted, "
                        "and beautiful person you are. Wishing you a birthday as wonderful as you are 💖✨ 🌟"
                    ),
                    'color': '#ff4d6d',
                    'emojis': '🎂🎈🎉🎁'
                },
                'anniversary': {
                    'title': '💕 Happy Anniversary',
                    'message': 'Celebrating your beautiful journey together! 💑',
                    'color': '#ffb703',
                    'emojis': '💕🥂💍💐'
                },
                'valentine': {
                    'title': '🌹 Happy Valentines Day',
                    'message': 'You deserve all the love in the world! 💖',
                    'color': '#ff69b4',
                    'emojis': '💖🌹💘💕'
                }
            }
            default = defaults.get(occasion, defaults['birthday'])
            context = {
                'name': name,
                'occasion': occasion,
                'title': default['title'],
                'message': default['message'],
                'theme_color': default['color'],
                'emojis': default['emojis'],
            }
    
    return render(request, 'home.html', context)

def friends_wall(request):
    """Display all friends' wishes in a gallery wall"""
    all_friends = FriendWish.objects.all().order_by('-added_date')
    return render(request, 'wall.html', {'friends': all_friends})

def add_friend(request):
    """Add a new friend wish to the wall"""
    if request.method == 'POST':
        name = request.POST.get('name')
        message = request.POST.get('message')
        if name and message:
            FriendWish.objects.create(name=name, message=message)
    return redirect('friends_wall')