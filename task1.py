#Task 1
def calculate_area(length,width):
  if length==width:
    return "This is a square!"
  else:
    area_of_rectangle=(length*width)
    return area_of_rectangle
inp1=float(input(""))
inp2=float(input(""))
output=calculate_area(inp1,inp2)
print(output)

