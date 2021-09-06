Problem statement:

The parameter weekday is True if it is a weekday, and the parameter vacation is True if we are on vacation. We sleep in if it is not a weekday or we're on vacation. Return True if we sleep in.

sleep_in(False, False) → True
sleep_in(True, False) → False
sleep_in(False, True) → True

So thinking through how I would logically solve this problem, it's really asking if I can sleep in. I can sleep in if it's not a weekday, or if I'm on vacation. So the function should return a boolean.

I should give a simple answer, thought I could complicate this by creating a list of weekdays and checking it, I think the point of the question is just to play with booleans.

Can I sleep in?

1. Check if I'm on Vacation
    - If True, close the program and return True
    - If False, proceed to the next check
2. Is it a weekday?
    - If True, return False
    - If False, return True
    
I can optimize the logic of this later.