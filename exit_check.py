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
    print()
    print("Matching... \nCar number plate: "+plate+"\nDate: " +
          hash[-10:-8]+"-"+hash[-8:-6]+"-20"+hash[-6:-4])
    print()
    #print(str(carp).upper() + " vs " + plate)
    if str(carp).upper() == plate:
        print("Match confirmed")
        fee = (int(curr_time)-int(hash[-4:]))
        fee /= 4
        return (fee)
    else:
        print("Invalid")
        return("Invalid")

    """
    key = input("Press 'Y' to Create Fee\nPress 'N' to Cancel\n\n:")
    if key == 'n' or key == 'N':
        print("Incorrect Match")
        #print('date: '+hash[-10:-8]+"-"+hash[-8:-6]+"-20"+hash[-6:-4])
        #print('time: '+hash[-4:-2]+":"+hash[-2:])
    elif key == 'y' or key == 'Y':
        print("Match confirmed by user\nGenerating Parking fee")
        #print("INR: "+str(int(curr_time)-int(hash[-4:]))+"/-")
    """

    #print('plate: '+hash[:10])
