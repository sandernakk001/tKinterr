import tkinter as tk

aken = tk.Tk()
aken.title("Kole majakas")
aken.resizable(False, False)

# Akna ette toomine
aken.lift()
aken.attributes('-topmost', True)
aken.after_idle(aken.attributes, '-topmost', False)

louend = tk.Canvas(aken, width=400, height=400, bg="white")
louend.pack()

# Kollane tsirkuse-valguskiir
louend.create_polygon(100, 100, 0, 0, 0, 200, fill="yellow", outline="black")

# Sinine maa/vesi
louend.create_rectangle(0, 300, 400, 400, fill="blue", outline="black")

# Majakas (hall kasti-hunnik)
louend.create_rectangle(80, 100, 120, 300, fill="gray", outline="black")
louend.create_rectangle(70, 70, 130, 100, fill="red", outline="black")
louend.create_polygon(70, 70, 100, 30, 130, 70, fill="green", outline="black")

# Kandi-maja majaka kõrval
louend.create_rectangle(200, 250, 280, 300, fill="brown", outline="black")
louend.create_polygon(200, 250, 240, 210, 280, 250, fill="purple", outline="black")
louend.create_rectangle(230, 270, 250, 300, fill="orange", outline="black")

aken.mainloop()