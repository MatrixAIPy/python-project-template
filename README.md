# python-project-template

## Quick Start

Żeby przygotować środowisko do pracy i zainstalować zależności, odpal skrypt:
bash scripts/create_venv.sh

## Narzędzia

Skrypty odpalamy z poziomu głównego katalogu.
bash scripts/format_check.sh - weryfikuje formatowanie kodu (Black)
bash scripts/lint.sh - uruchamia analizę statyczną (Pylint)
bash scripts/test.sh - odpala testy jednostkowe w Pyteście
bash scripts/clean.sh - usuwa środowisko wirtualne i pliki tymczasowe

## CI Pipeline
Repozytorium korzysta z GitHub Actions. Przy każdym Pushu i Pull Request do głównych gałęzi uruchamiany jest pipeline, który instaluje zależności, sprawdza formatowanie, weryfikuje kod Pylintem oraz uruchamia testy jednostkowe.