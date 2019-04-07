from django.shortcuts import render
from django.http import HttpResponse


import json
import os


import numpy as np
from PIL import Image

# Create your views here.
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
imgPath = os.path.join(BASE_DIR, 'regis/static/images/layers/000.png')



def index(request):
    # data = open(url, 'rb').read()
    # print(BASE_DIR)
    # Convert PIL Image to NumPy array
    # img = open(url)
    # arr = array(img)    
    # jsarr = json.dumps(arr.tolist())
    # jsarr = pd.Series(arr).to_json(orient='split')

    return render(request, 'map.html')

def sendPic(request):
    ''' A View that Returns a PNG Image generated using PIL'''
    x = 900
    y = 900

    
    imarray = np.random.rand(x,y,3) * 255
    im = Image.fromarray(imarray.astype('uint8')).convert('RGBA')
    

    # im = Image.open(imgPath)        # create the image
    # alpha = Image.new('L', im.size, 80)
    # im.putalpha(alpha)
    
    # We need an HttpResponse object with the correct mimetype
    response = HttpResponse(content_type='application/octet-stream')
    # now, we tell the image to save as a PNG to the 
    # provided file-like object
    im.save(response, 'png')

    return response # and we're done!



