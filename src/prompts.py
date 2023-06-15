TASK = {
    'Quote + Mises': (
        "Answer the question truthfully based on the text below. "
        "Include at least one verbatim quote (marked with quotation marks) and a comment where to find it in the text (i.e., name of the section and page number). "
        "Use ellipsis in the quote to omit irrelevant parts of the quote. "
        "After the quote, compare this opinion with what the Austrian School of Economics theorists (especially Ludwig von Mises) would think."
    ),
    'Comment': (
        "Answer the question truthfully based on the text below. "
        "Include a verbatim quote and a comment on where to find it in the text (page number). "
        "After the quote, make a comment as a knowledgeable person would."
    ),
    'Comprehensive': (
        "Generate a comprehensive and informative answer for a given question solely based on the provided document fragments. " 
        "You must only use information from the provided fragments. Use an unbiased and journalistic tone. Combine fragments together into coherent answer. " 
        "Do not repeat text. Cite fragments using [${number}] notation. Only cite the most relevant fragments that answer the question accurately. " 
        "If different fragments refer to different entities with the same name, write separate answer for each entity."
    ),
    'Request': 'Do what you are asked to do with the provided text.',
    'Summary': 'Make a summary with the provided text.',
    'FAQ': 'Make a FAQ with the provided text.',
}

HYDE = "Write an example answer to the following question. Don't write a generic answer, just assume everything that is not known."

SUMMARY = {
    'v2': 'Describe the document from which the fragment is extracted. Omit any details.',
    'v1': "Describe the document from which the fragment is extracted. Do not describe the fragment; focus on figuring out what kind of document it is.",
}
