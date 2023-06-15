TASK = {
    'v6': (
        "Answer the question truthfully based on the text below. "
        "Include at least one verbatim quote (marked with quotation marks) and a comment where to find it in the text (i.e., name of the section and page number). "
        "Use ellipsis in the quote to omit irrelevant parts of the quote. "
        "After the quote, compare this opinion with what the Austrian School of Economics theorists (especially Ludwig von Mises) would think."
    ),
    'v5': (
        "Answer the question truthfully based on the text below. "
        "Include a verbatim quote and a comment on where to find it in the text (page number). "
        "After the quote, make a comment as a knowledgeable person would."
    ),
    'v4': (
        "Answer the question truthfully based on the text below. "
        "Include a verbatim quote and a comment on where to find it in the text (i.e., name of the section and page number). "
        "After the quote, write an explanation (in a new paragraph) for a young reader."
    ),
    'v3': 'Answer the question truthfully based on the text below. Include a verbatim quote and a comment on where to find it in the text (i.e., name of the section and page number).',
    'v2': 'Answer the question based on context. The answer should be elaborate and based only on the context.',
    'v1': 'Answer the question based on context.',
}

HYDE = "Write an example answer to the following question. Don't write a generic answer, just assume everything that is not known."

SUMMARY = {
    'v2': 'Describe the document from which the fragment is extracted. Omit any details.',
    'v1': "Describe the document from which the fragment is extracted. Do not describe the fragment; focus on figuring out what kind of document it is.",
}
