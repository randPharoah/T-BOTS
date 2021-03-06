#!/usr/bin/env python

import cv2


#       key value
# cam.set(3 , 640  ) # width        
# cam.set(4 , 480  ) # height       
# cam.set(10, 120  ) # brightness     min: 0   , max: 255 , increment:1  
# cam.set(11, 50   ) # contrast       min: 0   , max: 255 , increment:1     
# cam.set(12, 70   ) # saturation     min: 0   , max: 255 , increment:1
# cam.set(13, 13   ) # hue         
# cam.set(14, 50   ) # gain           min: 0   , max: 127 , increment:1
# cam.set(15, -3   ) # exposure       min: -7  , max: -1  , increment:1
# cam.set(17, 5000 ) # white_balance  min: 4000, max: 7000, increment:1
# cam.set(28, 0    ) # focus          min: 0   , max: 255 , increment:5




def callback(value):
    pass

def setup_trackbars(range_filter):
    cv2.namedWindow("Thresholds",cv2.WINDOW_NORMAL)
    cv2.resizeWindow("Thresholds", 720, 720)
    for i in ["MIN", "MAX"]:
        v = 0 if i == "MIN" else 255
        for j in range_filter:
            cv2.createTrackbar("%s_%s" % (j, i), "Thresholds", v, 255, callback)

def get_trackbar_values(range_filter):
    values = []
    for i in ["MIN", "MAX"]:
        for j in range_filter:
            v = cv2.getTrackbarPos("%s_%s" % (j, i), "Thresholds")
            values.append(v)
    return values

def main():
    range_filter = 'HSV'
    camera = cv2.VideoCapture(0,cv2.CAP_V4L2)
    camera.set(cv2.CAP_PROP_AUTOFOCUS, 0)
    camera.set(cv2.CAP_PROP_FRAME_WIDTH, 720)
    camera.set(cv2.CAP_PROP_FRAME_HEIGHT, 405)
    camera.set(cv2.CAP_PROP_BRIGHTNESS, 100)
    camera.set(14, 10) # gain
    setup_trackbars(range_filter)

    while True:
        success, image = camera.read()
        frame_to_thresh = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
        v1_min, v2_min, v3_min, v1_max, v2_max, v3_max = get_trackbar_values(range_filter)
        thresh = cv2.inRange(frame_to_thresh, (v1_min, v2_min, v3_min), (v1_max, v2_max, v3_max))
        preview = cv2.bitwise_and(image, image, mask=thresh)
        cv2.imshow("Thresholds", preview)

        if cv2.waitKey(1) & 0xFF is ord('q'):
            camera.release()
            cv2.destroyAllWindows()
            break

if __name__ == '__main__':
    main()
