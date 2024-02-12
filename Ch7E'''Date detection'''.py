import re

pattern = re.compile(r"""
        (?P<day>31|(?:0[1-9]|[1-2][0-9]))/          # days
        (?P<month>1[0-2]|0[1-9])/                   # months range from 01 to 12
        (?P<year>1000|d\d{3}|2[0-9]{3})             # year in range 1000 - 9999
""", re.VERBOSE)

date1 = '09/09/2022'
date2 = '31/02/1000'
date3 = '07/12/1999'
date4 = '12/02/2024'

# Concatenate the strings or use a single string containing all dates
combined_dates = ' '.join([date1, date2, date3, date4])

# Find all occurrences of the date pattern in the combined string
matches = pattern.finditer(combined_dates)

# Print the matches
for match in matches:
    print("Day:", match.group('day'))
    print("Month:", match.group('month'))
    print("Year:", match.group('year'))
