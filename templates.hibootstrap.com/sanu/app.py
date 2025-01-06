from flask import Flask, render_template,url_for
from waitress import serve

app = Flask(__name__)

# Define routes for the listed HTML files
@app.route('/404')
def render_404():
    return render_template('404.html')

@app.route('/academics-details')
def render_academics_details():
    return render_template('academics-details.html')

@app.route('/academics')
def render_academics():
    return render_template('academics.html')

@app.route('/admission')
def render_admission():
    return render_template('admission.html')

@app.route('/alumni')
def render_alumni():
    return render_template('alumni.html')

@app.route('/campus-life')
def render_campus_life():
    return render_template('campus-life.html')

@app.route('/contact-us')
def render_contact_us():
    return render_template('contact-us.html')

@app.route('/contact')
def render_contact():
    return render_template('contact.html')

@app.route('/courses-details')
def render_courses_details():
    return render_template('courses-details.html')

@app.route('/courses')
def render_courses():
    return render_template('courses.html')

@app.route('/events-details')
def render_events_details():
    return render_template('events-details.html')

@app.route('/events')
def render_events():
    return render_template('events.html')

@app.route('/faq')
def render_faq():
    return render_template('faq.html')

@app.route('/graduate-admission')
def render_graduate_admission():
    return render_template('graduate-admission.html')

@app.route('/health-care-details')
def render_health_care_details():
    return render_template('health-care-details.html')

@app.route('/health-care')
def render_health_care():
    return render_template('health-care.html')

@app.route('/')
def render_index_2():
    return render_template('index-2.html')

@app.route('/latest-news')
def render_latest_news():
    return render_template('latest-news.html')

@app.route('/login')
def render_login():
    return render_template('login.html')

@app.route('/news-details')
def render_news_details():
    return render_template('news-details.html')

@app.route('/privacy-policy')
def render_privacy_policy():
    return render_template('privacy-policy.html')

@app.route('/recover-password')
def render_recover_password():
    return render_template('recover-password.html')

@app.route('/register')
def render_register():
    return render_template('register.html')

@app.route('/terms-conditions')
def render_terms_conditions():
    return render_template('terms-conditions.html')
# Courses Routing
@app.route('/ushering')
def ushering():
    return render_template('courses/ushering.html')


@app.route('/church')
def church():
    return render_template('courses/church.html')


@app.route('/corporate')
def corporate():
    return render_template('courses/corporate.html')


@app.route('/value')
def value():
    return render_template('courses/value.html')

@app.route('/trainer')
def trainer():
    return render_template('courses/trainer.html')

@app.route('/branding')
def branding():
    return render_template('courses/branding.html')

@app.route('/climate')
def climate():
    return render_template('courses/climate.html')


@app.route('/strategy')
def strategy():
    return render_template('courses/strategy.html')


@app.route('/ai')
def ai():
    return render_template('courses/ai.html')

@app.route('/personal')
def personal():
    return render_template('courses/personal.html')


@app.route('/others')
def others():
    return render_template('courses/others.html')

 

if __name__ == "__main__":
    # Run Flask app using Waitress server
    # serve(app, host="0.0.0.0", port=8080)
     app.run(debug=True, host="0.0.0.0", port=5000)
