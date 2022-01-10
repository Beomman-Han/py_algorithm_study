[A, B, C] = [ int(x) for x in input().strip().split() ]

val_1 = (A + B) % C
val_2 = ((A % C) + (B % C)) % C
print(val_1)
print(val_2)

val_3 = (A * B) % C
val_4 = ((A % C) * (B % C)) % C
print(val_3)
print(val_4)
