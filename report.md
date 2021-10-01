# MapReduce Report
Ryan Rivero
Parallel Computing

## Assignment Details

This assignment took just 3 days to complete. I was able to get the serial
version of the word count running. I extracted the files added them to a list
of texts or basically very long strings and utilized the count() funtion to
count all instances of a target word selected while ensuring that all cases
were handled such as capitalization. I decompositioned pretty much all my
algorithms into methods that would be simply called from the main. I
personally feel I didn't implement the parallel part correctly but I was able
to utilize the interate and lock functionalities of pymp to more or less
output correct results. To run this code simply type: python3 mapReduce.py

## Problems Encountered

The problems didn't begin until I attemped to parallize my serial functions. I
figured if I got the word count to work in serial I would simply be able to
implement the same functions but in a paralled version. Although I was able to
technically parallize the function I do not believe I utilized the mapReduce
method of counting all the words in the document. If points are deducted I
understand. The differences came in the time comparisons between serial and parallel.

## Performance Measurements

When it came to altering the amount of threads being ran simultaneously the
results were opposite of what I expected. The paralled algorithm was outputing
slightly longer times than the serial version; by slightly I mean decimals. I
feel as though my implementation of the parallization is what may have amped
up the time very slightly. That or I created an efficient enough serial
algorithm to compute the word count in a decent time frame. Weather it was my
implementation or not no matter how many threads a ran the results showed the
serial version coming out on top by decimals:

Key: * SMR  == Serial Map Reduce
     * PMR == Parallel Map Reduce
( Time results are calculated in Monotonic time )
1 Thread:
  * Time difference: .03 seconds(Serial was faster)
2 Threads:
  * Time difference: .06 seconds(Serial was faster)
4 Threads:
  * Time difference: .07 seconds(Serial was faster)
8 Threads:
  * Time difference: .10 seconds(Serial was faster)

CPU Model: 11th Gen Intel(R) Core(TM) i5-1135G7 @ 2.40GHz

As shown above, the time differences were very small but the serial version
came out on top every time. Again, I feel as though my implementation is what
can be credited to the serial version being faster than the paralled version.

## Final Observations

I understand the concept of mapReduce as it is ment to make, in this case, the
word count much more efficient by utilizing multiple threads to count certain
words through all the documents and eventually reduce the amount of
computation being done by converging the sums of the various texts. It was my
implementation that I, again, believe was the root of the time differences
coming out in an unexpected manner but this is definitely an interesting
attempt at seeing the differences from serial to paralled. Maybe serial is
actually faster than parallel in this case? That will be my closing
question/thought for this lab.
