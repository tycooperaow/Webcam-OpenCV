import numpy as np
import  cv2
#Alpha (Template)

cap = cv2.VideoCapture(0) #video capture is capable of taking photos


while(True):
       #Capture the video  frame-by-frame
       ret, frame = cap.read()

       gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
       
       #Display the resulting frame
       cv2.imshow('default frame', frame)
       cv2.imshow('gray', gray)
       
       if cv2.waitKey(20) & 0xFF == ord('q'):
              break

#When everythng done, relase the capture

cap.release()
cv2.destroyAllWindows()
