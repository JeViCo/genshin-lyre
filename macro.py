from pynput import keyboard
from time import sleep
import threading
import os

songs = [
    'AVN-A-A-A-D-D-D-D-SBM-S-S-S-G-G-G-G-DH-DH-DH-DH-DH-DH-DH-DH-DH-S-A-M-B-VN-N-D-SV-A-BM-M-M-SM-A-M-CN-H-Q-J-Q-J-Q-H-H-Q-J-Q-J-Q-VN-N-D-SV-A-BM-M-M-SM-A-M-CN-H-Q-J-Q-J-Q-H-H-Q-J-Q-J-Q-AVN-A-A-A-D-D-D-D-SBM-S-S-S-G-G-G-G-DH-DH-DH-DH-DH-DH-DH-DH-DH',
    'G-Q-G-H-J-D-D-H-G-F-G-A-A-S-S-D-F-F-G-H-J-Q-W-G-E-W-Q-W-J-G-Q-J-H-J-D-D-H-G-F-G-A-A-Q-J-H-G-E-W-Q-J-Q-W-G-G-Q-J-H-G-H-J-D-D-Q-H-J-Q-H-J-Q-H-Q-R-R-E-W-Q-W-E-Q-Q-W-Q-J-H-J-Q-H-H-Q-J-H-G-A-A-Q-J-H-G'
]

for i in range ( len ( songs ) ):
    songs[ i ] = list ( songs[ i ].lower ( ).split ( '-' ) )

delays = [
    [ 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 900, 200, 200, 200, 200, 400, 200, 200, 400, 400, 400, 200, 200, 400, 200, 200, 400, 200, 200, 200, 200, 200, 200, 400, 200, 200, 200, 200, 200, 200, 400, 200, 200, 400, 400, 400, 200, 200, 400, 200, 200, 400, 200, 200, 200, 200, 200, 200, 400, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200 ],
    [
        350, 350, 750, 350, 350, 750, 350, 350, 750, 350, 350,
        750, 350, 350, 750, 350, 350, 750, 350, 350, 750, 350, 350,
        750, 750, 750, 350, 350, 750, 350, 350, 750, 350, 350,
        750, 350, 350, 750, 350, 350, 750, 350, 350, 750, 350, 350,

        750, 750, 350, 350, 350, 350, 750, 350,
        750, 750, 350, 350, 350, 350, 750, 350,
        750, 750, 350, 350, 750, 350, 350, 750, 350, 350,

        750, 750, 350, 350, 350, 350, 750, 350,
        750, 750, 350, 350, 350, 350, 750, 350,
        750, 750, 350, 350, 750, 350, 350, 750, 350, 350
    ]
]

# Core

started = False
selected = 0
keyb = keyboard.Controller ( )

def executeSong ( i ):
    global started

    for j in range ( len ( songs[ i ] ) ):
        if not started:
            return
        if i > len ( delays[ i ] ):
            started = False
            return

        sleep ( delays[ i ][ j ] * 0.001 )
        keys = list ( songs[ i ][ j ] )
        for k in range ( len ( keys ) ):
            keyb.press ( keys[ k ] )
            keyb.release ( keys[ k ] )
    started = False

# Binder

def on_press ( key ):
    pass

def on_release ( key ):
    global started
    global selected

    if key == keyboard.Key.page_up:
        selected = min ( selected + 1, 1 )
    elif key == keyboard.Key.page_down:
        selected = max ( selected - 1, 0 )

    #if hasattr ( key, 'vk' ) and key.vk == 12: # Numpud 5
    elif key == keyboard.Key.home:
        started = not started
        if started:
            t = threading.Thread ( target = executeSong, args = ( selected, ) )
            t.start ( )

with keyboard.Listener ( on_press = on_press, on_release = on_release ) as listener:
    listener.join ( )

#input ( 'Используйте Numpad 8/2 для выбора мелодии, Numpad 5 для запуска.\n' )
