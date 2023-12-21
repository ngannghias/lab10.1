#10.1
class Student:
    def __init__(self, ten, diem_toan, diem_ly, diem_hoa):
        self.ten = ten
        self.diem_toan = diem_toan
        self.diem_ly = diem_ly
        self.diem_hoa = diem_hoa

    def print_diemtk(self):
        diem_tk = round((self.diem_toan + self.diem_ly + self.diem_hoa) / 3, 2)
        print(f"Tên: {self.ten}")
        print(f"Điểm Toán: {self.diem_toan}")
        print(f"Điểm Lý: {self.diem_ly}")
        print(f"Điểm Hóa: {self.diem_hoa}")
        print(f"Điểm Tổng Kết: {diem_tk}")

# Sử dụng class Student
ten_sv = input("Nhập tên sinh viên: ")
diem_toan_sv = float(input("Nhập điểm Toán: "))
diem_ly_sv = float(input("Nhập điểm Lý: "))
diem_hoa_sv = float(input("Nhập điểm Hóa: "))

sinh_vien = Student(ten_sv, diem_toan_sv, diem_ly_sv, diem_hoa_sv)
sinh_vien.print_diemtk()