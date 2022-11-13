from flask import Flask, request
from linebot import LineBotApi, WebhookHandler
from linebot.models import MessageEvent, TextMessage

channel_secret = "014f3203cf18b9259f40bf91bfdfdacd"
channel_access_token = "VHI4yI2z+XfIV26Es67/slOMAOsnwCut0tpXYVp5gwXMVWbfqZMiha6MdgHQUv8Wl39Pghy3yLGcAWoOUT2Uuy5oz+ZAM3k3HmGgURq2L4BRtSjNrVU5VnNBIl+2D3gZs4eRySOQz3eo8rkXUMrRSwdB04t89/1O/w1cDnyilFU="

line_bot_api = LineBotApi(channel_access_token) # หลังบ้าน --> หน้าบ้าน
handler = WebhookHandler(channel_secret)        # หน้าบ้าน --> หลังบ้าน

app = Flask(__name__) 

@app.route("/", methods=["GET","POST"])
def home():
    try:
        signature = request.headers["X-Line-Signature"]
        body = request.get_data(as_text=True)
        handler.handle(body, signature)
    except:
        pass
    
    return "Hello Line Chatbot"

@handler.add(MessageEvent, message=TextMessage)
def handle_text_message(event):
    text = event.message.text
    print(text)

if __name__ == "__main__":  
    app.run(port=5002)


    

