import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Dự đoán lượng mưa")
root.geometry("650x850")
root.configure(bg="#f5f7fa")

# ======= DỮ LIỆU (Dạng dict) =======
provinces_dict = {
    1: 'Bac Lieu', 2: 'Ho Chi Minh City', 3: 'Tam Ky', 4: 'Ha Noi', 5: 'Da Nang',
    6: 'Can Tho', 7: 'Hai Phong', 8: 'Quang Nam', 9: 'Binh Duong', 10: 'Dong Nai',
    11: 'Nghe An', 12: 'Thanh Hoa', 13: 'Khanh Hoa', 14: 'Lam Dong', 15: 'Phu Yen',
    16: 'Binh Thuan', 17: 'Ninh Thuan', 18: 'Tay Ninh', 19: 'Long An', 20: 'Tien Giang',
    21: 'Ben Tre', 22: 'Tra Vinh', 23: 'Vinh Long', 24: 'Dong Thap', 25: 'An Giang',
    26: 'Kien Giang', 27: 'Ca Mau', 28: 'Soc Trang', 29: 'Bac Giang', 30: 'Bac Ninh',
    31: 'Ha Tinh', 32: 'Quang Binh', 33: 'Quang Tri', 34: 'Thua Thien Hue', 35: 'Binh Dinh',
    36: 'Gia Lai', 37: 'Kon Tum', 38: 'Dak Lak', 39: 'Dak Nong', 40: 'Ba Ria - Vung Tau'
}

wind_directions_dict = {
    1: 'ESE', 2: 'SE', 3: 'E', 4: 'WSW', 5: 'ENE', 6: 'SW', 7: 'SSE',
    8: 'SSW', 9: 'W', 10: 'NE', 11: 'NNE', 12: 'WNW', 13: 'NNW', 14: 'N'
}

# Tạo danh sách value để hiển thị trong Combobox
provinces_values = list(provinces_dict.values())  # ['Bac Lieu', 'Ho Chi Minh City', ...]
wind_directions_values = list(wind_directions_dict.values())  # ['ESE', 'SE', ...]

# Tạo ánh xạ ngược từ value về key
provinces_value_to_key = {v: k for k, v in provinces_dict.items()}  # {'Bac Lieu': 1, ...}
wind_directions_value_to_key = {v: k for k, v in wind_directions_dict.items()}  # {'ESE': 1, ...}

# ======= STYLE =======
style = ttk.Style()
style.configure("TCombobox", font=("Arial", 12), padding=5)
style.configure("TButton", font=("Arial", 13, "bold"))

# ======= FRAME CHÍNH =======
main_frame = tk.Frame(root, bg="white", padx=30, pady=30, relief="groove", bd=2)
main_frame.pack(padx=30, pady=30, fill="both", expand=True)

# ======= TIÊU ĐỀ =======
title = tk.Label(main_frame, text="🚗 Hệ Thống Dự Đoán Lượng Mưa", font=("Arial", 22, "bold"), fg="#2c3e50", bg="white")
title.pack(pady=10)

sub_title = tk.Label(main_frame, text="Thông tin thời tiết", font=("Arial", 14), bg="white", fg="#7f8c8d")
sub_title.pack(pady=(0, 20))

# ======= KHUNG NHẬP LIỆU =======
form_frame = tk.Frame(main_frame, bg="white")
form_frame.pack()

def add_field(label_text, row, widget):
    label = tk.Label(form_frame, text=label_text, font=("Arial", 13), bg="white", anchor="w", width=20)
    label.grid(row=row, column=0, padx=10, pady=10, sticky="e")
    widget.grid(row=row, column=1, padx=10, pady=10, sticky="w")

# Province (Hiển thị tên tỉnh)
province_cb = ttk.Combobox(form_frame, values=provinces_values, state="readonly", font=("Arial", 13), width=33)
province_cb.current(0)  # Chọn tỉnh đầu tiên (Bac Lieu)
add_field("Tỉnh:", 0, province_cb)

# Max temp
max_temp = tk.Entry(form_frame, font=("Arial", 13), width=35)
add_field("Nhiệt độ tối đa (°C):", 1, max_temp)

# Min temp
min_temp = tk.Entry(form_frame, font=("Arial", 13), width=35)
add_field("Nhiệt độ tối thiểu (°C):", 2, min_temp)

# Wind speed
wind_speed = tk.Entry(form_frame, font=("Arial", 13), width=35)
add_field("Tốc độ gió (km/h):", 3, wind_speed)

# Wind direction (Hiển thị hướng gió)
wind_cb = ttk.Combobox(form_frame, values=wind_directions_values, state="readonly", font=("Arial", 13), width=33)
wind_cb.current(0)  # Chọn hướng gió đầu tiên (ESE)
add_field("Hướng gió:", 4, wind_cb)

# Humidity
humidity = tk.Entry(form_frame, font=("Arial", 13), width=35)
add_field("Độ ẩm (%):", 5, humidity)

# Cloud cover
cloud = tk.Entry(form_frame, font=("Arial", 13), width=35)
add_field("Độ che phủ mây (%):", 6, cloud)

# Pressure
pressure = tk.Entry(form_frame, font=("Arial", 13), width=35)
add_field("Áp suất (hPa):", 7, pressure)

# Date input (Entry thay vì Combobox)
date_entry = tk.Entry(form_frame, font=("Arial", 13), width=35)
add_field("Ngày (YYYY-MM-DD):", 8, date_entry)

# ======= NÚT DỰ ĐOÁN =======
predict_btn = tk.Button(main_frame, text="🔍 Dự đoán", bg="#3498db", fg="white", font=("Arial", 14, "bold"), width=20)
predict_btn.pack(pady=25)

# ======= KẾT QUẢ =======
result_frame = tk.Frame(main_frame, bg="#ecf0f1", height=60)
result_frame.pack(fill="x", padx=10, pady=10)

result_label = tk.Label(result_frame, text="Dự đoán lượng mưa: ", font=("Arial", 14), bg="#ecf0f1", fg="#2c3e50")
result_label.pack(pady=10)

# Chạy giao diện
root.mainloop()