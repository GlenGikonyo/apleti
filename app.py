from flask import Flask, render_template,url_for,request,jsonify
from pymongo import MongoClient
from datetime import datetime
from bson import ObjectId
import os
from dotenv import load_dotenv
from flask_talisman import Talisman



app = Flask(__name__)
load_dotenv() 
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
app.config['DEBUG'] = False


# Content Security Policy



# MongoDB connection string
connection_string = os.getenv("MONGODB_URI")
client = MongoClient(connection_string)
db = client['apleti']
collection = db['ContactForm']




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

@app.route('/contact-us', methods=['GET', 'POST'])
def render_contact_us():
    if request.method == 'POST':
        # Retrieve form data
        name = request.form.get('name')
        email = request.form.get('email')
        phone_number = request.form.get('phone_number')
        msg_subject = request.form.get('msg_subject')
        message = request.form.get('message')
        status = "New"

        try:
            # Insert form data into MongoDB
            form_data = {
                "name": name,
                "email": email,
                "phone_number": phone_number,
                "msg_subject": msg_subject,
                "message": message,
                "status":status,
                "created_at": datetime.now()
            }

            

            result = collection.insert_one(form_data)
           
            print(f"Data inserted with ID: {result.inserted_id}")

        
            # Provide success response
            return "Form submitted successfully!"  # Replace with a redirect or template if needed

        except Exception as e:
            print(f"Error inserting data: {e}")

            return "An error occurred while submitting the form. Please try again later."

    # Render the HTML form for GET requests
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


@app.route('/leadership')
def leadership():
    return render_template('courses/leadership.html')


@app.route('/corporate')
def corporate():
    return render_template('courses/corporate.html')


@app.route('/value')
def value():
    return render_template('courses/value.html')

@app.route('/customer')
def customer():
    return render_template('courses/customer.html')

@app.route('/transformational')
def transformational():
    return render_template('courses/transformational.html')

@app.route('/new')
def new():
    return render_template('courses/new.html')


@app.route('/adaptive')
def adaptive():
    return render_template('courses/adaptive.html')


@app.route('/quality')
def quality():
    return render_template('courses/quality.html')

@app.route('/financial')
def financial():
    return render_template('courses/financial.html')

@app.route('/proposal')
def proposal():
    return render_template('courses/proposal.html')

@app.route('/business')
def business():
    return render_template('courses/business.html')

@app.route('/women')
def women():
    return render_template('courses/women.html')

@app.route('/others')
def others():
    return render_template('courses/others.html')

@app.route('/admin')
def admin():
    # Retrieve data from MongoDB, sorted by the timestamp or creation date field in descending order
    data = list(collection.find({}).sort("created_at", -1))  # Replace 'timestamp' with the actual field name
    print(data)
    return render_template('admin.html', messages=data)

@app.route('/delete_message', methods=['POST'])
def delete_message():
    # Get the ID from the request body
    data = request.get_json()
    message_id = data.get('id')

    if not message_id:
        return jsonify({'success': False, 'message': 'No ID provided'}), 400

    # Delete the message from MongoDB
    result = collection.delete_one({'_id': ObjectId(message_id)})

    if result.deleted_count > 0:
        return jsonify({'success': True})
    else:
        return jsonify({'success': False, 'message': 'Message not found'}), 404





if __name__ == "__main__":    
    app.run(debug=False, host="0.0.0.0", port=5000)
