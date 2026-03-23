from flask import Flask, render_template, request # These are the necessary imports for our Flask application. We import Flask to create the app, render_template to render HTML templates, and request to handle form data.

app = Flask(__name__) # This line initializes the Flask application. The __name__ variable is passed to Flask to help it determine the root path of the application.

@app.route("/", methods=["GET", "POST"]) #This is a route decorator that defines the URL endpoint for the home page ("/"). It allows both GET and POST requests, meaning users can access the page and submit data through a form.
def home():
    if request.method == "POST":
        age = int(request.form["age"])
        height = float(request.form["height"])
        weight = float(request.form["weight"])
        goal = request.form["goal"]
        days = int(request.form["days"])

        bmr = (10 * weight) + (6.25 * height) - (5 * age) + 5
        calories = bmr * 1.55

        if goal == "bulk":
            calories += 300
        elif goal == "cut":
            calories -= 300

        protein = weight * 1.8
        # Basic Diet Suggestion 
        if goal == "bulk":
            diet = "High Carb , High Protien diet with calorie surplus."    
        elif goal == "cut":
            diet = "Low Carb, High Protien diet with calorie deficit."
        else:
            diet = "Balanced diet with moderate carbs and protien."

        height_m = height / 100
        bmi = weight / (height_m ** 2)
        #BMI Category 
        if bmi < 18.5:
            bmi_status = "Underweight - Focus on Lean Bulking "
        elif 18.5 <= bmi < 25:
            bmi_status = "Normal weight - Maintain or Lean Bulk"
        elif 25 <= bmi < 30:
            bmi_status = "Overweight - Mild Fatloss Recommended"
        else:
            bmi_status = "Obese - Structured Fatloss Plan Required"

        if days == 3:
            workout = "Full Body Split"
        elif days == 4:
            workout = "Upper/Lower Split"
        else:
            workout = "Push Pull Legs"

        return render_template("index.html",
                               calories=round(calories),
                               protein=round(protein),
                               bmi=round(bmi, 1),
                               bmi_status=bmi_status,
                               workout=workout,
                               diet=diet)

    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)