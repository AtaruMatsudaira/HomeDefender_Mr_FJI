from serial import Serial
import requests
import random
import json

ser: Serial = None

sensiteve_data = {}

with open("sensitive_data.json", "r") as f:
    sensiteve_data = json.load(f)

uri = sensiteve_data["url"]

past_distance = None

threshold_distance = 20


def send_message():
    senders = [
        {
            "username": "シャドウミストレス優子",
            "avatar_url": "https://cdn-ak.f.st-hatena.com/images/fotolife/g/gumitan_com/20220528/20220528075840.jpg",
            "content": "人が...通りました☆ :peach: ",
        },
        {
            "username": "藤井神(10)",
            "avatar_url": "https://media.discordapp.net/attachments/928622055602159667/995736978429595649/unknown.png",
            "content": "人が来たぞおい"
        },
        {
            "username": "藤井神(17)",
            "avatar_url": "https://media.discordapp.net/attachments/928622055602159667/995737408589008896/unknown.png",
            "content": "人が来てたはず多分"
        },
        {
            "username": "藤井神(20)",
            "avater_url": "https://media.discordapp.net/attachments/928622055602159667/995737704765591583/unknown.png",
            "content": "人が来てた気がする"
        }

    ]
    main_content = random.choice(senders)
    requests.post(uri, main_content)


def check_big_change(now_distance):
    global past_distance
    if past_distance == None:
        past_distance = now_distance
        return False

    flag = abs(past_distance - now_distance) > threshold_distance
    past_distance = now_distance
    return flag


def get_senser():
    data = ser.read_all()
    if(len(data.decode()) == 0) or not data.decode().isdigit():
        return

    if(check_big_change(int(data))):
        send_message()


if __name__ == "__main__":
    with Serial('COM10', 115200, timeout=0.1) as s:
        ser = s
        while True:
            get_senser()
