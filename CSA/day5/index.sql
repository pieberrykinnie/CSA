CREATE TABLE HocSinh (
  MaHocSinh VARCHAR(10),
  HoTen VARCHAR(50),
  DiaChi VARCHAR(100),
  NgaySinh DATE,
  GioiTinh VARCHAR(10),
  Lop VARCHAR(10)
);

ALTER TABLE HocSinh
ADD Truong VARCHAR(50),
REMOVE Lop
