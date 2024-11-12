import requests
import os

captcha_enabled = False

def toggle_captcha(status):
    global captcha_enabled
    captcha_enabled = status

def solve_captcha(image_url):
    api_key = os.getenv("2CAPTCHA_API_KEY")
    # 2Captcha ile çözüm
    response = requests.post("https://2captcha.com/in.php", data={
        "key": api_key,
        "method": "base64",
        "body": image_url,
    })
    return response.text  # CAPTCHA çözümünü döndür
