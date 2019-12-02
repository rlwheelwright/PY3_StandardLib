# Zipfile Module
import zipfile

# Open and List
zip = zipfile.ZipFile('Archive.zip', 'r')
print(zip.namelist()) # Lists everything within zip file

# Metadata in the zip folder
for meta in zip.infolist(): # List of the metadata within zip file
    print(meta)

info = zip.getinfo("purchased.txt")

# Access to files in zip folder
print(zip.read("wishlist.txt"))
with zip.open('wishlist.txt') as f: # establishing f = zip.open('wishlist.txt')
    print(f.read())

# Extracting files
zip.extract('purchased.txt') # Extract just the one file
input("Continue? Press any key.")
zip.extractall() # Extracts everything

# Closing the zip
zip.close()
