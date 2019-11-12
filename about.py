from flask import Flask, render_template
app=Flask(__name__)

@app.route('/about-me')
def about():
    about={'name':'Hai Nguyen','work':'Creative','hobbies':['Read books','Write']}
    return render_template('me.html',data=about)

@app.route('/school')
def school():
    return '''<html>
    <a href="http://techkids.vn">school</a>
    </html>
    '''

if __name__ == '__main__':
    app.run(host='127.0.0.1',port=8000,debug=True)



