import cv2

# Hàm xử lý sự kiện click chuột
def click_event(event, x, y, flags, params):
    if event == cv2.EVENT_LBUTTONDOWN:
        print(f'Tọa độ điểm click: ({x}, {y})')
        # Vẽ một vòng tròn nhỏ tại điểm click
        cv2.circle(img, (x, y), 3, (0, 0, 255), -1)
        cv2.imshow('Anh', img)

# Đọc ảnh
img = cv2.imread('images/manGame.png')
if img is None:
    print("Không thể đọc ảnh. Vui lòng kiểm tra đường dẫn.")
else:
    cv2.imshow('Anh', img)
    # Gán hàm xử lý sự kiện chuột cho cửa sổ ảnh
    cv2.setMouseCallback('Anh', click_event)
    cv2.waitKey(0)
    cv2.destroyAllWindows()