# import db
import cv2
import PIL
import time
import multiprocessing
from matplotlib.pyplot import bar
from pyzbar import pyzbar


def read_barcodes(frame, plate):
    barcodes = pyzbar.decode(frame)
    for barcode in barcodes:
        x, y, w, h = barcode.rect
        # 1
        barcode_info = barcode.data.decode('utf-8')
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

        # 2
        font = cv2.FONT_HERSHEY_DUPLEX
        cv2.putText(frame, barcode_info, (x + 3, y - 6),
                    font, 1.5, (255, 255, 255), 1)
        # 3
        with open("barcode_result.txt", mode='w+') as file:
            f = str(file.readlines())
            #print("f "+str(f[3:]))
            #print("plate "+str(plate))
            #print("barcode_info "+str(barcode_info)[:-10])
            if str(barcode_info)[:-10] == str(plate):
                print("MATCH!\n"+barcode_info)
                file.write("ID:" + str(barcode_info))
                file.close()
                exit()
            file.close()
            # cv2.VideoCapture(0).release()
            # cv2.destroyAllWindows
            # quit()
            # return
    return frame


def camera(plate):
    # 1
    camera = cv2.VideoCapture(0)
    ret, frame = camera.read()
    # 2
    while ret:
        ret, frame = camera.read()
        frame = read_barcodes(frame, str(plate))
        cv2.imshow('Ticket Scanner', frame)
        if cv2.waitKey(1) & 0xFF == 27:
            break
    # 3
    camera.release()
    cv2.destroyAllWindows()

# this function is to kill the camera window and prevent it from staying active forever. 
# you can change the kill time from time.sleep( x seconds) 
def capture(plate):
    p = multiprocessing.Process(target=camera, name="cam", args=(plate,))
    p.start()
    time.sleep(8)
    p.terminate()
    p.join()

# 4
# if __name__ == '__main__':
#    capture("RJ01AB1234")
