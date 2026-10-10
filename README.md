# Viet Trios

Viet Trios la mot he sinh thai lap trinh theo phong cach Python ma duoc viet bang tieng Viet khong dau. Dung de hoc tap, giang day, demo sang tao va mo rong thanh mot ecosystem phat trien chuan.

## Tong quan

- Ngon ngu script theo huong Python
- Co tap hop lenh, bien, ham, vong lap va lop theo tieng Viet khong dau
- Ho tro xu ly du lieu, CLI, API, bot va ung dung nhieu lop
- Co khung du an va mo hinh phat trien de bat dau nhanh
- Co the mo rong thanh mot he sinh thai lap trinh cho nguoi Viet

## Tinh nang chinh

- Hieu thuc CLI: `vtr`
- Chay file `.vt` theo phong cach Python-like
- Ho tro bien, so sanh, danh sach, tu dien, dieu kien, vong lap, ham va lop
- Khoi tao du an moi bang lenh `vtr khoi_tao`
- Ho tro demo, kiem thu va phat trien mo hinh ecosystem

## Cai dat

```bash
python -m venv .venv
source .venv/bin/activate
pip install -e .
```

## Su dung

```bash
vtr demo
vtr chay examples/hello.vt
vtr khoi_tao my_app
```

## Mau script

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

## Cau truc thu muc

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
|   |-- ham.vt
|   |-- lop.vt
|-- tests/
|   |-- test_core.py
|-- docs/
|   |-- huong_dan.md
|   |-- cau_truc_du_an.md
|   |-- roadmap.md
```

## Muc tieu du an

Muc tieu cua Viet Trios la tao ra mot he sinh thai lap trinh tieng Viet san sang cho:

- Hoc tap va giang day
- Phat trien moi truong script
- Xay dung ung dung nhieu lop
- Phat trien tool va CLI nhanh
- Tang cuong ecosystem cho cac phat trien vien viet
- Mo rong thanh mot nguon mo cho cong dong

## Giay phep

MIT
