from . import auth
import os 
from app.auth.forms import LoginForm, RegistrationForm
from flask import render_template, flash, session, redirect, url_for, request, current_app
from flask_login import login_user, logout_user, login_required, current_user
from app import db
from app.auth.models import User, Image
from werkzeug.utils import secure_filename


@auth.route('/register', methods=["GET", "POST"])
@login_required  
def register_user():
    form = RegistrationForm()
    
    if form.validate_on_submit():
        User.create_user(
            username=form.username.data,
            email=form.email.data,
            password=form.password.data
        )
        
        flash("¡Registro exitoso!")
        return redirect(url_for("auth.home"))  # Redirige a la página principal u otra página apropiada
    
    return render_template("registration.html", form=form)

@auth.route('/login', methods=["GET", "POST"])
def log_in_user():
    if current_user.is_authenticated:
        flash("El usuario ya se encuentra autenticado en el sistema")
        return redirect(url_for("auth.home"))

    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()

        if user and user.check_password(form.password.data):
            login_user(user, remember=form.stay_loggedin.data)
            session["username"] = form.username.data
            flash("Ingreso Correcto al sistema", "success")
            return redirect(url_for("auth.home"))  # Redirige al usuario después del login

        # Si las credenciales son incorrectas
        flash("Credenciales no válidas. Por favor, verifique su usuario y contraseña.", "error")
        return render_template('login.html', form=form), 400

    return render_template('login.html', form=form)

@auth.route('/edit_user/<int:user_id>', methods=['GET', 'POST'])
@login_required
def edit_user(user_id):
    user = User.query.get_or_404(user_id)
    if request.method == 'POST':
        user.username = request.form['username']
        user.email = request.form['email']
        db.session.commit()
        flash("Usuario actualizado exitosamente.", "success")
        return redirect(url_for('auth.home'))
    return render_template('edit_user.html', user=user)

@auth.route('/delete_user/<int:user_id>', methods=['GET', 'POST'])
@login_required
def delete_user(user_id):
    user = User.query.get_or_404(user_id)
    db.session.delete(user)
    db.session.commit()
    flash("Usuario eliminado exitosamente.", "success")
    return redirect(url_for('auth.home'))

@auth.route('/home')
@login_required
def home():
    users = User.query.all()
    images = Image.query.all()
    current_user_info = {
        "username": current_user.username,
        "email": current_user.email,
        "name": current_user.username  # Puedes ajustar esto si tienes un campo de nombre real
    }
    return render_template("home.html", users=users, images=images, current_user_info=current_user_info)

@auth.route('/obras')
@login_required
def obras():
    return render_template("obras.html")

@auth.route('/logout', methods=["GET"])
@login_required
def log_out_user():
    logout_user()
    return redirect(url_for("auth.log_in_user"))


@auth.app_errorhandler(404)
def page_not_found(error):
    return render_template('404.html'), 404



@auth.route('/carga', methods=['GET', 'POST'])
@login_required
def carga():
    if request.method == 'POST':
        image = request.files['image']
        titulo = request.form['titulo']
        content = request.form['content']

        if image:
            # Asegúrate de que el nombre de archivo sea seguro
            filename = secure_filename(image.filename)
            # Guarda el archivo en la carpeta de uploads
            filepath = os.path.join(current_app.config['UPLOAD_FOLDER'], filename)
            image.save(filepath)

            # Guarda la ruta relativa de la imagen en la base de datos
            relative_filepath = os.path.join('uploads', filename).replace("\\", "/")
            new_image = Image(filename=filename, filepath=relative_filepath, titulo=titulo, content=content)
            db.session.add(new_image)
            db.session.commit()

            flash("¡Carga exitosa!", "success")
            return redirect(url_for('auth.home'))

    images = Image.query.all()
    print(images)  
    return render_template('section_obras.html', images=images)

@auth.route('/edit/<int:image_id>', methods=['GET', 'POST'])
@login_required
def edit_image(image_id):
    image = Image.query.get_or_404(image_id)

    if request.method == 'POST':
        # Actualizar el título y el contenido
        image.titulo = request.form['titulo']
        image.content = request.form['content']

        # Manejar la carga de una nueva imagen si se proporciona
        if 'image' in request.files:
            new_image = request.files['image']
            if new_image:
                # Asegurarse de que el nombre de archivo sea seguro
                filename = secure_filename(new_image.filename)
                # Guardar el archivo en la carpeta de uploads
                filepath = os.path.join(auth.config['UPLOAD_FOLDER'], filename)
                new_image.save(filepath)
                # Actualizar la ruta de la imagen en la base de datos
                image.filepath = os.path.join('uploads', filename).replace("\\", "/")

        # Guardar los cambios en la base de datos
        db.session.commit()
        flash('Imagen actualizada correctamente', 'success')
        return redirect(url_for('auth.home'))

    # Renderizar el formulario con la información actual de la imagen
    return render_template('edit_image.html', image=image)

@auth.route('/delete_image/<int:image_id>', methods=['GET', 'POST'])
@login_required
def delete_image(image_id):
    image = Image.query.get_or_404(image_id)
    db.session.delete(image)
    db.session.commit()
    flash("Imagen eliminada exitosamente.", "success")
    return redirect(url_for('auth.home'))

