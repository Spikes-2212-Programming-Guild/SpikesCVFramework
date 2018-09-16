import cv2
from networktables import NetworkTables


class NetworkTableIO:
    def __init__(self, ip, name):
        NetworkTables.initialize(ip)
        self.nt = NetworkTables.getTable(name)
        self.contour_count = 2

    def settings_supplier(self, callback):
        def entry_listener(table, key, value, isNew):
            callback(key, value)

        self.nt.addEntryListener(entry_listener)

    def output_consumer(self, output):
        contours = sorted(output, key=cv2.contourArea, reverse=True)
        self.contour_count = max(self.contour_count, len(contours))

        # sends info about all the filtered contours received by the function
        for i, c in enumerate(contours):
            self.nt.putNumber("contourArea{}".format(cv2.contourArea(c)))

            x, y, w, h = cv2.boundingRect(c)

            self.nt.putNumber("width{}".format(w))
            self.nt.putNumber("height{}".format(h))
            self.nt.putNumber("x{}".format(x))
            self.nt.putNumber("y{}".format(y))

            self.nt.putBoolean("isUpdated{}".format(i), True)
            self.nt.putNumber("numberOfContours", len(contours))

        # turning off isUpdated flag for contours that were not updated
        for i in range(len(contours), self.contour_count):
            self.nt.putBoolean("isUpdated{}".format(i), False)
