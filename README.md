# 🎮 Memory Game (Streamlit)

A visually appealing **Memory Matching Game** built with **Streamlit**, where players flip cards and match identical images. This project demonstrates interactive web apps using Python, with a focus on UI styling, game logic, and session management.

## 🌟 Features

* **Image-based cards**: Each card displays an image when flipped.
* **Dark-themed UI**: Custom CSS for a sleek, modern look.
* **Animated buttons**: Hover effects for interactive experience.
* **Game logic**: Tracks turns, matches, and automatically handles card flipping.
* **Victory celebration**: Balloons animation when all matches are found.
* **Custom restart button**: Styled and centered to fit the theme.

## 🛠️ Installation

1. Clone this repository:

```bash
git clone https://github.com/yourusername/memory-game.git
cd memory-game
```

2. (Optional) Create a virtual environment:

```bash
python -m venv venv
source venv/bin/activate  # macOS/Linux
venv\Scripts\activate     # Windows
```

3. Install dependencies:

```bash
pip install streamlit
```

4. Add **your images**:
   Place 8 images inside an `images/` folder in the same directory as the script, named:

```
images/1.png
images/2.png
...
images/8.png
```

## 🚀 Run the Game

```bash
streamlit run memory_game.py
```

*(Replace `memory_game.py` with your filename if different)*

## 🎮 How to Play

1. Click on a **card** to reveal its image.
2. Click a second card to try to **match it** with the first.
3. If the images match, they remain visible; otherwise, they flip back.
4. Track your **turns** and **matches** in real-time.
5. Click the **Restart Game** button to start over.
6. Win the game by matching all 8 pairs of images! 🎉

## ⚙️ Code Structure

* **Game Initialization**: Shuffles cards and sets session state variables.
* **UI Rendering**: Displays cards in a 4x4 grid using `st.columns`.
* **Game Logic**: Checks for matches, updates turns, and flips cards.
* **Score Tracking**: Displays current turns and matched pairs.
* **Restart Button**: Resets the game while keeping UI styling intact.

## 🖌️ Customization

* Replace `images/` with your own set of images.
* Adjust **CSS** in the script for colors, button size, and hover effects.
* Change **grid size** or number of cards by modifying the code in `init_game()` and UI loop.

## 📚 Requirements

* Python 3.9+
* Streamlit

Install requirements:

```bash
pip install streamlit
```

## ✨ Credits

* Built with ❤️ using **Python** and **Streamlit**
* Inspired by classic memory card games

## 📄 License

This project is **MIT Licensed** – feel free to use and modify for personal or educational purposes.
