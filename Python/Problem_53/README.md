# Problem 53 Solution

This problem ask to find how many, not necessarily distinct, values of  ![](https://latex.codecogs.com/gif.latex?\inline&space;\large&space;\binom{n}{r})  for ![](https://latex.codecogs.com/gif.latex?\inline&space;\large&space;1&space;\leq&space;n&space;\leq&space;100)  are greater than one-million. It is not until n = 23 that a value exceeds a one-million threshold. (23,10) = 1,144,066 For this reason we can reduce our range of n to ![](https://latex.codecogs.com/gif.latex?\inline&space;\large&space;23&space;\leq&space;n&space;\leq&space;100) 

Now we can solve this problem using the combination formula ![](https://latex.codecogs.com/gif.latex?\inline&space;\large&space;\binom{n}{r}&space;=&space;\frac{n!}{r!(n-r)!}).

But instead I used a reverse factorial formula to solve the combinations faster as seen in `def reverse_factorial`. My motivation for this approach was to avoid large numbers in the numerator or denominator which can contribute to slower calculation times. I made a gif to illustrate how quickly sets of ![](https://latex.codecogs.com/gif.latex?\inline&space;\large&space;\binom{n}{r}) will begin to exceed our one-million threshold. 

![](nCr_animation.gif)

As soon as we approach n=23 the combination results easily surpass our threshold of one-million. It is interesting to see the combination results shift with new sets of ![](https://latex.codecogs.com/gif.latex?\inline&space;\large&space;\binom{n}{r})  and how the percentage of one-million combinations slowly increases as you move up in n values. 


