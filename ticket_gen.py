import random
import cv2
import barcode
#import db
from barcode.writer import ImageWriter
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
from datetime import datetime
from datetime import date
# 480 by 200 px
# W-VOL-POL-0935-280901
# white volks polo 9:35 28/09/01


def dater():
    date_str = ""
    now = datetime.now()
    time = now.strftime("%H%M")

    today = date.today()
    date_str += str(today.strftime("%d%m%y"))
    date_str += str(time)

    # print(date_str)
    return date_str


def testEan(car_hash):
    car_hash += (str(dater()))
    print(car_hash)
    EAN = barcode.get_barcode_class('code128')
    ean = EAN(car_hash, writer=ImageWriter())

    fullname = ean.save('barcode_id', options={
                        'write_text': True})


def ticket_gen(car_hash="Invalid"):
    #car_hash = "WVOLPOL2809010935"

    testEan(str(car_hash).upper())
    image = cv2.imread('barcode_id.png')
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    thresh = cv2.threshold(
        gray, 0, 255, cv2.THRESH_OTSU + cv2.THRESH_BINARY_INV)[1]
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))
    dilate = cv2.dilate(thresh, kernel, iterations=3)

    cnts = cv2.findContours(dilate, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    cnts = cnts[0] if len(cnts) == 2 else cnts[1]
    cnts = sorted(cnts, key=cv2.contourArea)
    # take id no. from database
    id_no = random.randint(10, 10000)
    #
    for c in cnts:
        x, y, w, h = cv2.boundingRect(c)
        image[y:y+h, x:x+w] = [255, 255, 255]
        cv2.putText(image, 'Parking Ticket Id no: '+str(id_no),
                    (x, y), cv2.FONT_HERSHEY_SIMPLEX, .6, (0, 0, 0), 1)
        break

    #cv2.imshow('thresh', thresh)
    #cv2.imshow('dilate', dilate)
    
    #cv2.imshow('image', image)
    # cv2.waitKey(0)
    #turn cv2.imshow and cv2.waitkey to LOAD image on generation (and press key to proceed)
    filename = 'pid_'+str(id_no)+'.png'
    print(id_no)
    if not cv2.imwrite(filename, image):
        raise Exception("Could not save image")

    return (id_no)


#car_hash = "WVOLPOL2809010935"

#car_hash = "RJ14CK2030"

# ticket_gen(car_hash)
