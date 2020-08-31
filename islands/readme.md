# Islands detection
## usage: 
main.sh <filepath>
### more info:
I have written the program with the assumption of being able to handle long file inputs, that is why I went with the approach of 
scanning two lines at a time, as to not strain the memory usage. 

Another assumption is that we want to handle loops, such as

```
000000000
000111000
001000100
000111000
000000000
```

to be counted as 1 island.

As can be seen above, I also count in the diagonal connections.

