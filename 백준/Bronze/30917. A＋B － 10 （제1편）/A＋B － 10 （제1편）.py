import sys

def ask(var: str, x: int) -> int:
    print(f"? {var} {x}", flush=True)
    
    while True:
        s = sys.stdin.readline()
        if not s:
            sys.exit(0)
        s = s.strip()
        if s in ("0", "1"):
            return int(s)

def main():
    A = None
    B = None

    for x in range(1, 10):
        if ask("A", x) == 1:
            A = x
            break

    for x in range(1, 10):
        if ask("B", x) == 1:
            B = x
            break

    total = (A or 0) + (B or 0)
    print(f"! {total}", flush=True)

if __name__ == "__main__":
    main()