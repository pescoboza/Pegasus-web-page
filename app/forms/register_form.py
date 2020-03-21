class RegisterForm(FlaskForm):
    firstName = TextField(label="First Name", validators=[
                          InputRequired(), Length(**flen["firstName"])])
    lastName = TextField(label="Last Name", validators=[
                         InputRequired(), Length(**flen["lastName"])])
    username = TextField(label="Username", validators=[
                         InputRequired(), Length(**flen["username"])])
    email = TextField(label="Email", validators=[
                      InputRequired(), Length(**flen["email"])])

    password_first = PasswordField(label="Password", validators=[
                                   InputRequired(), Length(**flen["password"])])
    password_again = PasswordField(label="Password", validators=[
                                   InputRequired(), Length(**flen["password"])])

    newsletter = BooleanField()
    accept_terms_and_conditions = BooleanField()
