import cv2

cao = cv2.VideoCapture(0)

while cao.isOpened():

    r,f = cao.read()

    if r == True:
        f = cv2.flip(f, 1)
        f = cv2.resize(f, (500, 500))

        gray = cv2.cvtColor(f, cv2.COLOR_BGR2GRAY)
        fil = cv2.CascadeClassifier(r"C:\Users\soban\AppData\Local\Programs\Python\Python313\Lib\site-packages\cv2\data\haarcascade_frontalface_default.xml")
        d = fil.detectMultiScale(gray, 1.2, 4)

        for (x, y, w, h) in d:
            cv2.rectangle(f, (x, y), (x + w, y + h), (0, 255, 0), 2, 3)
            
        cv2.imshow('img', f)

        if cv2.waitKey(25) & 0xFF == ord('p'):
            break

    else:
        break

cao.release()
cv2.destroyAllWindows()
