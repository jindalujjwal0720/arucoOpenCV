# aruco

import cv2

images = [
	"LMAO.jpg",
	"XD.jpg",
	"Ha.jpg",
	"HaHa.jpg"
]
# img = cv2.imread("XD.jpg")

def detectAruco(img):
	ARUCO_DICT = {
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
	}

	for (arucoName, arucoDict) in ARUCO_DICT.items():
		arucoDict = cv2.aruco.Dictionary_get(arucoDict)
		arucoParams = cv2.aruco.DetectorParameters_create()
		(corners, ids, rejected) = cv2.aruco.detectMarkers(img, arucoDict, parameters=arucoParams)
		if len(corners) > 0:
			print(f"[INFO] detected {len(corners)} markers for '{arucoName}'")
			# print(f"{corners} : {ids} : {rejected}")

for i in images:
	img = cv2.imread(i)
	arucoDict = cv2.aruco.Dictionary_get(cv2.aruco.DICT_5X5_50)
	arucoParams = cv2.aruco.DetectorParameters_create()
	(corners, ids, rejected) = cv2.aruco.detectMarkers(img, arucoDict, parameters=arucoParams)

	cv2.drawContours(img, [corners[0].astype(int)], -1, (0, 255, 0), 3)
	cv2.putText(img, f"{ids[0][0]}", (50, 50), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 255, 0), 3)

	print(f"{corners[0]}")

	cv2.imshow(f"Aruco {i}", img)

cv2.waitKey(0)