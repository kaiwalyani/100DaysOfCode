
import math
def paint_calc(height, width, cover):
  num = (height * width) / cover
  ro = math.ceil(num)
  print(f"You'll need {ro} cans of paint.")

test_h = int(input()) # Height of wall (m)
test_w = int(input()) # Width of wall (m)
coverage = 5
paint_calc(height=test_h, width=test_w, cover=coverage)
