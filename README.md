# 📸 Code Image Generator

Turn your code snippets into beautiful images effortlessly! This **Flask-based** web app allows you to paste code, apply syntax highlighting, and convert it into a downloadable image.

## 🚀 Features
- 🖌️ **Syntax Highlighting** with Pygments
- 📸 **Convert Code to Image** using Playwright
- 🎨 **Monokai Theme** for a sleek look
- 💾 **Downloadable Images** in PNG format
- 🌐 **Simple Web UI** for easy interaction

## 📂 Project Structure
```
code_image_generator/
│── app.py               # Flask backend
│── templates/
│   ├── index.html       # HTML frontend
│── static/
│   ├── styles.css       # Styling
│── screenshots/         # Stores generated images
```

## 🛠 Installation
### **1️⃣ Clone the Repository**
```sh
git clone https://github.com/your-username/code-image-generator.git
cd code-image-generator
```

### **2️⃣ Create a Virtual Environment**
```sh
python -m venv venv
venv\Scripts\activate     
```

### **3️⃣ Install Dependencies**
```sh
pip install -r requirements.txt
playwright install  # Required for taking screenshots
```

## ▶️ Usage
### **Run the Flask App**
```sh
python app.py
```
Open **http://127.0.0.1:5000/** in your browser.

### **Generate an Image**
1. Paste your code snippet
2. Click **Generate Image**
3. Download the generated image

## 🤝 Contributing
1. **Fork** the repository
2. **Clone** your fork
3. Create a **new branch** (`git checkout -b feature-name`)
4. **Commit** your changes (`git commit -m 'Added feature'`)
5. **Push** to GitHub (`git push origin feature-name`)
6. Open a **Pull Request** 🎉

## 📝 License
This project is licensed under the **MIT License**. Feel free to modify and distribute it as needed!

---
💡 **Made with ❤️ by Yagyansh**

