import requests
import subprocess
import socket
import time
import os

baglanti = input("taramak istediginiz siteyi yaziniz....")
dosyaAdi = input("yazmak istediginiz dosya adini yaziniz...")

print ("domainine goz dikeni ez ogul... Domain namustur...")
time.sleep(3) 

BlockListMail=requests.get('https://lists.blocklist.de/lists/mail.txt',verify=False)
if (BlockListMail.status_code == 200):

    print (BlockListMail.status_code)
    print ("baglanti geldi. Kodu 200....")
    print ("*"*100)
    print ("el feneriyle bizi mi korkutacaksin...")
    print ("*"*100)
    time.sleep(3)

print ("BlockListMail")
print (BlockListMail.content)
print ("============")
if baglanti in str(BlockListMail.content):
    BlockListMailBilgi=str(baglanti)+" son 48 icerisinde mail servisi üzerinde bir saldiri icin blocklistde raporlanmistir GGWP reis sictin... -:).\n"
    dosya=open(dosyaAdi,"a")
    dosya.write(BlockListMailBilgi)
    dosya.close()
else:
    BlockListMailBilgi=str(baglanti)+" son 48 icerisinde mail servisi üzerinde bir saldiri icin blocklistde raporlanmamistir. Afferim la .\n"
    dosya=open(dosyaAdi,"a")
    dosya.write(BlockListMailBilgi)
    dosya.close()

BlockListSip=requests.get('https://lists.blocklist.de/lists/sip.txt',verify=False)
print ("BlockListSip")
print (BlockListSip.content)
print ("============")
if baglanti in str(BlockListSip.content):
    BlockListSipBilgi=str(baglanti)+" SIP, VOIP serverlarına giris icin blocklistde raporlanmistir.\n"
    dosya=open(dosyaAdi,"a")
    dosya.write(BlockListSipBilgi)
    dosya.close()
else:
    BlockListSipBilgi=str(baglanti)+" SIP, VOIP serverlarına giris icin blocklistde raporlanmamistir.\n"
    dosya=open(dosyaAdi,"a")
    dosya.write(BlockListSipBilgi)
    dosya.close()

i = 0 #aga bu ne? Bu ne ise yariyor? Bu neden burada? Bilemiyorum altan

BlockListFtp=requests.get('https://lists.blocklist.de/lists/ftp.txt',verify=False)
print ("BlockListFtp")
print (BlockListFtp.content)
print ("="*75)
if baglanti in str(BlockListFtp.content):
    BlockListFtpBilgi=str(baglanti)+" son 48 icerisinde FTP servisi üzerinden bir saldiri icin blocklistde raporlanmistir.\n"
    dosya=open(dosyaAdi,"a")
    dosya.write(BlockListFtpBilgi)
    dosya.close()
else:
    BlockListFtpBilgi=str(baglanti)+" son 48 icerisinde FTP servisi üzerinden bir saldiri icin blocklistde raporlanmamistir.\n"
    dosya=open(dosyaAdi,"a")
    dosya.write(BlockListFtpBilgi)
    dosya.close()

some = requests.get('https://www.usom.gov.tr/zararli-baglantilar/1.html',verify=False)
print ("USOM List")
print (some.content)
print ("-"*50)
if baglanti in str(some.content):
    usombilgi = str(baglanti)+ "USOM listesinde adiniz gecmektedir... sictiniz babba .\n"
    dosya = open(dosyaAdi,"a")
    dosya.write(usombilgi)
    dosya.close()
else:
    usombilgi = str(baglanti)+ "USOM listesinde adiniz gecmiyor... Adamsin lan afferin .\n"
    dosya = open(dosyaAdi,"a")
    dosya.write(usombilgi)
    dosya.close()

Openphish=requests.get('https://openphish.com/feed.txt',verify=False)
print ("Openphish")
print (Openphish.content)
print ("============")
if baglanti in str(Openphish.content):
    OpenphishBilgi=str(baglanti)+"  Openphishte phishing sosyal muhendislik saldirilarinda kullanilabilir olarak belirlenmistir.\n"
    dosya=open(dosyaAdi,"a")
    dosya.write(OpenphishBilgi)
    dosya.close()
else:
    OpenphishBilgi=str(baglanti)+"  Openphishte phishing sosyal muhendislik saldirilarinda kullanilabilir olarak belirlenmemistir.\n"
    dosya=open(dosyaAdi,"a")
    dosya.write(OpenphishBilgi)
    dosya.close()

#subprocess.call('gnome-terminal',shell=True) --> yorum satiri olarak eklenmistir. Daha sonradan ek olarak islemler terminal uzerinden devam edecektir.
