from flask import Flask, render_template_string, request
from datetime import datetime

app = Flask(__name__)

def get_color_hex(color_name):
    colors = {"black": "000000", "red": "ff0000", "green": "00ff00", "yellow": "ffff00", "blue": "0000ff", 
              "magenta": "ff00ff", "cyan": "00ffff", "white": "ffffff"}
    return colors.get(color_name.lower(), color_name)

@app.route('/', methods=['GET', 'POST'])
def color_alert():
    if request.method == 'POST':
        name = request.form['name']
        id_no = request.form['id_no']
        id_text_color = get_color_hex(request.form['id_text_color'])
        id_background_color = get_color_hex(request.form['id_background_color'])
        due_date = request.form['due_date']
        today = datetime.today().date()

        due_date_obj = datetime.strptime(due_date, '%Y-%m-%d').date()
        overdue = due_date_obj < today

        if overdue:
            id_background_color = 'fa00bc'
            id_no = ''  # Hide ID for overdue

        return render_template_string("""
            <h1>Details</h1>
            <p>Name: {{name}}</p>
            <p>Due Date: {{due_date}} ({{'Overdue' if overdue else 'Upcoming'}})</p>
            <p>ID: <span style="color:#{{id_text_color}}; background-color:#{{id_background_color}};">{{id_no}}</span></p>
            """, name=name, due_date=due_date, overdue=overdue, id_no=id_no, id_text_color=id_text_color, id_background_color=id_background_color)
    
    return '''
        <form method="POST">
            Name: <input type="text" name="name"><br>
            ID No: <input type="text" name="id_no"><br>
            ID Text Colour: <input type="text" name="id_text_color"><br>
            ID Background Colour: <input type="text" name="id_background_color"><br>
            Due Date (YYYY-MM-DD): <input type="text" name="due_date"><br>
            <input type="submit">
        </form>
    '''

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)

