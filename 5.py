import tkinter as tk

def vicsekFractals():
    # 1. Akna ja lõuendi seadistamine
    akna_suurus = 400
    aken = tk.Tk()
    aken.title("Vicsek Fractal")
    aken.geometry(f"{akna_suurus}x{akna_suurus}")
    aken.resizable(False, False)

    louend = tk.Canvas(aken, width=akna_suurus, height=akna_suurus, bg="white")
    louend.pack(fill="both", expand=True)

    # 2. Rekursiivne funktsioon Vicseki fraktaali joonistamiseks
    def joonista_vicsek(x, y, suurus, sugavus):
        # Baasjuht: kui sügavus on 0, joonistame täidetud ruudu
        if sugavus == 0:
            louend.create_rectangle(x, y, x + suurus, y + suurus, fill="black", outline="black")
            return

        # Jagame ruudu 3x3 võrgustikuks (iga alamruudu külg on suurus / 3)
        uus_suurus = suurus / 3

        # Vicseki X-mustri 5 ruudu koordinaatide nihked (reaindeks, veeruindeks):
        # 4 nurka + keskruut
        nihked = [
            (0, 0),  # Ülemine vasak
            (0, 2),  # Ülemine parem
            (1, 1),  # Keskruut
            (2, 0),  # Alumine vasak
            (2, 2)   # Alumine parem
        ]

        # Rekursiivne samm iga 5 ruudu jaoks
        for rida, veerg in nihked:
            uus_x = x + veerg * uus_suurus
            uus_y = y + rida * uus_suurus
            joonista_vicsek(uus_x, uus_y, uus_suurus, sugavus - 1)

    # 3. Klahvivajutuse käitleja (sündmuste kuulaja)
    def klahvi_vajutus(event):
        # Kontrollime, kas vajutatud klahv on number 0-9
        if event.char.isdigit():
            uue_sugavus = int(event.char)
            # Puhastame vana pildi
            louend.delete("all")
            # Joonistame fraktaali uue sügavusega
            joonista_vicsek(0, 0, akna_suurus, uue_sugavus)

    # Seome klaviatuurisündmused aknaga
    aken.bind("<Key>", klahvi_vajutus)

    # Algne joonistamine (alustame näiteks sügavusest 0 või 1)
    joonista_vicsek(0, 0, akna_suurus, 0)

    # Peamine sündmuste tsükkel
    aken.mainloop()

# Funktsiooni käivitamine
if __name__ == "__main__":
    vicsekFractals()