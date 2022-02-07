from PIL import Image
import ticket_gen
import random
from pyzbar.pyzbar import decode
from datetime import datetime
from datetime import date
#import db


def chexit(id, carp):

    file = 'pid_'+str(id)+'.png'
    data = decode(Image.open(file))
    hash = str(data[0][0])[2:-1]
    #
    plate = hash[:10]
    curr_time = ticket_gen.dater()[-4:]
    #print()
    #print("Matching... \nCar number plate: "+plate+"\nDate: " +
          hash[-10:-8]+"-"+hash[-8:-6]+"-20"+hash[-6:-4])
    print()
    #print(str(carp).upper() + " vs " + plate)
    if str(carp).upper() == plate:
        #print("Match confirmed")
        fee = (int(curr_time)-int(hash[-4:]))
        fee /= 4
        return (fee)
    else:
        print("Invalid")
        return("Invalid")
