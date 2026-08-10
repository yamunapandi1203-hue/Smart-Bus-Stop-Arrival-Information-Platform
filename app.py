from flask import Flask, render_template, request, redirect, url_for
from database import get_connection

app = Flask(__name__)


# =========================================================
# HOME
# =========================================================

@app.route("/")
def home():
    return render_template("index.html")


# =========================================================
# REGISTER
# =========================================================

@app.route("/register", methods=["GET", "POST"])
def register():

    if request.method == "POST":

        name = request.form["name"]
        email = request.form["email"]
        password = request.form["password"]

        try:
            connection = get_connection()
            cursor = connection.cursor()

            query = """
                INSERT INTO users (name, email, password)
                VALUES (%s, %s, %s)
            """

            values = (name, email, password)

            cursor.execute(query, values)
            connection.commit()

            cursor.close()
            connection.close()

            return redirect(url_for("login"))

        except Exception as error:
            return f"Registration error: {error}"

    return render_template("register.html")


# =========================================================
# LOGIN
# =========================================================

@app.route("/login", methods=["GET", "POST"])
def login():

    if request.method == "POST":

        email = request.form["email"]
        password = request.form["password"]

        try:
            connection = get_connection()
            cursor = connection.cursor()

            query = """
                SELECT *
                FROM users
                WHERE email = %s AND password = %s
            """

            values = (email, password)

            cursor.execute(query, values)

            user = cursor.fetchone()

            cursor.close()
            connection.close()

            if user:
                return redirect(url_for("home"))

            else:
                return "Invalid email or password"

        except Exception as error:
            return f"Login error: {error}"

    return render_template("login.html")


# =========================================================
# ROUTES
# =========================================================

@app.route("/routes")
def routes():
    return render_template("routes.html")


# =========================================================
# BUS STOPS
# =========================================================

@app.route("/bus_stops")
def bus_stops():

    try:
        connection = get_connection()

        cursor = connection.cursor(dictionary=True)

        cursor.execute("""
            SELECT *
            FROM bus_stops
            ORDER BY id
        """)

        stops = cursor.fetchall()

        cursor.close()
        connection.close()

        return render_template(
            "bus_stops.html",
            stops=stops
        )

    except Exception as error:
        return f"Bus stops database error: {error}"


# =========================================================
# BUSES
# =========================================================

@app.route("/buses")
def buses():

    try:
        connection = get_connection()

        cursor = connection.cursor(dictionary=True)

        cursor.execute("""
            SELECT *
            FROM buses
            ORDER BY id
        """)

        buses = cursor.fetchall()

        cursor.close()
        connection.close()

        return render_template(
            "buses.html",
            buses=buses
        )

    except Exception as error:
        return f"Bus database error: {error}"


# =========================================================
# LIVE TRACKING
# =========================================================

@app.route("/tracking")
def tracking():
    return render_template("tracking.html")


# =========================================================
# AI PREDICTION
# =========================================================

@app.route("/ai_prediction")
def ai_prediction():
    return render_template("ai_prediction.html")


# =========================================================
# WEATHER
# =========================================================

@app.route("/weather")
def weather():
    return render_template("weather.html")
# =========================================================
# CONTACT
# =========================================================

@app.route("/contact")
def contact():
    return render_template("contact.html")


# =========================================================
# DATABASE TEST
# =========================================================

@app.route("/test_db")
def test_db():

    try:
        connection = get_connection()

        cursor = connection.cursor()

        cursor.execute("SELECT DATABASE()")

        result = cursor.fetchone()

        cursor.close()
        connection.close()

        return f"Connected database: {result[0]}"

    except Exception as error:
        return f"Database connection error: {error}"


# =========================================================
# RUN APPLICATION
# =========================================================

if __name__ == "__main__":
    app.run(debug=True)