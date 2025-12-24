import streamlit as st
import random
import time

# ---------- PAGE CONFIG ----------
st.set_page_config(page_title="Memory Game", layout="centered")

# ---------- GAME STYLE BACKGROUND ----------
st.markdown(
    """
    <style>
    .stApp {
        background: radial-gradient(circle at top, #1f2933, #0f172a);
        color: white;
    }

    h1 {
        text-align: center;
        color: #38bdf8;
        text-shadow: 0 0 12px #38bdf8;
    }

    button {
        background: linear-gradient(145deg, #111827, #1f2937);
        border: 2px solid #38bdf8;
        color: white;
        font-size: 30px !important;
        height: 75px;
        border-radius: 14px;
        box-shadow: 0 0 12px rgba(56, 189, 248, 0.4);
        transition: 0.2s ease-in-out;
    }

    button:hover {
        transform: scale(1.06);
        box-shadow: 0 0 20px #38bdf8;
    }

    div[data-testid="metric-container"] {
        background: #020617;
        border: 1px solid #38bdf8;
        border-radius: 14px;
        padding: 12px;
        box-shadow: 0 0 12px rgba(56, 189, 248, 0.3);
    }
    </style>
    """,
    unsafe_allow_html=True
)

# ---------- INIT GAME ----------
def init_game():
    # Use image paths for cards
    logos = [f"images/{i}.png" for i in range(1, 9)]
    cards = logos * 2
    random.shuffle(cards)

    st.session_state.cards = cards
    st.session_state.visible = [False] * 16
    st.session_state.selected = []
    st.session_state.turns = 0
    st.session_state.matches = 0

if "cards" not in st.session_state:
    init_game()

# ---------- UI ----------
st.title("🎮 Memory Game")
st.caption("Match the same images")

cols = st.columns(4)

for i in range(16):
    with cols[i % 4]:
        if st.session_state.visible[i]:
            st.image(st.session_state.cards[i], use_column_width=True)
        else:
            if st.button("❓", key=i, use_container_width=True):
                if len(st.session_state.selected) < 2:
                    st.session_state.visible[i] = True
                    st.session_state.selected.append(i)

# ---------- GAME LOGIC ----------
if len(st.session_state.selected) == 2:
    a, b = st.session_state.selected
    time.sleep(0.5)
    st.session_state.turns += 1

    if st.session_state.cards[a] == st.session_state.cards[b]:
        st.session_state.matches += 1
    else:
        st.session_state.visible[a] = False
        st.session_state.visible[b] = False

    st.session_state.selected = []

# ---------- SCORE ----------
st.divider()
st.metric("Turns", st.session_state.turns)
st.metric("Matches", f"{st.session_state.matches}/8")

# ---------- WIN ----------
if st.session_state.matches == 8:
    st.success("🎉 You matched all images!")
    st.balloons()

# ---------- RESET BUTTON ----------
st.markdown(
    """
    <style>
    .restart-button button {
        background-color: #0f172a;  /* dark background */
        color: #38bdf8;             /* text color */
        font-size: 24px;
        font-weight: bold;
        height: 60px;
        width: 200px;
        border-radius: 10px;
        border: 2px solid #38bdf8;
        box-shadow: 0 0 8px rgba(56, 189, 248, 0.4);
        transition: 0.2s ease-in-out;
        display: block;
        margin: 0 auto;
    }

    .restart-button button:hover {
        transform: scale(1.05);
        box-shadow: 0 0 16px #38bdf8;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown('<div class="restart-button">', unsafe_allow_html=True)
if st.button("🔄 Restart Game", key="restart"):
    init_game()
st.markdown('</div>', unsafe_allow_html=True)
