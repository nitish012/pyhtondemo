x={
    "car":"blue",
    "color":"red"
}
print (x["color"])
print (x.get("car"))
print (x.get("cart","bmw"))
x["color"]='ferarri'
print (x["color"])

for y in x:
    print (y)

x=lambda a:a/3
print (x(12))