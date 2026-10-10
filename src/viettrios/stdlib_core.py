# Standard Library v2 capped


def phuong_trinh_bac_nhat(a, b):
    if a == 0:
        raise ValueError("He so a khong duoc bang 0")
    return -b / a


def trung_binh(*numbers):
    return sum(numbers) / len(numbers) if numbers else 0


def max_value(*numbers):
    return max(numbers) if numbers else None


def min_value(*numbers):
    return min(numbers) if numbers else None
