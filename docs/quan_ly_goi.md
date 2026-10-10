import argparse
from pathlib import Path

from viettrios.bo_dich import chuyen_thanh_khong_dau
from viettrios.core import chay_ma
from viettrios.quan_ly_goi import danh_sach_goi, tao_goi, cai_dat_goi


def tao_tep_demo(duong_dan: Path) -> None:
    duong_dan.parent.mkdir(parents=True, exist_ok=True)
    duong_dan.write_text(
        'x = 10\n'
        'neu x > 5:\n'
        '    in ra "x lon hon 5"\n'
        'in ra "Xin chao, toi la Viet Trios!"\n',
        encoding='utf-8',
    )


def khoi_tao_du_an(ten: str) -> None:
    goc = Path(ten)
    goc.mkdir(parents=True, exist_ok=True)
    (goc / "src").mkdir(exist_ok=True)
    (goc / "tests").mkdir(exist_ok=True)
    (goc / "README.md").write_text(
        "# " + ten + "\n\n"
        "Day la du an Viet Trios moi.\n\n"
        "Cac lenh co ban:\n\n"
        "```text\n"
        "vtr chay app.vt\n"
        "```\n",
        encoding='utf-8',
    )
    (goc / "app.vt").write_text(
        'in ra "Xin chao tu ' + ten + '!"\n',
        encoding='utf-8',
    )
    print(f"Du an '{ten}' da duoc khoi tao.")


def xu_ly_goi(gia_tri):
    if gia_tri is None:
        print("Danh sach goi:")
        for ten, phien_ban in danh_sach_goi():
            print(f"- {ten}: {phien_ban}")
        return

    if gia_tri == "danh_sach":
        for ten, phien_ban in danh_sach_goi():
            print(f"- {ten}: {phien_ban}")
        return

    if gia_tri == "tao":
        ten = input("Ten goi: ").strip()
        phien_ban = input("Phien ban: ").strip() or "0.1.0"
        print(tao_goi(ten, phien_ban))
        return

    if gia_tri == "cai_dat":
        ten = input("Ten goi can cai dat: ").strip()
        print(cai_dat_goi(ten))
        return

    print(f"Lenh goi khong ho tro: {gia_tri}")


def main() -> None:
    parser = argparse.ArgumentParser(description="Viet Trios CLI")
    subparser = parser.add_subparsers(dest="lenh")

    chay_parser = subparser.add_parser("chay", help="Chay tep Viet Trios")
    chay_parser.add_argument("duong_dan", help="Duong dan den tep .vt")

    demo_parser = subparser.add_parser("demo", help="Chay demo co ban")

    khoi_tao_parser = subparser.add_parser("khoi_tao", help="Khoi tao du an moi")
    khoi_tao_parser.add_argument("ten", help="Ten du an")

    bo_dich_parser = subparser.add_parser("bo_dich", help="Chuyen doi chuoi sang tieng Viet khong dau")
    bo_dich_parser.add_argument("van_ban", help="Van ban dau vao")

    goi_parser = subparser.add_parser("goi", help="Quan ly goi trong Viet Trios")
    goi_parser.add_argument("hanh_dong", nargs="?", default=None, help="danh_sach | tao | cai_dat")

    args = parser.parse_args()

    if args.lenh in ("chay", "run"):
        tep = Path(args.duong_dan)
        if not tep.exists():
            raise FileNotFoundError(f"Tep khong ton tai: {tep}")
        nguon = tep.read_text(encoding='utf-8')
        print(chay_ma(nguon))
        return

    if args.lenh in ("demo", "show_demo"):
        tep_demo = Path("examples/demo.vt")
        tao_tep_demo(tep_demo)
        nguon = tep_demo.read_text(encoding='utf-8')
        print(chay_ma(nguon))
        return

    if args.lenh in ("khoi_tao", "init"):
        khoi_tao_du_an(args.ten)
        return

    if args.lenh == "bo_dich":
        print(chuyen_thanh_khong_dau(args.van_ban))
        return

    if args.lenh == "goi":
        xu_ly_goi(args.hanh_dong)
        return

    parser.print_help()


if __name__ == "__main__":
    main()
