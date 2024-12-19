# Interactive Lab: Sorting Files by Type

## 🎯 Objective
Extend our file management skills by creating a script that sorts files into subdirectories based on their file extensions.

## 📚 Pre-lab Reading
- [Python os.path module](https://docs.python.org/3/library/os.path.html) (10 minutes)

## 🧪 Lab Steps

### Step 1: Setup (5 minutes)
1. Open your IDE (PyCharm or VS Code).
2. Create a new file named `file_sorter.py`.
3. At the top of the file, add the following line to import the `os` module:
   ```python
   import os
   ```

###
---
### Step 2: Implement File Type Detection (20 minutes)

1. Create a function to determine the file type based on its extension:
   ```python
   def get_file_type(filename):
       _, extension = os.path.splitext(filename)
       extension = extension.lower()
       
       if extension in ['.jpg', '.png', '.gif']:
           return 'Images'
       elif extension in ['.doc', '.docx', '.txt', '.pdf']:
           return 'Documents'
       elif extension in ['.mp3', '.wav']:
           return 'Audio'
       else:
           return 'Other'
   ```

   Explanation:
   - `os.path.splitext(filename)` splits the filename into two parts: the name and the extension.
   - We use `_` to ignore the name part and only keep the extension.
   - `.lower()` converts the extension to lowercase to make our comparisons case-insensitive.
   - We then use if-elif statements to categorize the file based on its extension.

2. Test this function:
   Add the following code at the end of your file:
   ```python
   # Test get_file_type function
   test_files = ['vacation.jpg', 'report.docx', 'song.mp3', 'script.py']
   for file in test_files:
       print(f"{file} is a {get_file_type(file)} file")
   ```

Create a test folder with sample files:
- In your file explorer, navigate to the directory where your `file_sorter.py` script is located.
- Create a new folder named "test_files".
- Inside "test_files", create the following empty files:
    - vacation.jpg
    - report.docx
    - song.mp3
    - script.py

> [!NOTE] Test Files
> You can create these files by right-clicking in the folder, selecting "New File" and then naming them with the appropriate extensions.

3. Test the `get_file_type` function:
   Add the following code at the end of your file:
   ```python
   # Test get_file_type function
   test_directory = os.path.join(os.getcwd(), "test_files")
   test_files = os.listdir(test_directory)
   for file in test_files:
       print(f"{file} is a {get_file_type(file)} file")
   ```

4. Run your script:
   - Open a terminal and type `python file_sorter.py`

   You should see output like:
   ```
   vacation.jpg is a Images file
   report.docx is a Documents file
   song.mp3 is a Audio file
   script.py is a Other file
   ```

###
---
### Step 3: Implement File Sorting (25 minutes)

1. Create a function to sort files into subdirectories:
   ```python
   def sort_files(directory):
       for filename in os.listdir(directory):
           if os.path.isfile(os.path.join(directory, filename)):
               file_type = get_file_type(filename)
               type_dir = os.path.join(directory, file_type)
               
               if not os.path.exists(type_dir):
                   os.makedirs(type_dir)
               
               old_path = os.path.join(directory, filename)
               new_path = os.path.join(type_dir, filename)
               os.rename(old_path, new_path)
               print(f"Moved {filename} to {file_type} folder")
   ```

   Explanation:
   - `os.listdir(directory)` lists all files and directories in the given directory.
   - `os.path.isfile()` checks if the item is a file (not a directory).
   - We create a new directory for each file type if it doesn't exist.
   - `os.rename()` moves the file to its new location.

Test this function:
   We'll use the "test_files" directory we created earlier. Add the following code at the end of your file:
   ```python
   # Test sort_files function
   test_directory = os.path.join(os.getcwd(), "test_files")
   sort_files(test_directory)
   ```

3. Run your script again. You should see output indicating that files were moved to their respective type folders.

4. Check your "test_files" directory in your file explorer. You should see new subdirectories created for each file type (Images, Documents, Audio, Other), with the files moved into their respective folders.

###
---
### Step 4: Implement User Input and Main Script (15 minutes)

1. Create the main part of the script:
   ```python
   if __name__ == "__main__":
       directory = input("Enter the directory path to sort: ")
       if os.path.exists(directory):
           sort_files(directory)
           print("Sorting complete!")
       else:
           print("The specified directory does not exist.")
   ```

   Explanation:
   - `__name__ == "__main__"` ensures this code only runs if the script is executed directly.
   - We use `input()` to get the directory path from the user.
   - `os.path.exists()` checks if the specified directory exists before attempting to sort it.

1. Test the full script:
   - Remove or comment out the test code from steps 2 and 3.
   - Create new files or "undo" the previous sorting by moving files out of directories (*creating new files is simpler*)
   - Run your script again.
   - When prompted, enter the path to your "test_files" directory. You can copy this path from your file explorer.
     - On Windows, it might look like: C:\Users\YourUsername\path\to\test_files
     - On Mac or Linux, it might look like: /Users/YourUsername/path/to/test_files
   - Check your "test_files" directory again to confirm that the files have been sorted into the appropriate subdirectories.
###
---
### Wrap-Up

📝 Reflection Question: How might this file sorting script be useful in a game development or digital content creation workflow?

## 🧠 Knowledge Check Quiz
1. What does the `os.path.splitext()` function do?
2. Why do we convert the file extension to lowercase?
3. How does the script handle file types it doesn't recognize?

## 🏆 Bonus Challenge
Modify the script to count how many files of each type were sorted and print a summary at the end. Here's a hint to get you started:

```python
file_counts = {'Images': 0, 'Documents': 0, 'Audio': 0, 'Other': 0}
# Update these counts in your sort_files function
# Print the summary after sorting is complete
```

> [!NOTE] Introduction to Dictionaries
> In this bonus challenge, we use a new data structure called a `dictionary`. A dictionary in Python is a collection that stores key-value pairs. It's like a real-world dictionary where you have a word (the key) and its definition (the value).
>
> In our script, we use a dictionary like this:
> ```python
> file_counts = {'Images': 0, 'Documents': 0, 'Audio': 0, 'Other': 0}
> ```
> Dictionaries are very useful for keeping track of counts or associating related pieces of information.
>
> To learn more about dictionaries, check out this detailed explanation from GeeksforGeeks: [Python Dictionary](https://www.geeksforgeeks.org/python-dictionary/)
