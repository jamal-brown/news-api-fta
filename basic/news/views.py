from django.shortcuts import render

def home(request):
    import requests
    import json
    
    # Grabs the Price Data Information
    price_request = requests.get("https://min-api.cryptocompare.com/data/pricemultifull?fsyms=BTC,ETH&tsyms=USD")
    price = json.loads(price_request.content)

    # Grabs the News Information
    api_request = requests.get("https://min-api.cryptocompare.com/data/v2/news/?lang=EN")
    api = json.loads(api_request.content)
    return render(request, 'home.html', {'api': api, 'price': price})

def prices(request):
    import requests
    import json
   
    if request.method == 'POST':
        quote = request.POST['quote']
        quote_request = requests.get("https://min-api.cryptocompare.com/data/pricemultifull?fsyms="+quote+"&tsyms=USD")
        quote = json.loads(quote_request.content)
        return render(request, 'prices.html', {'quote':quote})
    else:
        unknown = "Please use the form above"
        return render(request, 'prices.html', {'unknown': unknown})
