# Viết Trios

Viết Trios là một hệ sinh thái lập trình theo phong cách Python, nhưng được viết bằng tiếng Việt không dấu. Dự án này mang mục tiêu xây dựng một ngôn ngữ mô phỏng việc lập trình theo kiểu Python, nhưng thân thiện với người Việt, dễ học và dễ mở rộng.

## Tổng quan

- Ngôn ngữ script theo hướng Python
- Có tập hợp lệnh và cấu trúc tiếng Việt không dấu
- Hỗ trợ xử lý dữ liệu, giao diện dòng lệnh, bot, API và ứng dụng nhiều lớp
- Có khung dự án và mô hình phát triển chuẩn để bắt đầu nhanh

## Tính năng chính

- Hệ thống CLI: `vtr`
- Chạy file `.vt` theo phong cách Python-like
- Mở rộng qua module và package
- Khởi tạo dự án mới bằng lệnh `vtr khoi_tao`
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
```

## Mẫu script

```text
x = 7
neu x > 5:
    in ra "x lon hon 5"
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
|-- examples/
|   |-- hello.vt
|-- tests/
|   |-- test_core.py
|-- docs/
|   |-- roadmap.md
```

## Mục tiêu dự án

Mục tiêu của Viết Trios là tạo ra một hệ sinh thái lập trình tiếng Việt sẵn sàng cho:

- Học tập và giảng dạy
- Phát triển môi trường script
- Xây dựng ứng dụng nhiều lớp
- Phát triển tool và CLI nhanh
- Mở rộng thành ecosystem lập trình Việt Nam chuẩn hóa

## Giấy phép

MIT
