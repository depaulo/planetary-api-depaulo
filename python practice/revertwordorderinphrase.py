s = []
t=("i.like.this.program.very.much")
for i in t.split("."):
    print(i)
    s.append(i)
    print(s)
s='.'.join(s[::-1])
print(s)