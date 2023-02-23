#import required modules
import sqlite3
import traceback
import sys
import tkinter as tk
from tkinter import scrolledtext
from tkinter import messagebox
from tkinter.ttk import *

root = tk.Tk() # Creating main window
root.title("Sql Interpreter") # Title of main window
root.configure(bg = "lightblue") # Background colour of main window
tk.Label(root,text = "Query bar", width = 10).grid(row = 1, padx = 20, pady = 15)
# Creating Query bar for fetching query
query_bar = scrolledtext.ScrolledText(root,wrap = tk.WORD,height = 15,width = 80,bg = "black",fg = "yellowgreen",insertbackground = "yellowgreen")
query_bar.grid(row = 2, padx = 10, pady = 15) # Placing query bar
query_bar.focus() # creating cursor on query bar
# Creating connection and cursor object
try:
    connection = sqlite3.connect("test-db")# connection
    print("opened database successfully")
    Cursor = connection.cursor()# Cursor object
except : # handling exception if some error occur in opening database
    print("Cannot open your Database currently")
# creating function to run query
def run_query():
    try :
        
        query = query_bar.get('1.0','end - 1c') # Fetch query from query bar
        assert query.endswith(";") # Assertion for missing semicolon
        
        que = Cursor.execute(query) # Execute fetched query
        query_bar.insert(tk.INSERT,"\nQuery executed successfully") # assurance of successful execution

        out_con = tk.Toplevel(root)
        out_con.title("Output window")
        
        if query.startswith("select") :
            r1 =  0
            j = 0
            global List
            List = []
            for column in que.description : # Display column names
                e1 = tk.Entry(out_con, width = 15, fg = "black", bg = "yellow", justify = "center") # creating multiple entry widgets
                e1.grid(row = r1, column = j+5)
                e1.insert(0, column[0]) # Inserting column names inside empty entry widgets
                List.append(e1)
                j+=1
            row = 2
            for x in que : # Display rows
                for y in range(len(x)) :
                    e = tk.Entry(out_con, width = 15, fg = "blue", justify = "center")# creating entries for displaying rows
                    e.grid(row = row, column = y+5) # Placing rows
                    e.insert(0, x[y]) # Display data in rows
                    List.append(e)
                row+=1
    # Exception handing if there is syntax error
    except sqlite3.Error as er :
        tk.messagebox.showerror("Error Alert","SQLite error: %s" % (' '.join(er.args)))# Shows syntax error in message box
        query_bar.insert(tk.INSERT, "\n")
        query_bar.insert(tk.INSERT, er.__class__)#shows exception class
        query_bar.insert(tk.INSERT, "SQLite traceback: ")
        exc_type, exc_value, exc_tb = sys.exc_info()
        query_bar.insert(tk.INSERT, traceback.format_exception(exc_type, exc_value, exc_tb))
    except AssertionError : # handles exception if there is a missing semicolon in query
        tk.messagebox.showerror('Error Alert', "SQLite traceback: Missing semicolon near " + "'" + query + "'")
    except : # If any unknown error occures
        tk.messagebox.showerror('Error Alert', "unknown error has occured")
# Main function
def run_main():
    if len(query_bar.get('1.0','end - 1c'))>0 : # when query bar is not empty run query
        run_query()
def Exit() : # To exit window after user completes his work
    root.destroy() # Destroy main window
    sys.exit() # Exit console
def clear() :# Function to clear everything in query bar 
   query_bar.delete('1.0', tk.END)
   for entry in List:
       entry.destroy()
tk.Button(root, text = "Clear", command = clear,width = 20,height=2).grid(row = 2, column = 4, padx = 15, pady = 30)# Button for clearing query_bar    
tk.Button(root, text = "Execute", command = run_main, width = 20, height = 2).grid(row = 2,column = 2, padx = 15 , pady = 30) # Button to execute query
tk.Button(root, text = "Exit", command = Exit, width = 20, height = 2).grid(row = 2,column = 3) # Button for exit
root.mainloop()
    
        
