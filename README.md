# 🍍 Pineapple Pathways

**Your All-in-One University Application Companion**

Pineapple Pathways empowers students to navigate the complex world of university applications with confidence. From personalized scholarship matching to AI-powered essay feedback, we're here to help you achieve your academic dreams while securing the financial support you need.

![Python](https://img.shields.io/badge/Python-3776AB?style=flat&logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-000000?style=flat&logo=flask&logoColor=white)
![React](https://img.shields.io/badge/React-20232A?style=flat&logo=react&logoColor=61DAFB)
![OpenAI](https://img.shields.io/badge/OpenAI-412991?style=flat&logo=openai&logoColor=white)
![Cohere](https://img.shields.io/badge/Cohere-39594D?style=flat&logo=cohere&logoColor=white)

---

## 🌟 Inspiration

Being surrounded by many high school and university students, along with two of ourselves applying to universities, we wanted to create an all-in-one tool to help students navigate the complex world of university applications. We recalled how **over $20 million worth of scholarship money goes unclaimed in Canada each year**, and given many struggle with the weight of tuition, one of our key functionalities is a scholarship database ensuring that students can get all the financial support they deserve.

Applying to university is not an easy task—quite the opposite. With so many resources spread out sparsely, we wanted to create a one-stop platform to empower students on their journey toward the future.

---

## 🚀 What It Does

Pineapple Pathways offers:

- **Personalized scholarship matching** tailored to your profile and aspirations
- **AI-powered essay feedback** to help you craft compelling application materials
- **Tuition calculator** to plan your budget and financial future
- **Stats predictor** to assess your chances of admission at different programs
- **Step-by-step application guidance** to make the process smoother

Whether you're aiming for top universities or seeking financial aid, Pineapple Pathways is here to make your journey smoother, helping you achieve your academic dreams with confidence.

---

## ✨ Key Features

### 🎓 Scholarship Database (Our Favorite Feature!)
- Access to **500+ scholarships** specifically curated for Canadian students
- Powered by **Cohere Rerank API** for intelligent matching
- Find scholarships relevant to your aspirations, characteristics, and qualifications
- Ensure you claim all the financial aid you're eligible for

### 📝 Essay Helper
- AI-powered feedback on short answers and essays
- Trained custom **ChatGPT model** for detailed improvement tips
- Communicate yourself in the best way possible on your applications

### 📊 Stats Predictor
- Calculate your chances of admission at different programs
- Comprehensive university statistics database
- Make informed decisions about where to apply

### 💰 Tuition Calculator
- Estimate tuition costs for your desired program
- Compare costs across various universities
- Begin your budgeting plans with confidence

---

## 🏗️ How We Built It

### Backend Architecture

**Scholarship Recommender:**
- Built with **Python and Flask** for server-side processing
- Compiled a comprehensive spreadsheet with 500+ scholarships
- User inputs sent via POST request as JSON to Flask server
- **Cohere Rerank API** intelligently ranks scholarships based on user parameters
- Top 12 recommendations returned to frontend for display

**Essay Helper:**
- Trained a custom **ChatGPT model** for application-specific feedback
- Flask server communicates between OpenAI API and React frontend
- Provides detailed, actionable tips for essay improvement

**Stats Predictor:**
- Downloaded and processed extensive university statistics
- Converted Excel files to CSV for efficient data handling
- Integrated with Flask backend for real-time predictions

**Tuition Calculator:**
- Flask and Python backend processing
- POST requests compare user inputs with compiled tuition dataset
- Returns approximate costs for various programs and universities

### Frontend Design

**Landing Page:**
- Built with **React** for dynamic functionality
- Brutalist design approach for eye-catching, unique aesthetic
- Raw, unpolished feeling that stands out from corporate templates
- No smooth animations—intentionally minimalistic

**Dashboard:**
- Maintains minimalistic, "bare bones" aesthetic
- Complex React architecture with clean presentation
- Intuitive navigation between features

---

## 🧩 Tech Stack

**Backend:**
- Python
- Flask
- OpenAI API
- Cohere Rerank API
- Beautiful Soup (Web Scraping)
- CSV/Database Management

**Frontend:**
- React
- HTML5
- CSS

**Data Processing:**
- Excel/CSV conversion
- Database management
- Web scraping

---

## 🎯 Check Out Our Site

Visit the live project here: [**Pineapple Pathways Live Demo**](https://ai-teacher-njyu-git-main-gorgocaptaingmailcoms-projects.vercel.app)

> **Note:** This is currently a static version hosted on Vercel. Some features require dynamic backend connectivity and work best when run locally. We're working on hosting improvements for full functionality!

---

## 💪 Challenges We Ran Into

**Learning Flask:**
This was all of our first time using Flask for backend processing. We faced challenges with sending specific user inputs (checkboxes, dropdown menus) to the server, requiring a lot of experimentation and learning.

**Data Processing:**
The stats predictor was by far the most challenging feature. We had to download tons of university statistics as Excel files, convert them to CSV, and process them into our application—all while ensuring data accuracy.

**Hosting Hurdles:**
Our biggest challenge was hosting the webpage. Since we created a dynamic site that makes requests to the Flask server, we couldn't use static hosts like GitHub Pages. After scouring the web, we found Vercel, but even then faced many debugging challenges getting the scripts to run properly on the server.

---

## 🏆 Accomplishments That We're Proud Of

- **First-time success** with ChatGPT API and Cohere Rerank
- **Exceeded expectations** with Cohere Rerank—scholarship ranking was incredibly consistent and relevant
- Created a **clean, polished UI** that breaks away from cookie-cutter designs
- Built an **all-in-one platform** that genuinely helps students navigate university applications
- Successfully connected multiple technologies (Flask, React, OpenAI, Cohere) into one cohesive project

---

## 📚 What We Learned

Every member of our team tried something new for the first time:

- **Flask** for backend development
- **OpenAI API** integration and custom model training
- **Cohere Rerank** for intelligent data matching
- **React** for dynamic frontend development
- **Web scraping** with Beautiful Soup
- **Database management** and CSV processing

While we all had basic understanding of these technologies, this project allowed us to explore even further and, most importantly, **connect everything into one big, functional project**.

---

## 🔮 What's Next for Pineapple Pathways

**AI Model Improvements:**
- Integrate newest AI models to enhance platform capabilities
- Improve recommendation accuracy and personalization

**Data Expansion:**
- Expand scholarship dataset using web scraping and automated databasing
- Add statistics for more universities and programs
- Collect more accurate and up-to-date university data

**Infrastructure:**
- Purchase a dedicated domain for professional hosting
- Migrate from free plan to reliable server for consistent uptime
- Enable full dynamic functionality for all users (not just local)
- Make the platform accessible to students worldwide

**Feature Additions:**
- More comprehensive application deadline tracking
- Interview preparation resources
- Community forum for students to share experiences
- Mobile app for on-the-go access

---

## 🛠️ Local Setup & Installation

### Prerequisites
- Python 3.8+
- Node.js and npm
- OpenAI API key
- Cohere API key

### Backend Setup

1. Navigate to the backend directory:
   ```bash
   cd backend
   ```

2. Install Python dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Set up environment variables:
   ```bash
   export OPENAI_API_KEY='your-openai-key'
   export COHERE_API_KEY='your-cohere-key'
   ```

4. Run the Flask server:
   ```bash
   python app.py
   ```

   The server will start on `http://localhost:5000`

### Frontend Setup

1. Navigate to the frontend directory:
   ```bash
   cd frontend
   ```

2. Install Node.js dependencies:
   ```bash
   npm install
   ```

3. Start the development server:
   ```bash
   npm start
   ```

   The app will open at `http://localhost:3000`

---

## 📂 Project Structure

```
PineapplePathways/
├── backend/
│   ├── app.py
│   ├── scholarships.csv
│   ├── tuition_data.csv
│   ├── university_stats.csv
│   └── requirements.txt
├── frontend/
│   ├── src/
│   │   ├── components/
│   │   ├── pages/
│   │   └── App.js
│   └── package.json
└── README.md
```

---

## 🤝 Contributing

We welcome contributions! If you'd like to improve Pineapple Pathways:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

---

## 🙏 Acknowledgments

- **Cohere** for their amazing Rerank API
- **OpenAI** for ChatGPT API access
- **Beautiful Soup** for web scraping capabilities
---

## 💡 Fun Fact

Over **$20 million** in scholarship money goes unclaimed in Canada each year. Pineapple Pathways was built to change that.

---

**Made with 🍍 for students everywhere**

*Empowering the next generation, one application at a time.*
