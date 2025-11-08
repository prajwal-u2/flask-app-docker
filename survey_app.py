from flask import Flask, request, render_template, Response
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from dotenv import load_dotenv
import os
import json

load_dotenv()

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class SurveyResponse(db.Model):
    __tablename__ = 'hw1_survey_responses'
    
    id = db.Column(db.Integer, primary_key=True)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)
    name = db.Column(db.String(50), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    frequency = db.Column(db.String(20))
    travel_type = db.Column(db.String(20))
    travel_companions = db.Column(db.Text)
    destination = db.Column(db.Boolean, default=False)
    dream_destination = db.Column(db.Text)
    
with app.app_context():
    # db.drop_all()  # Uncomment this to drop the table and recreate it
    db.create_all()

@app.route("/", methods=["GET", "POST"])
def survey():
    message = None
    if request.method == "POST":
        name = request.form.get('name')
        age = request.form.get('age')
        frequency = request.form.get('frequency')
        travel_type = request.form.get('travel_type')
        travel_companions = ','.join(request.form.getlist('travel_companions'))
        destination = 'destination' in request.form
        dream_destination = request.form.get('dream_destination')
        
        response = SurveyResponse(
            name=name,
            age=int(age) if age else None,
            frequency=frequency,
            travel_type=travel_type,
            travel_companions=travel_companions,
            destination=destination,
            dream_destination=dream_destination
        )
        
        db.session.add(response)
        db.session.commit()
        message = "Thank you! Your survey response has been saved successfully."
        
    return render_template("survey.html", message=message)

@app.route("/api/results")
def results():
    reverse = request.args.get('reverse', 'false').lower() == 'true'
    
    if reverse:
        responses = SurveyResponse.query.order_by(SurveyResponse.id.desc()).all()
    else:
        responses = SurveyResponse.query.order_by(SurveyResponse.id.asc()).all()
    
    data = [{
        'id': response.id,
        'timestamp': response.timestamp.isoformat(),
        'name': response.name,
        'age': response.age,
        'frequency': response.frequency,
        'travel_type': response.travel_type,
        'travel_companions': response.travel_companions,
        'destination': response.destination,
        'dream_destination': response.dream_destination
    } for response in responses]
    
    return Response(
        json.dumps(data),
        mimetype='application/json'
    )

