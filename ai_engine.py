import openai
import PyPDF2

from dotenv import load_dotenv

load_dotenv()

openai.api_key = os.getenv("OPENAI_KEY")


def extract_text(file):
    reader = PyPDF2.PdfReader(file)
    text = ""
    for p in reader.pages:
        text += p.extract_text()
    return text


def generate_plan(role, resume_text):

    prompt = f"""
    You are enterprise onboarding AI.

    Role: {role}

    Resume:
    {resume_text}

    Generate structured 30 day onboarding roadmap.

    Format:

    Week 1:
        Module:
            Task:
    """

    res = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.7
    )

    return res["choices"][0]["message"]["content"]


def mentor_chat(msg):

    prompt = f"""
    You are senior AI mentor helping in tech onboarding.

    User message:
    {msg}
    """

    res = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}]
    )

    return res["choices"][0]["message"]["content"]
