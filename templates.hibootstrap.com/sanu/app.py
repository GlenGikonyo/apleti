from flask import Flask, render_template,url_for
from waitress import serve

app = Flask(__name__)

# Define routes for the listed HTML files
@app.route('/404.html')
def render_404():
    return render_template('404.html')

@app.route('/academics-details.html')
def render_academics_details():
    return render_template('academics-details.html')

@app.route('/academics.html')
def render_academics():
    return render_template('academics.html')

@app.route('/admission.html')
def render_admission():
    return render_template('admission.html')

@app.route('/alumni.html')
def render_alumni():
    return render_template('alumni.html')

@app.route('/campus-life.html')
def render_campus_life():
    return render_template('campus-life.html')

@app.route('/contact-us.html')
def render_contact_us():
    return render_template('contact-us.html')

@app.route('/contact.html')
def render_contact():
    return render_template('contact.html')

@app.route('/courses-details.html')
def render_courses_details():
    return render_template('courses-details.html')

@app.route('/courses.html')
def render_courses():
    return render_template('courses.html')

@app.route('/events-details.html')
def render_events_details():
    return render_template('events-details.html')

@app.route('/events.html')
def render_events():
    return render_template('events.html')

@app.route('/faq.html')
def render_faq():
    return render_template('faq.html')

@app.route('/graduate-admission.html')
def render_graduate_admission():
    return render_template('graduate-admission.html')

@app.route('/health-care-details.html')
def render_health_care_details():
    return render_template('health-care-details.html')

@app.route('/health-care.html')
def render_health_care():
    return render_template('health-care.html')

@app.route('/')
def render_index_2():
    return render_template('index-2.html')

@app.route('/latest-news.html')
def render_latest_news():
    return render_template('latest-news.html')

@app.route('/login.html')
def render_login():
    return render_template('login.html')

@app.route('/news-details.html')
def render_news_details():
    return render_template('news-details.html')

@app.route('/privacy-policy.html')
def render_privacy_policy():
    return render_template('privacy-policy.html')

@app.route('/recover-password.html')
def render_recover_password():
    return render_template('recover-password.html')

@app.route('/register.html')
def render_register():
    return render_template('register.html')

@app.route('/terms-conditions.html')
def render_terms_conditions():
    return render_template('terms-conditions.html')

if __name__ == "__main__":
    # Run Flask app using Waitress server
    # serve(app, host="0.0.0.0", port=8080)
     app.run(debug=True, host="0.0.0.0", port=5000)
