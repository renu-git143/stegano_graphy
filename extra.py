from PIL import Image

# Creates a simple blue banner (600px x 100px)
banner = Image.new("RGB", (600, 100), color=(100, 150, 255))
banner.save("banner.png")

print("✅ Dummy banner created successfully.")
