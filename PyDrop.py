import tkinter as tk

aiPercentByDeltaLev = [
    1, 5, 10, 20, 30, 50, 70, 80, 85, 90, 92, 94, 96, 98, 100,
    100, 105, 110, 115, 120, 125, 130, 135, 140, 145, 150, 155, 160, 165, 170, 180,
]

aiPercentByDeltaLevForBoss = [
    1, 3, 5, 7, 15, 30, 60, 90, 91, 92, 93, 94, 95, 97, 99,
    100, 105, 110, 115, 120, 125, 130, 135, 140, 145, 150, 155, 160, 165, 170, 180,
]

def get_drop_pct(player_level, monster_level, is_boss=False):
    level_difference = (monster_level + 15) - player_level
    if level_difference < 0:
        level_difference = 0
    if level_difference > 30:
        level_difference = 30

    if is_boss:
        drop_pct = aiPercentByDeltaLevForBoss[level_difference]
    else:
        drop_pct = aiPercentByDeltaLev[level_difference]

    return drop_pct / 100

def calculate_probability(mobs, initial_probability, player_level, monster_level, is_boss=False):
    drop_pct = get_drop_pct(player_level, monster_level, is_boss)
    adjusted_probability = initial_probability * drop_pct
    return 1 - (1 - adjusted_probability) ** (1 / mobs)

def on_calculate_button_click():
    mobs = int(mobs_entry.get())
    initial_probability = float(initial_probability_entry.get())
    player_level = int(player_level_entry.get())
    monster_level = int(monster_level_entry.get())
    is_boss = boss_var.get()

    target_probability = calculate_probability(mobs, initial_probability, player_level, monster_level, is_boss)
    if isinstance(target_probability, complex):
        target_probability = target_probability.real

    target_probability_label.config(text=f"Target probability: {target_probability:.2%}")


root = tk.Tk()
root.title("Drop Calculator")

mobs_label = tk.Label(root, text="Mobs:")
mobs_label.grid(row=0, column=0)
mobs_entry = tk.Entry(root)
mobs_entry.grid(row=0, column=1)

initial_probability_label = tk.Label(root, text="Initial probability:")
initial_probability_label.grid(row=1, column=0)
initial_probability_entry = tk.Entry(root)
initial_probability_entry.grid(row=1, column=1)

player_level_label = tk.Label(root, text="Player level:")
player_level_label.grid(row=2, column=0)
player_level_entry = tk.Entry(root)
player_level_entry.grid(row=2, column=1)

monster_level_label = tk.Label(root, text="Monster level:")
monster_level_label.grid(row=3, column=0)
monster_level_entry = tk.Entry(root)
monster_level_entry.grid(row=3, column=1)

boss_var = tk.BooleanVar()
boss_checkbox = tk.Checkbutton(root, text="Boss monster", variable=boss_var)
boss_checkbox.grid(row=4, column=0)

calculate_button = tk.Button(root, text="Calculate", command=on_calculate_button_click)
calculate_button.grid(row=4, column=1)

target_probability_label = tk.Label(root, text="Target probability:")
target_probability_label.grid(row=5, column=0)

root.mainloop()
