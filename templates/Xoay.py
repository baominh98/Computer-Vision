# coding=utf-8
from PIL import Image
from pylab import *


def rotate_coords(x, y, theta, ox, oy):
    """Xoay mảng tọa độ x và y theo radian theta về
    điểm (ox, oy).

    """

    """
    x = (np.asarray(x) - ox)*np.cos(theta) - (np.asarray(y) - oy)*np.sin(theta) + ox
    y = (np.asarray(x) - ox)*np.sin(theta) - (np.asarray(y) - oy)*np.cos(theta) + oy

    """
    s, c = np.sin(theta), np.cos(theta)
    x, y = np.asarray(x) - ox, np.asarray(y) - oy
    return x * c - y * s + ox, x * s + y * c + oy


def rotate_image(src, theta, ox, oy, fill=155):
    """Xoay  ảnh nguon theo radian voi goc toa do la (ox, oy).
    Các pixel trong kết quả không nam trong src thi duoc
    thay thế bằng cách điền giá trị fill.

    """
    # Hình ảnh có nguồn gốc ở phía trên bên trái, do đó phủ nhận góc, Doi Degree thanh Radian.
    theta = -(theta*(math.pi/180))

    # Kích thước của hình ảnh nguồn.
    # src.shape đưa ra (chiều cao, chiều rộng).
    sh, sw = src.shape

    # Vị trí xoay góc của hình ảnh nguồn.
    cx, cy = rotate_coords([0, sw, sw, 0], [0, 0, sh, sh], theta, ox, oy)

    # Xác định kích thước của hình ảnh đích.
    dw, dh = (int(np.ceil(c.max() - c.min())) for c in (cx, cy))

    #  Tọa độ của pixel trong ảnh đích.
    dx, dy = np.meshgrid(np.arange(dw), np.arange(dh))

    # Tọa độ tương ứng trong hình ảnh nguồn. Vì chúng ta
    # chuyển đổi Dest-to-src ở đây, phép quay bị phủ định.
    sx, sy = rotate_coords(dx + cx.min(), dy + cy.min(), -theta, ox, oy)

    # Làm Tròn.
    sx, sy = sx.round().astype(int), sy.round().astype(int)

    # tim tọa độ hợp lệ neu Hop le la True nguoc lai la False.
    mask = (0 <= sx) & (sx < sw) & (0 <= sy) & (sy < sh)
    print (mask)
    # Tạo Ảnh.
    dest = np.empty(shape=(dh, dw), dtype=src.dtype)

    # Chép các điểm ảnh từ ảnh nguồn
    dest[dy[mask], dx[mask]] = src[sy[mask], sx[mask]]
    # Thêm các điểm ảnh không có thật
    dest[dy[~mask], dx[~mask]] = fill

    return dest

while (1):
    # arr = input('Nhap Duong Dan: ')
    img = array(Image.open('/home/caohuy/Python/LnchVbA.png').convert('L'))  # convert('L'))=>trang den
    gray()
    img1 = np.ones([8, 8])
    for i in range(8):
        for j in range(8):
            img1[i, j] = j+1
    row, col = img1.shape
    centerX = np.round(col / 2)
    centerY = np.round(row / 2)
    try:
        Angle = int(input('Nhap Goc Xoay: '))
        Fill = int(input('Nhap Fill: '))
    except Exception:
        print('Vui Long Nhap So')
        continue
    imgOut = rotate_image(img1, Angle, centerX, centerY, Fill)
    imshow(imgOut)
    print(imgOut)
    show()
    break