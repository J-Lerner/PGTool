# PGTool
Create games with ease in PyGame!

## Full Documentation
Use example.py to help understand how certain concepts are used.
### Initialization
Create a new variable using the pgt.PGT() class. The parameters for the class are window_x_size and window_y_size. These set the size of the game's window.  
  
set_background_color(String color) : sets the color of the game's window.
set_<key>_key(String key) : sets the key binding for a certain action


### Sprites
To create a new sprite, create a new variable and assign it to pgt.Sprite(). Sprites include:
###### * = mandatory
<ul>
    <li>Name of the image it uses</li>
    <li>Starting x-position</li>
    <li>Starting y-position</li>
    <li>Movement speed</li>
    <li>If it is controllable *</li>
    <li>Main game class *</li>
</ul>

### Images
Images are rendered through the assets folder. This folder may need to be created manually. It should be located in the same directory as the pgt.py file.

## Credits
Jordan Lerner - Developer