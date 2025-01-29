# 🖐️ ASL-to-ISL Real-Time Translation  

## 📄 Overview  

Sign language is the primary mode of communication for individuals with speech and hearing impairments. With over **300 different sign languages** worldwide, communication barriers arise when two individuals use different sign languages—such as **American Sign Language (ASL)** and **Indian Sign Language (ISL)**.  

This project presents a **novel real-time translation system** that automates the conversion of ASL to ISL using **deep learning and computer vision**. Our approach eliminates the need for human translators by leveraging a **Convolutional Neural Network (CNN)** to recognize ASL signs, mapping them to corresponding ISL signs, and generating a video-based ISL translation.  

## ✨ Key Features  

- **Real-time ASL recognition** using a CNN model  
- **36-class ASL sign classification** with **96.43% accuracy**  
- **Mapping ASL signs to ISL equivalents**  
- **Video synthesis for ISL output**  
- **Automated pipeline leveraging deep learning and NLP techniques**  

## 🏗️ Methodology  

1. **ASL Sign Recognition:**  
   - A **CNN model** is trained on a dataset of **36 ASL signs**.  
   - Achieved a **testing accuracy of 96.43%**.  

2. **Temporal Sign Processing:**  
   - A **Gated Recurrent Unit (GRU)** processes sequential sign inputs.  

3. **Textual Sign Mapping & Query Processing:**  
   - The **BM25 algorithm** is used for efficient sign-to-text retrieval.  
   - **NLP techniques** assist in refining translations.  

4. **ISL Video Generation:**  
   - Recognized ASL signs are **mapped to ISL gestures**.  
   - A **Flask-based API** generates ISL video outputs.  

## 🛠️ Tech Stack  

- **Deep Learning:** CNN, GRU  
- **Natural Language Processing (NLP):** BM25  
- **Computer Vision:** OpenCV, TensorFlow/Keras  
- **Backend:** Flask  

## 🔧 Setup & Installation  

### 1️⃣ Clone the Repository  

```bash
git clone https://github.com/sudhanvarajesh/Sign2Sign/
cd asl-to-isl
```

### 2️⃣ Install Dependencies  

```bash
pip install -r requirements.txt
```

### 3️⃣ Run the Application  

```bash
python app.py
```

## 📊 Model Performance  

- **CNN Model Accuracy:** 96.43% on ASL sign recognition  
- **GRU for Sequence Learning:** Improved sign interpretation  
- **BM25 & NLP:** Enhanced text-to-sign mapping efficiency  

## 🚀 Future Work  

- Expanding the sign language dataset  
- Enhancing model robustness for real-world scenarios  
- Supporting additional sign languages  

## 📜 License  

This project is licensed under the [MIT License](LICENSE).  

## 👨‍💻 Contributing  

We welcome contributions! To contribute:  

1. Fork the repository  
2. Create a feature branch (`git checkout -b feature-name`)  
3. Commit your changes (`git commit -m "Added feature"`)  
4. Push to your fork (`git push origin feature-name`)  
5. Open a Pull Request  
