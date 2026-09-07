# -*- coding: utf-8 -*-
import os
import shutil

# Ścieżky
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
UPDATE_DIR = os.path.join(BASE_DIR, "update")

print("=== SYSTEM AUTOMATYCZNEJ AKTUALIZACJI ===")

if not os.path.exists(UPDATE_DIR):
    print(f"[BŁĄD] Nie znaleziono folderu 'update' w katalogu głównym!")
    print(f"Utwórz folder 'update' i wrzuć do niego pliki do aktualizacji.")
    input("Naciśnij Enter, aby zakończyć...")
    exit()

# Sprawdź zawartość folderu update
files_to_update = os.listdir(UPDATE_DIR)
if not files_to_update:
    print(f"[INFO] Folder 'update' jest pusty. Brak plików do zaktualizowania.")
    input("Naciśnij Enter, aby zakończyć...")
    exit()

print(f"Znaleziono pliki do aktualizacji: {files_to_update}")
confirm = input("Czy chcesz przeprowadzić aktualizację? (t/n): ")

if confirm.lower() == 't':
    for filename in files_to_update:
        src_path = os.path.join(UPDATE_DIR, filename)
        dst_path = os.path.join(BASE_DIR, filename)
        
        if os.path.isfile(src_path):
            # Kopiuj plik nadpisując stary
            shutil.copy2(src_path, dst_path)
            print(f"[OK] Zaktualizowano plik: {filename}")
            
    print("\n[SUKCES] Aktualizacja zakończona pomyślnie!")
    print("Możesz teraz uruchomić ponownie serwer aplikacji.")
else:
    print("[ANULOWANO] Aktualizacja została przerwana.")

input("Naciśnij Enter, aby zamknąć okno...")