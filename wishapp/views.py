from django.shortcuts import render
from .models import OccasionMessage

def home(request):
    # Get parameters from URL
    occasion = request.GET.get('occasion', 'birthday')
    name = request.GET.get('to', 'Sec-C')
    
    # Get custom parameters
    custom_title = request.GET.get('title', '')
    custom_message = request.GET.get('message', '')
    custom_color = request.GET.get('color', '')
    custom_emojis = request.GET.get('emojis', '')
    
    # Check if custom parameters exist
    if custom_title and custom_message:
        # Use custom values
        context = {
            'name': name,
            'occasion': occasion,
            'title': custom_title,
            'message': custom_message,
            'theme_color': custom_color if custom_color else '#ff4d6d',
            'emojis': custom_emojis if custom_emojis else '✨🎉✨',
        }
        return render(request, 'home.html', context)
    
    # Try database
    msg = OccasionMessage.objects.filter(occasion=occasion).first()
    if msg:
        context = {
            'name': name,
            'occasion': occasion,
            'title': msg.title,
            'message': msg.message,
            'theme_color': msg.theme_color,
            'emojis': msg.emojis,
        }
        return render(request, 'home.html', context)
    
    # Default birthday message
    if occasion == 'birthday':
        context = {
            'name': name,
            'occasion': occasion,
            'title': '🎉 Happy Birthday',
            'message': "You are truly one of the most special people in my life. Your friendship is a treasure that I'll always be grateful for. No matter how much time passes, the memories we created together still bring a smile to my face. I really miss those beautiful days, the laughter, the fun, and all the moments we shared.\n\nMay your life always be filled with happiness, success, love, and endless smiles. Stay the amazing, kind-hearted, and beautiful person you are. Wishing you a birthday as wonderful as you are 💖✨ 🌟",
            'theme_color': '#ff4d6d',
            'emojis': '🎂🎈🎉🎁',
        }
        return render(request, 'home.html', context)
    
    # Default anniversary message
    if occasion == 'anniversary':
        context = {
            'name': name,
            'occasion': occasion,
            'title': '💕 Happy Anniversary',
            'message': 'Celebrating your beautiful journey together! 💑',
            'theme_color': '#ffb703',
            'emojis': '💕🥂💍💐',
        }
        return render(request, 'home.html', context)
    
    # Default valentine message
    if occasion == 'valentine':
        context = {
            'name': name,
            'occasion': occasion,
            'title': '🌹 Happy Valentines Day',
            'message': 'You deserve all the love in the world! 💖',
            'theme_color': '#ff69b4',
            'emojis': '💖🌹💘💕',
        }
        return render(request, 'home.html', context)
    
    # Fallback (should never reach here)
    context = {
        'name': name,
        'occasion': occasion,
        'title': '✨ Special Wish',
        'message': 'Wishing you a wonderful day!',
        'theme_color': '#ff4d6d',
        'emojis': '✨🎉✨',
    }
    return render(request, 'home.html', context)
