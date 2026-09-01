str = "google.com"
str1 = "Sample url"
str2 = "google"

print(str[1])
print(str[-1])
print(str[0:5]) #substring

#concatenate
print(str+str1)
# validate if a string is present in the main string
print(str2 in str)
# split strings
var = str.split(".")
print(var[0])
print(var)
# trim
str4 = " test@test.com "
print(str4.strip())
print(str4.rstrip())