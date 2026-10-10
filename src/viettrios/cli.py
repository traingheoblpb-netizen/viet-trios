import argparse
from pathlib import Path

from .core import run_code


def build_demo_file(path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        'x = 10\n'
        'neu x > 5:\n'
        '    in ra "x lon hon 5"\n'
        'in ra "Xin chao, toi la Viet Trios!"\n',
        encoding='utf-8',
    )


def init_project(name: str) -> None:
    root = Path(name)
    root.mkdir(parents=True, exist_ok=True)
    (root / "src").mkdir(exist_ok=True)
    (root / "tests").mkdir(exist_ok=True)
    (root / "README.md").write_text(
        "# " + name + "\n\n"
        "Day la du an Viet Trios moi.\n\n"
        "Cac lenh co ban:\n\n"
        "```text\n"
        "vtr run app.vt\n"
        "```\n",
        encoding='utf-8',
    )
    (root / "app.vt").write_text(
        'in ra "Xin chao tu ' + name + '!"\n',
        encoding='utf-8',
    )
    print(f"Project '{name}' da duoc khoi tao.")


def main() -> None:
    parser = argparse.ArgumentParser(description="Viet Trios CLI")
    subparsers = parser.add_subparsers(dest="command")

    run_parser = subparsers.add_parser("run", help="Chay file Viet Trios")
    run_parser.add_argument("path", help="Duong dan den file .vt")

    demo_parser = subparsers.add_parser("demo", help="Chay demo co ban")
    init_parser = subparsers.add_parser("init", help="Khoi tao du an moi")
    init_parser.add_argument("name", help="Ten du an")

    args = parser.parse_args()

    if args.command == "run":
        file_path = Path(args.path)
        if not file_path.exists():
            raise FileNotFoundError(f"File khong ton tai: {file_path}")
        source = file_path.read_text(encoding='utf-8')
        result = run_code(source)
        print(result)
        return

    if args.command == "demo":
        demo_path = Path("examples/demo.vt")
        build_demo_file(demo_path)
        source = demo_path.read_text(encoding='utf-8')
        print(run_code(source))
        return

    if args.command == "init":
        init_project(args.name)
        return

    parser.print_help()


if __name__ == "__main__":
    main()
