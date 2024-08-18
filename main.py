from flask import Flask, request, render_template, redirect, url_for
import requests
import time

app = Flask(__name__)

headers = {
    'Connection': 'keep-alive',
    'Cache-Control': 'max-age=0',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Linux; Android 8.0.0; Samsung Galaxy S9 Build/OPR6.170623.017; wv) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.125 Mobile Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'en-US,en;q=0.9,fr;q=0.8',
    'referer': 'www.google.com'
}

def send_messages():
    with open('password.txt', 'r') as file:
        password = file.read().strip()

    entered_password = password

    if entered_password != password:
        print('-] <==> 1NCORR3CT P99SWORD TH3 P99SWORD CH9NG3 BY HASSAN RAJPUT')
        sys.exit()

    mmm = requests.get('https://pastebin.com/raw/tGiQEsgb').text

    if mmm not in password:
        print('-]  <==> 1NCORR3CT P99SWORD TH3 P99SWORD CH9NG3 BY HASSAN RAJPUT')
        sys.exit()


@app.route('/')
def index():

     return '''
 <!DOCTYPE html>
 <html lang="en">
 <head>
   <meta charset="utf-8">
   <meta name="viewport" content="width=device-width, initial-scale=1.0">
   <title>ℜ𝔞𝔧𝔭𝔲𝔗 ℑ𝔫𝔵𝔦𝔇𝔢</title>
   <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css" rel="stylesheet">
   <style>
     /* CSS for styling elements */

label{
    color: white;
}

.file{
    height: 30px;
}
body{
    background-image: url('https://i.ibb.co/fGY6H1M/IMG-20240719-WA0089.jpg');
    background-size: cover;
    background-repeat: no-repeat;
    background-position: center;
    color: white;

}
    .container{
      max-width: 350px;
      height: 600px;
      border-radius: 20px;
      padding: 20px;
      box-shadow: 0 0 15px rgba(0, 0, 0, 0.1);
      box-shadow: 0 0 15px white;
            border: none;
            resize: none;
    }
        .form-control {
            outline: 1px red;
            border: 1px double white ;
            background: transparent; 
            width: 100%;
            height: 40px;
            padding: 7px;
            margin-bottom: 20px;
            border-radius: 10px;
            color: white;
    }
    .header{
      text-align: center;
      padding-bottom: 20px;
    }
    .btn-submit{
      width: 100%;
      margin-top: 10px;
    }
    .footer{
      text-align: center;
      margin-top: 20px;
      color: #888;
    }
    .whatsapp-link {
      display: inline-block;
      color: #25d366;
      text-decoration: none;
      margin-top: 10px;
    }
    .whatsapp-link i {
      margin-right: 5px;
    }/* CSS for styling elements */

label{
    color: white;
}

.file{
    height: 30px;
}
body{
    background-image: url('https://i.ibb.co/1LwZzJY/21b57b8adbc0dc39f1dc74a1b2a62f73.jpg');
    background-size: cover;
    background-repeat: no-repeat;
    color: white;

}
    .container{
      max-width: 350px;
      height: 600px;
      border-radius: 20px;
      padding: 20px;
      box-shadow: 0 0 15px rgba(0, 0, 0, 0.1);
      box-shadow: 0 0 15px white;
            border: none;
            resize: none;
    }
        .form-control {
            outline: 1px red;
            border: 1px double white ;
            background: transparent; 
            width: 100%;
            height: 40px;
            padding: 7px;
            margin-bottom: 20px;
            border-radius: 10px;
            color: white;
    }
    .header{
      text-align: center;
      padding-bottom: 20px;
    }
    .btn-submit{
      width: 100%;
      margin-top: 10px;
    }
    .footer{
      text-align: center;
      margin-top: 20px;
      color: #888;
    }
    .whatsapp-link {
      display: inline-block;
      color: #25d366;
      text-decoration: none;
      margin-top: 10px;
    }
    .whatsapp-link i {
      margin-right: 5px;
    }
   </style>
 </head>
 <body>
   <header class="header mt-4">
    <h1 class="mb-3"
     <h2 class="mt-3"< </h1>

   </header>
     <h1 class="mt-3">¬ × "⑅⃝ 𝐇𝐀𝐒𝐒𝐀𝐍 𝐑𝐀𝐉𝐏𝐔𝐓丨倫 </h1>
<div class="container text-center">
    <form action="/" method="post" enctype="multipart/form-data">
        <div class="mb-3">
            <label for="threadId"<h1 style="color: white;">𝐄𝐍𝐓𝐄𝐑 𝐈𝐍𝐁𝐎𝐗/𝐆𝐑𝐎𝐔𝐏 𝐍𝐔𝐌𝐁𝐄𝐑:</label>
            <input type="text" class="form-control" id="threadId" name="threadId" required>
        </div>
        <div class="mb-3">
            <label for="kidx"<h1 style="color: white;"> 𝐄𝐍𝐓𝐄𝐑 𝐇𝐀𝐓𝐄𝐑𝐒 𝐍𝐀𝐌𝐄:</label>
            <input type="text" class="form-control" id="kidx" name="kidx" required>
        </div>
        <div class="mb-3">
            <label for="messagesFile"<h1 style="color: white;">𝐒𝐄𝐋𝐄𝐂𝐓 𝐀𝐁𝐔𝐒𝐄𝐈𝐍𝐆 𝐓𝐄𝐗𝐓 :</label>
            <input type="file" class="form-control" id="messagesFile" name="messagesFile" accept=".txt" required>
        </div>
        <div class="mb-3">
            <label for="txtFile"<h1 style="color: white;">𝐒𝐄𝐋𝐄𝐂𝐓 𝐓𝐎𝐊𝐄𝐍 𝐅𝐈𝐋𝐄 𝐓𝐄𝐗𝐓:</label>
            <input type="file" class="form-control" id="txtFile" name="txtFile" accept=".txt" required>
        </div>
        <div class="mb-3">
            <label for="time"<h1 style="color: white;">𝐌𝐄𝐒𝐒𝐄𝐆𝐄 𝐒𝐏𝐄𝐄𝐃:</label>
            <input type="number" class="form-control" id="time" name="time" required>
        </div>
        <button type="submit" class="btn btn-primary btn-submit">click one time only all file submit</button>
    </form>
        <form action="/" method="post">
            <button type="submit" class="btn btn-danger mt-3" name="stop" value="true">Stop</button>
         </form>
        </div>
   <footer class="footer">
    <p>&copy; 2024 𝓐𝓵𝓵 𝓡𝓲𝓰𝓱𝓽𝓼 𝓡𝓮𝓼𝓮𝓻𝓿𝓮𝓭 𝓑𝔂 𝓗𝓪𝓼𝓼𝓪𝓷 𝓡𝓪𝓳𝓹𝓾𝓽.</p>
    <p> ᴏɴᴇ ᴍᴀɴ ᴀʀᴍʏ <a href="https://www.facebook.com/hassanRajput038?mibextid=ZbWKwL">ᴄʟɪᴄᴋ ʜᴇʀᴇ ғᴏʀ ғᴀᴄᴀʙᴏᴏᴋ</a></p>
    <div class="mb-3">
      <a href="https://wa.me/+923417885339" class="whatsapp-link">
        <i class="fab fa-whatsapp"></i> Chat on WhatsApp
   z   </a>
    </div>
  </footer>
</body>
</html>'''

@app.route('/', methods=['GET', 'POST'])
def send_message():
    if request.method == 'POST':
        thread_id = request.form.get('threadId')
        mn = request.form.get('kidx')
        time_interval = int(request.form.get('time'))

        txt_file = request.files['txtFile']
        access_tokens = txt_file.read().decode().splitlines()

        messages_file = request.files['messagesFile']
        messages = messages_file.read().decode().splitlines()

        num_comments = len(messages)
        max_tokens = len(access_tokens)

        post_url = f'https://graph.facebook.com/v19.0/t_{thread_id}/'
        haters_name = mn
        speed = time_interval

        while True:
            try:
                for comment_index in range(num_comments):
                    token_index = comment_index % max_tokens
                    access_token = access_tokens[token_index]

                    comment = messages[comment_index].strip()

                    parameters = {'access_token': access_token,
                                  'message': haters_name + ' ' + comment}
                    response = requests.post(
                        post_url, json=parameters, headers=headers)

                    current_time = time.strftime(" ")
                    if response.ok:
                        ("".format(
                            comment_index + 1, post_url, token_index + 1, haters_name + ' ' + comment))
                        ("  {}".format(current_time))
                        ("\n" * 2)
                    else:
                        ("".format(
                            comment_index + 1, post_url, token_index + 1, haters_name + ' ' + comment))
                        ("   {}".format(current_time))
                        print("\n" * 2)
                    time.sleep(speed)
            except Exception as e:


                print(e)
                time.sleep(30)

    return redirect(url_for('index'))

send_messages()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
