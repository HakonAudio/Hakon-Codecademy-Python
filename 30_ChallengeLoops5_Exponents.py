# 30_ChallengeLoops5_Exponents
# hakon.code@gmail.com


#Write your function here
def exponents(bases, powers):
  results = []
  for base in bases:
    for power in powers:
      results.append(base ** power)

  return results

# def exponents(bases, powers):
#   results = []
#   n = len(bases)  # define variable n as the length of bases list
#   for i in range(n):
#     result = bases[i] ** powers[i]  # raise the i-th base to the i-th power
#     results.append(result)  # add the result to the results list

#   return results


  #base_count = bases



# def exponents(bases, powers):
#   results = []
#   base_count = 0
#   for bases[base_count] in bases:
#     results = bases[base_count] ** powers[base_count]
#     base_count += 1

#   return results

#Uncomment the line below when your function is done
print(exponents([2, 3, 4], [1, 2, 3]))











# First try... returns 64, the last value of 4 ** 3

# def exponents(bases, powers):
#   results = []
#   base_count = 0
#   for bases[base_count] in bases:
#     results = bases[base_count] ** powers[base_count]
#     base_count += 1

#   return results

# #Uncomment the line below when your function is done
# print(exponents([2, 3, 4], [1, 2, 3]))