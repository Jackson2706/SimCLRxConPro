import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.axes_grid1 import ImageGrid
from PIL import Image

# Đường dẫn tới 6 hình ảnh
image_paths = [
    "/mnt/d/AiThings/SimCLRxConPro/images/image.png",
    "/mnt/d/AiThings/SimCLRxConPro/images/label.png",
    "/mnt/d/AiThings/SimCLRxConPro/images/new_proposal.png",
    "/mnt/d/AiThings/SimCLRxConPro/images/image2.png",
    "/mnt/d/AiThings/SimCLRxConPro/images/label2.png",
    "/mnt/d/AiThings/SimCLRxConPro/images/new_proposal2.png"
]

# Đọc các hình ảnh từ đường dẫn
images = [Image.open(image_path) for image_path in image_paths]

# Tạo figure với kích thước phù hợp
fig = plt.figure(figsize=(8., 6.))  # Bạn có thể thay đổi kích thước này cho phù hợp

# Tạo lưới 2x3
grid = ImageGrid(fig, 111,  # similar to subplot(111)
                 nrows_ncols=(2, 3),  # lưới 2x3
                 axes_pad=0.1,  # khoảng cách giữa các hình ảnh
                 )

# Hiển thị từng ảnh trong từng ô
for ax, im in zip(grid, images):
    ax.imshow(im)
    ax.axis('off')  # Tắt hiển thị trục

# Hiển thị lưới ảnh
plt.show()
