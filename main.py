from random import randint
from typing import List

import matplotlib.pyplot as plt
import numpy as np


def vec_format(vec: np.ndarray, start=np.zeros((3, 1))):
    """将三维向量格式化成带有起点的六维向量形式

    Args:
        vec (np.ndarray): 三维向量
        start (np.ndarray): 起点

    Returns:
        np.ndarray: 格式化后的六维向量
    """
    return np.concatenate([start.flatten(), vec.flatten()])


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
    v1 = np.array([1, 1, 0]).reshape(3, 1)  # 向量(5, 5, 0).T
    v2 = np.array([1, -1, 0]).reshape(3, 1)  # 向量(3, -4, 0).T
    v3 = np.cross(v1, v2, 0, 0, 0)  # 叉乘v1 v2 得其矩
    show_vecs(
        [[0, 0, 0, *v1.flatten()], [0, 0, 0, *v2.flatten()], [0, 0, 0, *v3.flatten()]],  # 传入三个向量 每个元素前三个是起点 后三个是向量本身
        (-1.0, 1.0)  # 坐标系大小
    )
    show_vecs([vec_format(v_, start=np.array([2, 2, 0])) for v_ in (v1, v2, v3)], (-1.0, 3.0))  # 利用vec_format函数对向量格式化，使其偏移2个单位长度


if __name__ == "__main__":
    main()
