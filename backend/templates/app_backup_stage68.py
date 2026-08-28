from flask import Flask, request, redirect, session, render_template, send_from_directory
import mysql.connector

app = Flask(__name__)

app.secret_key = "capacity_connect_secret_key"


@app.route("/")
def home():
    return "Welcome to CAPACITY CONNECT!"


@app.route("/test-db")
def test_db():
    try:
        db = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Capacity@123",
            database="capacity_connect"
        )

        if db.is_connected():
            db.close()
            return "Database Connected Successfully!"

    except mysql.connector.Error as err:
        return f"Database Connection Failed: {err}"


@app.route("/register", methods=["POST"])
def register():

    name = request.form["name"]
    email = request.form["email"]
    password = request.form["password"]

    try:
        db = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Capacity@123",
            database="capacity_connect"
        )

        cursor = db.cursor()

        sql = """
        INSERT INTO users (name, email, password)
        VALUES (%s, %s, %s)
        """

        values = (name, email, password)

        cursor.execute(sql, values)
        db.commit()

        cursor.close()
        db.close()

        return "Registration Successful!"

    except mysql.connector.Error as err:
        return f"Registration Failed: {err}"


@app.route("/login", methods=["POST"])
def login():

    email = request.form["email"]
    password = request.form["password"]

    try:
        db = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Capacity@123",
            database="capacity_connect"
        )

        cursor = db.cursor()

        sql = """
        SELECT * FROM users
        WHERE email = %s AND password = %s
        """

        values = (email, password)

        cursor.execute(sql, values)

        user = cursor.fetchone()

        cursor.close()
        db.close()

        if user:

            session["user_id"] = user[0]
            session["user_name"] = user[1]
            session["user_email"] = user[2]

            return redirect("http://127.0.0.1:5000/dashboard")

        else:
            return "Invalid Email or Password!"

    except mysql.connector.Error as err:
        return f"Login Failed: {err}"


@app.route("/dashboard")
def dashboard():

    if "user_id" not in session:
        return redirect("http://127.0.0.1:5500/frontend/login.html")

    return render_template("dashboard.html")
@app.route("/admin")
def admin():

    if "user_id" not in session:
        return redirect("http://127.0.0.1:5500/frontend/login.html")

    try:

        db = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Capacity@123",
            database="capacity_connect"
        )

        cursor = db.cursor()

        cursor.execute("SELECT COUNT(*) FROM users")

        user_count = cursor.fetchone()[0]
        cursor.execute("SELECT id, name, email FROM users")

        users = cursor.fetchall()
        course_count = 4
        certificate_count =4

        cursor.close()
        db.close()

        return render_template(
    "admin.html",
    user_count=user_count,
    users=users,
    course_count=course_count,
    certificate_count=certificate_count
)

    except mysql.connector.Error as err:

        return f"Admin Database Error: {err}"
@app.route("/courses")
def courses():
    if "user_id" not in session:
        return redirect("http://127.0.0.1:5500/frontend/login.html")

    return render_template("courses.html")
@app.route("/progress")
def progress():
    if "user_id" not in session:
        return redirect("http://127.0.0.1:5500/frontend/login.html")

    return render_template("progress.html")
@app.route("/learning-goals")
def learning_goals():
    if "user_id" not in session:
        return redirect("/login")

    return render_template("learning-goals.html")
@app.route("/certificates")
def certificates():
    if "user_id" not in session:
        return redirect("http://127.0.0.1:5500/frontend/login.html")

    return render_template(
    "certificates.html",
    name=session["user_name"]
)
@app.route("/verify-certificate")
def verify_certificate():

    return render_template("verify-certificate.html")
@app.route("/download-certificate")
def download_certificate():
    if "user_id" not in session:
        return redirect("http://127.0.0.1:5500/frontend/login.html")

    return send_from_directory(
        "static/certificates",
        "Kiran_python_Certificate.pdf",
        as_attachment=True
    )
@app.route("/download-java-certificate")
def download_java_certificate():
    if "user_id" not in session:
        return redirect("http://127.0.0.1:5500/frontend/login.html")

    return send_from_directory(
        "static/certificates",
        "Kiran_Java_Certificate.pdf",
        as_attachment=True
    )


@app.route("/download-web-certificate")
def download_web_certificate():
    if "user_id" not in session:
        return redirect("http://127.0.0.1:5500/frontend/login.html")

    return send_from_directory(
        "static/certificates",
        "Kiran_Web_Certificate.pdf",
        as_attachment=True
    )


@app.route("/download-data-certificate")
def download_data_certificate():
    if "user_id" not in session:
        return redirect("http://127.0.0.1:5500/frontend/login.html")

    return send_from_directory(
        "static/certificates",
        "Kiran_Data_Certificate.pdf",
        as_attachment=True
    )
@app.route("/python-course")
def python_course():
    if "user_id" not in session:
        return redirect("http://127.0.0.1:5500/frontend/login.html")

    return render_template("Python-course.html")
@app.route("/java-course")
def java_course():
    if "user_id" not in session:
        return redirect("http://127.0.0.1:5500/frontend/login.html")

    return render_template("Java-course.html")
@app.route("/web-course")
def web_course():
    if "user_id" not in session:
        return redirect("http://127.0.0.1:5500/frontend/login.html")

    return render_template("Web-course.html")
@app.route("/data-course")
def data_course():
    if "user_id" not in session:
        return redirect("http://127.0.0.1:5500/frontend/login.html")

    return render_template("data-course.html")

@app.route("/profile")
def profile():

    if "user_id" not in session:
        return redirect("http://127.0.0.1:5500/frontend/login.html")

    return render_template(
        "profile.html",
        name=session["user_name"],
        email=session["user_email"]
    )


@app.route("/logout")
def logout():

    session.clear()

    return redirect("http://127.0.0.1:5500/frontend/login.html")


if __name__ == "__main__":
    app.run(debug=True)