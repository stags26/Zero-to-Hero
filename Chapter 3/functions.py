barrel_length = ['10.5', '11.5', '12.5', '13.5', '14.5', '16', '18']

print (f"Here is a list of desired barrel length for 5.56 NATO: {barrel_length}")
print (f"I currently have a {barrel_length[0]}, {barrel_length[4]}, and a {barrel_length[-1]} inch barrels.")
print (f"I want to build a  {barrel_length[1]}")
print (f"After i build a {barrel_length[1]}, I will build a {barrel_length[2]}.")
print (f"Maybe I'll buy a {barrel_length[3]} and a {barrel_length[-2]}.")

popped_barrel= barrel_length.pop(0)
print (f"The only AR that is in .300blk is my {popped_barrel}.")
purchased_ar = '18'
barrel_length.remove(purchased_ar)
print (f"Currently, the only AR I did not build is my {purchased_ar}.")
barrel_length.append(popped_barrel)
barrel_length.append(purchased_ar)

barrel_length.sort()
print (f"Here is the current list again of AR barrel lengths: {sorted(barrel_length)}")
barrel_length.sort(reverse=True)
print (f"Here it is in descending order: {barrel_length}")
print (f"There are {len(barrel_length)} barrel lengths.")
# print (barrel_length[7]) induced error