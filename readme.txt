# shielderize

Shielderize takes text and splits it up into segments of random length and creates randomly colored shields.
The shields link to a site selected at random from a configurable list.

Go ahead, try clicking on one of these badges, see where you end up :)

Why, you may ask, would someone want to make this?

Do I really need to answer that?

I hope that question was already answered for you while reading this awesomely colorful readme.
In fact, I'm going to keep typing whatever comes to mind just for your (and my) enjoyment.


<details>
<summary>
Here is a poem for you, I hope you like it:
</summary>
Everywhere I look,
<br>
Every cranny, every nook,
<br>
I see shields popping out at me,
<br>
And now I'm verily hooked.
</details>

<hr>

Now wasn't that sweet?
Okay, I'll stop now.
But really, isn't this fun to look at?
It totally changes the way you read the words.


## Installation

To install shielderizer with pip, run:
```
pip install shielderizer
```

After that you should be able to run `shielderizer` (as long as you have your PATH setup correctly).
It will by default try to read from standard input, or you can pass in a file as the first command line argument.

If you want to call shielderizer from Python code, here's an example you can build on:
```python
from shielderize import shielderize

text = "this is a bunch of random text that's spewing out of my mouth"

print(shielderize(text))

# Example raw output:
![](https://img.shields.io/badge/this-is%20a-3f459c?style=plastic&labelColor=1d31e2) ![](https://img.shields.io/badge/bunch%20of%20random%20text-7bda01?style=flat-square) ![](https://img.shields.io/badge/that%27s-71f7b1?style=flat-square) ![](https://img.shields.io/badge/spewing%20out-of-52492f?style=plastic&labelColor=98fe63) ![](https://img.shields.io/badge/my%20mouth-f168ba?style=plastic)

# Actual output below:
```
![](https://img.shields.io/badge/this-is%20a-3f459c?style=plastic&labelColor=1d31e2) ![](https://img.shields.io/badge/bunch%20of%20random%20text-7bda01?style=flat-square) ![](https://img.shields.io/badge/that%27s-71f7b1?style=flat-square) ![](https://img.shields.io/badge/spewing%20out-of-52492f?style=plastic&labelColor=98fe63) ![](https://img.shields.io/badge/my%20mouth-f168ba?style=plastic)

## Disclaimer

Shielderize is a project I will most likely not work on often, if at all.

I just happened to decide to make this. There are a lot of fun things that could be made to improve it, e.g.

- use a markdown parser instead of my hackish code to decide what to shielderize
- make it more configurable (more easily customize style, words in each shield, colors, etc)
- and so on.

## Thank yous

Many thanks to
[https://shields.io/](https://shields.io/)
for being free and open source.
I hope this doesn't cause any unnecessary load on your servers.
