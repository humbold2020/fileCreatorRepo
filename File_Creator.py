file_name = input("What would you like to name your new file? ")

def file_creator(file):
    if not file.__contains__('.html'):
        file = file.__add__('.html')
    
    html_format = """<!DOCTYPE html>
    <html>
        <head>
                       
        </head>
        <body>

        </body>
    </html>
    """
   
    try:                   
        with open(file, 'x+') as new_html:
            new_html.seek(0)
            new_html.write(html_format)
    except FileExistsError:
        ow_YN = input("That file already exists, are you sure you would like to overwrite it? Y or N: ")
        ow_YN = ow_YN.upper()
        if ow_YN == 'Y':
            with open(file, 'w+') as new_html:
                new_html.seek(0)
                new_html.write(html_format)
        elif ow_YN == 'N':
            print(f"Ok, {file} will not be overwritten.")
            nf_YN = input("Do you still want to create a new file? Y or N: ")
            nf_YN = nf_YN.upper()
            if nf_YN == 'Y':
                file_creator(input(f"choose a name for your file (remember you cannont use {file}): "))
            elif nf_YN == 'N':
                print('Ok have a blessed day! Oh, and let me know if you ever need an html file!')
            else:
                print("Sorry, I am not smart enough to understand your input yet. Soon I shall be though.")
        else:
            print("Sorry, I am not smart enough to understand your input yet. Soon I shall be though.")

file_creator(file_name)    