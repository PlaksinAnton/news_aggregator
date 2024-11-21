import google.generativeai as genai
import os

if "GEMINI_API_KEY" not in os.environ:
    raise EnvironmentError("GEMINI_API_KEY is not set in the environment variables.")

genai.configure(api_key=os.environ["GEMINI_API_KEY"])

# Create the model
generation_config = {
  "temperature": 0.2,
  "top_p": 0.95,
  "top_k": 40,
  "max_output_tokens": 40,
  "response_mime_type": "text/plain",
}

model = genai.GenerativeModel(
  model_name="gemini-1.5-flash",
  generation_config=generation_config,
  system_instruction="Context: \nYou are precise summarizer of user requests. User sends you information about what news articles he wants to get. You summarize user preferences for better searching news by titles.\n\nSteps:\n1. Understand topics that the user is interested in.\n2. If you find more than 3 topics, find the way to compact it in 3 or less.\n3. Write out user topics trying your best not to loode initial meaning.\n\nOutput format:\nEach topic should be no more than 3 words. Topics (or topic) should be written in line in lowercase without punctuation marks. Separated by 'AND', 'AND NOT', or 'OR' in uppercase, depending on the meaning of the user request.\n\nOutput example:\ntechnoligies AND NOT war technoligies OR politics\n",
)
