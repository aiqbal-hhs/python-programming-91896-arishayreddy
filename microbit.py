def on_forever():
    basic.show_string("Hello Arishay!")
    basic.show_leds("""
        # . . . #
        # . . . #
        # . . . #
        # . . . #
        # . . . #
        """)
    basic.show_leds("""
        . . . . .
        . . . . .
        . . . . .
        . . . . .
        . . . . .
        """)
basic.forever(on_forever)
