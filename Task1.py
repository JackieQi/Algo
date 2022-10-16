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
TASK 1:
How many different telephone numbers are there in the records?
Print a message:
"There are <count> different telephone numbers in the records."
"""
if __name__ == '__main__':
    number_lookup_table = set()
    for call in calls:
        # check incoming number
        if call[0] not in number_lookup_table:
            number_lookup_table.add(call[0])
        # check answering number
        if call[1] not in number_lookup_table:
            number_lookup_table.add(call[1])

    print("There are " + str(number_lookup_table.__len__()) + " different telephone numbers in the records.")