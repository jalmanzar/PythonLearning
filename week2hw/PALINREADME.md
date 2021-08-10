This is a thought dump, I'll be exercising how to write proper markdowns as I go I guess.

%1 Initial thoughts and catching my failure mode
%2 Solving for cherrypicking
%3 Solving for "I guess I'm proving I can slice and iterate"
%4 My takeaway from this thought exercise

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

%1============ Initial thoughts and catching my failure mode

I created a test case but couldn't even create a simple test solution.

I'm having such a hard time thinking about this problem in plain English. I caught myself in one of my failure modes on that first attempt by jumping straight into how to do it with code. So let's step back. What's the actual problem?

I went and looked up parts of the problem and it feels a little disingenius now, but I guess the important thing is I stepped out of my head for a bit and I can try to solve the problem first before coding it. Here goes.

What the heck is a palindrome in the first place?

A set of letters that are the same from some midpoint out towards the beginning and end of the set. Wtf is this definition I can do better than that.

A set of characters that read the same from left to right as right to left. Better.

Samples: abba, aaabbbbaaa, catac, madam

So if I split abba, I get ab ba. The second half is the same as the first half reversed. How can I compare that second half to that first half?

Actually, what even is my intention on this solution the first place? Right now that I understand possible outputs better, would be a good time to ask that question.

If I am supplied a string, what do I do with it? For this exercise, I can think of different ways of solving it, but I need to pick one and actually solve it. 

Some possibilities:

Am I looking for a set of characters across the entire string and putting together a palindrome?

    - Can they be taken in any order to put together a palindrome?
        - Cherrypicking
        - This one sounds fun and like the most practical implementation.

    - Do I lift them out of the string in the order they are in and put together a new string?
        -Example I/O: "Not cherrypickiNg" -> nn
        -Example I/O: "SmapLe tabLeS" -> slls
        - I'm gonna cross this one out on account of the fact that this doesn't seem useful after exploring those examples. Yeah fuck that.

    - The prevailing rhetoric around what this problem is seems to be "find the longest palindromic substring," with solutions arond slicing and iterating.
        - I guess we can cut up the string and compare the slices?
        Example I/O: herpabracarbaderp -> abracarba

%2============ Solving for cherrypicking

Let's cherrypick. That sounds monumentally harder on the surface, but let's see what I come up with!

I could go over the set of characters and check for even numbers of letters that are present, then pop those out. If I did this by hand, I would take something like:

"I am trying the hardest I can to use a bunch of vowels."

And grab: 3 Is, 3 As, 1 M, 4 Ts, 2 Rs, 1 Y, 3 Ns, 1 G, 3 Hs, 4 Es, 3 Ss, 1 D, 2 Cs, 3 Os, 2 Us, 1 F, 1 W

I'm honestly not sure if I got all of those right. That's a lot of manual work prone to human error. The acceptable characters should look like this:

ttttrreeeeccuu

And a possible palindrome could look like this: ttureecceerutt

I'm only using the even counts because I can guarantee a palindrome with an even number of instances for every character. If I'm being liberal with the use of the word "character" here, I can include numbers and special characters like a period, but I'll get there later and only use letters for now. This also opens up the option of giving the user of this hypothetical program the option to take a character with an uneven count and place that subset in the center to "divide" the palindrome.

But okay before these thoughts leave me, solving that by hand was kinda cool.

So my actual steps were:

1. Count the number of times the first unique letter appears in the sentence.
    1.a Save that value somewhere to reference.

2. Realize I don't need to count that letter again. Move on to the next unique letter. Repeat and move on to the next step once I run out of unique letters

###After three or four of these. it's becoming hard to manually keep track of, so I make a mental note of how powerful automation is.###

3. Grab the even counts and put them in a set, in the order I picked them out. 
    
###I realize they can be in any order, but this is easier to understand and work with so I stick with it.###

4. (Since I put them in order), I grab half of the first set of unique letters, and stick them on the other end of the entire set. 
TTTTrreeeeccuu -> TTrreeeeccuuTT

5. I look backwards from the other end of the string, and find the next set of unique letters. I grab half of those and place them where the last set of unique letters originally ended.
ttrreeeeccUUtt -> ttUrreeeeccUtt

6. Repeat steps 4 and 5. Break when... the difference between the original "index" and "reverse index" is zero. Or, maybe as a better check, break when the middle two characters match each other. (To be explored, w/e spent lots of time already on this).
ttuRReeeeccutt -> ttuReeeeccRutt
tturEEEEccrutt -> tturEEccEErutt
ttureeCCeerutt -> ttureeCCeerutt

Alright this is the moonshot solution. This is the one that sounds fun though.

%3============ Solving for "I guess I'm proving I can slice and iterate"

After all that, I find this one boring actually but I get why it's important and what I'm supposed to show off.

Assumptions:
There is a palindrome in the string and I don't have to re-order the entire thing.

-grumble- use two for loops and slice the strings. Compare them. Making unit tests for this will be the fun part.

%4============ My takeaway from this thought exercise

This was like outlinining those essays I used to like so much. It's a thought exploration around a problem and I like to think I'm really good at that.