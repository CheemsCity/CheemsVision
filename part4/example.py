import cv2
import numpy as np
import math
import yaml
from pkg_resources import resource_string
import matplotlib.pyplot as plt

class ArucoDetector:

    def __init__(self, cam_matrix, dist_coeff):
        file = open("../part3/aruco_settings.yaml", "r")
        self.settings = yaml.full_load(file)
        self.arucoDictionary = {
            "DICT_4X4_50": cv2.aruco.DICT_4X4_50,
            "DICT_4X4_100": cv2.aruco.DICT_4X4_100,
            "DICT_4X4_250": cv2.aruco.DICT_4X4_250,
            "DICT_4X4_1000": cv2.aruco.DICT_4X4_1000,
            "DICT_5X5_50": cv2.aruco.DICT_5X5_50,
            "DICT_5X5_100": cv2.aruco.DICT_5X5_100,
            "DICT_5X5_250": cv2.aruco.DICT_5X5_250,
            "DICT_5X5_1000": cv2.aruco.DICT_5X5_1000,
            "DICT_6X6_50": cv2.aruco.DICT_6X6_50,
            "DICT_6X6_100": cv2.aruco.DICT_6X6_100,
            "DICT_6X6_250": cv2.aruco.DICT_6X6_250,
            "DICT_6X6_1000": cv2.aruco.DICT_6X6_1000,
            "DICT_7X7_50": cv2.aruco.DICT_7X7_50,
            "DICT_7X7_100": cv2.aruco.DICT_7X7_100,
            "DICT_7X7_250": cv2.aruco.DICT_7X7_250,
            "DICT_7X7_1000": cv2.aruco.DICT_7X7_1000,
            "DICT_ARUCO_ORIGINAL": cv2.aruco.DICT_ARUCO_ORIGINAL,
            "DICT_APRILTAG_16h5": cv2.aruco.DICT_APRILTAG_16h5,
            "DICT_APRILTAG_25h9": cv2.aruco.DICT_APRILTAG_25h9,
            "DICT_APRILTAG_36h10": cv2.aruco.DICT_APRILTAG_36h10,
            "DICT_APRILTAG_36h11": cv2.aruco.DICT_APRILTAG_36h11
        }.get(self.settings['aruco_dictionary'], 'ERROR')
        if(self.arucoDictionary == 'ERROR'):
            print('Dizionario definito nell aruco_settings non esistente (DEFAULT: DICT_6X6_50)\n')
            self.arucoDictionary = cv2.aruco.DICT_6X6_50
        self.streetSign = self.settings['aruco_streetSign']
        self.dict = cv2.aruco.getPredefinedDictionary(self.arucoDictionary)
        self.params = cv2.aruco.DetectorParameters()
        self.cam_matrix = cam_matrix
        self.dist_coeff = dist_coeff
        self.corners = None
        self.ids = None
        self.rejected = None
        self.rvec = None
        self.tvec = None
        self.markerLength = self.settings['aruco_markerLength']

    def undistort(self, raw_image):
        image = cv2.undistort(raw_image, self.cam_matrix, self.dist_coeff, None, self.cam_matrix)
        return image

    def frameDetector(self, image):
        try:
            (self.corners, self.ids, self.rejected) = cv2.aruco.detectMarkers(image, self.dict, parameters=self.params)
            for id in self.ids:
                try:
                    descr_cartello = self.streetSign[id[0]][1]
                    print(descr_cartello)
                    print("Trovato l'id {0} che equivale al cartello {1}\n".format(id[0], descr_cartello))
                except:
                    print("L'id {0} trovato non equivale a nessun cartello a DB\n".format(id[0]))
            print("[INFO] Trovati {:d} aruco\n".format(len(self.ids)))
        except:
            print("[ERRORE] Impossibile riconoscere i markers\n")
        return self.corners
    
    def estimatePoseMarkers(self):
        self.rvec, self.tvec, _ = cv2.aruco.estimatePoseSingleMarkers(self.corners, self.markerLength, self.cam_matrix, self.dist_coeff)
        return self.rvec, self.tvec

    def rodrigues(self, r):
        theta = np.linalg.norm(r)
        u = np.array(r / theta)
        cross_u = np.array([[0,-u[2],u[1]],[u[2],0,-u[0]],[-u[1],u[0],0]])
        R = np.array(np.eye(3)*math.cos(theta) + (1-math.cos(theta))*np.matmul(u,u.T) + cross_u*math.sin(theta))
        return R

    def drawDetectedMarkers(self, image):
        return cv2.aruco.drawDetectedMarkers(image, self.corners)

    def drawAxis(self, image):
        #try:
        for i in range(len(self.ids)):
            image = cv2.drawFrameAxes(image, self.cam_matrix, self.dist_coeff, self.rvec[i], self.tvec[i], self.markerLength/2)
        return image
        #except:
        #    print("[ERRORE] Non ci sono markers di cui calcolare gli assi")
        #    return image

    def printImage(self, image):
        comboBig = cv2.resize(image, self.settings['aruco_canvasResolution'])
        plt.imshow(image)
        plt.show()

    def close(self):
        cv2.destroyAllWindows()

class ColorFinder():
    def __init__(self, image = None, color = None, radius = None):
        self.image = image
        self.color = color
        self.raggio = radius
        if self.image is not None:
            self.width = self.image.shape[0]
            self.height = self.image.shape[1]
            
    def changeValues(self, colorNew = None, radiusNew = None):
        if colorNew is not None:
            self.color = colorNew
        if radiusNew is not None:
            self.raggio = radiusNew
        
    def newImage(self, imageNew):
        self.image = imageNew
        self.or_image = self.image
        self.width = self.image.shape[0]
        self.height = self.image.shape[1]
        
    def distInRange(self):
        self.lower = np.array([])
        for i in range(3):
            if self.color[i]-self.raggio < 0:
                self.lower = np.append(self.lower,0)
            else:
                self.lower = np.append(self.lower, self.color[i]-self.raggio)
        self.upper = np.array([])
        for i in range(3):
            if self.color[i]+self.raggio > 255:
                self.upper = np.append(self.upper, 255)
            else:
                self.upper = np.append(self.upper, self.color[i]+self.raggio)

        self.bool_Md = cv2.inRange(self.image, self.lower, self.upper)

        return self.bool_Md

class StreetLight:

    def __init__(self, image=None):
        self.image = image
        if self.image is not None:
            self.width = math.trunc(self.image.shape[0])
            self.height = math.trunc(self.image.shape[1])
            self.SO = (0, self.height)
            self.NE = (self.width, 0)

    def changeImage(self, imageNew=None):
        self.image = imageNew
        if self.image is not None:
            self.width = math.trunc(self.image.shape[0])
            self.height = math.trunc(self.image.shape[1])
            self.SO = (0, self.height)
            self.NE = (self.width, 0)

    def inBorder(self, SO, NE):
        if SO[0] < 0:
            SO[0] = 0
        if NE[0] > self.width:
            NE[0] = self.width
        return (int(SO[0][0]), int(SO[1][0])), (int(NE[0][0]), int(NE[1][0]))

    def roi(self, sign):
        coordinates = np.array(sign[0]).T 
        xs = coordinates[0].astype(int)
        ys = coordinates[1].astype(int)
        len = max(xs) - min(xs)
        
        yMedia = (max(ys) + min(ys))/2; 
        
        xMin = min(xs) - len
        xMax = min(xs)
        self.SO, self.NE = self.inBorder([xMin, yMedia+len], [xMax, yMedia-len])
        return self.SO, self.NE

    def color(self):
        finder = ColorFinder(image = self.image[self.NE[1]:self.SO[1], self.SO[0]:self.NE[0]], color = (255,0,0), radius = 50)
        self.redMask = finder.distInRange()
       
        finder.changeValues(colorNew = (255,255,0), radiusNew = 60)
        self.yellowMask = finder.distInRange()
        
        finder.changeValues(colorNew = (0,255,0), radiusNew = 50)
        self.greenMask = finder.distInRange()
        return self.redMask, self.yellowMask, self.greenMask

    def lightColor(self):
        self.r_num = np.count_nonzero(self.redMask)
        self.y_num = np.count_nonzero(self.yellowMask)
        self.g_num = np.count_nonzero(self.greenMask)
        max_num = max([self.r_num, self.y_num, self.g_num])
        if max_num == self.r_num:
            return 'r'
        elif max_num == self.y_num:
            return 'y'
        else: 
            return 'g'


raw_image = cv2.imread('img/semaforo-colori.jpg')
raw_image = cv2.cvtColor(raw_image, cv2.COLOR_BGR2RGB)
# plt.imshow(raw_image)

detector = ArucoDetector(None, None)


image = raw_image
corner = detector.frameDetector(image)

semaforo = StreetLight(image)
SO, NE = semaforo.roi(corner)
# plt.imshow(image[NE[1]:SO[1],SO[0]:NE[0]])

r,y,g = semaforo.color()

f, axarr = plt.subplots(1,4) 
axarr[0].imshow(image[NE[1]:SO[1],SO[0]:NE[0]])
axarr[1].imshow(r)
axarr[2].imshow(y)
axarr[3].imshow(g)

colore = {
    'r' : 'Rosso',
    'g' : 'Giallo',
    'v' : 'Verde'
}.get(semaforo.lightColor())
print(colore)

plt.show()