# Yoghurt dev diary

#### The first 2 days of work were not written down immediately, thus this part will be a reconstruction:

day 1: The first day I setup a headless configuration for the raspberry pi which went smoothly. Afterwards I installed Igor via a pip install which went decently smooth. Later we however noticed that I did not install the Igor files with SUDO, this means that I cannot run sudo commands via Igor. If that ever becomes necessary I should only have to reinstall the "logic files" of Igorand can leave the database the same. This should thus not change any of the work I would have done up to that point.

day 2: The second day I worked on Igor I spend most of my time to try and figure out how to program Igor in the current system of actions. This also required a lot of help from Jack as the documentation was quite sub par (due to the fact that this way of programming Igor with action is only temporary). I've made a small hello world program which could be triggered with a URL and tried to make it triggerable with the buttons on `LcdButtons` but this did not work as I (we) expected as the LcdButtons can not handle multiple open HTTP requests, thus my testing for the second day came to an end after learning a lot about the internal structures (and a bit of their flaws) of Igor.

#### Day 3:

started reading up about PEG parser generators via [this](https://medium.com/@gvanrossum_83706/peg-parsing-series-de5d41b2ed60) site

Some key things from "Building a PEG parser"

- Grammar rules correspond to parser methods, and when a grammar rule references  another grammar rule, its parsing method calls the other rule’s parsing  method.
- When multiple items make up an alternative, the parsing method calls the corresponding methods one after the other.
- When a grammar rule references a token, its parsing method calls `expect()`.
- When a parsing method successfully recognizes its grammar rule at the given  input position, it returns a corresponding AST node; when it fails to  recognize its grammar rule, it returns `None`.
- Parsing methods must explicitly reset the tokenizer position when they abandon a parse after having consumed one or more tokens (directly, or indirectly by calling another parsing method that succeeded). This applies when  abandoning one alternative to try the next, and also when abandoning the parse altogether.



#### Day 4:

Sadly the PEG parser Pegen was not yet usable for us. We encountered different errors that would be to costly to try and fix for the upsides they may bring. Thus we will now try to use the parser [Parso](https://parso.readthedocs.io/en/latest/).