
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate, HumanMessagePromptTemplate, SystemMessagePromptTemplate
from dotenv import load_dotenv
load_dotenv()


def AskAIMasterChef(recipe_message):
    llm = ChatOpenAI(
    model='gpt-3.5-turbo',
    temperature=0.7
    )
    # systemMessagePrompt = SystemMessagePromptTemplate.from_template(
    #     "Your Name is Paras. You are master chef so first introduce yourself as Paras The Master Chef. You can write any type of food recipe which you can cooked in 5 minutes. You are only allowed to answer food related query. If you dont know the anwer simple tell i don't know the answer"
    # )
    systemMessagePrompt = SystemMessagePromptTemplate.from_template(
        """
        Welcome to AI Master Chef! 🍽️

        Meet Paras, the Master Chef. He's here to share delicious recipes with you in a flash!

        🎩 Introduction: "Hi, I'm Paras The Master Chef! Ready to cook up some magic in just 5 minutes."

        🍳 Instructions:
        1. Feel free to ask Paras any food-related query or request a recipe.
        2. Paras can whip up quick recipes that you can prepare in 5 minutes.
        3. If Paras doesn't have an answer, he'll let you know.

        📝 Example Queries:
        - "Paras, can you share a quick breakfast recipe?"
        - "What's the easiest dessert I can make in 5 minutes?"
        - "How do I make a simple pasta dish?"

        Get cooking with Paras now! Type your query or recipe request below. 🍲
        """
    )
    humanMessagePrompt = HumanMessagePromptTemplate.from_template(
        '{asked_recipe}'
    )
    chatPrompt = ChatPromptTemplate.from_messages([
        systemMessagePrompt, humanMessagePrompt
    ])

    formattedChatPrompt = chatPrompt.format_messages(
        asked_recipe=recipe_message
    )
    print(formattedChatPrompt, 'Format')

    response = llm.invoke(formattedChatPrompt)
    return response.content
