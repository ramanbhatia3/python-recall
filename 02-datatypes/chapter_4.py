# Strings - Immutable

name = "Raman"
order = "PS5"

print(f"Order for {name}: {order}")


GTA = "Grand Theft Auto"

print(f"First Word of GTA: {GTA[0:5]}")
print(f"First Word of GTA: {GTA[0:5:1]}")
print(f"First Word of GTA: {GTA[0:5:2]}")
print(f"First Word of GTA: {GTA[:5]}")
print(f"Last Word of GTA: {GTA[12:]}")
print(f"Reverse of GTA: {GTA[::-1]}")


label_text = "Spécial Text"
encoded_label = label_text.encode("utf-8")

print(f"Label Text: {label_text}")
print(f"Encoded Label: {encoded_label}")

decoded_label = encoded_label.decode("utf-8")
print(f"Decoded Label: {decoded_label}")