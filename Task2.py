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
    call_records = dict() # store phone number and total duration in the period

    for call in calls:
        phone_number_to_check = call[1]
        duration_of_each_call = call[3]
        if call_records.__contains__(phone_number_to_check): # already contain the number, add up duration
            existing_duration = call_records[phone_number_to_check]
            call_records[phone_number_to_check] = int(existing_duration) + int(duration_of_each_call)
        else: # doesn't exist, store the duration with the number
            call_records[phone_number_to_check] = duration_of_each_call


    # check which number has the most duration
    for key, value in call_records.items():
        if int(value) >= int(total_duration):
            total_duration = value
            number_with_longest_duration = key

    print(number_with_longest_duration + " spent the longest time, " + str(total_duration) + " seconds, on the phone during September 2016.")
    