import sys
import numpy as np
import cv2
import os

def find_image_points(path, pattern_size):    
    imgs_names = os.listdir(path)
    image_points = []
    for n in imgs_names:
        img = cv2.imread(os.path.join(path, n))
        if img is None:
            continue
        image_size = img.shape[1::-1]
        img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        ret, corners = cv2.findChessboardCorners(img_gray, pattern_size, None)
        if ret:
            image_points.append(corners)
    return image_points, image_size

def generate_object_points(pattern_size, image_count):
    mesh_grid = np.mgrid[: pattern_size[0], : pattern_size[1]].T.reshape(-1, 2)
    mesh_grid_3D = np.append(mesh_grid, np.zeros((mesh_grid.shape[0], 1)), axis=1)
    object_points = np.repeat(mesh_grid_3D[None, :], image_count, axis=0)
    return object_points

def camera_caliberation(image_points, object_points, image_size):  
    error, camera_matrix, distort_coef, rotation_vec, translation_vec = cv2.calibrateCamera(
        object_points.astype(np.float32), image_points, image_size, None, None
    )
    
    print("Error: {:.4f}".format(error))
    print(f"Camera Matrix:\n {camera_matrix}")
    print(f"Distortion Coeficient: {distort_coef}")
    
    for idx in range(len(image_points)):
        print(f"image {idx+1}:")
        print(f"Rotation Vector: {rotation_vec[idx].T}")
        print(f"Translation Vector: {translation_vec[idx].T}\n")

if __name__ == "__main__":
    args = sys.argv
    pattern_size = (int(args[2]),int(args[3]))
    image_points, image_size = find_image_points(args[1], pattern_size) 
    object_points = generate_object_points(pattern_size, len(image_points))
    camera_caliberation(image_points, object_points, image_size)
    