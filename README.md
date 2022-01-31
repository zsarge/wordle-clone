# wordle-clone
Inspired by https://github.com/SamKiehl/ButterDog-Bot

### Example 1:
```
Enter a 5 letter word: fork
Invalid guess!
Enter a 5 letter word: shelf
 1/6 |- -  |
     |shelf|

Enter a 5 letter word: seven
 2/6 |--   |
     |seven|

Enter a 5 letter word: raise
 3/6 |--✓✓✓|
     |raise|

Enter a 5 letter word: arise
 4/6 |✓✓✓✓✓|
     |arise|

Good Job!
```

Note the counter on the left counts turns.

### Example 2:

```
Enter a 5 letter word: chair
 1/6 |     |
     |chair|

Enter a 5 letter word: quail
 2/6 |    -|
     |quail|

Enter a 5 letter word: droop
 3/6 |  ✓- |
     |droop|

Enter a 5 letter word: sends
 4/6 |--   |
     |sends|

Enter a 5 letter word: moose
 5/6 | ✓✓✓✓|
     |moose|

Enter a 5 letter word: loose
 6/6 |✓✓✓✓✓|
     |loose|

Good Job!
```

