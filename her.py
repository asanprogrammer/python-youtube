# Python With Youte Video Download
# Developer Asanprogrammer
from pytube import YouTube
import os
import time

while True:
    link = input('Youtube Linki Giriniz: ')
    yt = YouTube(link)
    
    print('''
        Tip Seçiniz
    ''')

    x = 1
    for i in yt.streams:
        print(x,i)
        x += 1
    type = int(input('Tip Seçiniz: '))
    type = type - 1;

    select = yt.streams[type]

    check = input('İndirmek İstediğinize emin misiniz ? [yes,no] : ')

    if(check == 'yes'):
        print('İndiriliyor , Folder : ',os.getcwd())
        select.download()
        time.sleep(2)
        print('İndirildi')

        break
    else :
        print('İptal Edildi')
        time.sleep(1)
        break