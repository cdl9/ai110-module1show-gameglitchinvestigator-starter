# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
  *I was able to guess number once loaded. I saw options to change difficultu, see hints, and restart games
- List at least two concrete bugs you noticed at the start  
  (for example: "the hints were backwards").
  *The hints are backward
  *The difficulty dropdown does not correspond to the right level.
  *After changing difficulty, the main section, doesn't update range or attemps
  *After the first game is finished. Clicking new game doesn't reset values

**Bug Reproduction Log**

Document at least 3 bugs you found. Add rows as needed.

| Input | Expected Behavior | Actual Behavior | Console Output / Error |
|-------|-------------------|-----------------|------------------------|
|25|Correct number was 74. Hint should be go higher|The hint was saying to go lower | Line 38 and 40 - Correct output, wrong message being sent|

|Click New Game Button|Empty input fill and how new game message |Previous input stays and it shows a message that "You already won. Start a new game to play again."| Line 140|

| Difficulty dropdown|The number of attempts shoudl be consistent with the difficulty level | If i choose easy, it's 6, normal, it's 8, hard, it's 5. The attempts are fine, but Hard's guess range (1-50) is narrower than Normal's (1-100), so Hard is actually easier to win| Line 4 - get_range_for_difficulty gives Hard a smaller range than Normal, Line 109-111 - the "Guess a number between 1 and 100" message never updates to match the real range |

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
  Claude

- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
  The ouput for the hints when check_guess was called were inverted. The AI suggested to swap them. I check on the live app if the hints were correct and they were. We also used pytest and verify with a test case for higher and lower inputs.

- Give one example of an AI suggestion you did not accept as written (including what the AI suggested, why you rejected or changed it, and how you verified your version). It does not have to be a suggestion that was wrong: over-engineered, out of scope, harder to read, or a poor fit for this codebase all count.
 At some point it suggested to add test cases for the live app. These tests would include actions as press buttons, etc. Since we are testing only logic, I did not accept it as it would be out of the scope that we needed for this exercise.


---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
  I verify the logic and code that was being suggested by Claude. I also used pytest and manually test it on the live app

- Describe at least one test you ran (manual or using pytest) and what it showed you about your code.
  I manually entered a number lower than the secret and the hint told me to go higher. 

  I also pressed the "New Game" button and it reset all the fields, including the guess input field.

  At the end, I asked Claude to add some test cases to verify the bugs that were solved. I checked the test cases and then run them. They all went through

- Did AI help you design or understand any tests? How?
  Yes, the first test cases that were already included the file were receiving the output and message. Therefore, it was giving an error when comparing to the expected result.
---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?

Streamlit reruns the whole code ob every interaction, and session state can hold values that remain permanent on reruns. It needs to be explicitly changed.
---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
  - I like using Claude to explain certain lines of code. Or if I need to find out why a ceertain behavior is happening, it can help me pin point it.
- What is one thing you would do differently next time you work with AI on a coding task?
  - I would always revise any improvements is suggesting. Giving specific and clear prompts is necessary too.
- In one or two sentences, describe how this project changed the way you think about AI generated code.
  -It helped me get used to working with an AI tool to understand concepts and to optmize workflow. As long as I review and suggestions. 
  -Generating test cases to verify functionality
