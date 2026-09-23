from ast import While


name = "Nguyễn Thọ Nguyên" 
age = 18
school = "Đại học Công Nghệ Bưu chính Viễn thông" 
print(f"Xin chào, tôi là {name}, năm nay {age} tuổi, học tại {school}.")
# tính diện tích và chu vi hình chữ nhật
length = 5
width = 3
area = length * width
perimeter = 2 * (length + width)
print(f"Diện tích hình chữ nhật là {area}, chu vi là {perimeter}.")
# chuyển đổi độ C sang độ F
celsius = 25
fahrenheit = (celsius * 9/5) + 32
print(f"{celsius} độ C tương ứng với {fahrenheit} độ F.")
# tính điểm trung bình của 3 môn học
math = 8.5
physics = 7.8
chemistry = 9.2
average = (math + physics + chemistry) / 3
print(f"Điểm trung bình của 3 môn học là {average}.")
# ghép chuỗi
name ="Nguyễn Thọ Nguyên" 
age = 18
print(f"Tôi tên là {name}, tôi {age} tuổi.")
print(f"Sang năm tôi sẽ {age + 1} tuổi.")
# kiểm tra số chẵn lẻ
number = 10
if number % 2 == 0:
    print(f"{number} là số chẵn.")
else:
    print(f"{number} là số lẻ.")
    # so sánh 2 số
a = 5
b = 10
if a > b:
    print(f"{a} lớn hơn {b}.")
elif a < b:
    print(f"{a} nhỏ hơn {b}.")
else:
    print(f"{a} bằng {b}.")
    # xếp loại học lực
average = 8.5
if average >= 8.0:
    print("Học lực giỏi.")
elif average >= 6.5 and average < 8.0:
    print("Học lực khá.")
elif average >= 5.0 and average < 6.5:
    print("Học lực trung bình.")
else: 
    print("Học lực yếu.")
    # tính tiền điện
electricity_usage = 100
if electricity_usage <= 50:
    cost = electricity_usage * 1800
elif electricity_usage <= 100:
    cost = 50 * 1800 + (electricity_usage - 50) * 2000
else:
    cost = 50 * 1800 + 50 * 2000 + (electricity_usage - 100) * 2500
print(f"Số tiền điện phải trả là {cost} đồng.")
# kiểm tra năm nhuận
year = 2020
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(f"{year} là năm nhuận.")
else:
    print(f"{year} không phải là năm nhuận.")
    # in bảng cửu chương
for i in range(1, 10):
    for j in range(1, 10):
        print(f"{i} x {j} = {i * j}")
    print()
    # tính tổng các số từ 1 đến n
n = 10
total = sum(range(1, n + 1))
print(f"Tổng các số từ 1 đến {n} là {total}.")
# đếm số chẵn trong dãy
count = 0
for i in range(1, n + 1):
    if i % 2 == 0:
        count += 1
print(f"Số lượng số chẵn từ 1 đến {n} là {count}.")
# đoán số bí mật
secret_number = 7
while True:
    try:
        guess = int(input("Hãy đoán số bí mật (từ 1 đến 10): "))
    except ValueError:
        print("Vui lòng nhập một số hợp lệ.")
        continue
    if guess < secret_number:
        print("Số bạn đoán nhỏ hơn số bí mật.")
    elif guess > secret_number:
        print("Số bạn đoán lớn hơn số bí mật.")
    else:
        print("Chúc mừng! Bạn đã đoán đúng số bí mật.")
        break
# vẽ tam giác *
n = 5
for i in range(1, n + 1):
    print(" " * (n - i) + "*" * (2 * i - 1))