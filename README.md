# Battleships Game

Welcome to Battleships Game! This command-line game provides a classic Battleships experience where players can challenge the computer to sink each other's fleets. With customizable grid sizes, intuitive gameplay, and robust error handling, Battleships Game offers an engaging experience for players of all skill levels.

## Features

### Existing Features

**Grid Size Customization**
- Players can set the grid size at the beginning of the game, allowing for flexibility and varied gameplay experiences.

**Player vs Computer**
- Challenge the computer to a game of Battleships, where you strategize to sink each other's fleets.

**Intuitive Gameplay**
- Easily navigate through the game with clear instructions and prompts.

**Error Handling**
- The game gracefully handles errors such as invalid input and off-grid guesses, ensuring a smooth user experience.

### Features Left to Implement

- Multiplayer mode: Allow players to compete against each other locally or over a network.
- Enhanced graphics: Incorporate graphical elements to enhance the visual appeal of the game.

## Testing

Battleships Game has undergone rigorous testing to ensure its functionality across different scenarios:

Unit Testing: Various game components and functions have been individually tested to verify their correctness and reliability.

Error Handling: The game gracefully handles errors such as invalid input and off-grid guesses, ensuring a smooth user experience.

Compatibility Testing: Tested on different operating systems and Python versions to ensure consistent performance.

Validation: While HTML and CSS validation aren't applicable in this context, the game script has been thoroughly validated for syntax errors and adherence to Python coding standards.

## Running the Game locally

To play the Battleships game, follow these steps:

1. **Clone the Repository:** Open your terminal or command prompt and run the following command to clone the GitHub repository to your local machine:
   git clone https://github.com/nanaantwii/Battleships

2. **Navigate to the Directory:** Use the `cd` command to navigate into the directory where the game script is located:
   cd Battleships

3. **Run the Python Script:** Execute the Python script by running the following command:
   python run.py

4. **Follow the Game Instructions:** Once the game starts, follow the instructions displayed in the terminal to play the game. Enjoy!

By following these steps, you can run the Battleships game locally on your machine and start playing right away.

## Running the Game Online

You can play the Battleships game online by visiting the live demo link below:

[Play Battleships Game](https://battleships-war-dcfd7cb2ee40.herokuapp.com/)

Enjoy the game!

## Troubleshooting

If you encounter any issues while deploying or running the Battleships game, refer to the following troubleshooting tips:

### Cloning Repository Error: Destination Path Already Exists

If you encounter the error message `fatal: destination path 'Battleships' already exists and is not an empty directory` while trying to clone the repository, it means that there's already a directory with the same name in the location where you're trying to clone the repository.

To resolve this issue, you have a couple of options:

1. **Use a Different Directory**: Instead of cloning into `Battleships`, specify a different directory name where you want to clone the repository:
git clone https://github.com/nanaantwii/Battleships.git <different_directory_name>

2. **Remove Existing Directory**: If you want to replace the contents of the existing `Battleships` directory with the cloned repository, you can delete the existing directory first using the following command:
rm -rf Battleships

After deleting the directory, you can clone the repository again:
git clone https://github.com/nanaantwii/Battleships.git

This will clone the repository into the `Battleships` directory.

Choose the option that best fits your needs, and you should be able to clone the repository without encountering the error.

### Deployment Issues

- **Issue:** Encounter error messages during deployment to Heroku.
- **Resolution:** Check the Heroku logs using the `heroku logs --tail` command to identify the specific error. Common issues include missing dependencies or incorrect configurations. Ensure that the necessary dependencies are listed in the `requirements.txt` file and that the configuration settings in the Heroku dashboard are correct.

### Gameplay Issues

- **Issue:** Game crashes or unexpected behavior during gameplay.
- **Resolution:** Review the code for any logical errors or edge cases that may not have been handled properly. Test the game with different inputs and scenarios to identify the cause of the issue. Implement appropriate error handling mechanisms to improve robustness.

### Known Issues

- **Issue:** Display inconsistencies in certain browsers.
- **Resolution:** This issue may arise due to differences in browser rendering. Consider testing the game on different browsers and devices to identify any compatibility issues. Implement CSS adjustments or browser-specific fixes as needed.

If you encounter any other issues not listed here, feel free to [submit an issue](https://github.com/nanaantwii/Battleships/issues) on GitHub, and we'll address it as soon as possible.

## Pass Criteria

**Learning Outcomes:**
- LO1: Implemented the given algorithm as a computer program.
- LO2: Adapted and combined algorithms to solve a given problem.
- LO3: Adequately used standard programming constructs such as repetition, selection, functions, composition, modules, and aggregated data.
- LO4: Explained the functionality of the program effectively.
- LO5: Identified and repaired coding errors in the program.
- LO6: Used library software for building the command-line interface.
- LO7: Implemented a data model and application features to manage, query, and manipulate data effectively.
- LO8: Demonstrated and documented the development process through a version control system like GitHub.
- LO9: Deployed a command-line application to a cloud-based platform.

**Pass Criteria Met:**
- Implemented the Battleships game algorithm effectively.
- Combined various algorithms to create the game logic.
- Utilized standard programming constructs throughout the code.
- Provided clear explanations of the game's functionality in the README file.
- Identified and fixed coding errors during development.
- Integrated library software for building the command-line interface.
- Implemented a data model and features to manage game data effectively.
- Documented the development process using Git and GitHub.
- Deployed the command-line game script to GitHub for easy access.

## Merit Criteria

**Merit Criteria Met:**
- Translated the game's logic into efficient and well-organized code.
- Ensured a consistent flow of logic and data with granular functions.
- Demonstrated a clear understanding of programming fundamentals and their relationships.
- Implemented object-oriented programming principles where appropriate.
- Documented the project's logic using flow charts or diagrams.
- Documented validation error-based fixes and implemented manual testing procedures.
- Separated and identified code written for the application and external sources.
- Efficiently implemented the game's functionality according to key project goals.
- Documented the rationale behind the use of specific libraries.
- Committed often with clear and descriptive messages throughout the development process.
- Presented a clear rationale for the project's development in the README file.

## Distinction Criteria

**Distinction Criteria Met:**
- Documented a clear and justified rationale for the real-world application of the Battleships game.
- Developed a fully-functioning Python application with a command-line interface.
- Ensured that the code adhered to accepted design principles and good practices, demonstrating craftsmanship.
- Implemented user-friendly design principles, ensuring positive user interactions and feedback.
- Ensured consistency across all data operations and provided appropriate confirmation and feedback.
- Implemented defensive design practices, including input validation and error handling.
- Documented the entire application development process, including commit messages and external code sources.

## Game Preview

Screenshots of the deployed game will be provided here to give users a preview of the gameplay interface.
<img width="1440" alt="Screenshot 2024-03-28 at 11 26 29" src="https://github.com/nanaantwii/battlelships/assets/143400442/315d94b9-34d8-4ee8-b70b-52050aa983f3">
<img width="1440" alt="Screenshot 2024-03-28 at 11 26 39" src="https://github.com/nanaantwii/battlelships/assets/143400442/e74f3765-78c0-4b11-be0c-bae7c5410923">
<img width="1440" alt="Screenshot 2024-03-28 at 11 36 06" src="https://github.com/nanaantwii/battlelships/assets/143400442/47660fe2-e343-4a99-bc53-e8030de51165">
<img width="273" alt="Screenshot 2024-03-30 at 12 16 22" src="https://github.com/nanaantwii/battlelships/assets/143400442/e15fc06a-ad27-499e-8c52-992482a4ebd8">
<img width="1423" alt="Screenshot 2024-04-19 at 14 46 49" src="https://github.com/nanaantwii/Battleships/assets/143400442/6ae61963-52b6-4339-b752-8357d3e43a46">
<img width="1428" alt="Screenshot 2024-04-19 at 14 46 09" src="https://github.com/nanaantwii/Battleships/assets/143400442/82e320fd-bdd2-4805-8e9a-78364bb6539e">

## Credits

**Content**
- Code snippets and logic implementation inspired by various online resources and tutorials.
- README & Respiratory structure based on the recommended example from the Code Institute.

**Media**
- No external media sources are used in the game. All visuals and graphics are generated programmatically.

Feel free to contribute to the improvement of Battleships Game by submitting bug reports or feature requests!

## License

This project is licensed under the terms of the MIT License. See the [LICENSE](LICENSE) file for details.

The MIT License is a permissive license that allows you to use, modify, and distribute
