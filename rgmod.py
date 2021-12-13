import time
import os
import shutil
import pyglet
from tkinter import *
from tkinter import ttk
from tkinter import font
from tkinter.messagebox import *

pyglet.font.add_file("upheavtt.ttf")

profiles = sorted(os.listdir("profiles"))

root = Tk()
root.title("RG Mod")
root.resizable(False, False)
root.iconbitmap("icon.ico")

font_family = "Upheaval TT BRK" if "Upheaval TT BRK" in font.families() else "Helvetica"
title_font = font.Font(family=font_family, size=18)
subtitle_font = font.Font(family=font_family, size=12)
credits = font.Font(family="Helvetica", size=8)

frm = ttk.Frame(root, padding=20)
frm.grid()

ttk.Label(frm, text="RG Mod", font=title_font).grid(column=0, row=0)
ttk.Label(frm, text="A Rogue Glitch Mod Loader", font=subtitle_font).grid(column=0, row=1)

mod = StringVar(value="Normal")
ttk.Combobox(frm, textvariable=mod, values=profiles).grid(column=0, row=2)

save = StringVar(value="normal")
ttk.Checkbutton(frm, text="Use Separate Profile Save Data.", variable=save, onvalue="mod", offvalue="normal").grid(column=0, row=3)

def start():
  m = mod.get()
  s = save.get()
  
  if m not in profiles:
    showwarning(title="Warning", message="You must select a profile to run.")
  
  else:
    
    if not os.path.exists(f".game/RogueGlitch_Data/BypassSteamVerification.txt"):
      f = open(".game/RogueGlitch_Data/BypassSteamVerification.txt", "w+")
      f.close()
    
    if os.path.exists(f"profiles/{m}/Assembly-CSharp.dll"):
      shutil.copy2(f"profiles/{m}/Assembly-CSharp.dll", ".game/RogueGlitch_Data/Managed/Assembly-CSharp.dll")
    else:
      shutil.copy2("profiles/Normal/Assembly-CSharp.dll", ".game/RogueGlitch_Data/Managed/Assembly-CSharp.dll")
    
    if os.path.exists(".game/SaveData.glitch"):
      os.remove(".game/SaveData.glitch")
    
    if os.path.exists(f"profiles/{m}/SaveData.glitch") and s == "mod":
      shutil.copy2(f"profiles/{m}/SaveData.glitch", ".game/SaveData.glitch")
    
    if s == "normal":
      shutil.copy2("profiles/Normal/SaveData.glitch", ".game/SaveData.glitch")
    
    root.destroy()
    os.system("cd .game && RogueGlitch.exe")
    
    if s == "mod" or m == "Normal":
      shutil.copy2(".game/SaveData.glitch", f"profiles/{m}/SaveData.glitch")
    
    os.remove(".game/SaveData.glitch")
  
ttk.Button(frm, text="Start", command=start).grid(column=0, row=4)

ttk.Label(frm, text="Made by gignaWedi, 2021", font=credits, foreground="grey50").grid(column=0, row=5)

root.mainloop()
