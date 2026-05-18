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
        context = {
            'name': name,
            'occasion': occasion,
            'title': custom_title,
            'message': custom_message,
            'theme_color': custom_color if custom_color else '#ff4d6d',
            'emojis': custom_emojis if custom_emojis else '✨🎉✨',
        }
        return render(request, 'home.html', context)
    
    # Check database first
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
    
    # Birthday message
    if occasion == 'birthday':
        context = {
            'name': name,
            'occasion': occasion,
            'title': '🎉 Happy Birthday',
            'message': "You are truly one of the most special people in my life. Your friendship is a treasure that I'll always be grateful for. No matter how much time passes, the memories we created together still bring a smile to my face. I really miss those beautiful days, the laughter, the fun, and all the moments we shared.\n\nMay your life always be filled with happiness, success, love, and endless smiles. Stay the amazing, kind-hearted, and beautiful person you are. Wishing you a birthday as wonderful as you are 💖✨ 🌟",
            'theme_color': '#ff4d6d',
            'emojis': '🎂🎈🎉🎁',
        }
    # Anniversary message
    elif occasion == 'anniversary':
        context = {
            'name': name,
            'occasion': occasion,
            'title': '💕 Happy Anniversary',
            'message': 'Congratulations on your anniversary! May your love continue to grow stronger with each passing year. Wishing you both a day filled with beautiful memories and many more years of happiness together! 💑',
            'theme_color': '#ffb703',
            'emojis': '💕🥂💍💐',
        }
    # Valentine message
    elif occasion == 'valentine':
        context = {
            'name': name,
            'occasion': occasion,
            'title': '🌹 Happy Valentines Day',
            'message': 'Happy Valentines Day! You deserve all the love, joy, and happiness in the world. May your day be filled with romance, sweet moments, and lots of chocolate! 💖',
            'theme_color': '#ff69b4',
            'emojis': '💖🌹💘💕',
        }
    # Default fallback
    else:
        context = {
            'name': name,
            'occasion': occasion,
            'title': '✨ Special Occasion',
            'message': f'Wishing you a wonderful {occasion} celebration! 🎉',
            'theme_color': '#ff4d6d',
            'emojis': '✨🎉✨',
        }
    
    return render(request, 'home.html', context)
