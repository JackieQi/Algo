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
TASK 4:
The telephone company want to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers:
these are numbers that make outgoing calls but never send texts,
receive texts or receive incoming calls.

Print a message:
"These numbers could be telemarketers: "
<list of numbers>
The list of numbers should be print out one per line in lexicographic order with no duplicates.
"""

if __name__ == '__main__':
    telemarketers = set()
    unique_outgoing_numbers = set()
    unique_incoming_numbers = set()
    unique_text_sending_numbers = set()
    unique_text_receiving_numbers = set()

    # store unique outgoing and incoming numbers separately
    for call in calls:
        outgoing_number = str(call[0])
        incoming_number = str(call[1])

        unique_incoming_numbers.add(incoming_number)
        unique_outgoing_numbers.add(outgoing_number)

    # store unique sending and receiving numbers separately
    for text in texts:
        sender_number = str(text[0])
        receiver_number = str(text[1])

        unique_text_sending_numbers.add(sender_number)
        unique_text_receiving_numbers.add(receiver_number)

    # numbers not in reciving phone call, sending and receiving texts
    for number in unique_outgoing_numbers:
        if not unique_incoming_numbers.__contains__(number) \
           and not unique_text_receiving_numbers.__contains__(number) \
           and not unique_text_sending_numbers.__contains__(number):
            telemarketers.add(number)

    result = sorted(telemarketers)

    print("These numbers could be telemarketers: ")

    for number in result:
        print(str(number))
        