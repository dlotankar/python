from flask import Flask, request, render_template
app = Flask(__name__)
import sys
from io import StringIO

@app.route('/', methods=['GET', 'POST']) # Create a route at the root page that accepts get and post requests
def input():
    if(request.method == "POST"): # Check if request is a post request (If the person has submitted something through the form)
        try:
            inp=str(request.form.get('inp')).split("; ") # Get form input and split it up if multiple commands are entered
            response = ""
            for x in inp: # Loop through all commands
                old_stdout = sys.stdout
                sys.stdout = mystdout = StringIO() # This is to start recording of output in the console
                eval(x) # Evaluate expression
                sys.stdout = old_stdout # End recording of output
                response+=mystdout.getvalue() + "<br>" # Save output and add <br> tag to make a new line so the output is seperated
            return "Response: <br>" + response # Return the response to show on website
        except Exception as e:
            return "Error: " + str(e) # Show if any errors happend
    else:
        return '<!DOCTYPE html><html lang="en"><head><meta charset="UTF-8"><link href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css"rel="stylesheet"integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T" crossorigin="anonymous"> <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css"><link rel="stylesheet" type="text/css" href="../static/styles.css"/><title>CLI</title></head><body><div class="container"><h1 class="title-text" id="title-text">CLI</h1><form method="POST"><div class="input-group flex-nowrap" > <input type="text" class="form-control" placeholder="Input" name="inp" aria-label="Input" aria-describedby="addon-wrapping"> </div><button type="submit" class="btn btn-primary" id="button-main">Submit</button></form></div></body></html>'

if __name__ == '__main__':
    app.run()
