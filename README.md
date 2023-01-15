# annoyances
Collection of utilities and fixes for games

## steam

disable_notifications:

Steam style that disables drawing of notification overlay popups. Affects achievements, friend notifications, etc. Found somewhere, modified and archived for posterity.

## utils

y_axis:

Increase movement rate of mouse on Y axis using xinput. Intended for games where the vertical sensitivity is not equal to horizontal sensitivity (usually halved). Example: Metro 2033. Supply the integer ID of the mouse device (`xinput list`) at the top of the file. This toggle script could be bound to a hotkey for ease of use.

eqlogin.py:

EQ Emulator login servers can fail to connect when using Wine due to some Winsock anachronism. This Python script routes activity on port 5998 to the correct destination address. Found somewhere, archived for posterity.

ppi:

Report resolution, diagonal size (inches), and PPI of connected displays using xrandr.

## noita

startpos:

Noita mod that sets the player X,Y start position closer to the mine entrance to facilitate faster gameplay when starting a new run. (Obviates the need to run through the starting corridor every time.)

## worms

no_startup:

Naive method of disabling startup fanfare when booting Worms: Armageddon.
