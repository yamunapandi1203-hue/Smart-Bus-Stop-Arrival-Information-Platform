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
# ROUTE DETAILS
# =========================================================

@app.route("/route-details/<route_number>")
def route_details(route_number):

    connection = get_connection()
    cursor = connection.cursor(dictionary=True)

    cursor.execute(
        "SELECT * FROM routes WHERE route_number = %s",
        (route_number,)
    )

    route = cursor.fetchone()

    cursor.close()
    connection.close()

    if route is None:
        return "Route not found"

    return render_template(
        "route_details.html",
        route=route
    )


# =========================================================
# BUS STOPS
# =========================================================

@app.route("/bus-stops")
def bus_stops():

    connection = get_connection()
    cursor = connection.cursor(dictionary=True)

    cursor.execute("SELECT * FROM bus_stops")

    stops = cursor.fetchall()

    cursor.close()
    connection.close()

    return render_template(
        "bus_stops.html",
        stops=stops
    )


# =========================================================
# BUSES
# =========================================================

@app.route("/buses/<int:stop_id>")
def buses(stop_id):

    connection = get_connection()
    cursor = connection.cursor(dictionary=True)

    # Get selected bus stop
    cursor.execute(
        "SELECT * FROM bus_stops WHERE id = %s",
        (stop_id,)
    )

    stop = cursor.fetchone()

    if stop is None:
        cursor.close()
        connection.close()
        return "Bus stop not found"

    # Get buses for selected bus stop
    cursor.execute(
        "SELECT * FROM busess WHERE stop_id = %s",
        (stop_id,)
    )

    buses = cursor.fetchall()

    cursor.close()
    connection.close()

    return render_template(
        "buses.html",
        stop=stop,
        buses=buses
    )


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

@app.route("/contact", methods=["GET", "POST"])
def contact():

    if request.method == "POST":

        name = request.form.get("name")
        email = request.form.get("email")
        message = request.form.get("message")

        print("================================")
        print("CONTACT MESSAGE")
        print("Name:", name)
        print("Email:", email)
        print("Message:", message)
        print("================================")

        return "Thank you! Your message has been received."

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
# SMART NOTIFICATIONS
# =========================================================

@app.route("/notifications")
def notifications():
    return render_template("notifications.html")

# =========================================================
# QR CODE
# =========================================================


@app.route("/qr-code")
def qr_code():
    return render_template("qr_code.html")
# =========================================================
# EMERGENCE
# =========================================================


@app.route("/emergency")
def emergency():
    return render_template("emergency.html")
# =========================================================
# RUN APPLICATION
# =========================================================

if __name__ == "__main__":
    app.run(debug=True)