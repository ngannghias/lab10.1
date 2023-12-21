class NhanVien:
    def __init__(self, ten, luong_co_ban, so_ngay_lam):
        self.ten = ten
        self.luong_co_ban = luong_co_ban
        self.so_ngay_lam = so_ngay_lam

    def tinh_luong(self):
        luong_thuc_nhan = round(self.luong_co_ban * self.so_ngay_lam / 30)
        return luong_thuc_nhan

    def hien_thi_luong(self):
        luong = self.tinh_luong()
        print(f"Lương của nhân viên {self.ten} trong tháng này là: {luong} đồng")