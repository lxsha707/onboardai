import openai
import PyPDF2

openai.api_key = "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"


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
