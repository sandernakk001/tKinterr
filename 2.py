import tkinter as tk
import math

# Loome peakna
aken = tk.Tk()
aken.title("Liiklusmärk")
aken.resizable(False, False)

# Lõuendi mõõtmed
laius = 500
korgus = 500
louend = tk.Canvas(aken, width=laius, height=korgus, bg="white")
louend.pack()

# Märgi keskkoht ja raadius
cx, cy = laius / 2, korgus / 2
marge_raadius = 200

# Sinine liiklusmärgi taustavärv
sinine_varv = "#00529B"

# --- 1. SININE RING KOOS VALGE VÄLISPIIRDEGA ---
# Valge välisjoon (ääris)
louend.create_oval(
    cx - marge_raadius - 5, cy - marge_raadius - 5,
    cx + marge_raadius + 5, cy + marge_raadius + 5,
    fill="white", outline="#CCCCCC", width=1
)

# Peamine sinine ketas
louend.create_oval(
    cx - marge_raadius, cy - marge_raadius,
    cx + marge_raadius, cy + marge_raadius,
    fill=sinine_varv, outline=sinine_varv
)

# --- 2. NOOLED TSÜKLIGA (RINGLIIKLUS - 3 NOOLT) ---
# Ringliikluse nooled asuvad 120-kraadiste vahedega (0°, 120°, 240°)
noolte_raadius = 110  # Trajektoori raadius märgi keskmest
noole_kaare_nurk = 70  # Iga noolevarre kaare pikkus kraadides

for i in range(3):
    # Iga noole algusnurk raadiustes (teisendame kraadid radiaanideks)
    baas_nurk = i * 120
    
    # a) Noolevars (kaari kujul)
    # Tkinteri create_arc kasutab kraade: 0° on paremal (kell 3), liigub vastupäeva.
    # Seetõttu korrigeerime nurki ringliikluse päripäeva suuna jaoks.
    algus_nurk = (90 - baas_nurk) % 360
    
    louend.create_arc(
        cx - noolte_raadius, cy - noolte_raadius,
        cx + noolte_raadius, cy + noolte_raadius,
        start=algus_nurk,
        extent=-noole_kaare_nurk,  # Negatiivne väärtus joonistab päripäeva
        style=tk.ARC,
        outline="white",
        width=24
    )
    
    # b) Nooleots (kolmnurk) iga kaare lõpus
    # Arvutame täpse punkti kaare lõpus matemaatiliselt
    lopp_nurk_rad = math.radians(baas_nurk + noole_kaare_nurk)
    
    # Otsa tsenter ringjoonel
    ox = cx + noolte_raadius * math.sin(lopp_nurk_rad)
    oy = cy - noolte_raadius * math.cos(lopp_nurk_rad)
    
    # Tangendi nurk otsa juures (suund kuhu nool näitab)
    tangent_rad = lopp_nurk_rad + math.pi / 2
    
    # Kolmnurga tippude arvutamine suunavektori järgi
    pikkus = 35
    laius_nool = 22
    
    # Tipu punkt
    tx = ox + pikkus * math.cos(tangent_rad)
    ty = oy + pikkus * math.sin(tangent_rad)
    
    # Alumised nurgad
    perpendikulaar = tangent_rad + math.pi / 2
    x1 = ox + laius_nool * math.cos(perpendikulaar)
    y1 = oy + laius_nool * math.sin(perpendikulaar)
    x2 = ox - laius_nool * math.cos(perpendikulaar)
    y2 = oy - laius_nool * math.sin(perpendikulaar)
    
    # Joonistame valge nooleotsa kolmnurga
    louend.create_polygon(tx, ty, x1, y1, x2, y2, fill="white", outline="white")

# Käivitame akna
aken.mainloop()