"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during
September 2016.".
"""
if __name__ == '__main__':
    total_duration = 0
    number_with_longest_duration = ''
    call_records = dict()  # store phone number and total duration in the period

    for call in calls:
        outoging_number = call[0]
        incoming_number = call[1]
        duration_of_each_call = call[3]

        # store duration for outgoing numbers
        if call_records.__contains__(outoging_number):  # already contain the number, add up duration
            existing_duration = call_records[outoging_number]
            call_records[outoging_number] = int(existing_duration) + int(duration_of_each_call)
        else: # doesn't exist, store the duration with the number
            call_records[outoging_number] = duration_of_each_call

        # store duration for incoming numbers
        if call_records.__contains__(incoming_number):  # already contain the number, add up duration
            existing_duration = call_records[incoming_number]
            call_records[incoming_number] = int(existing_duration) + int(duration_of_each_call)
        else: # doesn't exist, store the duration with the number
            call_records[incoming_number] = duration_of_each_call

    # check which number has the most duration
    for key, value in call_records.items():
        if int(value) >= int(total_duration):
            total_duration = value
            number_with_longest_duration = key

    print(number_with_longest_duration + " spent the longest time, "
          + str(total_duration) + " seconds, on the phone during September 2016.")
    