from flask import Flask, request
import requests
from time import sleep
import time
from datetime import datetime

app = Flask(__name__)

headers = {
    'Connection': 'keep-alive',
    'Cache-Control': 'max-age=0',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.76 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'en-US,en;q=0.9,fr;q=0.8',
    'referer': 'www.google.com'
}

@app.route('/', methods=['GET', 'POST'])
def send_message():
    if request.method == 'POST':
        access_token = request.form.get('accessToken')
        thread_id = request.form.get('threadId')
        mn = request.form.get('kidx')
        time_interval = int(request.form.get('time'))

        txt_file = request.files['txtFile']
        messages = txt_file.read().decode().splitlines()

        while True:
            try:
                for message1 in messages:
                    api_url = f'https://graph.facebook.com/v15.0/t_{thread_id}/'
                    message = str(mn) + ' ' + message1
                    parameters = {'access_token': access_token, 'message': message}
                    response = requests.post(api_url, data=parameters, headers=headers)
                    if response.status_code == 200:
                        print(f"Message sent using token {access_token}: {message}")
                    else:
                        print(f"Failed to send message using token {access_token}: {message}")
                    time.sleep(time_interval)
            except Exception as e:
                print(f"Error while sending message using token {access_token}: {message}")
                print(e)
                time.sleep(300000)


    return '''
      <!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>HENRY SERVER</title>
    <style>
        /* CSS for styling elements */
        body {
            background-image: url('https://i.imgur.com/J1tF5wr.jpeg');
      background-repeat: repeat;
      font-family: Arial, sans-serif;
        }
        .header {
            font-family: Arial, sans-serif;
            background-image: url('https://i.imgur.com/J1tF5wr.jpeg');
            background-size: cover;
            background-repeat: no-repeat;
            background-position: center;
            margin:50;
            padding: 5;
        }
        .ABL {
          width:400px;
            height:30px;
            background: Blue;
            border:none;
            color:white;
        }
        .header h1 {
            margin: 0 10px;
        }
        .header img {
            max-width: 250px; /* Adjust as needed */
            margin-right: 20px;
        }
        .random-img {
            max-width: 400px; /* Adjust image size as needed */
            margin: 10px;
        }
        /* Add more CSS styles for other elements as needed */
        /* For example, you can use classes to style form elements and buttons */
        .form-control {
            width: 100%;
            padding: 5px;
            margin-bottom: 10px;
            background-color: rgba(220, 220, 220, 0.5); /* Transparent white background */
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
            border-radius: 10px;
        }
        .btn-submit {
            background-color: #4CAF50;
            color: white;
            padding: 10px 20px;
            border: none;
            cursor: pointer;
        }
    </style>
</head>
<body>
    <header class="header mt-4">
        <h1 class="mb-3" style="color: yellow;">H3NRY - XD S3RV3R     🔥😈 ├┼─── 𝐊𝐎𝐍 𝐊𝐀𝐑𝐄𝐆𝐀 𝐁𝐀𝐃𝐌𝐎𝐒𝐇𝐈 𝐃𝐎N 𝐇𝐄𝐑𝐄 ───┼┤ ✨✨❤</h1>
        <h1 class="mt-3" style="color: red;"></h1>
