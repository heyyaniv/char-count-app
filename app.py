from flask import Flask, request, render_template_string

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        sentence = request.form["sentence"]
        char_count = len(sentence)
        return render_template_string("""
            <form method="post">
                <label for="sentence">Enter Sentence:</label><br>
                <input type="text" id="sentence" name="sentence" value="{{ sentence }}"><br><br>
                <input type="submit" value="Submit">
            </form>
            <p>Character count: {{ char_count }}</p>
        """, sentence=sentence, char_count=char_count)
    return render_template_string("""
        <form method="post">
            <label for="sentence">Enter Sentence:</label><br>
            <input type="text" id="sentence" name="sentence"><br><br>
            <input type="submit" value="Submit">
        </form>
    """)

if __name__ == "__main__":
    app.run(debug=True)
