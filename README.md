
# Asteroids Game

Asteroids Game is a classic arcade-style game where players navigate a spaceship to destroy incoming asteroids. The game is built using Python and Pygame, offering a great learning experience for game development enthusiasts.

## Features

- **Player-controlled spaceship:** Navigate and shoot down asteroids.
- **Dynamic asteroid fields:** Randomly generated asteroids with split mechanics.
- **Scoring system:** Keep track of your achievements with a real-time score panel.
- **Collision detection:** Avoid crashing into asteroids or risk ending the game.
- **Optimized rendering:** Uses Pygame's sprite groups for efficient drawing and updating.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/Reve1ation/Asteroids_Game.git
   cd Asteroids_Game
   ```

2. Create a virtual environment and activate it:
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Run the game:
   ```bash
   python main.py
   ```

## Gameplay

- **Move:** Use the arrow keys to navigate your spaceship.
- **Shoot:** Press the space bar to fire shots at incoming asteroids.
- **Goal:** Destroy asteroids to earn points while avoiding collisions.

## Project Structure

```
Asteroids_Game/
├── Game_Objects/
│   ├── asteroid.py          # Asteroid behavior and splitting logic
│   ├── asteroidfield.py     # Generates and manages the asteroid field
│   ├── player.py            # Player's spaceship logic
│   ├── rectangle_shape.py   # Base class for rectangular shapes
│   ├── score_panel.py       # Displays and updates the player's score
│   ├── shot.py              # Shot mechanics
├── utilities/
│   ├── constants.py         # Screen dimensions and other global constants
├── main.py                  # Entry point for the game
└── README.md                # Project documentation
```

## Future Improvements

- Add power-ups for the player (e.g., shields, rapid fire).
- Implement levels with increasing difficulty.
- Introduce multiplayer mode for shared fun.
- Add background music and sound effects for a richer experience.

## Contributions

Contributions are welcome! Feel free to fork the repository, make changes, and submit a pull request. For major changes, please open an issue first to discuss what you'd like to change.

## License

This project is open-source and available under the [MIT License](LICENSE).
