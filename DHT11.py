#de Rapsbery ket noi duoc voi mang qua WIFI bac buot phai dung mang hinh, co the su dung day Lan 
# nhung de dieu khien Rapsberry qua mang noi bo bac buoc phai mo ssl
import Adafruit_DHT
import RPi.GPIO as GPIO
import time
import BlynkLib
import os
BLYNK_AUTH = 'CODE BLYNK'

# Initialize Blynk
blynk = BlynkLib.Blynk(BLYNK_AUTH)


# Adafruit_DHT ho tro nhieu loai cam bien DHT, o day dung DHT11 nen chon cam bien  DHT11
chon_cam_bien = Adafruit_DHT.DHT11

GPIO.setmode(GPIO.BCM)

# chan DATA duoc noi vao chan GPIO25 cua PI GPOI.output(pin,GPOI.HIGH)
pin_sensor = 18
buffer = 23
count = 6# Bien dem de diem so lan nhan nut reboot tren blynk de khi nhan 6 lan thi Rapspery moi khoi dong lai
GPIO.setup(buffer,GPIO.OUT)
print ("RASPI.VN Demo cam bien do am DHT 11")
@blynk.VIRTUAL_READ(0)
@blynk.VIRTUAL_READ(1)
@blynk.VIRTUAL_READ(3)
@blynk.VIRTUAL_READ(4)
def my_read_handler():
   # Doc Do am va Nhiet do tu cam bien thong qua thu vien Adafruit_DHT
   # Ham read_retry se doc gia tri Do am va Nhiet do cua cam bien
   # neu khong thanh cong se thu 15 lan, moi lan cach nhau 2 giay.
   do_am, nhiet_do = Adafruit_DHT.read_retry(chon_cam_bien, pin_sensor)
   # Kiem tra gia tri tra ve tu cam bien (do _am va nhiet_do) khac NULL
   blynk.virtual_write(4,255)
   if do_am is not None and nhiet_do is not None:
     print ('\rNhiet Do =',nhiet_do,'Do Am = ',do_am)
     blynk.virtual_write(0,int(nhiet_do))
     blynk.virtual_write(1,int(do_am))
     global count #khai bao count la bien toan cuc (cho chuong trinh hieu day la bien count o phia tren)
     count = 6#reset so lan dem
     blynk.virtual_write(4,111)
     time.sleep(1)
     blynk.virtual_write(4,255)
   else:
    # Loi :(
     print('\nLoi khong the doc tu cam bien DHT11 :(\n')
@blynk.VIRTUAL_WRITE(5)
def Reboot(reboot):
  if(reboot=="1"):
    global count
    count-=1
    print(count)
    if (count==0):
     # 
     count =6
     for i in range(0,10):
      blynk.virtual_write(4,0)
      time.sleep(0.1)
      blynk.virtual_write(4,255)
      time.sleep(0.1)
     os.system('sudo shutdown -r now')
     print('\nDang Khoi Dong Lai')
    blynk.virtual_write(4,150)
    time.sleep(0.2)
    blynk.virtual_write(4,255)
    time.sleep(0.2)
print('Start')
blynk.run()
