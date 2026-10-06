import cv2
import os
import numpy as np 
def resize_image(image, target_size=(480, 480)):
    return cv2.resize(image, target_size)
images_training = []
images_test = []
images_training_name = []

for fichier in os.listdir(r"C:\STUDY\TAI\TPfinal\Test"):
                          
    chemin_image = os.path.join(r'C:\STUDY\TAI\TPfinal\Test', fichier)
    imgTest = cv2.imread(chemin_image, cv2.IMREAD_ANYCOLOR)
    resized_img = resize_image(imgTest)
    images_test.append(resized_img)

for fichier in os.listdir(r"C:\STUDY\TAI\TPfinal\Training"):
                          
    chemin_image = os.path.join(r'C:\STUDY\TAI\TPfinal\Training', fichier)
    imgTrain = cv2.imread(chemin_image, cv2.IMREAD_ANYCOLOR)
    resized_img = resize_image(imgTrain)
    images_training.append((resized_img, fichier))


for image in images_training : 
    result = image[1].split('.')    
    images_training_name.append(result[0])

print("Available images:")
i=0
for name in images_training_name:
    print(str(i)+'- '+name)
    i=i+1
index = input('choose an image according to the index  :  ' )
    
# print(len(images_test))1
# Prompt the user to choose an image




img = images_training[int(index)]

image_request = img[0]

# Display the converted BGR image
cv2.imshow('You chosed:', image_request)
cv2.waitKey(0)
cv2.destroyAllWindows()





sift = cv2.SIFT_create()

keypoints_request = sift.detect(image_request, None)

_,descriptor_request = sift.compute(image_request, keypoints_request)
descriptor_request = descriptor_request.astype(np.float32)

img_with_keypoints = cv2.drawKeypoints(image_request, keypoints_request, None, color=(0, 255, 0), flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
cv2.imshow('Image avec points clés SIFT', img_with_keypoints)
cv2.waitKey(0)
cv2.destroyAllWindows()

bf = cv2.BFMatcher()
# we will use the brute force matching 
good_matches_num = 0
for image in images_test :
    keypoints = sift.detect(image, None)
    _,descriptor = sift.compute(image, keypoints)
    descriptor = descriptor.astype(np.float32)
    
    matches = bf.knnMatch(descriptor_request, descriptor, k=2)  
    good_matches = []
    for m, n in matches:
        if m.distance < 0.75 * n.distance:  
            good_matches.append(m)
    if len( good_matches) > good_matches_num : 
        good_matches_num = len(good_matches)
        candidate_image = image
        candidate_keypoints = keypoints
        candidate_descriptor = descriptor

cv2.imshow('best matching image : ', candidate_image)
cv2.waitKey(0)
cv2.destroyAllWindows()



match_img = cv2.drawMatches(image_request, keypoints_request, candidate_image, candidate_keypoints, good_matches, None, flags=2)
cv2.imshow('Matches', match_img)
cv2.waitKey(0)
        
    

    