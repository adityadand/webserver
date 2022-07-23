from flask import Flask, request, render_template ,redirect , jsonify
import screen_brightness_control as sbc
import webbrowser
import os
import subprocess
import requests
import shutil 
import ctypes
import pyautogui

from flask_ngrok import run_with_ngrok

app = Flask(__name__)
run_with_ngrok(app)

@app.route('/')
def my_form():
    return render_template('index.html')
    return render_template('style.css')

@app.route('/', methods=['POST'])
def my_form_post():
	text = request.form['text']
	return text

@app.route('/openapp')
def my_form_openapp():
    return render_template('openapp.html')

@app.route('/openapp', methods=['POST'])
def my_form_openapp_post():
    text = request.form['text']
    os.system('start '+text+'.exe') 
    return redirect(request.referrer)

@app.route('/runcmmd')
def my_form_runcmmdapp():
    return render_template('runcmmd.html')

@app.route('/runcmmd', methods=['POST'])
def my_form_runcmmdapp_post():
    text = request.form['text']
    os.system("start cmd /k "+text) 
    return redirect(request.referrer)

@app.route('/closeapp')
def my_form_closeapp():
    return render_template('closeapp.html')

@app.route('/closeapp', methods=['POST'])
def my_form_closeapp_post():
    text = request.form['text']
    os.system('taskkill /IM  '+text+'.exe  /F') 
    return redirect(request.referrer)


@app.route('/mediacontrol')
def my_form_mediacontrol():
    return render_template('mediacontrol.html')

@app.route('/mediacontrol', methods=['POST','GET'])
def my_form_mediacontrol_post():
    soundb = request.form.get('soundb')
    brightb = request.form.get('brightb')
    soundintb = int(soundb)
    brightintb = int(brightb)
    os.system("setvol "+soundb)
    sbc.set_brightness(brightintb)
    return ('',204)

    
@app.route('/websearch')
def my_form_websearch():
    return render_template('websearch.html')

@app.route('/websearch', methods=['POST'])
def my_form_websearch_post():
    text = request.form['text']
    webbrowser.open_new_tab('https://www.'+str(text)+'.com')
    return redirect(request.referrer)

@app.route('/gsearch')
def my_form_gsearch():
    return render_template('gsearch.html')

@app.route('/gsearch', methods=['POST'])
def my_form_gsearch_post():
    text = request.form['text']
    value = request.form.getlist('check')
    webbrowser.open('https://google.com/search?q='+text) 
    if(len(value) == 0 ):
        return redirect(request.referrer)
    elif(value[0] == "on"):
        webbrowser.open('https://google.com/search?q='+text+'&tbm=isch')
    else:
        return redirect(request.referrer)
    return redirect(request.referrer)

@app.route('/yousearch')
def my_form_yousearch():
    return render_template('yousearch.html')

@app.route('/yousearch', methods=['POST'])
def my_form_yousearch_post():
    text = request.form['text']
    webbrowser.open('https://www.youtube.com/results?search_query='+text)
    return redirect(request.referrer)

@app.route('/screenshot')
def my_form_screenshot():
    return render_template('screenshot.html')

@app.route('/screenshot', methods=['POST','GET'])
def my_form_screenshot_post():
    im = pyautogui.screenshot()
    im.save('static\\screenshot.jpg')
    return redirect(request.referrer)

@app.route('/changewallpaper')
def my_form_changewallpaper():
    return render_template('changewallpaper.html')

@app.route('/changewallpaper', methods=['POST'])
def my_form_changewallpaper_post():
    image_url = request.form['text']
    filename = image_url.split("/")[-1]
    r = requests.get(image_url, stream = True)
    if r.status_code == 200:
        r.raw.decode_content = True
        with open(filename,'wb') as f:
            shutil.copyfileobj(r.raw, f)
        print('Image sucessfully Downloaded: ',filename)
    else:
        print('Image Couldn\'t be retreived')
    SPI_SETDESKWALLPAPER = 20 
    ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, os.path.abspath(filename), 0)

    return redirect(request.referrer)


if __name__ == "__main__":
	app.run()
