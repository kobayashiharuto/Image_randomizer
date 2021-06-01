import numpy as np
from PIL import Image
from numpy.core.fromnumeric import size


def quad_as_rect(quad):
    if quad[0] != quad[2]:
        return False
    if quad[1] != quad[7]:
        return False
    if quad[4] != quad[6]:
        return False
    if quad[3] != quad[5]:
        return False
    return True


def quad_to_rect(quad):
    assert(len(quad) == 8)
    assert(quad_as_rect(quad))
    return (quad[0], quad[1], quad[4], quad[3])


def rect_to_quad(rect):
    assert(len(rect) == 4)
    return (rect[0], rect[1], rect[0], rect[3], rect[2], rect[3], rect[2], rect[1])


def shape_to_rect(shape):
    assert(len(shape) == 2)
    return (0, 0, shape[0], shape[1])


def griddify(rect, w_div, h_div):
    w = rect[2] - rect[0]
    h = rect[3] - rect[1]
    print(rect)
    x_step = w / float(w_div)
    y_step = h / float(h_div)
    y = rect[1]
    grid_vertex_matrix = []
    for _ in range(h_div + 1):
        grid_vertex_matrix.append([])
        x = rect[0]
        for _ in range(w_div + 1):
            grid_vertex_matrix[-1].append([int(x), int(y)])
            x += x_step
        y += y_step
    grid = np.array(grid_vertex_matrix)
    print(grid.shape)
    print(grid)
    return grid


def distort_grid(org_grid, max_shift):
    new_grid = np.copy(org_grid)
    x_min = np.min(new_grid[:, :, 0])
    y_min = np.min(new_grid[:, :, 1])
    x_max = np.max(new_grid[:, :, 0])
    y_max = np.max(new_grid[:, :, 1])
    print(max_shift, new_grid.shape)
    new_grid += np.random.randint(- max_shift, max_shift + 1, new_grid.shape)
    print(new_grid)
    new_grid[:, :, 0] = np.maximum(x_min, new_grid[:, :, 0])
    new_grid[:, :, 1] = np.maximum(y_min, new_grid[:, :, 1])
    new_grid[:, :, 0] = np.minimum(x_max, new_grid[:, :, 0])
    new_grid[:, :, 1] = np.minimum(y_max, new_grid[:, :, 1])
    print(new_grid)
    return new_grid


def grid_to_mesh(src_grid, dst_grid):
    assert(src_grid.shape == dst_grid.shape)
    mesh = []
    for i in range(src_grid.shape[0] - 1):
        for j in range(src_grid.shape[1] - 1):
            src_quad = [src_grid[i, j, 0], src_grid[i, j, 1],
                        src_grid[i + 1, j, 0], src_grid[i + 1, j, 1],
                        src_grid[i + 1, j + 1, 0], src_grid[i + 1, j + 1, 1],
                        src_grid[i, j + 1, 0], src_grid[i, j + 1, 1]]
            dst_quad = [dst_grid[i, j, 0], dst_grid[i, j, 1],
                        dst_grid[i + 1, j, 0], dst_grid[i + 1, j, 1],
                        dst_grid[i + 1, j + 1, 0], dst_grid[i + 1, j + 1, 1],
                        dst_grid[i, j + 1, 0], dst_grid[i, j + 1, 1]]
            dst_rect = quad_to_rect(dst_quad)
            mesh.append([dst_rect, src_quad])
    print(mesh)
    return mesh


def randomize_image(image):
    print(image.size)
    dst_grid = griddify(shape_to_rect(image.size), 1, 1)
    src_grid = distort_grid(dst_grid, 3)
    mesh = grid_to_mesh(src_grid, dst_grid)
    image = image.transform(image.size, Image.MESH, mesh)
    return image


def main():
    image = Image.open('out/binary.png')
    randomized_image = randomize_image(image)
    randomized_image.save('out/rand.png')


if __name__ == '__main__':
    main()