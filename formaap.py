from flask import Flask, url_for, render_template, request

app = Flask(__name__) #__name__ = "__main__" if this is the file that was run.  Otherwise, it is the name of the file (ex. webapp)

@app.route("/")
def render_main():
    return render_template('index.html')
    
@app.route("/f1")
def render_form1():
    return render_template('form1.html')
    
@app.route("/f0")
def render_form0():
    return render_template('form0.html')

@app.route("/response")
def render_responseName():
    Color = request.args['optradio']
    Size = request.args['sellist1']
    Fruit = ""
    Name = request.args['Nme']
    
    if Size == "big":
        if Color == "red":
            Fruit = "Pomegreanate"
        if Color == "orange":
            Fruit = "pumpkin"
        if Color == "yellow":
            Fruit = "pineaple"
        if Color == "green":
            Fruit = "honeydew Melons"
        if Color == "blue":
            Fruit = "java bananas"
        if Color == "purple":
            Fruit = "plum"
    elif Size == "small":
        if Color == "red":
            Fruit = "apple"
        if Color == "orange":
            Fruit = "Mango"
        if Color == "yellow":
            Fruit = "banana"
        if Color == "green":
            Fruit = "kiwi"
        if Color == "blue":
            Fruit = "blueberry"
        if Color == "purple":
            Fruit = "grape"
    elif Size == "unkown sized":
        Fruit = ", hold on, don't you think you should choose a size"
    
        
    
            
        
    
    reply1 =  Name + "'s favorite fruit a " + Size + " " + Color + " " + Fruit + "?"
    
    return render_template("response.html", response = reply1)


if __name__=="__main__":
    app.run(debug=True)
