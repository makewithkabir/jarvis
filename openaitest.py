import os
import openai
from config import apikey


openai.api_key = apikey


response = openai.ChatCompletion.create(
  model="gpt-3.5-turbo",
  messages=[
    {
      "role": "user",
      "content": "write a resignation email to your boss "
    },
    {
      "role": "assistant",
      "content": "Subject: Resignation Letter – [Your Name]\n\nDear [Boss's Name],\n\nI hope this email finds you well. \n\nI am writing to inform you that I have decided to resign from my position as [your job title] at [company name], effective [last working day, typically two weeks from the date of the email].\n\nI would like to express my deepest gratitude for the opportunities I have had to grow and develop both professionally and personally during my time at [company name]. Working with such a dedicated and supportive team has been an incredible experience, and I am truly thankful for the knowledge and skills I have acquired.\n\nHowever, after careful consideration, I have made the decision to pursue a new career opportunity that aligns more closely with my long-term goals and aspirations. While I am excited about this next chapter in my professional journey, it is with a heavy heart that I tender my resignation.\n\nI am committed to ensuring a smooth transition during this period. I am willing to assist with the training and handover process for my replacement, as well as completing any pending projects or tasks I am currently responsible for. Please let me know how I can be of assistance during this transition period.\n\nI sincerely apologize for any inconvenience my resignation may cause to the team or the company."
    }
  ],
  temperature=1,
  max_tokens=256,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0
)

#print(response)
print(response["choices"][0]["message"]["content"])






'''
{
  "id": "chatcmpl-7mOxftAfgVecTCgr9eqesFHI3AfAy",
  "object": "chat.completion",
  "created": 1691770051,
  "model": "gpt-3.5-turbo-0613",
  "choices": [
    {
      "index": 0,
      "message": {
        "role": "assistant",
        "content": "I would like to take this opportunity to express my deep gratitude for the support and guidance you have provided me throughout my tenure at [company name]. Your leadership and mentorship have been invaluable, and I am truly grateful for all the opportunities I have had under your supervision.\n\nI believe that the time spent at [company name] has significantly contributed to my personal and professional growth. The knowledge and skills I have gained here will undoubtedly serve as a strong foundation for my future endeavors. I want to assure you that I will do my best to ensure a smooth transition and tie up any loose ends before my departure.\n\nI would also like to extend my appreciation to the entire team at [company name]. The camaraderie, collaboration, and shared goals among my colleagues have made my time here truly enjoyable. It is the people at [company name] that have made it such a special place to work, and I will sincerely miss being a part of this team.\n\nPlease consider this email as a formal notice of my resignation. I will be happy to discuss the transition further and provide any assistance needed to ensure a seamless transfer of responsibilities. Please let me know how I can best support this process.\n\nOnce again, I want to thank you for the opportunities, support, and experiences I have had"
      },
      "finish_reason": "length"
    }
  ],
  "usage": {
    "prompt_tokens": 275,
    "completion_tokens": 256,
    "total_tokens": 531
  }
}
'''