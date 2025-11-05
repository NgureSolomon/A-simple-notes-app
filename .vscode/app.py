from flask import Flask, request, render_template_string

app = Flask(__name__)
notes = []

HTML = '''
<html>
<head><title>Notes App</title></head>
<body>
  <h1>Notes</h1>
  <form method="POST">
    <input type="text" name="note" placeholder="Write a note">
    <input type="submit" value="Add Note">
  </form>
  <ul>
    {% for note in notes %}
      <li>{{ note }}</li>
    {% endfor %}
  </ul>
</body>
</html>
'''

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        note = request.form.get('note')
        if note:
            notes.append(note)
    return render_template_string(HTML, notes=notes)

if __name__ == '__main__':
    app.run(debug=True)
