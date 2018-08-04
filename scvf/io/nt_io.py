import cv2
from networktables import NetworkTables


class NetworkTableIO:
    def __init__(self, ip, name):
        NetworkTables.initialize(ip)
        self.nt = NetworkTables.getTable(name)
        self.contour_count = 2

    def settings_supplier(self, key):
        return self.nt.getString(key, defaultValue="")

    def output_consumer(self, output):
        contours = sorted(output, cv2.contourArea, reverse=True)
        self.contour_count = max(self.contour_count, len(contours))

        # sends info about all the filtered contours received by the function
        for i, c in enumerate(contours):
            self.nt.putNumber(f"contourArea{i}", cv2.contourArea(c))

            x, y, w, h = cv2.boundingRect(c)

            self.nt.putNumber(f"width{i}", w)
            self.nt.putNumber(f"height{i}", c)
            self.nt.putNumber(f"x{i}", x)
            self.nt.putNumber(f"y{i}", y)

            self.nt.putBoolean(f"isUpdated{i}", True)
            self.nt.putNumber("numberOfContours", len(contours))

        # turning off isUpdated flag for contours that were not updated
        for i in range(len(contours), self.contour_count):
            self.nt.putBoolean(f"isUpdated{i}", False)
