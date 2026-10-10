# Viet Trios Runtime - Hướng A

Viet Trios da duoc nang cap theo huong A: runtime va ngon ngu lap trinh chuyen nghiep. Day la pha nham to chuc lai he thong thanh mot runtime co cau truc ro rang, ho tro parser, compiler, bytecode, virtual machine va standard library chuan.

## Muc tieu

- Xay dung runtime chinh xac hon
- Chuẩn hóa code parser, compiler, VM
- Hỗ trợ API, web va toolchain
- Nâng cấp chất lượng cho cộng đồng phát triển

## Cấu trúc runtime

```text
src/viettrios/
|-- engine_v2.py
|-- parser.py
|-- compiler.py
|-- vm.py
|-- stdlib_toan_hoc.py
|-- stdlib_chuoi.py
|-- stdlib_tep.py
|-- stdlib_mang.py
|-- stdlib_du_lieu.py
|-- web_framework.py
|-- ide_support.py
|-- quan_ly_goi_v2.py
|-- cli_v2.py
```

## Thành phần chính

### Parser
- Phân tách token
- Hỗ trợ từ khoá, số, chuỗi, toán tử
- Chuẩn bị cho compile

### Compiler
- Chuyển token sang bytecode
- Chuẩn hóa instruction set

### Virtual Machine
- Thực thi bytecode
- Dùng stack để tính toán

### Standard Library
- Toán học
- Chuỗi
- File
- Mạng
- Dữ liệu

### Tooling
- CLI v2
- Package manager v2
- Web framework
- IDE support

## Ví dụ chạy mã

```python
from viettrios.engine_v2 import EngineVietTriosV2

engine = EngineVietTriosV2()
print(engine.chay('in_ra "Xin chao Viet Trios"'))
```

## Kết luận

Hướng A đã đưa Viet Trios sang giai đoạn runtime chuyên nghiệp hơn, sẵn sàng cho cộng đồng phát triển tiếp tục mở rộng.
