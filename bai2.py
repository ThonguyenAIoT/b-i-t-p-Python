#1 đếm ký tự và chiều dài chuỗi
a = input("Nhập chuỗi: ")
print("Chiều dài chuỗi là: ", len(a))
ky_tu = input("Nhập ký tự cần đếm: ")
print("Số lần ký tự '{}' xuất hiện trong chuỗi là: {}".format(ky_tu, a.count(ky_tu)))

#2 kiểm tra chuỗi đối xứng
b = input("Nhập chuỗi: ")
if b == b[::-1]:
    print("Chuỗi '{}' là chuỗi đối xứng.".format(b))
else:
    print("Chuỗi '{}' không phải là chuỗi đối xứng.".format(b))

#3 đếm nguyên âm và phụ âm trong chuỗi
c = input("Nhập chuỗi: ")
nguyen_am = "aeiouAEIOU"
so_nguyen_am = 0
so_phu_am = 0

for char in c:
    if char in nguyen_am:
        so_nguyen_am += 1
    elif char.isalpha():
        so_phu_am += 1

print("Số lượng nguyên âm:", so_nguyen_am)
print("Số lượng phụ âm:", so_phu_am)

#4 Viết hoa chữ cái đầu tiên của mỗi từ trong chuỗi
d = input("Nhập chuỗi: ")
print("Chuỗi sau khi viết hoa chữ cái đầu tiên của mỗi từ:", d.title())

#5 Thay thế từ trong chuỗi
e = input("Nhập chuỗi: ")
tu_cu = input("Nhập từ cần thay thế: ")
tu_moi = input("Nhập từ mới: ")
print("Chuỗi sau khi thay thế:", e.replace(tu_cu, tu_moi))

#6 Tách câu thành danh sách và nối lại

f = input("Nhập câu: ")
danh_sach = f.split()
print("Danh sách các từ:", danh_sach)
print("Câu sau khi nối lại:", " ".join(danh_sach))

#7  đếm số từ trong chuỗi
g = input("Nhập chuỗi: ")
print("Số lượng từ trong chuỗi là:", len(g.split()))

#8 tổng,trung bình và giá trị lớn nhất của chuỗi số
h = input("Nhập chuỗi số (cách nhau bởi dấu cách): ")
so_list = [float(x) for x in h.split()]
print("Tổng:", sum(so_list))
print("Trung bình:", sum(so_list) / len(so_list))
print("Giá trị lớn nhất:", max(so_list))

#9 Loại bỏ phần tử trùng lặp trong chuỗi
i = input("Nhập chuỗi: ")
print("Chuỗi sau khi loại bỏ phần tử trùng lặp:", "".join(dict.fromkeys(i)))

#10 Đảo ngược chuỗi
j = input("Nhập chuỗi: ")
print("Chuỗi sau khi đảo ngược:", j[::-1])

#11 tính tổng các phần tử chẵn
k = input("Nhập chuỗi số: ")
so_list = [int(x) for x in k.split()]
tong_chan = sum(x for x in so_list if x % 2 == 0)
print("Tổng các phần tử chẵn:", tong_chan)

#12 tìm phần tử xuất hiện nhiều nhất trong chuỗi
l = input("Nhập chuỗi: ")
max_char = max(l, key=l.count)
print("Phần tử xuất hiện nhiều nhất trong chuỗi là:", max_char)

#13 gộp 2 danh sách thành 1 danh sách mới
m1 = input("Nhập danh sách 1 (cách nhau bởi dấu cách): ")
m2 = input("Nhập danh sách 2 (cách nhau bởi dấu cách): ")
list1 = m1.split()
list2 = m2.split()
list_moi = list1 + list2
print("Danh sách mới sau khi gộp:", list_moi)