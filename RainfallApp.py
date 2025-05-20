import tkinter as tk
from tkinter import ttk, messagebox
import pandas as pd
from datetime import datetime
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import StandardScaler
from tkcalendar import Calendar

# Khởi tạo cửa sổ Tkinter
root = tk.Tk()
root.title("Dự đoán lượng mưa")
root.geometry("650x850")
root.configure(bg="#f5f7fa")

# Từ điển ánh xạ
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

# Danh sách giá trị cho Combobox
provinces_values = list(provinces_dict.values())
wind_directions_values = list(wind_directions_dict.values())

# Style
style = ttk.Style()
style.configure("TCombobox", font=("Arial", 12), padding=5)
style.configure("TButton", font=("Arial", 13, "bold"))

# Frame chính
main_frame = tk.Frame(root, bg="white", padx=30, pady=30, relief="groove", bd=2)
main_frame.pack(padx=30, pady=30, fill="both", expand=True)

# Tiêu đề
title = tk.Label(main_frame, text="🚗 Hệ Thống Dự Đoán Lượng Mưa", font=("Arial", 22, "bold"), fg="#2c3e50", bg="white")
title.pack(pady=10)
sub_title = tk.Label(main_frame, text="Thông tin thời tiết", font=("Arial", 14), bg="white", fg="#7f8c8d")
sub_title.pack(pady=(0, 20))

# Khung nhập liệu
form_frame = tk.Frame(main_frame, bg="white")
form_frame.pack()


def add_field(label_text, row, widget):
    label = tk.Label(form_frame, text=label_text, font=("Arial", 13), bg="white", anchor="w", width=20)
    label.grid(row=row, column=0, padx=10, pady=10, sticky="e")
    widget.grid(row=row, column=1, padx=10, pady=10, sticky="w")


# Widgets
province_cb = ttk.Combobox(form_frame, values=provinces_values, state="readonly", font=("Arial", 13), width=33)
province_cb.current(0)
add_field("Tỉnh:", 0, province_cb)

max_temp = tk.Entry(form_frame, font=("Arial", 13), width=35)
add_field("Nhiệt độ tối đa (°C):", 1, max_temp)

min_temp = tk.Entry(form_frame, font=("Arial", 13), width=35)
add_field("Nhiệt độ tối thiểu (°C):", 2, min_temp)

wind_speed = tk.Entry(form_frame, font=("Arial", 13), width=35)
add_field("Tốc độ gió (km/h):", 3, wind_speed)

wind_cb = ttk.Combobox(form_frame, values=wind_directions_values, state="readonly", font=("Arial", 13), width=33)
wind_cb.current(0)
add_field("Hướng gió:", 4, wind_cb)

humidity = tk.Entry(form_frame, font=("Arial", 13), width=35)
add_field("Độ ẩm (%):", 5, humidity)

cloud = tk.Entry(form_frame, font=("Arial", 13), width=35)
add_field("Độ che phủ mây (%):", 6, cloud)

pressure = tk.Entry(form_frame, font=("Arial", 13), width=35)
add_field("Áp suất (hPa):", 7, pressure)

# Widget lịch cho ngày
cal = Calendar(form_frame, selectmode="day", year=2025, month=5, day=20, date_pattern="yyyy-mm-dd")
cal.grid(row=8, column=1, padx=10, pady=10, sticky="w")
add_field("Ngày:", 8, cal)

# Nút dự đoán
predict_btn = tk.Button(main_frame, text="🔍 Dự đoán", bg="#3498db", fg="white", font=("Arial", 14, "bold"), width=20)
predict_btn.pack(pady=25)

# Khung kết quả
result_frame = tk.Frame(main_frame, bg="#ecf0f1", height=60)
result_frame.pack(fill="x", padx=10, pady=10)

result_label = tk.Label(result_frame, text="Dự đoán lượng mưa: ", font=("Arial", 14), bg="#ecf0f1", fg="#2c3e50")
result_label.pack(pady=10)

# Đọc và xử lý dữ liệu
try:
    weather_df = pd.read_csv('Data/weather_filled_after.csv')

    # Chuẩn bị dữ liệu cho mô hình
    X = weather_df[['province', 'max', 'min', 'wind', 'wind_d', 'humidi', 'cloud', 'pressure', 'date']]
    y = weather_df['rain']

    # Chuẩn hóa dữ liệu
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    # Huấn luyện mô hình
    model = LinearRegression()
    model.fit(X_scaled, y)
except Exception as e:
    messagebox.showerror("Lỗi", f"Không thể đọc hoặc xử lý file dữ liệu: {e}")
    weather_df = pd.DataFrame()
    scaler = None
    model = None


# Hàm xử lý dữ liệu đầu vào
def preprocess_input():
    try:
        # Lấy dữ liệu từ các trường nhập liệu
        province = province_cb.get()
        max_temp_val = max_temp.get()
        min_temp_val = min_temp.get()
        wind_speed_val = wind_speed.get()
        wind_direction = wind_cb.get()
        humidity_val = humidity.get()
        cloud_val = cloud.get()
        pressure_val = pressure.get()
        date_str = cal.get_date()  # Lấy ngày từ widget lịch

        # Xác thực các trường số
        for val, name in [
            (max_temp_val, "Nhiệt độ tối đa"),
            (min_temp_val, "Nhiệt độ tối thiểu"),
            (wind_speed_val, "Tốc độ gió"),
            (humidity_val, "Độ ẩm"),
            (cloud_val, "Độ che phủ mây"),
            (pressure_val, "Áp suất")
        ]:
            if not val:
                raise ValueError(f"Vui lòng nhập {name}.")
            try:
                float(val)
            except ValueError:
                raise ValueError(f"{name} phải là số hợp lệ.")

        # Chuyển đổi các giá trị số
        max_temp_val = float(max_temp_val)
        min_temp_val = float(min_temp_val)
        wind_speed_val = float(wind_speed_val)
        humidity_val = float(humidity_val)
        cloud_val = float(cloud_val)
        pressure_val = float(pressure_val)

        # Ánh xạ tỉnh và hướng gió
        province_key = [key for key, value in provinces_dict.items() if value == province][0]
        wind_direction_key = [key for key, value in wind_directions_dict.items() if value == wind_direction][0]

        # Chuẩn hóa ngày
        try:
            base_date = datetime(2009, 1, 1)
            date_obj = datetime.strptime(date_str, "%Y-%m-%d")
            delta_days = (date_obj - base_date).days
        except ValueError:
            raise ValueError("Ngày không hợp lệ. Vui lòng chọn ngày hợp lệ từ lịch.")

        # Chuẩn bị dữ liệu đầu vào
        input_data = [
            province_key,
            max_temp_val,
            min_temp_val,
            wind_speed_val,
            wind_direction_key,
            humidity_val,
            cloud_val,
            pressure_val,
            delta_days
        ]

        return input_data

    except ValueError as e:
        messagebox.showerror("Lỗi", str(e))
        return None


# Hàm dự đoán
def predict():
    if model is None or scaler is None:
        messagebox.showerror("Lỗi", "Mô hình chưa được huấn luyện. Vui lòng kiểm tra file dữ liệu.")
        return

    input_data = preprocess_input()
    if input_data is None:
        return

    try:
        # Chuẩn hóa dữ liệu đầu vào
        input_array = np.array([input_data])
        input_scaled = scaler.transform(input_array)

        # Dự đoán
        prediction = model.predict(input_scaled)[0]

        # Đảm bảo dự đoán không âm
        prediction = max(0, prediction)

        # Hiển thị kết quả
        result_label.config(text=f"Dự đoán lượng mưa: {prediction:.2f} mm")
    except Exception as e:
        messagebox.showerror("Lỗi", f"Lỗi khi dự đoán: {e}")


predict_btn.config(command=predict)

root.mainloop()