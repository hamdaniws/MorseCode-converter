import time
import threading

def konversi(teks, morse_map, hasil_list, label):
    for karakter in teks:
        if karakter != ' ':
            morse_code = morse_map.get(karakter, '?') # format angka/spec. char tidak didukung dan diganti dengan "?"
            print(f"{label}:{morse_code}", end=" ", flush=True)
            hasil_list.append(morse_code)
        else:
            print(f"{label}:/", end=" ", flush=True)
            hasil_list.append(' ')
        
        time.sleep(1)


def morse():
    # konversi morse dengan dictionary
    morse_map = {
        'a': ".-", 'b': "-...", 'c': "-.-.", 'd': "-..", 'e': ".",
        'f': "..-.", 'g': "--.", 'h': "....", 'i': "..", 'j': ".---",
        'k': "-.-", 'l': ".-..", 'm': "--", 'n': "-.", 'o': "---",
        'p': ".--.", 'q': "--.-", 'r': ".-.", 's': "...", 't': "-",
        'u': "..-", 'v': "...-", 'w': ".--", 'x': "-..-", 'y': "-.--", 'z': "--.."
    }

    teks1 = input("Teks 1: ").lower() #biar huruf kecil semua
    teks2 = input("Teks 2: ").lower()

    hasil1 = []
    hasil2 = []

    print("\nProses konversi:")

    t1 = threading.Thread(target=konversi, args=(teks1, morse_map, hasil1, "T1")) #argumen buat milih teks mana yang dijadiin thread
    t2 = threading.Thread(target=konversi, args=(teks2, morse_map, hasil2, "T2"))

    t1.start()
    time.sleep(1)  # delay 1 detik
    t2.start()

    t1.join()
    t2.join()

    # output
    hasil_konversi1 = ' '.join(hasil1)
    hasil_konversi2 = ' '.join(hasil2)

    print("\nHasil akhir:")
    print("Teks 1:", hasil_konversi1)
    print("Teks 2:", hasil_konversi2)
    print(f"\n{hasil_konversi1}/{hasil_konversi2} ({teks1} {teks2})")


morse()