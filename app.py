from flask import Flask, render_template, url_for, request, redirect
import sql_commands

app = Flask(__name__)


@app.route('/')
@app.route('/home')  # home root
def home_page():
    return render_template('home.html')



@app.route('/trainer')  # display all trainers root
def classes():
    clas = sql_commands.get_classes()
    return render_template('class.html', results=clas)

@app.route('/trainer')  # display all trainers root
def trainers():
    trainer = sql_commands.get_trainers()
    return render_template('trainer.html', results=trainer)


@app.route('/member')  # display all members root
def members():
    members = sql_commands.get_members()
    return render_template('member.html', results=members)


# member registration loop
@app.route('/register_member', methods=['GET', 'POST'])
def register_member():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        firstname = request.form['firstname']
        lastname = request.form['lastname']
        # date time function needs integers to work
        year = int(request.form['year'])
        month = int(request.form['month'])
        day = int(request.form['day'])
        # date time function needs integers to work
        height = request.form['height']
        weight = request.form['weight']

        sql_commands.create_member(
            username, password, firstname, lastname, year, month, day, height, weight)
        return redirect(url_for('members'))  # references name of function ^

    return render_template('register_member.html')


@app.route('/delete/<string:username>', methods=['GET', 'POST'])
def delete(username):
    sql_commands.delete_member(username)
    return redirect(url_for('members'))


if __name__ == '__main__':
    app.run(debug=True)
