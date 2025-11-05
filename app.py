from flask import Flask, render_template_string, request, redirect, url_for

app = Flask(__name__)

notes = []

# Home page that lists all notes and a form to add new notes
@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        content = request.form['note']
        notes.append(content)
        return redirect(url_for('home'))
    return render_template_string('''
        <h2>Simple Notes App</h2>
        <form method="post">
            <input type="text" name="note" placeholder="Enter note here" required>
            <input type="submit" value="Add Note">
        </form>
        <ul>
        {% for note in notes %}
            <li>{{ note }}</li>
        {% endfor %}
        </ul>
    ''', notes=notes)

if __name__ == '__main__':
    app.run(debug=True)
