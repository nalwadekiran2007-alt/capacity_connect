from flask import Flask, request, redirect, session, render_template, send_from_directory, url_for
import mysql.connector
import os

app = Flask(
    __name__,
    template_folder="../frontend"
)
# Secret key
app.secret_key = os.getenv(
    "SECRET_KEY",
    "capacity_connect_secret_key"
)


# =====================================================
# DATABASE CONNECTION
# =====================================================

def get_db_connection():
    return mysql.connector.connect(
        host=os.getenv("DB_HOST", "localhost"),
        user=os.getenv("DB_USER", "root"),
        password=os.getenv("DB_PASSWORD", ""),
        database=os.getenv("DB_NAME", "capacity_connect"),
        port=int(os.getenv("DB_PORT", "3306"))
    )


# =====================================================
# HOME
# =====================================================

@app.route("/")
def home():
    return render_template("index.html")

# =====================================================
# TEST DATABASE
# =====================================================

@app.route("/test-db")
def test_db():

    try:
        db = get_db_connection()

        if db.is_connected():
            db.close()
            return "Database Connected Successfully!"

    except mysql.connector.Error as err:
        return f"Database Connection Failed: {err}"


# =====================================================
# REGISTER
# =====================================================

@app.route("/register", methods=["POST"])
def register():

    name = request.form["name"]
    email = request.form["email"]
    password = request.form["password"]

    try:
        db = get_db_connection()
        cursor = db.cursor()

        sql = """
        INSERT INTO users (name, email, password)
        VALUES (%s, %s, %s)
        """

        cursor.execute(sql, (name, email, password))

        db.commit()

        cursor.close()
        db.close()

        return "Registration Successful!"

    except mysql.connector.Error as err:
        return f"Registration Failed: {err}"


# =====================================================
# LOGIN
# =====================================================

@app.route("/login", methods=["POST"])
def login():

    email = request.form["email"]
    password = request.form["password"]

    try:
        db = get_db_connection()
        cursor = db.cursor()

        sql = """
        SELECT * FROM users
        WHERE email = %s AND password = %s
        """

        cursor.execute(sql, (email, password))

        user = cursor.fetchone()

        cursor.close()
        db.close()

        if user:

            session["user_id"] = user[0]
            session["user_name"] = user[1]
            session["user_email"] = user[2]

            return redirect(url_for("dashboard"))

        else:
            return "Invalid Email or Password!"

    except mysql.connector.Error as err:
        return f"Login Failed: {err}"


# =====================================================
# DASHBOARD
# =====================================================

@app.route("/dashboard")
def dashboard():

    if "user_id" not in session:
        return redirect(url_for("home"))

    return render_template("dashboard.html")


# =====================================================
# ADMIN DASHBOARD
# =====================================================

@app.route("/admin")
def admin():

    if "user_id" not in session:
        return redirect(url_for("home"))

    try:

        db = get_db_connection()
        cursor = db.cursor()

        # Registered Users Count
        cursor.execute("SELECT COUNT(*) FROM users")
        user_count = cursor.fetchone()[0]

        # Registered Users Information
        cursor.execute("SELECT id, name, email FROM users")
        users = cursor.fetchall()

        # Total Courses
        course_count = 4

        # Total Certificates
        certificate_count = 4

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


# =====================================================
# DELETE USER
# =====================================================

@app.route("/delete-user/<int:user_id>")
def delete_user(user_id):

    if "user_id" not in session:
        return redirect(url_for("home"))

    try:

        db = get_db_connection()
        cursor = db.cursor()

        cursor.execute(
            "DELETE FROM users WHERE id = %s",
            (user_id,)
        )

        db.commit()

        cursor.close()
        db.close()

        return redirect(url_for("admin"))

    except mysql.connector.Error as err:
        return f"Delete User Failed: {err}"


# =====================================================
# COURSES
# =====================================================

@app.route("/courses")
def courses():

    if "user_id" not in session:
        return redirect(url_for("home"))

    return render_template("courses.html")


# =====================================================
# PROGRESS
# =====================================================

@app.route("/progress")
def progress():

    if "user_id" not in session:
        return redirect(url_for("home"))

    return render_template("progress.html")


# =====================================================
# LEARNING GOALS
# =====================================================

@app.route("/learning-goals")
def learning_goals():

    if "user_id" not in session:
        return redirect(url_for("home"))

    return render_template("learning-goals.html")


# =====================================================
# CERTIFICATES
# =====================================================

@app.route("/certificates")
def certificates():

    if "user_id" not in session:
        return redirect(url_for("home"))

    return render_template(
        "certificates.html",
        name=session["user_name"]
    )


# =====================================================
# VERIFY CERTIFICATE
# =====================================================

@app.route("/verify-certificate")
def verify_certificate():

    return render_template("verify-certificate.html")


# =====================================================
# PYTHON CERTIFICATE
# =====================================================

@app.route("/download-certificate")
def download_certificate():

    if "user_id" not in session:
        return redirect(url_for("home"))

    return send_from_directory(
        "static/certificates",
        "Kiran_Python_Certificate.pdf",
        as_attachment=True
    )


# =====================================================
# JAVA CERTIFICATE
# =====================================================

@app.route("/download-java-certificate")
def download_java_certificate():

    if "user_id" not in session:
        return redirect(url_for("home"))

    return send_from_directory(
        "static/certificates",
        "Kiran_Java_Certificate.pdf",
        as_attachment=True
    )


# =====================================================
# WEB CERTIFICATE
# =====================================================

@app.route("/download-web-certificate")
def download_web_certificate():

    if "user_id" not in session:
        return redirect(url_for("home"))

    return send_from_directory(
        "static/certificates",
        "Kiran_Web_Certificate.pdf",
        as_attachment=True
    )


# =====================================================
# DATA CERTIFICATE
# =====================================================

@app.route("/download-data-certificate")
def download_data_certificate():

    if "user_id" not in session:
        return redirect(url_for("home"))

    return send_from_directory(
        "static/certificates",
        "Kiran_Data_Certificate.pdf",
        as_attachment=True
    )


# =====================================================
# PYTHON COURSE
# =====================================================

@app.route("/python-course")
def python_course():

    if "user_id" not in session:
        return redirect(url_for("home"))

    return render_template("Python-course.html")


# =====================================================
# JAVA COURSE
# =====================================================

@app.route("/java-course")
def java_course():

    if "user_id" not in session:
        return redirect(url_for("home"))

    return render_template("Java-course.html")


# =====================================================
# WEB COURSE
# =====================================================

@app.route("/web-course")
def web_course():

    if "user_id" not in session:
        return redirect(url_for("home"))

    return render_template("Web-course.html")


# =====================================================
# DATA COURSE
# =====================================================

@app.route("/data-course")
def data_course():

    if "user_id" not in session:
        return redirect(url_for("home"))

    return render_template("data-course.html")


# =====================================================
# PROFILE
# =====================================================

@app.route("/profile")
def profile():

    if "user_id" not in session:
        return redirect(url_for("home"))

    return render_template(
        "profile.html",
        name=session["user_name"],
        email=session["user_email"]
    )


# =====================================================
# LOGOUT
# =====================================================

@app.route("/logout")
def logout():

    session.clear()

    return redirect(url_for("home"))


# =====================================================
# RUN APPLICATION
# =====================================================

if __name__ == "__main__":

    port = int(os.environ.get("PORT", 5000))

    app.run(
        host="0.0.0.0",
        port=port,
        debug=False
    )