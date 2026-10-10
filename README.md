# Viết Trios

Viết Trios là một hệ sinh thái lập trình theo phong cách Python, nhưng được viết bằng tiếng Việt không dấu để phù hợp với cách diễn đạt, cách học và cách phát triển của người Việt. Dự án này không chỉ là một ngôn ngữ mô phỏng Python đơn thuần, mà còn là một ecosystem mở rộng, tích hợp được nhiều thành phần: ngôn ngữ, CLI, thư viện, mô hình quản lý gói, demo, tài liệu và phát triển cộng đồng.

## Tổng quan

- Ngôn ngữ script theo hướng Python
- Có tập hợp lệnh, biến, hàm, vòng lặp, đối tượng và lớp theo tiếng Việt không dấu
- Hỗ trợ xử lý dữ liệu, CLI, bot, API, ứng dụng nhiều lớp và hệ thống mô phỏng ecosystem
- Có khung dự án và mô hình phát triển để bắt đầu nhanh
- Có khả năng mở rộng thành một môi trường lập trình tiếng Việt chuẩn cho cộng đồng

## Tính năng chính

- Hệ thống CLI: `vtr`
- Chạy file `.vt` theo phong cách Python-like
- Hỗ trợ biến, phép toán, điều kiện, danh sách, từ điển, vòng lặp, hàm và lớp
- Quản lý gói và package manager cơ bản
- Chuyển đổi văn bản sang tiếng Việt không dấu
- Thư viện chuẩn và ví dụ mẫu
- Hỗ trợ demo, kiểm thử và mở rộng hệ sinh thái

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
|-- examples/
|   |-- hello.vt
|   |-- ham.vt
|   |-- lop.vt
|   |-- goi.vt
|-- tests/
|   |-- test_core.py
|-- docs/
|   |-- huong_dan.md
|   |-- cau_truc_du_an.md
|   |-- quan_ly_goi.md
|   |-- thu_vien_chuan.md
|   |-- roadmap.md
```

## Mục tiêu dự án

Mục tiêu của Viết Trios là tạo ra một hệ sinh thái lập trình tiếng Việt sẵn sàng cho:

- Học tập và giảng dạy
- Phát triển môi trường script
- Xây dựng ứng dụng nhiều lớp
- Phát triển tool và CLI nhanh
- Quản lý gói và module mở rộng
- Mở rộng thành ecosystem lập trình Việt Nam chuẩn hóa
- Tích hợp cộng đồng và các thành phần phụ trợ cho phát triển thực tế

## Giấy phép

MIT
