# Tempfile Module # Create temporary files in Python
import tempfile

# Create a temporary file
tempFile = tempfile.TemporaryFile() # Creates temporary file

# Write to a temporary file
tempFile.write(b"Save this special number for me: 8675309") # bytes literal
tempFile.seek(0)

# Read the temporary file
print(tempFile.read())

# Close the temporary file
tempFile.close()
