# Viết Trios

Viết Trios là một hệ sinh thái lập trình theo phong cách Python, nhưng được viết bằng tiếng Việt không dấu và có thể mở rộng thành một môi trường phát triển chuẩn cho nhiều ứng dụng.

## Tổng quan

- Ngôn ngữ script theo hướng Python
- Có phần tập hợp lệnh tiếng Việt không dấu
- Dùng được cho xử lý dữ liệu, CLI, bot, API và ứng dụng nhiều lớp
- Có khung dự án và phần mềm để bắt đầu nhanh

## Tính năng chính

- Hệ thống CLI: `vtr`
- Chạy script `.vt` theo phối cảnh Python-like
- Mở rộng được qua module và package
- Khởi tạo dự án mới bằng lệnh `vtr khoi tao`
- Hỗ trợ test và demo

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
vtr khoi tao my_app
```

## Mẫu script

```text
x = 7
neu x > 5:
    in ra "x lon hon 5"
```

## Các thư mục

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

## Giấy phép

MIT
