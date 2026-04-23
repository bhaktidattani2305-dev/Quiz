import streamlit as st
import matplotlib.pyplot as plt
from matplotlib.patches import Circle
import numpy as np

# Page configuration
st.set_page_config(
    page_title="Stand-Up, Show-Up & Shut-Up Quiz",
    page_icon="🎭",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Custom CSS for Gen Z style with large fonts
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;600;700&display=swap');
    
    * {
        font-family: 'Poppins', sans-serif;
    }
    
    .main {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 2rem;
    }
    
    .stButton>button {
        background: linear-gradient(45deg, #FF6B6B, #FF8E53);
        color: white;
        font-size: 22px;
        font-weight: 700;
        padding: 18px 40px;
        border-radius: 50px;
        border: none;
        box-shadow: 0 8px 15px rgba(0,0,0,0.3);
        transition: all 0.3s ease;
        width: 100%;
        margin: 10px 0;
    }
    
    .stButton>button:hover {
        transform: translateY(-3px);
        box-shadow: 0 12px 25px rgba(0,0,0,0.4);
    }
    
    .quiz-title {
        font-size: 52px;
        font-weight: 800;
        text-align: center;
        background: linear-gradient(45deg, #FFD700, #FF69B4, #00FFFF);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 30px;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
        animation: glow 2s ease-in-out infinite alternate;
    }
    
    .question-box {
        background: rgba(255, 255, 255, 0.95);
        padding: 35px;
        border-radius: 25px;
        box-shadow: 0 10px 30px rgba(0,0,0,0.3);
        margin: 25px 0;
        border: 3px solid #FFD700;
    }
    
    .question-text {
        font-size: 28px;
        font-weight: 700;
        color: #2D3748;
        margin-bottom: 25px;
        line-height: 1.5;
    }
    
    .score-box {
        background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%);
        padding: 25px;
        border-radius: 20px;
        text-align: center;
        font-size: 32px;
        font-weight: 800;
        color: white;
        box-shadow: 0 8px 20px rgba(0,0,0,0.3);
        margin: 20px 0;
    }
    
    .feedback-correct {
        background: linear-gradient(135deg, #11998e 0%, #38ef7d 100%);
        padding: 25px;
        border-radius: 20px;
        font-size: 26px;
        font-weight: 700;
        color: white;
        text-align: center;
        margin: 20px 0;
        box-shadow: 0 8px 20px rgba(0,0,0,0.3);
    }
    
    .feedback-wrong {
        background: linear-gradient(135deg, #ee0979 0%, #ff6a00 100%);
        padding: 25px;
        border-radius: 20px;
        font-size: 26px;
        font-weight: 700;
        color: white;
        text-align: center;
        margin: 20px 0;
        box-shadow: 0 8px 20px rgba(0,0,0,0.3);
    }
    
    .start-screen {
        text-align: center;
        padding: 60px;
        background: rgba(255, 255, 255, 0.95);
        border-radius: 30px;
        box-shadow: 0 15px 40px rgba(0,0,0,0.4);
        margin: 40px auto;
        max-width: 800px;
    }
    
    .start-emoji {
        font-size: 120px;
        margin: 20px 0;
    }
    
    .start-subtitle {
        font-size: 26px;
        color: #4A5568;
        margin: 20px 0;
        font-weight: 600;
    }
    
    .final-score {
        font-size: 48px;
        font-weight: 800;
        text-align: center;
        color: #FFD700;
        margin: 30px 0;
        text-shadow: 3px 3px 6px rgba(0,0,0,0.4);
    }
    
    div[data-baseweb="radio"] > label {
        font-size: 22px !important;
        font-weight: 600 !important;
        color: #2D3748 !important;
        padding: 15px !important;
        margin: 10px 0 !important;
        background: #f7fafc !important;
        border-radius: 12px !important;
        transition: all 0.3s ease !important;
    }
    
    div[data-baseweb="radio"] > label:hover {
        background: #e6fffa !important;
        transform: translateX(10px) !important;
    }
    
    .stProgress > div > div > div > div {
        background: linear-gradient(90deg, #FF6B6B, #4ECDC4, #45B7D1);
        height: 30px;
        border-radius: 15px;
    }
    
    .stProgress > div > div > div {
        background: rgba(255,255,255,0.3);
        height: 30px;
        border-radius: 15px;
    }
    
    @keyframes glow {
        from {
            text-shadow: 0 0 10px #fff, 0 0 20px #fff, 0 0 30px #FFD700;
        }
        to {
            text-shadow: 0 0 20px #fff, 0 0 30px #FF69B4, 0 0 40px #FF69B4;
        }
    }
    </style>
""", unsafe_allow_html=True)

# Quiz data
QUIZ_DATA = [
    {
        "question": "According to Amaan's emotional autobiography, who is his 'most cherished' relative?",
        "options": [
            "A. Mum ❤️",
            "B. Dad 👑",
            "C. Sibling",
            "D. Bua (Photo already in danger)"
        ],
        "correct": "D. Bua (Photo already in danger)",
        "meme": "📸"
    },
    {
        "question": "Will Dishika be on time tomorrow?",
        "options": [
            "A. Let's not start unrealistic expectations in 2026",
            "B. Indian Standard Time + 30 minutes (scientifically proven)",
            "C. Time will come before her",
            "D. Scientists are still researching this Phenomenon"
        ],
        "correct": "D. Scientists are still researching this Phenomenon",
        "meme": "⏰"
    },
    {
        "question": "When Yajita puts on her earphones and starts vibing suspiciously hard, what is MOST likely playing?",
        "options": [
            "A. Sheila Ki Jawani (confidence level: illegal)",
            "B. Munni Badnaam (self-declared anthem)",
            "C. Fevicol Se (sticks in your head for 3–5 business days)",
            "D. Entire Bollywood Item Song Cinematic Universe (BISCU)"
        ],
        "correct": "D. Entire Bollywood Item Song Cinematic Universe (BISCU)",
        "meme": "🎧"
    },
    {
        "question": "When is Adi finally doing his first stand-up show for us?",
        "options": [
            "A. When the audience signs an NDA",
            "B. As soon as he finishes testing jokes on us for free",
            "C. Never",
            "D. The show is 'Coming Soon' — release date TBA since forever."
        ],
        "correct": "D. The show is 'Coming Soon' — release date TBA since forever.",
        "meme": "🎤"
    },
    {
        "question": "Nayan sabse zyada kis se darta hai duniya mein?",
        "options": [
            "A. 32 Bunglow wali Chudail jo lift maangti hai",
            "B. Boss",
            "C. Zombie Apocalypse",
            "D. Ruchi"
        ],
        "correct": "D. Ruchi",
        "meme": "😱"
    },
    {
        "question": "Hum sab ka official relationship status kis sabzi ke saath hai?",
        "options": [
            "A. 'It's complicated' with Dal",
            "B. 'Just friends' with Paneer",
            "C. 'Talking stage' with Mix Veg",
            "D. 'Forced commitment' with Matar-Tamatar (10 din mein 10 baar)"
        ],
        "correct": "D. 'Forced commitment' with Matar-Tamatar (10 din mein 10 baar)",
        "meme": "🍅"
    },
    {
        "question": "Which of the following would make Kalpana cry?",
        "options": [
            "A. An emotional poem she wrote at 2 AM",
            "B. Not getting food for more than 47 minutes",
            "C. Her favorite lipstick getting retired",
            "D. All of the above (but mostly the food one 👀)"
        ],
        "correct": "D. All of the above (but mostly the food one 👀)",
        "meme": "😭"
    },
    {
        "question": "Is Himanshu a good/innocent boy?",
        "options": [
            "A. 'Good boy' with premium hidden features",
            "B. Haan bilkul, woh toh group ka purest soul hai",
            "C. In his dreams, he is the ultimate good boy",
            "D. Error404 #iykyk"
        ],
        "correct": "D. Error404 #iykyk",
        "meme": "😇"
    }
]

# Initialize session state
if 'quiz_started' not in st.session_state:
    st.session_state.quiz_started = False
if 'current_question' not in st.session_state:
    st.session_state.current_question = 0
if 'score' not in st.session_state:
    st.session_state.score = 0
if 'answered' not in st.session_state:
    st.session_state.answered = False
if 'user_answer' not in st.session_state:
    st.session_state.user_answer = None
if 'answers_log' not in st.session_state:
    st.session_state.answers_log = []

def start_quiz():
    st.session_state.quiz_started = True
    st.session_state.current_question = 0
    st.session_state.score = 0
    st.session_state.answered = False
    st.session_state.user_answer = None
    st.session_state.answers_log = []

def submit_answer():
    if st.session_state.user_answer:
        st.session_state.answered = True
        correct_answer = QUIZ_DATA[st.session_state.current_question]['correct']
        is_correct = st.session_state.user_answer == correct_answer
        
        if is_correct:
            st.session_state.score += 1
        
        st.session_state.answers_log.append({
            'question': st.session_state.current_question + 1,
            'correct': is_correct
        })

def next_question():
    st.session_state.current_question += 1
    st.session_state.answered = False
    st.session_state.user_answer = None

def restart_quiz():
    st.session_state.quiz_started = False
    st.session_state.current_question = 0
    st.session_state.score = 0
    st.session_state.answered = False
    st.session_state.user_answer = None
    st.session_state.answers_log = []

def create_donut_chart(correct, incorrect):
    fig, ax = plt.subplots(figsize=(10, 10), facecolor='none')
    
    colors = ['#38ef7d', '#ff6a00']
    explode = (0.05, 0.05)
    
    wedges, texts, autotexts = ax.pie(
        [correct, incorrect],
        labels=['Correct ✅', 'Incorrect ❌'],
        autopct='%1.1f%%',
        startangle=90,
        colors=colors,
        explode=explode,
        textprops={'fontsize': 20, 'weight': 'bold', 'color': 'white'}
    )
    
    for autotext in autotexts:
        autotext.set_color('white')
        autotext.set_fontsize(24)
        autotext.set_weight('bold')
    
    for text in texts:
        text.set_fontsize(22)
        text.set_weight('bold')
        text.set_color('#2D3748')
    
    centre_circle = Circle((0, 0), 0.70, fc='white', linewidth=0)
    ax.add_artist(centre_circle)
    
    ax.text(0, 0, f'{correct}/{correct + incorrect}', 
            ha='center', va='center', fontsize=48, weight='bold', color='#667eea')
    
    ax.axis('equal')
    plt.tight_layout()
    return fig

# Main App
st.markdown("<h1 class='quiz-title'>🎭 Stand-Up, Show-Up & Shut-Up 🎭<br>The Ultimate Group Test</h1>", unsafe_allow_html=True)

# Start Screen
if not st.session_state.quiz_started:
    st.markdown("""
        <div class='start-screen'>
            <div class='start-emoji'>🔥💯🎪</div>
            <h2 style='font-size: 38px; color: #667eea; font-weight: 800;'>
                Welcome to the Most Chaotic Quiz Ever!
            </h2>
            <p class='start-subtitle'>
                8 Questions | Inside Jokes Only | No Survivors 💀
            </p>
            <p class='start-subtitle'>
                Test your knowledge about the squad's deepest secrets! 🤫
            </p>
            <p style='font-size: 22px; color: #718096; margin: 20px 0;'>
                ⚡ Real-time scoring<br>
                📊 Progress tracking<br>
                😂 Unlimited roasting potential
            </p>
        </div>
    """, unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.button("🚀 START QUIZ 🚀", on_click=start_quiz, use_container_width=True)

# Quiz Screen
elif st.session_state.current_question < len(QUIZ_DATA):
    # Progress bar
    progress = (st.session_state.current_question) / len(QUIZ_DATA)
    st.progress(progress)
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown(f"<p style='font-size: 24px; color: white; font-weight: 700;'>Question {st.session_state.current_question + 1} of {len(QUIZ_DATA)}</p>", unsafe_allow_html=True)
    
    with col2:
        st.markdown(f"<div class='score-box'>Score: {st.session_state.score} 🏆</div>", unsafe_allow_html=True)
    
    # Question
    current_q = QUIZ_DATA[st.session_state.current_question]
    
    st.markdown(f"""
        <div class='question-box'>
            <div style='font-size: 80px; text-align: center; margin-bottom: 20px;'>{current_q['meme']}</div>
            <div class='question-text'>{current_q['question']}</div>
        </div>
    """, unsafe_allow_html=True)
    
    # Options
    if not st.session_state.answered:
        st.session_state.user_answer = st.radio(
            "Choose your answer:",
            current_q['options'],
            key=f"q_{st.session_state.current_question}",
            label_visibility="collapsed"
        )
    else:
        st.radio(
            "Choose your answer:",
            current_q['options'],
            key=f"q_{st.session_state.current_question}_disabled",
            index=current_q['options'].index(st.session_state.user_answer) if st.session_state.user_answer else 0,
            disabled=True,
            label_visibility="collapsed"
        )
    
    # Feedback
    if st.session_state.answered:
        is_correct = st.session_state.user_answer == current_q['correct']
        
        if is_correct:
            st.markdown(f"""
                <div class='feedback-correct'>
                    ✅ YAAAS! Absolutely Correct! 🎉🎊<br>
                    You're on fire! 🔥
                </div>
            """, unsafe_allow_html=True)
        else:
            st.markdown(f"""
                <div class='feedback-wrong'>
                    ❌ Oops! Wrong Answer! 😬<br>
                    <br>
                    Correct Answer: <strong>{current_q['correct']}</strong><br>
                    Better luck next time! 💪
                </div>
            """, unsafe_allow_html=True)
    
    # Buttons
    col1, col2 = st.columns(2)
    
    with col1:
        if not st.session_state.answered:
            st.button("✨ SUBMIT ANSWER ✨", on_click=submit_answer, use_container_width=True)
        else:
            if st.session_state.current_question < len(QUIZ_DATA) - 1:
                st.button("➡️ NEXT QUESTION ➡️", on_click=next_question, use_container_width=True)
            else:
                st.button("🎯 SEE RESULTS 🎯", on_click=next_question, use_container_width=True)
    
    with col2:
        st.button("🔄 RESTART QUIZ 🔄", on_click=restart_quiz, use_container_width=True)

# Results Screen
else:
    correct = st.session_state.score
    incorrect = len(QUIZ_DATA) - st.session_state.score
    percentage = (correct / len(QUIZ_DATA)) * 100
    
    # Determine emoji based on score
    if percentage == 100:
        emoji = "👑"
        message = "ABSOLUTE LEGEND! You know everything!"
    elif percentage >= 75:
        emoji = "🌟"
        message = "Superstar! You're basically in the inner circle!"
    elif percentage >= 50:
        emoji = "😎"
        message = "Not bad! You know the squad pretty well!"
    elif percentage >= 25:
        emoji = "🤔"
        message = "Hmm... Do you even hang out with us?"
    else:
        emoji = "💀"
        message = "RIP! Were you even paying attention?"
    
    st.markdown(f"""
        <div style='text-align: center; font-size: 150px; margin: 30px 0;'>
            {emoji}
        </div>
    """, unsafe_allow_html=True)
    
    st.markdown(f"""
        <div class='final-score'>
            FINAL SCORE<br>
            {correct} / {len(QUIZ_DATA)}
        </div>
    """, unsafe_allow_html=True)
    
    st.markdown(f"""
        <h2 style='text-align: center; font-size: 36px; color: white; font-weight: 700; margin: 20px 0;'>
            {message}
        </h2>
    """, unsafe_allow_html=True)
    
    # Donut Chart
    st.markdown("<h3 style='text-align: center; font-size: 32px; color: white; font-weight: 700; margin: 30px 0;'>📊 Your Performance Breakdown 📊</h3>", unsafe_allow_html=True)
    
    fig = create_donut_chart(correct, incorrect)
    st.pyplot(fig)
    
    # Restart button
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.button("🔄 RESTART QUIZ 🔄", on_click=restart_quiz, use_container_width=True)
    
    # Fun messages
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("""
        <div style='background: rgba(255,255,255,0.9); padding: 30px; border-radius: 20px; text-align: center; margin: 30px 0;'>
            <h3 style='font-size: 28px; color: #667eea; margin-bottom: 20px;'>🎉 Quiz Complete! 🎉</h3>
            <p style='font-size: 22px; color: #4A5568;'>
                Thanks for playing! Share your score in the group chat! 📱<br>
                Time to roast each other! 😂🔥
            </p>
        </div>
    """, unsafe_allow_html=True)

# Footer
st.markdown("<br><br>", unsafe_allow_html=True)
st.markdown("""
    <div style='text-align: center; color: white; font-size: 18px; padding: 20px;'>
        Made with 💜 for Advanced ITT Training | Powered by Streamlit 🚀
    </div>
""", unsafe_allow_html=True)