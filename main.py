import matplotlib.pyplot as plt

# Tọa độ các đỉnh của ngôi nhà
house_x = [0, 4, 4, 0, 0]
house_y = [0, 0, 4, 4, 0]

# Tọa độ cửa sổ
window_x = [1, 1, 3, 3, 1]
window_y = [2, 4, 4, 2, 2]

# Tọa độ cánh cửa
door_x = [2, 2, 2.5, 2.5, 2, 2]
door_y = [0, 2, 2, 0, 0, 0]

# Vẽ ngôi nhà
plt.plot(house_x, house_y, color='blue')

# Vẽ cửa sổ
plt.plot(window_x, window_y, color='yellow')

# Vẽ cánh cửa
plt.plot(door_x, door_y, color='brown')

# Đặt tên cho trục x và y
plt.xlabel('X-axis')
plt.ylabel('Y-axis')

# Đặt tiêu đề cho đồ thị
plt.title('Hình ngôi nhà')

# Hiển thị đồ thị
plt.show()
