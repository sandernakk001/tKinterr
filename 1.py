import tkinter as tk

# Loome peakna
aken = tk.Tk()
aken.title("Lipp")
aken.resizable(False, False)

# Lõuendi mõõtmed (lipp vahekorras 7:11)
laius = 660
korgus = 420
louend = tk.Canvas(aken, width=laius, height=korgus, bg="white")
louend.pack()

# --- 1. LIPU TRIIPUDE JOONISTAMINE TSÜKLIGA ---
# Tartu lipul on 6 võrdse laiusega triipu: valge, sinine, valge, sinine, valge, sinine
triibu_korgus = korgus / 6
sinine_varv = "#00529B"  # Tartu sinine

for i in range(6):
    y1 = i * triibu_korgus
    y2 = (i + 1) * triibu_korgus
    # Paaritu indeksiga (1, 3, 5) lauad on sinised, paarisindeksiga (0, 2, 4) valged
    varv = sinine_varv if i % 2 != 0 else "white"
    louend.create_rectangle(0, y1, laius, y2, fill=varv, outline=varv)

# --- 2. TARTU VAPI JOONISTAMINE LIPU KESKELE ---
# Vapi tsenter ja mõõtmed
cx, cy = laius / 2, korgus / 2
vw, vh = 130, 160  # Vapi kilbi laius ja kõrgus
vx1, vy1 = cx - vw / 2, cy - vh / 2
vx2, vy2 = cx + vw / 2, cy + vh / 2

# Vapi kilbi taust (punane)
punane_varv = "#D71920"
louend.create_rectangle(vx1, vy1, vx2, vy2, fill=punane_varv, outline="black", width=2)

# Hall müür ja tornid
hall_varv = "#D9D9D9"

# Alumine linnusemüür koos avatud väravaga
louend.create_rectangle(vx1 + 10, cy + 10, vx2 - 10, vy2 - 5, fill=hall_varv, outline="black", width=2)
# Avatud väravaava (kaared ja ava)
louend.create_rectangle(cx - 15, cy + 35, cx + 15, vy2 - 5, fill="black", outline="black")
louend.create_arc(cx - 15, cy + 20, cx + 15, cy + 50, start=0, extent=180, fill="black", outline="black")

# Tsükliga müüri sakid müüri ülaservas
sakke = 5
saki_laius = (vw - 20) / (2 * sakke - 1)
for i in range(sakke):
    sx1 = (vx1 + 10) + i * 2 * saki_laius
    sx2 = sx1 + saki_laius
    louend.create_rectangle(sx1, cy, sx2, cy + 10, fill=hall_varv, outline="black")

# Kaks külgmist torni
for tx in [vx1 + 15, vx2 - 35]:
    # Torni kere
    louend.create_rectangle(tx, vy1 + 25, tx + 20, cy, fill=hall_varv, outline="black", width=2)
    # Torni katus (kolmnurk)
    louend.create_polygon(tx - 3, vy1 + 25, tx + 10, vy1 + 5, tx + 23, vy1 + 25, fill=punane_varv, outline="black", width=2)

# Keskne element: Ristatavad võti ja mõõk (hõbedased/kuldse detailiga)
# Mõõk (diagonaal vasakult alt paremale üles)
louend.create_line(cx - 25, cy + 5, cx + 25, cy - 35, fill="white", width=4)
louend.create_line(cx - 25, cy + 5, cx - 18, cy + 12, fill="gold", width=5) # käepide

# Võti (diagonaal paremalt alt vasakule üles)
louend.create_line(cx + 25, cy + 5, cx - 25, cy - 35, fill="gold", width=4)
# Võtme pea (tsükliline/ümargune)
louend.create_oval(cx + 20, cy, cx + 30, cy + 10, outline="gold", width=3)

# Rist tornide vahel müüri kohal
louend.create_line(cx, cy - 25, cx, cy - 5, fill="gold", width=3)
louend.create_line(cx - 7, cy - 18, cx + 7, cy - 18, fill="gold", width=3)

# Lipu välispiirjoon korrektsuse tagamiseks
louend.create_rectangle(0, 0, laius, korgus, outline="black", width=2)

# Käivitame akna
aken.mainloop()