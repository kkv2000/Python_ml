import cv2
vid = cv2.VideoCapture(0)
while (True):
    ret, frame = vid.read()
    cv2.imshow('live video',frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
vid.release()
cv2.destroyAllWindows()



import cv2
vid = cv2.VideoCapture(0)
while (True):
    ret, frame = vid.read()
    image = cv2.putText(frame, 'pov:day2 ICT funtime', (20, 30), cv2.FONT_HERSHEY_SIMPLEX, 2, (150,0,200), 8,
                         cv2.LINE_AA)
    cv2.imshow('live video',image)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
vid.release()
cv2.destroyAllWindows()
