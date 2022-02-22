from datetime import datetime, timedelta

# Current time
time_now = datetime.now()

print("Time now", str(time_now))

# Calculating for time travel... 1 year in the future
one_year_later = time_now + timedelta(days=365)
two_days_later = time_now + timedelta(days=2)
two_days_before = time_now - timedelta(days=2)
also_two_days_before = time_now + timedelta(days=-2)

# Print future dates
print('one_year_later:', str(one_year_later))
print('two_days_later:', str(two_days_later))
print('two days before:', str(two_days_before))
print('also two days before:', str(also_two_days_before))
#formatting a date
print(f"Two Days Before today is: {also_two_days_before.strftime('%m/%d/%y')}")
pretty_formed_date = also_two_days_before.strftime('%m/%d/%y')

def count_to(n):
    startTime = datetime.now()
    for x in range(n):
        continue
    endTime = datetime.now()
    return endTime - startTime

if __name__ == '__main__':
    oTime = datetime.now()
    print(oTime.isoformat())
    print(count_to(1000000000))
