from django.shortcuts import render, redirect
from django.contrib import messages
from .models import OccasionMessage, FriendWish

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
            'custom_image': None,
        }
        return render(request, 'home.html', context)
    
    # Try database first
    msg = OccasionMessage.objects.filter(occasion=occasion).first()
    if msg:
        context = {
            'name': name,
            'occasion': occasion,
            'title': msg.title,
            'message': msg.message,
            'theme_color': msg.theme_color,
            'emojis': msg.emojis,
            'custom_image': msg.custom_image.url if msg.custom_image else None,
        }
        return render(request, 'home.html', context)
    
    # Default messages based on occasion
    if occasion == 'birthday':
        context = {
            'name': name,
            'occasion': occasion,
            'title': '🎉 Happy Birthday',
            'message': "You are truly one of the most special people in my life. Your friendship is a treasure that I'll always be grateful for. No matter how much time passes, the memories we created together still bring a smile to my face. I really miss those beautiful days, the laughter, the fun, and all the moments we shared.\n\nMay your life always be filled with happiness, success, love, and endless smiles. Stay the amazing, kind-hearted, and beautiful person you are. Wishing you a birthday as wonderful as you are 💖✨ 🌟",
            'theme_color': '#ff4d6d',
            'emojis': '🎂🎈🎉🎁',
            'custom_image': None,
        }
    elif occasion == 'anniversary':
        context = {
            'name': name,
            'occasion': occasion,
            'title': '💕 Happy Anniversary',
            'message': 'Congratulations on your anniversary! May your love continue to grow stronger with each passing year. Wishing you both a day filled with beautiful memories and many more years of happiness together! 💑',
            'theme_color': '#ffb703',
            'emojis': '💕🥂💍💐',
            'custom_image': None,
        }
    elif occasion == 'valentine':
        context = {
            'name': name,
            'occasion': occasion,
            'title': '🌹 Happy Valentines Day',
            'message': 'Happy Valentines Day! You deserve all the love, joy, and happiness in the world. May your day be filled with romance, sweet moments, and lots of chocolate! 💖',
            'theme_color': '#ff69b4',
            'emojis': '💖🌹💘💕',
            'custom_image': None,
        }
    else:
        context = {
            'name': name,
            'occasion': occasion,
            'title': '✨ Special Occasion',
            'message': f'Wishing you a wonderful {occasion} celebration! 🎉',
            'theme_color': '#ff4d6d',
            'emojis': '✨🎉✨',
            'custom_image': None,
        }
    
    return render(request, 'home.html', context)

def upload_image(request):
    if request.method == 'POST' and request.FILES.get('custom_image'):
        occasion = request.POST.get('occasion', 'birthday')
        image = request.FILES['custom_image']
        
        # Get or create the occasion
        msg, created = OccasionMessage.objects.get_or_create(occasion=occasion)
        msg.custom_image = image
        msg.save()
        
        messages.success(request, 'Image uploaded successfully!')
        return redirect(f'/?occasion={occasion}')
    
    return redirect('/')