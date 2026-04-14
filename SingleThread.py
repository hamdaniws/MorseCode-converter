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

    # Dictionary mapping
    morse_map = {
        'a': a, 'b': b, 'c': c, 'd': d, 'e': e,
        'f': f, 'g': g, 'h': h, 'i': i, 'j': j,
        'k': k, 'l': l, 'm': m, 'n': n, 'o': o,
        'p': p, 'q': q, 'r': r, 's': s, 't': t,
        'u': u, 'v': v, 'w': w, 'x': x, 'y': y, 'z': z
    }

    # Terjemahan
    input_user = input("Masukkan karakter: ").lower()
    hasil = ' '.join(morse_map.get(karakter, '?') for karakter in input_user if karakter != ' ')
    print("hasil konversi: "+hasil)

morse()