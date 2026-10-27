results = []
for i in range(3):
    if (s := "count") == "count":
        results.append(i)
        def make_closure():
            return s
        results.append(make_closure())
print(results)
