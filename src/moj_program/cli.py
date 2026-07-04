import argparse
from src.moj_program.logic import dodaj_liczby

def main():
    parser = argparse.ArgumentParser(description="Program do dodawania dwóch liczb.")
    parser.add_argument("a", type=int, help="Pierwsza liczba")
    parser.add_argument("b", type=int, help="Druga liczba")
    args = parser.parse_args()

    wynik = dodaj_liczby(args.a, args.b)
    print(f"Wynik: {wynik}")

if __name__ == "__main__":
    main()