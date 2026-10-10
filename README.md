# Viet Trios

Viet Trios la mot he sinh thai lap trinh theo phong cach Python, nhung duoc viet bang tieng Viet khong dau va mo rong thanh mot ecosystem chuan. Du an nay da dua vao cac tinh nang cho muc 2 va muc 4: engine chay ngon ngu co ban va phan web api de ket noi he thong.

## Muc tieu phat trien

- Muc 2: nguyen tac ngon ngu lap trinh thuc su
- Muc 4: giao dien API va web cho ecosystem

## Tinh nang moi

- Engine chay tuong thich voi ma Viet Trios
- Api http co the chay ma va tra ve ket qua
- Trang demo web don gian
- Ho tro phan tich ket qua va hen tro duoc mo rong

## Su dung nhanh

```bash
python -m viettrios
```

## Api demo

```bash
python -m viettrios.api
```

Sau do truy cap:

- http://localhost:8000/ping
- http://localhost:8000/run?script=in%20ra%20%22xin%20chao%22

## Giao dien demo

```python
from viettrios.web import tao_trang_chao
print(tao_trang_chao())
```

## Ket luan

Viet Trios da co the duoc mo rong thanh mot nang luc phat trien day du, tu mo hinh ngon ngu den api va he thong web.
