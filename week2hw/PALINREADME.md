This is a thought dump, I'll be exercising how to write proper markdowns as I go I guess.

Ooookay then, do I even understand the problem statement?
"Find the longest palindrome in a string"

These are rarely as straightforward as they seem on the surface. So what tools do I have off the top of my head?

Strings.
Lists.
Dictionaries.
For loops.
While loops.
If/else conditionals.

I think there are some clever solutions hidden somewhere in this, but I guess this is one of those problems that simply thinking of a brute force solution won't really cut it. I'm wary of an O(n^2) or O(n^3) run time. But let's get anything working first so I understand the problem better.

First attempt... I iterate over the string. How? I can treat the string like a list, with indeces and values in each index. Can I design a set of loops that will take an index and compare to other stored values? How?

Take Maloy's advice. Let's create a simple test case and build up from there.

============

I created a test case but couldn't even create a simple test solution.

I'm having such a hard time thinking about this problem in plain English. I caught myself in one of my failure modes on that first attempt by jumping straight into how to do it with code. So let's step back. What's the actual problem?

I went and looked up parts of the problem and it feels a little disingenius now, but I guess the important thing is I stepped out of my head for a bit and I can try to solve the problem first before coding it. Here goes.

What the heck is a palindrome in the first place?

A set of letters that are the same from some midpoint out towards the beginning and end of the set. Wtf. I can do better than that.

A set of characters that read the same from left to right as right to left. Better.

Samples: abba, aaabbbbaaa, catac, madam

So if I split abba, I get ab ba. The second half is the same as the first half reversed. How can I compare that second half to that first half?

Actually, what even is my intention on this solution the first place? Right now that I understand possible outputs better, would be a good time to ask that question.

If I am supplied a string, what do I do with it? For this exercise, I can think of different ways of solving it, but I need to pick one and actually solve it. 

Some possibilities:

Am I looking for a set of characters across the entire string and putting together a palindrome?
    - Can they be taken in any order to put together a palindrome?
        - Cherrypicking
    - Do I lift them out of the string in the order they are in and put together a new string?
        -Example: "Not cherrypickiNg" -> nn
        -Example: "SmapLe tabLeS" -> slls
        - I'm gonna cross this one out on account of the fact that this doesn't seem useful after exploring those examples.