from stl import mesh
import numpy as np
from tqdm import tqdm
import os

def convert(file):
    cuboid = mesh.Mesh.from_file(file)

    x_min, y_min, z_min = np.floor(cuboid.min_).astype(int)
    x_max, y_max, z_max = np.ceil(cuboid.max_).astype(int)
    width = x_max - x_min
    height = y_max - y_min
    depth = z_max - z_min

    MASK = np.zeros((width+1, height+1, depth+1))

    print(MASK.shape)

    for triangle in tqdm(range(len(cuboid.vectors))):
        vertices = np.array(cuboid.vectors[triangle])

        min_voxel_coords = np.floor(vertices.min(axis=0)).astype(int)
        max_voxel_coords = np.ceil(vertices.max(axis=0)).astype(int)

        x_stop, x_start = max_voxel_coords[0]-x_min, min_voxel_coords[0]-x_min
        y_stop, y_start = max_voxel_coords[1]-y_min, min_voxel_coords[1]-y_min
        z_stop, z_start = max_voxel_coords[2]-z_min, min_voxel_coords[2]-z_min

        # Calculate tolerance based on maximum side length
        for i in range(x_start, x_stop):
            for j in range(y_start, y_stop):
                for k in range(z_start, z_stop):
                    point = [i, j, k]
                    v0 = vertices[2] - vertices[0]
                    v1 = vertices[1] - vertices[0]
                    normal = np.cross(v0, v1)

                    # Calculate the signed distance from the point to the plane
                    dist = np.dot(point - vertices[0], normal)

                    # Check if the point is within the plane of the triangle with tolerance
                    if np.abs(dist) <= 1e9:
                        MASK[i][j][k] = 1
    return MASK

if __name__ == '__main__':
    for dir, _, files in os.walk('./Data/'):
        for file in files:
            mask = convert(os.path.join(dir, file))
            np.save(f'Dataset/{file}.npy', mask)
