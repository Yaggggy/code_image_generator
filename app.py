from flask import Flask, render_template, request, session, send_file
from pygments import highlight
from pygments.lexers import get_lexer_by_name
from pygments.formatters import HtmlFormatter
import os
from playwright.sync_api import sync_playwright

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Required for session management

# Route for the home page
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Get user input
        code = request.form.get('code', '')
        language = request.form.get('language', 'python')
        theme = request.form.get('theme', 'monokai')

        # Highlight the code using Pygments
        lexer = get_lexer_by_name(language)
        formatter = HtmlFormatter(style=theme)
        highlighted_code = highlight(code, lexer, formatter)

        # Save preferences in session
        session['theme'] = theme

        # Render the template with the highlighted code
        return render_template('index.html', code=highlighted_code, css=formatter.get_style_defs('.highlight'))
    
    # Default GET request
    return render_template('index.html', code='', css='')

# Route to generate an image of the code snippet
@app.route('/generate_image', methods=['POST'])
def generate_image():
    # Capture the rendered HTML as an image using Playwright
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()

        # Serve the current page's HTML
        html_content = request.form.get('html_content', '')
        page.set_content(html_content)

        # Take a screenshot of the highlighted code
        image_path = 'static/output.png'
        page.locator('.highlight').screenshot(path=image_path)
        browser.close()

    # Return the image file
    return send_file(image_path, mimetype='image/png')

if __name__ == '__main__':
    app.run(debug=True)