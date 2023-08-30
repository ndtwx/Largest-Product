# Largest-Product

You are employed in a government agency that has intercepted a series of encrypted communication signals from a group of bank robbers. The signals contain a long sequence of digits. Your team needs to use various digital signal processing techniques to analyze the signals and identify any patterns that may indicate the planning of a heist.

Instructions  

Our task is to look for patterns in the long sequence of digits in the encrypted signal.

The technique you will use here is called the largest series product.

Task A (3 Hours Allocation)

Let's define a few terms first.

input: the sequence of digits that you need to analyze
series: a sequence of adjacent digits (those that are next to each other) that is contained within the input
length: how many digits long each series is
the product: what you get when you multiply numbers together
Let's work through an example with the input "63915".

To form a series, take adjacent digits in the original input.
If you are working with a length of 3, there will be three possible series:
"639"
"391"
"915"
Then we need to calculate the product of each series:
The product of the series "639" is 162 (6 × 3 × 9 = 162)
The product of the series "391" is 27 (3 × 9 × 1 = 27)
The product of the series "915" is 45 (9 × 1 × 5 = 45)
162 is bigger than both 27 and 45, so the largest series product of "63915" is from the series "639". So the answer is 162.
Task B ( 1 - 1.5 hrs Allocation )
Exception messages 

Sometimes it is necessary to raise an exceptionLinks to an external site.. When you do this, you should always include a meaningful error message to indicate what the source of the error is. This makes your code more readable and helps significantly with debugging. For situations where you know that the error source will be a certain type, you can choose to raise one of the built in error typesLinks to an external site., but should still include a meaningful message.

This particular exercise requires that you use the raise statementLinks to an external site. to "throw" a ValueError when your largest_product() function receives invalid input. The tests will only pass if you both raise the exception and include a message with it. Feel free to reuse your code from the series exercise!

To raise a ValueError with a message, write the message as an argument to the exception type:

# length of numbers is longer than number series

raise ValueError("length must be smaller than string length")

# length of number is negative

raise ValueError("length must not be negative")

# series includes non-number input

raise ValueError("digits input must only contain digits")

Bonus Task:

To take in input from the user for the string to be assessed as well as length.
