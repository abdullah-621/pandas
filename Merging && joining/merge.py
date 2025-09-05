import pandas as pd

data1 = pd.DataFrame({
  "ID" : [1,2,3],
  "name" : ["shafi", "noman", "kalam"]
})

data2 = pd.DataFrame({
  "ID" : [1,2,4],
  "price" : [120,340,670]
})

# Different merges

# Left Join (how="left") → data1 এর সব row থাকবে
left_merge   = pd.merge(data1, data2, on="ID", how="left") 

#Right Join (how="right") → data2 এর সব row থাকবে
right_merge  = pd.merge(data1, data2, on="ID", how="right")

#Inner Join (how="inner") → শুধু matching IDs আসবে
inner_merge  = pd.merge(data1, data2, on="ID", how="inner")

# Outer Join (how="outer") → দুই দিকের সব row আসবে (missing জায়গায় NaN)
outer_merge  = pd.merge(data1, data2, on="ID", how="outer")


# cross join মানে হলো প্রতিটি DataFrame এর প্রতিটি row অন্য DataFrame এর প্রতিটি row এর সাথে মিলে যাবে → অর্থাৎ Cartesian product।
cross_merge  = pd.merge(data1, data2, how="cross")

print("Left Join:\n", left_merge)
print("\nRight Join:\n", right_merge)
print("\nInner Join:\n", inner_merge)
print("\nOuter Join:\n", outer_merge)
print("\cross Join:\n", cross_merge)