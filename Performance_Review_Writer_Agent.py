"""Performance_Review_Writer_Agent — a LangChain agent that drafts an email from an idea,
then rewrites it to sound natural and human.

Setup: pip install -r requirements.txt, copy .env.example to .env, add your key.
Run:   python Performance_Review_Writer_Agent.py
"""

import logging
import os
import sys

from dotenv import load_dotenv
from langchain.agents import create_agent
from langchain_core.messages import HumanMessage
from langchain_core.prompts import PromptTemplate
from langchain_core.tools import tool
from langchain_openai import ChatOpenAI

# ----------------------------------------------------------------------
# Setup
# ----------------------------------------------------------------------

logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")
logger = logging.getLogger("Performance_Review_Writer")

load_dotenv()
if not os.getenv("OPENAI_API_KEY") or os.getenv("OPENAI_API_KEY").startswith("sk-your"):
    logger.error("OPENAI_API_KEY not set. Copy .env.example to .env and add your key.")
    sys.exit(1)

llm = ChatOpenAI(model="gpt-4.1-mini", temperature=0.7)

# ----------------------------------------------------------------------
# Tools
# ----------------------------------------------------------------------

DRAFT_PROMPT = PromptTemplate(
    input_variables=["performance_review"],
    template="""You are a professional performance review writer.
Given the following performance review, organises the accomplishments and then write a polished self-review narrative.

Performance Review: {performance_review}

Write the Performance Review with:
- Group the items into themes (delivery, collaboration, leadership, growth)
- quantify impact where possible
- flag which items are the strongest evidence
- Well-organized (2-3 short paragraphs)
- Professional closing

Return ONLY the Performance Review, nothing else.""",
)

HUMANIZE_PROMPT = PromptTemplate(
    input_variables=["draft"],
    template="""You are an expert at making Performance Reviews sound human and natural.

Take this Performance Review and rewrite it to sound like a real person wrote it.

Rules:
- Use contractions (I'm, we're, don't, can't)
- Vary sentence length (mix short and long sentences)
- Add a touch of warmth and personality
- Remove corporate jargon and stiff phrases
- Keep it professional but approachable
- Keep the same core message and structure
- Make it sound like something you'd actually send to a colleague

Performance Review draft:
{draft}

Return ONLY the humanized Performance Review, nothing else.""",
)


@tool
def draft_performance_review(organize_accomplishments: str) -> str:
    """Create a structured performance review draft from a list of accomplishments. Use this FIRST."""
    logger.info("[draft_performance_review] drafting: %s", organize_accomplishments)
    return llm.invoke(DRAFT_PROMPT.format(performance_review=organize_accomplishments)).content


@tool
def write_review_narrative(draft: str) -> str:
    """Rewrite a formal performance review draft to sound warm and natural. Use AFTER draft_performance_review."""
    logger.info("[write_review_narrative] writing narrative for draft")
    return llm.invoke(HUMANIZE_PROMPT.format(draft=draft)).content


# ----------------------------------------------------------------------
# Agent
# ----------------------------------------------------------------------

SYSTEM_PROMPT = """You are a Performance Review Humanizer assistant. Your job is to help users
write natural, human-sounding performance reviews.

When the user gives you a list of accomplishments, follow these steps:
1. First, use the draft_performance_review tool to create a structured performance review draft.
2. Then, use the write_review_narrative tool to make the draft sound natural and warm.
3. Return the final humanized performance review to the user.

Always use both tools in order: draft first, then humanize."""

agent = create_agent(model=llm, tools=[draft_performance_review, write_review_narrative], system_prompt=SYSTEM_PROMPT)


def run_performance_review_humanizer(accomplishments: str) -> str:
    """Run the agent on a list of accomplishments and return the humanized performance review."""
    result = agent.invoke({"messages": [HumanMessage(content=accomplishments)]})
    return result["messages"][-1].content


# ----------------------------------------------------------------------
# CLI
# ----------------------------------------------------------------------

def main() -> None:
    print("\nPERFORMANCE REVIEW HUMANIZER AGENT (LangChain + OpenAI)")
    print("Describe the accomplishments you want to review. Type 'quit' to exit.\n")

    while True:
        accomplishments = input("Your accomplishments: ").strip()
        if not accomplishments:
            continue
        if accomplishments.lower() in ("quit", "exit", "q"):
            break

        try:
            performance_review = run_performance_review_humanizer(accomplishments)
            print("\n" + "=" * 60)
            print(performance_review)
            print("=" * 60 + "\n")
        except Exception as e:
            logger.error("Agent failed: %s", e)


if __name__ == "__main__":
    main()
