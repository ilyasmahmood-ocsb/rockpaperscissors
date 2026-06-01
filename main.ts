let hand = 0
input.onGesture(Gesture.Shake, function on_gesture_shake() {
    
    hand = randint(0, 2)
    if (hand == 0) {
        //  Rock (represented by a small square)
        basic.showIcon(IconNames.SmallSquare)
    } else if (hand == 1) {
        //  Paper (represented by a large square)
        basic.showIcon(IconNames.Square)
    } else {
        //  Scissors
        basic.showIcon(IconNames.Scissors)
    }
    
})
