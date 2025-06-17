import tkinter as tk
from tkinter import ttk, messagebox
import pandas as pd
from datetime import datetime
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import mean_squared_error, r2_score
from tkcalendar import Calendar

# Khởi tạo cửa sổ Tkinter
root = tk.Tk()
root.title("Dự đoán lượng mưa")
root.state('zoomed')

# Tạo Canvas và Scrollbar
canvas = tk.Canvas(root, bg="#f5f7fa")
scrollbar = ttk.Scrollbar(root, orient="vertical", command=canvas.yview)
canvas.configure(yscrollcommand=scrollbar.set)

scrollbar.pack(side="right", fill="y")
canvas.pack(side="left", fill="both", expand=True)

# Frame chứa nội dung trong Canvas
container_frame = tk.Frame(canvas, bg="#f5f7fa")
canvas_window = canvas.create_window((0, 0), window=container_frame, anchor="n")

# Hàm cập nhật scrollregion và chiều rộng
def on_configure(event):
    canvas.configure(scrollregion=canvas.bbox("all"))
    canvas.itemconfig(canvas_window, width=canvas.winfo_width())

container_frame.bind("<Configure>", on_configure)

# Frame chính được căn giữa trong container
main_frame = tk.Frame(container_frame, bg="white", padx=30, pady=30, relief="groove", bd=2)
main_frame.pack(pady=30)

# Đảm bảo căn giữa sau khi giao diện được render
def center_main_frame():
    canvas.itemconfig(canvas_window, width=canvas.winfo_width())

root.after_idle(center_main_frame)


# Style
style = ttk.Style()
style.configure("TCombobox", font=("Arial", 12), padding=5)
style.configure("TButton", font=("Arial", 13, "bold"))

# Tiêu đề
title = tk.Label(main_frame, text="Hệ Thống Dự Đoán Lượng Mưa", font=("Arial", 22, "bold"), fg="#2c3e50", bg="white")
title.pack(pady=10)
sub_title = tk.Label(main_frame, text="Thông tin thời tiết", font=("Arial", 14), bg="white", fg="#7f8c8d")
sub_title.pack(pady=(0, 20))

# Khung nhập liệu
form_frame = tk.Frame(main_frame, bg="white")
form_frame.pack()

def add_field(label_text, row, col, widget):
    label = tk.Label(form_frame, text=label_text, font=("Arial", 13), bg="white", anchor="w", width=20)
    label.grid(row=row, column=col*2, padx=10, pady=5, sticky="e")
    widget.grid(row=row, column=col*2+1, padx=10, pady=5, sticky="w")

provinces_dict = {0: 'Bac Lieu', 1: 'Ben Tre', 2: 'Bien Hoa', 3: 'Buon Me Thuot', 4: 'Ca Mau', 5: 'Cam Pha',
                6: 'Cam Ranh', 7: 'Can Tho', 8: 'Chau Doc', 9: 'Da Lat', 10: 'Ha Noi', 11: 'Hai Duong',
                12: 'Hai Phong', 13: 'Hanoi', 14: 'Ho Chi Minh City', 15: 'Hoa Binh', 16: 'Hong Gai',
                17: 'Hue', 18: 'Long Xuyen', 19: 'My Tho', 20: 'Nam Dinh', 21: 'Nha Trang', 22: 'Phan Rang',
                23: 'Phan Thiet', 24: 'Play Cu', 25: 'Qui Nhon', 26: 'Rach Gia', 27: 'Soc Trang',
                28: 'Tam Ky', 29: 'Tan An', 30: 'Thai Nguyen', 31: 'Thanh Hoa', 32: 'Tra Vinh', 33: 'Tuy Hoa',
                34: 'Uong Bi', 35: 'Viet Tri', 36: 'Vinh', 37: 'Vinh Long', 38: 'Vung Tau', 39: 'Yen Bai'}

# Định nghĩa ánh xạ từ mã số sang tên tỉnh và hướng gió

wind_directions_dict = {
    0: 'ESE', 1: 'SE', 2: 'E', 3: 'WSW', 4: 'ENE', 5: 'SW', 6: 'SSE',
    7: 'SSW', 8: 'W', 9: 'NE', 10: 'NNE', 11: 'WNW', 12: 'NNW', 13: 'N'
}

# Tạo ánh xạ ngược từ tên về mã số
provinces_name_to_code = {v: k for k, v in provinces_dict.items()}
wind_directions_name_to_code = {v: k for k, v in wind_directions_dict.items()}

# Đọc và xử lý dữ liệu từ file
try:
    weather_df = pd.read_csv('Data/weather_filled_after.csv')

    # Lấy danh sách duy nhất cho province và wind_d
    unique_provinces_codes = sorted(weather_df['province'].unique().tolist())
    unique_wind_directions_codes = sorted(weather_df['wind_d'].unique().tolist())

    # Chuyển mã số thành tên để hiển thị trong Combobox
    unique_provinces_names = [provinces_dict[code] for code in unique_provinces_codes if code in provinces_dict]
    unique_wind_directions_names = [wind_directions_dict[code] for code in unique_wind_directions_codes if code in wind_directions_dict]

    # Widgets (sắp xếp 2 cột để tiết kiệm không gian)
    province_cb = ttk.Combobox(form_frame, values=unique_provinces_names, state="readonly", font=("Arial", 13), width=25)
    province_cb.current(0)  # Chọn tỉnh đầu tiên
    add_field("Tỉnh:", 0, 0, province_cb)

    max_temp = tk.Entry(form_frame, font=("Arial", 13), width=27)
    add_field("Nhiệt độ cao nhất (°C):", 1, 0, max_temp)

    min_temp = tk.Entry(form_frame, font=("Arial", 13), width=27)
    add_field("Nhiệt độ thấp nhất (°C):", 2, 0, min_temp)

    wind_speed = tk.Entry(form_frame, font=("Arial", 13), width=27)
    add_field("Tốc độ gió (km/h):", 3, 0, wind_speed)

    wind_cb = ttk.Combobox(form_frame, values=unique_wind_directions_names, state="readonly", font=("Arial", 13), width=25)
    wind_cb.current(0)  # Chọn hướng gió đầu tiên
    add_field("Hướng gió:", 0, 1, wind_cb)

    humidity = tk.Entry(form_frame, font=("Arial", 13), width=27)
    add_field("Độ ẩm (%):", 1, 1, humidity)

    cloud = tk.Entry(form_frame, font=("Arial", 13), width=27)
    add_field("Độ che phủ mây (%):", 2, 1, cloud)

    pressure = tk.Entry(form_frame, font=("Arial", 13), width=27)
    add_field("Áp suất (hPa):", 3, 1, pressure)

    # Widget lịch cho ngày
    cal = Calendar(form_frame, selectmode="day", year=2025, month=5, day=21, date_pattern="yyyy-mm-dd")
    cal.grid(row=4, column=1, columnspan=3, padx=10, pady=10, sticky="w")
    tk.Label(form_frame, text="Ngày:", font=("Arial", 13), bg="white", anchor="w", width=20).grid(row=4, column=0, padx=10, pady=10, sticky="e")

    # Nút dự đoán
    predict_btn = tk.Button(main_frame, text="🔍 Dự đoán", bg="#3498db", fg="white", font=("Arial", 14, "bold"), width=20)
    predict_btn.pack(pady=25)

    # Khung kết quả và chỉ số
    result_metrics_frame = tk.Frame(main_frame, bg="#ecf0f1", padx=20, pady=15)
    result_metrics_frame.pack(fill="x", padx=10, pady=10)

    # Tiêu đề kết quả
    result_title = tk.Label(result_metrics_frame, text="Kết quả dự đoán", font=("Arial", 14, "bold"), bg="#ecf0f1", fg="#2c3e50")
    result_title.pack(anchor="w", pady=(0, 10))

    # Khung cho kết quả dự đoán
    result_frame = tk.Frame(result_metrics_frame, bg="#ecf0f1")
    result_frame.pack(fill="x", pady=5)

    result_label = tk.Label(result_frame, text="Dự đoán lượng mưa: ", font=("Arial", 12), bg="#ecf0f1", fg="#2c3e50")
    result_label.pack(side="left", padx=5)

    # Khung cho các chỉ số mô hình
    metrics_frame = tk.Frame(result_metrics_frame, bg="#ecf0f1")
    metrics_frame.pack(fill="x", pady=10)

    # Nhãn cho các chỉ số mô hình
    mse_label = tk.Label(metrics_frame, text="Mean Squared Error (MSE): ", font=("Arial", 12), bg="#ecf0f1", fg="#2c3e50")
    mse_label.grid(row=0, column=0, padx=5, pady=2, sticky="w")
    mse_value = tk.Label(metrics_frame, text="N/A", font=("Arial", 12), bg="#ecf0f1", fg="#27ae60")
    mse_value.grid(row=0, column=1, padx=5, pady=2, sticky="w")

    r2_label = tk.Label(metrics_frame, text="R-squared (R²): ", font=("Arial", 12), bg="#ecf0f1", fg="#2c3e50")
    r2_label.grid(row=1, column=0, padx=5, pady=2, sticky="w")
    r2_value = tk.Label(metrics_frame, text="N/A", font=("Arial", 12), bg="#ecf0f1", fg="#27ae60")
    r2_value.grid(row=1, column=1, padx=5, pady=2, sticky="w")

    slope_label = tk.Label(metrics_frame, text="Slope (Coefficients): ", font=("Arial", 12), bg="#ecf0f1", fg="#2c3e50")
    slope_label.grid(row=2, column=0, padx=5, pady=2, sticky="w")
    slope_value = tk.Label(metrics_frame, text="N/A", font=("Arial", 12), bg="#ecf0f1", fg="#27ae60")
    slope_value.grid(row=2, column=1, padx=5, pady=2, sticky="w")

    intercept_label = tk.Label(metrics_frame, text="Intercept: ", font=("Arial", 12), bg="#ecf0f1", fg="#2c3e50")
    intercept_label.grid(row=3, column=0, padx=5, pady=2, sticky="w")
    intercept_value = tk.Label(metrics_frame, text="N/A", font=("Arial", 12), bg="#ecf0f1", fg="#27ae60")
    intercept_value.grid(row=3, column=1, padx=5, pady=2, sticky="w")

    # Chuẩn bị dữ liệu cho mô hình
    X = weather_df[['province', 'max', 'min', 'wind', 'wind_d', 'humidi', 'cloud', 'pressure', 'date']]
    y = weather_df['rain']

    # Chuẩn hóa dữ liệu
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    # Huấn luyện mô hình
    model = LinearRegression()
    model.fit(X_scaled, y)

    # Dự đoán trên tập huấn luyện để tính MSE và R²
    y_pred = model.predict(X_scaled)

    # Tính các chỉ số đánh giá
    mse = mean_squared_error(y, y_pred)
    r2 = r2_score(y, y_pred)
    coefficients = model.coef_  # Slope (hệ số hồi quy)
    intercept = model.intercept_  # Hệ số chặn

    # Hiển thị giá trị mặc định của các chỉ số
    mse_value.config(text=f"{mse:.4f}")
    r2_value.config(text=f"{r2:.4f}")
    slope_value.config(text=f"{', '.join([f'{coef:.4f}' for coef in coefficients])}")
    intercept_value.config(text=f"{intercept:.4f}")

except Exception as e:
    messagebox.showerror("Lỗi", f"Không thể đọc hoặc xử lý file dữ liệu: {e}")
    weather_df = pd.DataFrame()
    scaler = None
    model = None

# Hàm xử lý dữ liệu đầu vào
def preprocess_input():
    try:
        # Lấy dữ liệu từ các trường nhập liệu
        province_name = province_cb.get()
        max_temp_val = max_temp.get()
        min_temp_val = min_temp.get()
        wind_speed_val = wind_speed.get()
        wind_direction_name = wind_cb.get()
        humidity_val = humidity.get()
        cloud_val = cloud.get()
        pressure_val = pressure.get()
        date_str = cal.get_date()  # Lấy ngày từ widget lịch

        # Xác thực các trường số
        for val, name in [
            (max_temp_val, "Nhiệt độ cao nhất"),
            (min_temp_val, "Nhiệt độ thấp nhất"),
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

        # Ánh xạ tên tỉnh và hướng gió về mã số
        province = provinces_name_to_code.get(province_name, 0)
        wind_direction = wind_directions_name_to_code.get(wind_direction_name, 0)

        # Chuẩn hóa ngày
        try:
            base_date = datetime(2009, 1, 1)
            date_obj = datetime.strptime(date_str, "%Y-%m-%d")
            delta_days = (date_obj - base_date).days
        except ValueError:
            raise ValueError("Ngày không hợp lệ. Vui lòng chọn ngày hợp lệ từ lịch.")

        # Chuẩn bị dữ liệu đầu vào (không bao gồm date/delta_days)
        input_data = [
            province,
            max_temp_val,
            min_temp_val,
            wind_speed_val,
            wind_direction,
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

# Chạy giao diện
root.mainloop()