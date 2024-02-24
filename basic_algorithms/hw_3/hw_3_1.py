import argparse
import shutil
from pathlib import Path


def parse_argv():
    parser = argparse.ArgumentParser("Images sort")
    parser.add_argument(
        "-S",
        "--source",
        type=Path, 
        required=True,
        help="Folder with pictures"
    )
    
    parser.add_argument(
        "-O",
        "--output",
        type=Path,
        default=Path("output"),
        help="Folder with sorted images",
    )
    return parser.parse_args()


def recursive_copy(src: Path, dst: Path):
    try:
        for item in src.iterdir():
            if item.is_dir():
                recursive_copy(item, dst)
            else:
                folder = dst / item.suffix[1:]  
                folder.mkdir(exist_ok=True, parents=True)
                shutil.copy2(item, folder)
    except shutil.Error:
        print("Some problem")


def main():
    args = parse_argv()
    print(f"Input args: {args}")
    recursive_copy(args.source, args.output)


if __name__ == "__main__":
    main()
