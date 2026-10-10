# Viet Trios

Viet Trios la mot he sinh thai lap trinh theo phong cach Python, nhung duoc viet theo tieng Viet khong dau va co the mo rong thanh mot moi truong phat trien chuan cho nhieu ung dung.

## Tong quan

- Ngon ngu script theo huong Python
- Co phan tap hop lenh tieng Viet khong dau
- Dung duoc cho xu ly du lieu, CLI, bot, API va ung dung nhieu lop
- Co khung du an va phan mem de bat dau nhanh

## Tinh nang chinh

- He thong CLI: `vtr`
- Chay script `.vt` theo phoi canh Python-like
- Mo rong duoc qua module va package
- Khoi tao du an moi bang lenh `vtr init`
- Ho tro test va demo

## Cai dat

```bash
python -m venv .venv
source .venv/bin/activate
pip install -e .
```

## Su dung

```bash
vtr demo
vtr run examples/hello.vt
vtr init my_app
```

## Mau script

```text
x = 7
neu x > 5:
    in ra "x lon hon 5"
```

## Cac thu muc

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

## Muc tieu du an

Muc tieu cua Viet Trios la tao ra mot he sinh thai lap trinh tieng Viet san sang cho:

- hoc tap va giang day
- phat trien moi truong script
- xay dung ung dung nhieu lop
- phat trien tool va CLI nhanh

## Giay phep

MIT
