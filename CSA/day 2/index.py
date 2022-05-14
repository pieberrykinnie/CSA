from math import gcd

# Kiến thức:
# Các special method cơ bản
# Link: https://docs.python.org/3/reference/datamodel.html#special-method-names
# __str__: trả về chuỗi để in ra màn hình
# __init__: khởi tạo đối tượng
# __add__: cộng hai đối tượng
# __sub__: trừ hai đối tượng
# __mul__: nhân hai đối tượng
# __truediv__: chia hai đối tượng
# __floordiv__: chia hai đối tượng có thể làm tròn
# __mod__: chia hai đối tượng có thể làm tròn
# __pow__: lập bình phương
# __lt__: (lower than) < kiểm tra xem đối tượng này nhỏ hơn đối tượng khác
# __gt__: (greater than) > kiểm tra xem đối tượng này lớn hơn đối tượng khác
# __le__: (lower than or equal) <= kiểm tra xem đối tượng này nhỏ hơn hoặc bằng đối tượng khác
# __ge__: (greater than or equal) >= kiểm tra xem đối tượng này lớn hơn hoặc bằng đối tượng khác
# __eq__: (equal) == kiểm tra xem đối tượng này bằng đối tượng khác
# __ne__: (not equal) != kiểm tra xem đối tượng này không bằng đối tượng khác

# Bài tập trên lớp:
# Tạo một Class tên là Phân Số
# Giải thích:
#   - Class Phân Số có 2 thuộc tính: tử , mẫu
#   - Class Phân Số có các phép tính: +, -, *, /, ** (nhớ rút gọn phân số)
#   - Class Phân Số so sánh: <, >, <=, >=, ==, !=


class PhanSo:
    # __init__ là 1 phương thức khởi tạo
    def __init__(self, tu, mau):
        self.tu = tu
        self.mau = mau

    def rutgon(self):
        ucln = gcd(self.tu, self.mau)
        tu = int(self.tu / ucln)
        mau = int(self.mau / ucln)
        if mau < 0:
            tu *= -1
            mau *= -1
        return PhanSo(tu, mau)

    def __str__(self):
        return f"{self.tu}/{self.mau}"

    def __add__(self, other):
        tu = self.tu * other.mau + other.tu * self.mau
        mau = self.mau * other.mau
        return PhanSo(tu, mau).rutgon()

    def __sub__(self, other):
        tu = self.tu * other.mau - other.tu * self.mau
        mau = self.mau * other.mau
        return PhanSo(tu, mau).rutgon()

    def __mul__(self, other):
        tu = self.tu * other.tu
        mau = self.mau * other.mau
        return PhanSo(tu, mau).rutgon()

    def __truediv__(self, other):
        tu = self.tu * other.mau
        mau = self.mau * other.tu
        return PhanSo(tu, mau).rutgon()

    def __pow__(self, power, modulo=None):
        tu = self.tu ** power
        mau = self.mau ** power
        return PhanSo(tu, mau).rutgon()

    def __gt__(self, other):
        if self.tu * other.mau > other.tu * self.mau:
            return True
        else:
            return False

    def __lt__(self, other):
        if self.tu * other.mau < other.tu * self.mau:
            return True
        else:
            return False

    def __ge__(self, other):
        if self.tu * other.mau >= other.tu * self.mau:
            return True
        else:
            return False

    def __le__(self, other):
        if self.tu * other.mau <= other.tu * self.mau:
            return True
        else:
            return False

    def __eq__(self, other):
        if self.tu * other.mau == other.tu * self.mau:
            return True
        else:
            return False

    def __ne__(self, other):
        if self.tu * other.mau != other.tu * self.mau:
            return True
        else:
            return False


ps1 = PhanSo(5, 2)
ps2 = PhanSo(20, 25)
print(ps1 + ps2)
print(ps1 ** 2)
print(ps1 != ps2)
print(ps1 < ps2)
