#Create a lambda function that returns another lambda function which multiplies its argument by a given factor.

mul = lambda n: lambda x: x * n

print(mul(5)(10))
