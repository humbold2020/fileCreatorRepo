file_name = input("What would you like to name your new file? ")   # Here is where you will be prompted to input the name of your file

#This function prompts the user to enter string for browser tab,
#then restores that variable surrounded by HTML "Title" tags. 
#Finally the title element is returned to the program
def add_title():                                                   
    title = input("What would you like to show up in your browser tab? ")
    title = f"<title>{title}</title>"
    return title


# This is the meat of the program.
# Defines the parameters for file creation
# So far there is only html formatting but more will come
def file_creator(file):
     
    # This could be a function somehow. I would like to prompt the user to imput file type and then set up the look of each before creation
    if not file.__contains__('.html'):
        file = file.__add__('.html')

    title = add_title() # Title function utilization

    # This variable stores the html basic skelatal format to be called upon and inserted into the file.
    # I would like to create multiple different file_formats and put them into dictionary form for increasing use cases.
    html_format = """<!DOCTYPE html>
    <html>
        <head>
            %s               
        </head>
        <body>
        </body>
    </html>
    """ % title
   
   # try/except that atempts to create a new file. Exception is if file exists already.
    try:                   
        with open(file, 'x+') as new_html: # Attempts to create a new folder. If folder exists, go to except
            new_html.seek(0)               # Brings cursor to begin of page (perhaps not needed. Will find out)
            new_html.write(html_format)    # inserts the html format created and stored within the html_format variable above
    except FileExistsError:

        # If file exists already, informs user that file exists and gives option to overwrite file
        ow_YN = input("That file already exists, are you sure you would like to overwrite it? Y or N: ")
        ow_YN = ow_YN.upper()              
        if ow_YN == 'Y':

            # If user wants to overwrite, this part of the program will perform the same code within the try statement but this time using the 'w+' argument.
            # This argument basically overwrites the existing file
            with open(file, 'w+') as new_html:
                new_html.write(html_format)

        # If user does not want to overwrite the file, the following elif statement will ask the user if they still would like to create a new file
        elif ow_YN == 'N':
            print(f"Ok, {file} will not be overwritten.")
            nf_YN = input("Do you still want to create a new file? Y or N: ")
            nf_YN = nf_YN.upper()

            # If user still wants to create a new file, program will run the file_creator function again with input warning which name could not be used.
            if nf_YN == 'Y':
                file_creator(input(f"choose a name for your file (remember you cannont use {file}): "))

            # If user no longer wants to create a file, then the program will print out a message telling the user to have a blessed day
            elif nf_YN == 'N':
                print('Ok have a blessed day! Oh, and let me know if you ever need an html file!')
        
        # Final else statements appologize for not being able to understand their input
            else:
                print("Sorry, I am not smart enough to understand your input yet. Soon I shall be though.")
        else:
            print("Sorry, I am not smart enough to understand your input yet. Soon I shall be though.")

# Finally, the file_creator function is called upon and passed the file_name variable that contains the user input
file_creator(file_name) 