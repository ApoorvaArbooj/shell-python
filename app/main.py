import sys

def main():
    while True:
        sys.stdout.write("$ ")
        args = input().split(" ")
        if len(args) == 0:
            continue
        else:
            command, *params = args
            if command == "exit":
                return 0
            print(f"{command}: command not found")
if __name__ == "__main__":
    main()