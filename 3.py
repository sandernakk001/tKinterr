import tkinter as tk

# Loome peakna
aken = tk.Tk()
aken.title("Maja")
aken.resizable(False, False)

# Lõuendi mõõtmed
laius = 600
korgus = 500
louend = tk.Canvas(aken, width=laius, height=korgus, bg="white")
louend.pack()

# --- 1. KORSTEN JA SUITS ---
# Korstnasuits (tsükliga erineva suurusega ringid)
suitsu_raadiused = [8, 12, 16, 22]
suitsu_x = [415, 425, 440, 460]
suitsu_y = [110, 85, 60, 35]

for r, sx, sy in zip(suitsu_raadiused, suitsu_x, suitsu_y):
    louend.create_oval(
        sx - r, sy - r, sx + r, sy + r,
        fill="#E0E0E0", outline="#CCCCCC"
    )

# Korsten
louend.create_rectangle(390, 120, 430, 200, fill="#A52A2A", outline="black", width=2)
# Korstna äär/krae
louend.create_rectangle(385, 115, 435, 125, fill="#7A1E1E", outline="black", width=2)

# --- 2. MAJA SEINAD JA KATUS ---
# Maja kere / seinad (kollane)
louend.create_rectangle(120, 240, 480, 440, fill="#FCE883", outline="black", width=2)

# Katus (pruun kolmnurk)
louend.create_polygon(90, 240, 300, 120, 510, 240, fill="#8B4513", outline="black", width=2)

# Katuse räästas / dekoratiivne ots
louend.create_polygon(100, 240, 300, 130, 500, 240, fill="#A0522D", outline="", width=0)

# --- 3. UKS JA TREPP ---
# Trepiastmed
louend.create_rectangle(260, 440, 340, 448, fill="#808080", outline="black")
louend.create_rectangle(250, 448, 350, 455, fill="#696969", outline="black")

# Uks (pruun)
louend.create_rectangle(270, 320, 330, 440, fill="#5C4033", outline="black", width=2)

# Ukse aken (kaarikujuline)
louend.create_arc(280, 330, 320, 370, start=0, extent=180, fill="#ADD8E6", outline="black", width=2)

# Ukse link
louend.create_oval(318, 383, 324, 389, fill="gold", outline="black")

# --- 4. AKNAD (TSÜKLIGA) ---
# Joonistame 4 akent (2 vasakul pool ust, 2 paremal pool ust)
aken_laius = 60
aken_korgus = 60

# Akende ülemiste vasakute nurkade (x, y) koordinaadid
akende_positsioonid = [
    (150, 270),  # Vasak ülemine
    (150, 350),  # Vasak alumine
    (390, 270),  # Parem ülemine
    (390, 350)   # Parem alumine
]

for ax, ay in akende_positsioonid:
    # Akna klaas (helesinine)
    louend.create_rectangle(
        ax, ay, ax + aken_laius, ay + aken_korgus,
        fill="#E0F7FA", outline="#006064", width=2
    )
    # Akna sisemised raamid (rist)
    louend.create_line(ax + aken_laius / 2, ay, ax + aken_laius / 2, ay + aken_korgus, fill="#006064", width=2)
    louend.create_line(ax, ay + aken_korgus / 3, ax + aken_laius, ay + aken_korgus / 3, fill="#006064", width=2)

# Katuse alune pööninguaken (ümar)
louend.create_oval(275, 160, 325, 210, fill="#E0F7FA", outline="black", width=2)
louend.create_line(300, 160, 300, 210, fill="black", width=2)
louend.create_line(275, 185, 325, 185, fill="black", width=2)

# Maja alune maapind
louend.create_line(0, 455, laius, 455, fill="#4D7C0F", width=4)

# Käivitame akna
aken.mainloop()