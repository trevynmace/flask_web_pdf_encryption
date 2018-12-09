from flask import Flask, render_template, request, redirect, url_for
from PyPDF2 import PdfFileReader, PdfFileWriter
import time
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/encrypt_file', methods=['POST'])
def encrypt_file():
    password = request.form['password']
    confirm_password = request.form['confirmPassword']
    file = request.files['file']

    if password != confirm_password:
        return 'The passwords did not match, please try again'

    filename_without_extension = file.filename[:-4]
    filename = f'{filename_without_extension}-{int(round(time.time() * 1000))}'
    unencrypted_filename = f'{filename}-unencrypted.pdf'
    file.save(f'./static/uploaded_files/{unencrypted_filename}')

    encrypted_filename = f'{filename}-encrypted.pdf'

    try:
        encrypt_pdf(unencrypted_filename, password, encrypted_filename)
    except:
        return 'There was an error encrypting the pdf'

    return redirect(url_for('link_page', filename=f'{encrypted_filename}'))


@app.route('/decrypt_file', methods=['POST'])
def decrypt_file():
    password = request.form['password']
    file = request.files['file']

    filename_without_extension = file.filename[:-4]
    filename = f'{filename_without_extension}-{int(round(time.time() * 1000))}'
    encrypted_filename = f'{filename}-encrypted.pdf'
    file.save(f'./static/uploaded_files/{encrypted_filename}')

    decrypted_filename = f'{filename}-decrypted.pdf'

    try:
        decrypt_pdf(encrypted_filename, password, decrypted_filename)
    except:
        return 'There was an error decrypting the pdf, check your password and try again'

    return redirect(url_for('link_page', filename=f'{decrypted_filename}'))


def encrypt_pdf(input_filename, password, output_filename):
    with open(f'./static/uploaded_files/{input_filename}', 'rb') as in_file:
        input_pdf = PdfFileReader(in_file)
        output_pdf = PdfFileWriter()
        output_pdf.appendPagesFromReader(input_pdf)
        output_pdf.encrypt(password)
        with open(f'./static/uploaded_files/{output_filename}', 'wb') as out_file:
            output_pdf.write(out_file)

def decrypt_pdf(input_filename, password, output_filename):
    with open(f'./static/uploaded_files/{input_filename}', 'rb') as in_file:
        input_pdf = PdfFileReader(in_file)
        input_pdf.decrypt(password)
        output_pdf = PdfFileWriter()
        output_pdf.appendPagesFromReader(input_pdf)
        with open(f'./static/uploaded_files/{output_filename}', 'wb') as out_file:
            output_pdf.write(out_file)


@app.route('/link_page')
def link_page():
    filename = request.args.get('filename')
    return render_template('download_page.html', filename=filename)


if __name__ == '__main__':
    app.run(host='0.0.0.0')
