import os
import openai
openai.api_key = ("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")


def rewrite(prompt):
  print(openai.Completion.create(
    model="text-davinci-003",
    prompt=f"rewrite {prompt}",
    max_tokens=7,
    temperature=0
  )
  )

def split_paragraphs_into_sentences():
  pass