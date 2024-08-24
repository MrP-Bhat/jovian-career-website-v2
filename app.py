from flask import Flask, render_template,jsonify

app = Flask(__name__)

JOBS=[
{
'id':1,
    'title':'Data Analyst',
    'location':'Bengaluru, India',
    'salary':'Rs. 10,00,000'
},
    {
        'id':2,
        'title':'frontend engineer',
        'location':'remote',
        'salary':'Rs. 15,00,000'
    },
    {
    
    
    'id':3,
    'title':'Data Scientist',
    'location':'Delhi, India',
    'salary':'Rs. 15,00,000'
},
    {'id':4,
        'title':'Backend engineer',
        'location':'Sanfransisco',
        'salary':'$. 15,00,000'
        
    }
]


@app.route("/")
def hello_jovian():
    return render_template("home.html",jobs=JOBS,company_name="Jovian")
    
@app.route("/api/jobs")
def list_jobs():
    return jsonify(JOBS)
    

print(__name__)
if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
