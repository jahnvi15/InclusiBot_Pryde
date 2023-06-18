import cohere
from tqdm import tqdm
# Paste your API key here. Remember to not share publicly
api_key = 'HXDVfZgDHkcU58spHlviXDz0u82T06b7oZZlO7Xo'

# Create and retrieve a Cohere API key from os.cohere.ai
co = cohere.Client(api_key)
health_database = [
    ("flu", "The symptoms of the flu include fever, cough, sore throat, body aches, and fatigue. (Source: CDC)"),
    ("flu", "Getting vaccinated annually can help prevent the flu. (Source: CDC)"),
    ("headache", "Common causes of headaches include tension, dehydration, sinus congestion, and migraines. (Source: Mayo Clinic)"),
    ("headache", "Keeping a regular sleep schedule and managing stress can help reduce headaches. (Source: Mayo Clinic)"),
    ("diabetes", "Risk factors for diabetes include obesity, family history, physical inactivity, and unhealthy diet. (Source: American Diabetes Association)"),
    ("diabetes", "Maintaining a healthy weight and engaging in regular physical activity can help prevent diabetes. (Source: American Diabetes Association)"),
    ("sexual education", "Sexual education covers topics such as reproductive health, contraception, consent, sexually transmitted infections (STIs), and healthy relationships. (Source: Planned Parenthood)"),
    ("sexual education", "Effective communication and mutual respect are important in healthy relationships. (Source: Planned Parenthood)"),
    ("birth control", "Some common types of birth control methods include hormonal methods like birth control pills, patches, and injections, barrier methods like condoms and diaphragms, intrauterine devices (IUDs), and sterilization procedures. (Source: American Sexual Health Association)"),
    ("birth control", "It's important to consult with a healthcare provider to determine the most suitable birth control method for individual needs. (Source: American Sexual Health Association)"),
    ("asthma", "Common triggers for asthma attacks include allergens like pollen and pet dander, respiratory infections, exercise, cold air, and irritants like smoke and strong odors. (Source: American Academy of Allergy, Asthma, and Immunology)"),
    ("asthma", "Taking prescribed medications as directed and avoiding known triggers can help manage asthma symptoms. (Source: American Academy of Allergy, Asthma, and Immunology)"),
    ("nutrition", "A healthy diet includes a variety of fruits, vegetables, whole grains, lean proteins, and healthy fats. It is important to limit added sugars, sodium, and saturated fats. (Source: Academy of Nutrition and Dietetics)"),
    ("nutrition", "Drinking plenty of water and practicing portion control are essential for maintaining a balanced diet. (Source: Academy of Nutrition and Dietetics)"),
    ("cancer", "Common signs and symptoms of cancer include unexplained weight loss, fatigue, pain, changes in the skin, persistent cough, and changes in bowel or bladder habits. (Source: American Cancer Society)"),
    ("cancer", "Early detection through regular screenings can significantly improve cancer treatment outcomes. (Source: American Cancer Society)"),
    ("mental health", "Some self-care practices for maintaining good mental health include getting enough sleep, exercising regularly, practicing relaxation techniques, maintaining a healthy diet, and seeking support from loved ones. (Source: National Institute of Mental Health)"),
    ("mental health", "Open communication and destigmatization of mental health issues are crucial for promoting overall well-being. (Source: National Institute of Mental Health)"),
    ("allergies", "Common allergens that can cause allergic reactions include pollen, dust mites, pet dander, mold spores, certain foods, insect stings, and certain medications. (Source: American College of Allergy, Asthma, and Immunology)"),
    ("allergies", "Avoiding known allergens and carrying necessary medications, such as epinephrine autoinjectors, can help manage allergic reactions. (Source: American College of Allergy, Asthma, and Immunology)"),
    # Add more entries to the database as needed
]
class cohereExtractor():
    def __init__(self, examples, example_labels, labels, task_desciption, example_prompt):
        self.examples = examples
        self.example_labels = example_labels
        self.labels = labels
        self.task_desciption = task_desciption
        self.example_prompt = example_prompt

    def make_prompt(self, example):
        examples = self.examples + [example]
        labels = self.example_labels + [""]
        return (self.task_desciption +
                "\n---\n".join( [examples[i] + "\n" +
                                self.example_prompt +
                                 labels[i] for i in range(len(examples))]))

    def extract(self, example):
      extraction = co.generate(
          model='xlarge',
          prompt=self.make_prompt(example),
          max_tokens=10,
          temperature=0.1,
          stop_sequences=["\n"])
      return(extraction.generations[0].text[:-1])


cohereHealthExtractor = cohereExtractor([e[1] for e in health_database],
                                       [e[0] for e in health_database], [],
                                       "",
                                       "extract the Keywords from the health related answers:")
text = cohereHealthExtractor.make_prompt('What are the symptoms of the flu?')
# Create an instance of the SexualEducationChatbot and pass the health_database as the database

class SexualEducationChatbot:
    def __init__(self, database):
        self.database = database

    def extract_keywords(self, input_text):
        extraction = cohereHealthExtractor.extract(input_text)
        return extraction.split(',')

    def search_answer(self, keywords):
        for keyword, answer in self.database:
            if keyword in keywords:
                return answer
        return "I'm sorry, but I'm unable to provide information on that topic. For accurate and reliable information, please consult a healthcare professional or trusted educational resources."

    def chat(self):
        print("Welcome to the Sexual Education Chatbot!")
        print("I can provide information on various topics related to sexual education.")
        print("How can I assist you today?")

        while True:
            user_input = input("User: ")

            if user_input.lower() == "exit":
                print("Chatbot: Thank you for using the Sexual Education Chatbot. Goodbye!")
                break

            keywords = self.extract_keywords(user_input)
            answer = self.search_answer(keywords)
            print("Chatbot:", answer)

chatbot = SexualEducationChatbot(health_database)

# Start the chatbot
chatbot.chat()
