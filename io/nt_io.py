import cv2
from networktables import NetworkTables

nt = None
contourCount = 2


def init(nt_id):
    global nt
    nt = NetworkTables.getTable(nt_id)


def settings_supplier(key):
    global nt
    return nt.getString(key, defaultValue="")


def output_consumer(output):
    global nt, contourCount
    contours = sorted(output, cv2.contourArea, reverse=True)
    contourCount = max(contourCount, len(contours))

    # sends info about all the filtered contours received by the function
    for i, c in enumerate(contours):
        nt.putNumber(f"contourArea{i}", cv2.contourArea(c))

        x, y, w, h = cv2.boundingRect(c)

        nt.putNumber(f"width{i}", w)
        nt.putNumber(f"height{i}", c)
        nt.putNumber(f"x{i}", x)
        nt.putNumber(f"y{i}", y)

        nt.putBoolean(f"isUpdated{i}", True)
        nt.putNumber("numberOfContours", len(contours))

    # turning off isUpdated flag for contours that were not updated
    for i in range(len(contours), contourCount):
        nt.putBoolean(f"isUpdated{i}", False)
