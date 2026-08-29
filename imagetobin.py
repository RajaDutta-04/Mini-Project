

# # //0
# rows = 8 
# cols = 9

# 3
# rows = 8 
# cols = 8


# # //6
# rows = 30 
# cols = 30

# //5
# rows = 42 
# cols = 38

#triangle
# rows = 23
# cols = 32


from PIL import Image

img = Image.open("triangle.png")
img = img.convert("L")

width, height = img.size

rows = int(input("Enter Number of rows: "))
cols =  int(input("Enter Number of columns: "))
with open("output.txt", "w") as f:

    for r in range(rows):
        row = ""
        for c in range(cols):
            # exact boundary (FLOAT based)
            x_start = int(c * width / cols)
            x_end   = int((c + 1) * width / cols)

            y_start = int(r * height / rows)
            y_end   = int((r + 1) * height / rows)

            total = 0
            count = 0

            for y in range(y_start, y_end):
                for x in range(x_start, x_end):
                    total += img.getpixel((x, y))
                    count += 1

            avg = total / count

            if avg < 128:
                row += "1"
            else:
                row += "0"

        f.write(row + "\n")
print("Done")