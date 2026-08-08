from flask import Flask, render_template

app = Flask(__name__)


# ==========================================
# HOME PAGE
# ==========================================

@app.route("/")
def home():
    return render_template("index.html")


# ==========================================
# ROUTES PAGE
# ==========================================

@app.route("/routes")
def routes():
    return render_template("routes.html")


# ==========================================
# BUS STOPS PAGE
# ==========================================

@app.route("/bus_stops")
def bus_stops():
    return render_template("bus_stops.html")


# ==========================================
# LIVE TRACKING PAGE
# ==========================================

@app.route("/tracking")
def tracking():
    return render_template("tracking.html")


# ==========================================
# AI PREDICTION PAGE
# ==========================================

@app.route("/ai_prediction")
def ai_prediction():
    return render_template("ai_prediction.html")


# ==========================================
# WEATHER PAGE
# ==========================================

@app.route("/weather")
def weather():
    return render_template("weather.html")


# ==========================================
# CONTACT PAGE
# ==========================================

@app.route("/contact")
def contact():
    return render_template("contact.html")


# ==========================================
# LOGIN PAGE
# ==========================================

@app.route("/login")
def login():
    return render_template("login.html")


# ==========================================
# REGISTER PAGE
# ==========================================

@app.route("/register")
def register():
    return render_template("register.html")


# ==========================================
# DASHBOARD PAGE
# ==========================================

@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")


# ==========================================
# BUSES PAGE
# ==========================================

@app.route("/buses")
def buses():
    return render_template("buses.html")


# ==========================================
# BUS DETAILS PAGE
# ==========================================

@app.route("/bus_details")
def bus_details():
    return render_template("bus_details.html")


# ==========================================
# SCHEDULE PAGE
# ==========================================

@app.route("/schedule")
def schedule():
    return render_template("schedule.html")


# ==========================================
# AI ASSISTANT PAGE
# ==========================================

@app.route("/ai_assistant")
def ai_assistant():
    return render_template("ai_assistant.html")


# ==========================================
# NOTIFICATIONS PAGE
# ==========================================

@app.route("/notifications")
def notifications():
    return render_template("notifications.html")


# ==========================================
# QR CODE PAGE
# ==========================================

@app.route("/qr_code")
def qr_code():
    return render_template("qr_code.html")


# ==========================================
# EMERGENCY PAGE
# ==========================================

@app.route("/emergency")
def emergency():
    return render_template("emergency.html")


# ==========================================
# FAVORITES PAGE
# ==========================================

@app.route("/favorites")
def favorites():
    return render_template("favorites.html")


# ==========================================
# FEEDBACK PAGE
# ==========================================

@app.route("/feedback")
def feedback():
    return render_template("feedback.html")


# ==========================================
# PROFILE PAGE
# ==========================================

@app.route("/profile")
def profile():
    return render_template("profile.html")


# ==========================================
# ROUTE DETAILS PAGE
# ==========================================

@app.route("/route_details")
def route_details():
    return render_template("route_details.html")


# ==========================================
# BUS STOP DETAILS PAGE
# ==========================================

@app.route("/bus_stop")
def bus_stop():
    return render_template("bus_stop.html")


# ==========================================
# RUN FLASK APPLICATION
# ==========================================

if __name__ == "__main__":
    app.run(debug=True)

