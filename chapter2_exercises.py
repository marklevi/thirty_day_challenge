# Exercises for chapter 2: Problems 2.1, 2.2, 2.3, and 2.4 in Think Python


Mark Levi 

ex2.1 : 
When you type an integer with a leading zero, you get a SyntaxError because the octal numeral system is a base-8 number system, which only uses digits 0 to 7. Thus, digit 9 results in an error because it is an octal number. 
When you a valid octal numbers such as:

zipcode = 02132

result: 1114

what it really is doing is (2*512)+(1*64)+(3*8)+(2*1) which gives you 1114. 

ex2.2
The assignment statement produces no output. After transforming the expression into a print statement and runing it, the assignment produces the integer 6. 

ex2.3
1) value is 8      Type: 'int'
2) value is 8.5    Type: 'float'
3) value is 4.0	   Type: 'float'
4) value is 11 	   Type: 'int'
5) value is .....  Type: invalid syntax
	
ex2.4
1) 
pi=3.14
r=5
(4.0/3)*pi*r**3 
answer is 523.3

2)

 $24.95  Cost
  $9.98  Discount / book
 $14.97  Cost / book after discount
  60     Total number of books
$898.20  Total cost excluding shipment 

  $3.00  First book shipment fee
  $0.75  Additional book shipment fee
 $44.25  Total shipping cost for each of the remaining 59 books
 $47.25  Total shipping cost
    
4.95*0.6*60+0.75*59+3

$945.45  Total Bill

3) 

start = ((6*60)+52)*60
easy = ((8*60)+15)*2
fast = (((7*60)+12)*3)
finishhour = (start + easy + fast)/(60*60)
finishminute  = ((start + easy + fast)/(60*60.0) - finishhour) * 60


Finish time was 7:30

start = 6 * 60.0 + 52.0
easy = 2 * 8.15
fast = 3 * 7.12
# start + easy + fast = 449.66
finishhour = int((start+easy+fast)/ 60)
# finishhour equals 7
finishminute = 449.66%60
# finishminute equals 29.6

# she arrives at 7:30 am






