# ---------------------------------------------------------------------------- #
# Title: Pickling and Exception Handling
# Description: Working with pickles and exceptions
# ChangeLog (Who,When,What):
# Jonathan Ou, 05/23/2021, Created started script
# Jonathan Ou, 05/24/2021, Changed entries to pickle
# Jonathan Ou, 05/24/2021, Unpickled entries and printed results
# Jonathan Ou, 05/25/2021, Inserted exception handling
# ---------------------------------------------------------------------------- #

import pickle  # This imports code from another code file!

try:
    lunchItem = str(input("What do you want to have for lunch? "))
    if lunchItem.isnumeric():
        raise Exception("Do not use numbers for your food ideas!! Re-input your food choice!")
except Exception as e:
    print("There was a non-specific error!")
    print(e)
    pass
else:
    lunchTime = str(input('What time is lunch? [XX:XX AM/PM] '))
    lunch = [lunchItem, lunchTime]

# Now we store the data with the pickle.dump method
    objFile = open("LunchPlans.dat", "wb")
    pickle.dump(lunch, objFile)
    objFile.close()

# And, we read the data back with the pickle.load method
    objFile = open("LunchPlans.dat", "rb")
    lunch = pickle.load(objFile)

    objFile.close()

    print(lunch)