"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 3:
(080) is the area code for fixed line telephones in Bangalore.
Fixed line numbers include parentheses, so Bangalore numbers
have the form (080)xxxxxxx.)

Part A: Find all of the area codes and mobile prefixes called by people
in Bangalore. In other words, the calls were initiated by "(080)" area code
to the following area codes and mobile prefixes:
 - Fixed lines start with an area code enclosed in brackets. The area
   codes vary in length but always begin with 0.
 - Mobile numbers have no parentheses, but have a space in the middle
   of the number to help readability. The prefix of a mobile number
   is its first four digits, and they always start with 7, 8 or 9.
 - Telemarketers' numbers have no parentheses or space, but they start
   with the area code 140.

Print the answer as part of a message:
"The numbers called by people in Bangalore have codes:"
 <list of codes>
The list of codes should be print out one per line in lexicographic order with no duplicates.

Part B: What percentage of calls from fixed lines in Bangalore are made
to fixed lines also in Bangalore? In other words, of all the calls made
from a number starting with "(080)", what percentage of these calls
were made to a number also starting with "(080)"?

Print the answer as a part of a message::
"<percentage> percent of calls from fixed lines in Bangalore are calls
to other fixed lines in Bangalore."
The percentage should have 2 decimal digits
"""
if __name__ == '__main__':
    all_numbers_being_called = set() # store all of the fixed line and mobile called by (080)
    total_fixed_phone_calls = 0
    fixed_line_to_fixed_Line = 0

    for call in calls:
        outgoing = str(call[0])
        incoming = str(call[1])

        if outgoing.startswith('(080)'):
            # calculate number of fixed line to fixed line calls
            total_fixed_phone_calls += 1
            if incoming.startswith('(080)'):
                fixed_line_to_fixed_Line += 1

            if incoming.startswith('('): # find area code for fixed line
                all_numbers_being_called.add(incoming[incoming.find("(") + 1:incoming.rfind(")")])
            elif incoming.startswith('7') or incoming.startswith('8') \
                 or incoming.startswith('9'):  # find mobile numbers
                mobile_prefix = incoming.split()[0][:4]
                all_numbers_being_called.add(mobile_prefix)

    result = sorted(all_numbers_being_called)

    print("The numbers called by people in Bangalore have codes:")
    for number in result:
        print(number)

    precentage = '{0:.2f}'.format(fixed_line_to_fixed_Line/total_fixed_phone_calls * 100)
    print(str(precentage) + " percent of calls from fixed lines in Bangalore "
          + "are calls to other fixed lines in Bangalore.")
    