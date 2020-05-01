# Given an object/dictionary with keys and values that consist of both strings and integers, design an algorithm to calculate and return the sum of all of the numeric values.
# For example, given the following object/dictionary as input:

def returnSum(obj):

    sum = 0
    for i in obj:
        if isinstance(obj[i], int):
            sum = sum + obj[i]

    return sum

di = {
"cat": "bob",
"dog": 23,
19: 18,
90: "fish"
}

print(returnSum(di))
# Your algorithm should return 41, the sum of the values 23 and 18.