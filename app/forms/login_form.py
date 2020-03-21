class LoginForm(FlaskForm):
    username = TextField(label="Username", validators=[
                         InputRequired(), Length(**flen["username"])])
    password = PasswordField(label="Password", validators=[
                             InputRequired(), Length(**flen["password"])])
    remember = BooleanField()