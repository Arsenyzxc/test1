import argparse

def run_command(vfs_name, line):
    line = line.strip()
    if not line:
        return True

    parts = line.split()
    cmd = parts[0]
    args = parts[1:]

    if cmd == "exit":
        print("Выход из эмулятора")
        return False
    elif cmd in ("ls", "cd"):
        print(f"Вызвана команда: {cmd}, аргументы: {args}")
    else:
        print(f"Ошибка: неизвестная команда '{cmd}'")

    return True


def run_script(path, vfs_name):
    try:
        with open(path, encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue
                
                print(f"[{vfs_name}]$ {line}")
                if not run_command(vfs_name, line):
                    return False
    except Exception as e:             # тут отлавливаю ошибки: файла нет/нет прав на чтение/не та кодировка
        print(f"Ошибка исполнения скрипта: {e}")
    return True


def repl(vfs_name):
    while True:
        line = input(f"[{vfs_name}]$ ")
        if not run_command(vfs_name, line):
            break

# точка входа приложения
def main(): 
    parser = argparse.ArgumentParser()
    parser.add_argument("--vfs-path", help="Путь к VFS")
    parser.add_argument("--script", help="Путь к стартовому скрипту")
    args = parser.parse_args()

    print("Параметры запуска:")
    print("  vfs_path =", args.vfs_path)
    print("  script   =", args.script)

    if args.script:
        if not run_script(args.script, "VFS"):
            return

    repl("VFS")


if __name__ == "__main__":
    main()