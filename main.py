from random import randint
from typing import List

import matplotlib.pyplot as plt
import numpy as np


def show_vecs(vecs: List, lim=(-10, 10), r=0.1):
    """将多个3d向量绘制到空间坐标系中

    Args:
        vecs (List): 向量的可迭代对象，其中每个元素包含6个数，前三个为起点，后三个为向量本身
        lim (tuple): 空间坐标系的最大/最小限制
        r (float): 线段和箭头大小的比值
    """
    ax = plt.figure().add_subplot(projection='3d')
    ax.set_xlim3d(*lim)
    ax.set_ylim3d(*lim)
    ax.set_zlim3d(*lim)
    rand_colors = ["#{:02x}{:02x}{:02x}".format(*(randint(0, 255) for _ in range(3))) for _ in range(len(vecs))]
    for vec, color in zip(vecs, rand_colors):
        ax.quiver3D(*vec, arrow_length_ratio=r, color=color)
    plt.show()


def main():
    v1 = np.array([5, 5, 0]).reshape(3, 1)
    v2 = np.array([3, -4, 0]).reshape(3, 1)
    v3 = np.cross(v1, v2, 0, 0, 0)
    show_vecs([[0, 0, 0, *v1.flatten()], [0, 0, 0, *v2.flatten()], [0, 0, 0, *v3.flatten()]], (-40, 40))


if __name__ == "__main__":
    main()
