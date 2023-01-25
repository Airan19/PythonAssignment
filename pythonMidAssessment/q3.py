"""[1,2,3,1,3,4,6,5,3] get unique numbers from list with basic constructs"""

def uniqueEle(ele_list):

  unique = list(set(ele_list))
  print('Unique Elements using the list and set inbuilt functions', unique)

  # or

  unique = []
  for ele in ele_list:
    if ele not in unique:
      unique.append(ele)
  
  return f'Unique Elements using the loop {unique}'


li = [1,2,3,1,3,4,6,5,3]
print(uniqueEle(li))
