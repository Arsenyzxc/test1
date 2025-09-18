import argparse

def repl(vfs_name: str):
    """
    Минимальный REPL-цикл: приглашение, парсер, команды-заглушки.
    """
    while True:
        # приглашение вида [VFS]$
        line = input(f"[{vfs_name}]$ ").strip()

        if not line:
            continue

        parts = line.split()
        cmd = parts[0]
        args = parts[1:]

        # команды
        if cmd == "exit":
            print("Выход из эмулятора")
            break
        elif cmd in ("ls", "cd"):
            print(f"Вызвана команда: {cmd}, аргументы: {args}")
        else:
            print(f"Ошибка: неизвестная команда '{cmd}'")


def main():
    repl('VFS')


if __name__ == "__main__":
    main()
