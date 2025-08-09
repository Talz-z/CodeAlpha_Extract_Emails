# CodeAlpha_Extract_Emails
This repo consists of a task assigned by CodeAlpha for Python Programming

 # Task 3: Email Extractor

 ## Description
A Python script that extracts email addresses from text files using regular expressions. The program reads an input file, identifies all valid email patterns, and saves them to a new file with each email on a separate line.

 ## Key Features:
- Reads text content from "input.txt"
- Uses regex pattern matching to identify emails
- Handles various email formats (special characters, domains)
- Writes extracted emails to "emails.txt"
- Simple file handling operations
- Completion confirmation message

 ## How It Works:
1. Opens and reads "input.txt" file
2. Uses regex pattern `r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'` to:
   - Match standard email formats
   - Handle special characters (._%+-)
   - Recognize various domain extensions (.com, .org, .edu)
3. Writes results to "emails.txt" with line separation
4. Prints completion confirmation

 ## File Handling:
- Sequential file operations:
  1. Open input file (read mode)
  2. Process content
  3. Open output file (write mode)
  4. Write results
  5. Close files
- Minimal error handling (assumes input.txt exists)

