import tkinter as tk

# Loome peakna
aken = tk.Tk()
aken.title("Malelaud")
aken.resizable(False, False)

# Laua parameetrid
ruuduse_suurus = 60
rea_veeru_arv = 8
veerise_laius = 40  # Ruum servadele (tähed A-H ja numbrit 1-8)

# Lõuendi kogumõõtmed
kogu_laius = rea_veeru_arv * ruuduse_suurus + 2 * veerise_laius
kogu_korgus = rea_veeru_arv * ruuduse_suurus + 2 * veerise_laius

louend = tk.Canvas(aken, width=kogu_laius, height=kogu_korgus, bg="white")
louend.pack()

# Värvide definitsioonid
hele_ruut = "#F0D9B5"
tume_ruut = "#B58863"
valge_nupp = "#FFFFFF"
must_nupp = "#312E2B"

# Tähistuste massiivid
tahed = ["A", "B", "C", "D", "E", "F", "G", "H"]
numbrid = ["8", "7", "6", "5", "4", "3", "2", "1"]

# --- 1. MALELAUA RUUDUSTIK JA NUPUD (PESASTATED TSÜKLID) ---
for rida in range(rea_veeru_arv):
    for veerg in range(rea_veeru_arv):
        # Arvutame ruudu koordinaadid lõuendil
        x1 = veerise_laius + veerg * ruuduse_suurus
        y1 = veerise_laius + rida * ruuduse_suurus
        x2 = x1 + ruuduse_suurus
        y2 = y1 + ruuduse_suurus

        # Määrame ruudu värviskeemi:
        # Kui rea ja veeru indeksite summa on paaris, on ruut hele; muidu tume.
        ruudu_varv = hele_ruut if (rida + veerg) % 2 == 0 else tume_ruut
        
        # Joonistame maleruudu
        louend.create_rectangle(x1, y1, x2, y2, fill=ruudu_varv, outline="black")

        # --- 2. KABENUPPUDE PAIGUTAMINE TUME-RUUTUDELE ---
        # Joonistame kabenupud tavapärasesse algasendisse (3 esimest ja 3 viimast rida)
        if ruudu_varv == tume_ruut:
            # Padi/raadius nupu serva ja ruudu serva vahel
            padi = 8
            nx1 = x1 + padi
            ny1 = y1 + padi
            nx2 = x2 - padi
            ny2 = y2 - padi

            # Ülemised kolm rida -> mustad kabenupud
            if rida < 3:
                louend.create_oval(nx1, ny1, nx2, ny2, fill=must_nupp, outline="black", width=2)
                # Nupu sisejoon dekoratsiooniks
                louend.create_oval(nx1 + 4, ny1 + 4, nx2 - 4, ny2 - 4, outline="#555555", width=1)

            # Alumised kolm rida -> valged kabenupud
            elif rida >= 5:
                louend.create_oval(nx1, ny1, nx2, ny2, fill=valge_nupp, outline="black", width=2)
                # Nupu sisejoon dekoratsiooniks
                louend.create_oval(nx1 + 4, ny1 + 4, nx2 - 4, ny2 - 4, outline="#CCCCCC", width=1)

# --- 3. SERVA TÄHISTED (TÄHED JA NUMBRID) TSÜKLITEGA ---
for i in range(rea_veeru_arv):
    # Tähed A-H (üles ja alla)
    x_pos = veerise_laius + i * ruuduse_suurus + ruuduse_suurus / 2
    louend.create_text(x_pos, veerise_laius / 2, text=tahed[i], font=("Arial", 12, "bold"))
    louend.create_text(x_pos, kogu_korgus - veerise_laius / 2, text=tahed[i], font=("Arial", 12, "bold"))

    # Numbrid 1-8 (vasakule ja paremale)
    y_pos = veerise_laius + i * ruuduse_suurus + ruuduse_suurus / 2
    louend.create_text(veerise_laius / 2, y_pos, text=numbrid[i], font=("Arial", 12, "bold"))
    louend.create_text(kogu_laius - veerise_laius / 2, y_pos, text=numbrid[i], font=("Arial", 12, "bold"))

# Laua välispiirjoon
louend.create_rectangle(
    veerise_laius, veerise_laius,
    kogu_laius - veerise_laius, kogu_korgus - veerise_laius,
    outline="black", width=2
)

# Käivitame akna
aken.mainloop()