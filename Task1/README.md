Open Google Colab
Create a new notebook
Install dependencies: python!pip install transformers torch

Copy and paste the chatbot code into a new cell
Run the chatbot:
if __name__ == "__main__":
    Chatbot().run()


Code Structure
Classes

ModelLoader: Handles loading and initializing the TinyLlama model
ChatMemory: Manages conversation history using a circular buffer
Chatbot: Main chatbot interface that coordinates model and memory

Key Methods

ModelLoader.load(): Downloads and initializes the model
ChatMemory.add(): Stores user input and bot responses
ChatMemory.get_context(): Retrieves formatted conversation history
Chatbot.run(): Main chat loop


