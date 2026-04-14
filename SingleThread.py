import time

def morse():
    #define key
    a = ".-"
    b = "-..."
    c = "-.-."
    d = "-.."
    e = "."
    f = "..-."
    g = "--."
    h = "...."
    i = ".."
    j = ".---"
    k = "-.-"
    l = ".-.."
    m = "--"
    n = "-."
    o = "---"
    p = ".--."
    q = "--.-"
    r = ".-."
    s = "..."
    t = "-"
    u = "..-"
    v = "...-"
    w = ".--"
    x = "-..-"
    y = "-.--"
    z = "--.."

    # Dictionary key to convert as variable
    morse_map = {
        'a': a, 'b': b, 'c': c, 'd': d, 'e': e,
        'f': f, 'g': g, 'h': h, 'i': i, 'j': j,
        'k': k, 'l': l, 'm': m, 'n': n, 'o': o,
        'p': p, 'q': q, 'r': r, 's': s, 't': t,
        'u': u, 'v': v, 'w': w, 'x': x, 'y': y, 'z': z
    }

    teks1 = input("Teks 1: ").lower()
    teks2 = input("Teks 2: ").lower()

        
    # Process Teks1
    print("Teks 1: ", end="")
    
    teks1_morse_list = []
    for karakter in teks1:
        if karakter != ' ':
            morse_code = morse_map.get(karakter, '?')
            print(f"{morse_code} ", end="", flush=True)
            teks1_morse_list.append(morse_code)
            time.sleep(1)  # delay to show each printed character
        else:
            print("/", end="", flush=True) # space as '/'
            teks1_morse_list.append(' ')
            time.sleep(1)
    
    hasil_konversi = ' '.join(teks1_morse_list)
    
    # Process Teks2
    print("\nTeks 2: ", end="")
    
    teks2_morse_list = []
    for karakter in teks2:
        if karakter != ' ':
            morse_code = morse_map.get(karakter, '?')
            print(f"{morse_code} ", end="", flush=True)
            teks2_morse_list.append(morse_code)
            time.sleep(1)
        else:
            print("/", end="", flush=True)
            teks2_morse_list.append(' ')
            time.sleep(1)
    
    hasil_konversi2 = ' '.join(teks2_morse_list)
    
    # Output
    print(f"\n{hasil_konversi}/{hasil_konversi2} ({teks1} {teks2})")

morse()