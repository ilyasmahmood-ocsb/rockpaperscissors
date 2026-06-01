hand = 0

def on_gesture_shake():
    global hand
    hand = randint(0, 2)
    if hand == 0:
        # Rock (represented by a small square)
        basic.show_icon(IconNames.SMALL_SQUARE)
    elif hand == 1:
        # Paper (represented by a large square)
        basic.show_icon(IconNames.SQUARE)
    else:
        # Scissors
        basic.show_icon(IconNames.SCISSORS)
input.on_gesture(Gesture.SHAKE, on_gesture_shake)