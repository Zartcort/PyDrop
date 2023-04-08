# PyDrop

PyDrop is a small Python application that allows you to calculate the probability of getting an item when killing a monster in the popular online game Metin2.

## Requirements

- Python 3.x
- Tkinter (usually comes bundled with Python)

## Usage

The application has four input fields:

- **Mobs**: the number of monsters to be killed.
- **Initial probability**: the initial probability of getting the item.
- **Player level**: the level of the player.
- **Monster level**: the level of the monster to be killed.

There is also a checkbox to indicate whether the monster is a boss (Boss monster).

After entering the corresponding values, click the "Calculate" button to obtain the probability of getting the item. The probability will be displayed below the button.

## Functioning

The application uses two predefined lists to obtain the percentage probability of drop based on the level difference between the player and the monster. If the monster is a boss, a different list is used.

The `get_drop_pct` function takes the player level and monster level and returns the corresponding drop probability percentage.

The `calculate_probability` function takes the number of monsters, initial probability, player level, and monster level, and returns the probability of getting the item after killing the specified monsters.

The `on_calculate_button_click` function is executed when the "Calculate" button is clicked. It gets the values entered in the input fields and calls the `calculate_probability` function to get the probability of getting the item. It then displays the result in the corresponding label.

## Attributions

- Code written by [Zarcort].
- Percentage probability lists obtained from [Metin2 Source Code].
