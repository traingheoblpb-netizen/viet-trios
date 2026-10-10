# Viet Trios

Viet Trios la mot he sinh thai lap trinh theo phong cach Python, nhung duoc viet bang tieng Viet khong dau va phat trien theo mo hinh ecosystem. Dung de hoc tap, giang day, demo, phat trien ung dung, va xay dung mot python-like runtime co the mo rong de tro thanh mot ngon ngu lap trinh cho nguoi Viet.

## Tong quan

- Ngon ngu script theo huong Python
- Co tap hop lenh, bien, ham, vong lap, danh sach, tu dien va lop
- Hỗ trợ CLI, package manager, bo dich, thu vien chuan va demo
- Dung cho hoc tap, giang day, phat trien, API, bot va ung dung nhieu lop
- Mở rộng thành một he sinh thai chuan cho cong dong Viet Nam

## Tinh nang chinh

- Hệ thống CLI: `vtr`
- Chạy file `.vt` theo phong cách Python-like
- Hỗ trợ biến, phép toán, so sánh, điều kiện, vòng lặp, hàm và lớp
- Quản lý gói và package manager cơ bản
- Chuyển đổi văn bản sang tiếng Việt không dấu
- Thư viện chuẩn và ví dụ mẫu
- Demo, kiểm thử và mô hình ecosystem

## Cài đặt

```bash
python -m venv .venv
source .venv/bin/activate
pip install -e .
```

## Sử dụng

```bash
vtr demo
vtr chay examples/hello.vt
vtr khoi_tao my_app
vtr goi danh_sach
vtr bo_dich "Xin chao Viet Nam"
```

## Mẫu script

```text
x = 7
neu x > 5:
    in ra "x lon hon 5"

lap so trong [1, 2, 3]:
    in ra so

ham tong(a, b):
    tra_ve a + b

in ra tong(2, 3)
```

## Cấu trúc thư mục

```text
.
|-- README.md
|-- pyproject.toml
|-- src/
|   |-- viettrios/
|   |   |-- __init__.py
|   |   |-- __main__.py
|   |   |-- cli.py
|   |   |-- core.py
|   |   |-- runtime.py
|   |   |-- thu_vien.py
|   |   |-- quan_ly_goi.py
|   |   |-- bo_dich.py
|   |   |-- ho_tro.py
|-- examples/
|   |-- hello.vt
|   |-- ham.vt
|   |-- lop.vt
|   |-- goi.vt
|-- tests/
|   |-- test_core.py
|   |-- test_stdlib.py
|-- docs/
|   |-- huong_dan.md
|   |-- cau_truc_du_an.md
|   |-- quan_ly_goi.md
|   |-- thu_vien_chuan.md
|   |-- roadmap.md
```

## Mục tiêu dự án

Mục tiêu của Viet Trios là tạo ra một he sinh thai lap trinh tieng Viet san sang cho:

- Hoc tap va giang day
- Phat trien moi truong script
- Xay dung ung dung nhieu lop
- Phat trien tool va CLI nhanh
- Quan ly goi, module va resource
- Mo rong thanh mot ecosystem chuan cho cong dong
- Tich hop phat trien AI, du lieu va cong nghe moi

## Giay phep

MIT
