# 3.1 write a function called linear search product that takes the list of product and a target product  name  as input. the function should perform a linear search to find the target product in the list of indicesof all occurrences of the product if found,or an empty list if the product is not found

def linearSearchProduct(productList, targetProduct):
  indices = []
  
  for index, product in enumerate(productList):
    if product == targetProduct:
      indices.append(index)

  return indices

# Example usage
products = ["shoes", "boot", "loafer", "shoes", "sandal", "shoes"]
target = "shoes"
target2 = 'apple'
result = linearSearchProduct(products, target)
print(result)