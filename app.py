from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def input():
    return render_template('input.html')

@app.route('/output', methods = ['POST', 'GET'])
def output():
    if request.method == 'GET':
        return f'The URL /output is accessed directly, try going to top domain and resubmit the form...'

    if request.method == 'POST':
        form_data = request.form
        #key=var name
        #value=value
        old_vers=float(form_data["oldVers"])
        old_hp=float(form_data["oldHP"])
        new_vers=float(form_data["newVers"])
        new_hp=float(form_data["newHP"])

        old_eHP=eHP(old_vers,old_hp)
        new_eHP=eHP(new_vers,new_hp)

        if old_eHP>new_eHP:
            better='Old gear is better'
            diff=old_eHP-new_eHP
        else:
            better='New gear is better'
            diff=new_eHP-old_eHP

        return render_template('output.html', better=better, diff=diff,old_eHP=old_eHP,new_eHP=new_eHP)

def eHP(vers,hp):
    vers=vers/2
    vers=(vers/100)+1
    effective_hp=hp*vers

    return(effective_hp)