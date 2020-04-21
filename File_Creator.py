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

file_creator(file_name)    