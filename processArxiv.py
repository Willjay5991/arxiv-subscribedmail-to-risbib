import re

## form authors, "firstname lastname, firstname lastname, firstname lastname"
# ->"lastname, firstname and lastname, firstname and lastname, firstname"
def form_authors(authors):
    author_list = authors.strip().split(',')
    author_str = ''
    for i in range(len(author_list)):
        first_last_names = author_list[i].strip().rsplit(' ', 1)
        if author_str != '':
            author_str += ' and '
        author_str += first_last_names[-1].strip() + ', ' + first_last_names[0]
    return author_str


## extract paper info from arxiv email
def extract_paper_info(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()

    # Split the content by the separator
    papers = content.split('------------------------------------------------------------------------------')

    paper_info_list = []

    for paper in papers:
        if paper.strip():
            # Extract arXiv ID
            arxiv_id_match = re.search(r'arXiv:\d{4}\.\d{5}', paper)
            arxiv_id = arxiv_id_match.group(0) if arxiv_id_match else 'N/A'

            # jump over the paper if arxiv_id is not found
            if arxiv_id == 'N/A':
                continue

            # Extract Title
            title_match = re.search(r'Title:\s*(.*)', paper)
            title = title_match.group(1).strip() if title_match else 'N/A'

            # Extract Authors
            authors_match = re.search(r'Authors:\s*(.*)', paper)
            authors = authors_match.group(1).strip() if authors_match else 'N/A'
            authors = form_authors(authors)

            # # Extract Date
            # date_match = re.search(r'Date:\s*(.*)', paper)
            # date = date_match.group(1).strip() if date_match else 'N/A'

            # Extract Abstract
            areas = paper.split('\\\\\n')
            abstract = areas[-1].strip() if len(areas) > 1 else 'N/A'
            # abstract_match = re.search(r'\\\n\s*(.*)', paper, re.DOTALL)
            # abstract = abstract_match.group(1).strip() if abstract_match else 'N/A'

            # extract url
            url = f'https://arxiv.org/abs/{arxiv_id}'

            paper_info = {
                'Bibtex': arxiv_id,
                'Title': title,
                'Authors': authors,
                'Abstract': abstract,
                'Url': url
            }

            paper_info_list.append(paper_info)

    return paper_info_list

## wirte paper info into bib file
def wirte2bib(paper_info_list, new_bib):
    with open(new_bib, 'w') as f:
        for paper in paper_info_list:
            f.write(f"@article{{{paper['Bibtex']},\n")
            f.write(f"  title = {{{paper['Title']}}},\n")
            f.write(f"  author = {{{paper['Authors']}}},\n")
            f.write(f"  journal = {{arXiv preprint {paper['Bibtex']} }},\n")
            f.write(f"  year = {{20{paper['Bibtex'][6:8]}}},\n")
            f.write(f"  url = {{{paper['Url']}}},\n")
            f.write(f"  abstract = {{{paper['Abstract']}}}\n")
            f.write("}\n\n")
    print(f"Successfully wrote {len(paper_info_list)} papers to {new_bib}")

## wirte paper info into ris file
def wirte2ris(paper_info_list, new_ris):
    with open(new_ris, 'w') as f:
        for paper in paper_info_list:
            f.write(f"TY  - JOUR\n")
            f.write(f"TI  - {paper['Title']}\n")
            f.write(f"AU  - {paper['Authors']}\n")
            f.write(f"JO  - arXiv preprint {paper['Bibtex']}\n")
            f.write(f"PY  - 20{paper['Bibtex'][6:8]}\n")
            f.write(f"UR  - {paper['Url']}\n")
            f.write(f"AB  - {paper['Abstract']}\n")
            f.write("ER  - \n\n")
    print(f"Successfully wrote {len(paper_info_list)} papers to {new_ris}")



# Example usage
if __name__ == "__main__":
    file_path = 'arxiv.txt'
    mode = 'ris' # 'bib' or 'ris'
    name = file_path.split('.')[0]
    papers = extract_paper_info(file_path)
    if mode == 'bib':
        new_bib = f"{name}.bib"
        wirte2bib(papers, new_bib)
    elif mode == 'ris':
        new_ris = f"{name}.ris"
        wirte2ris(papers, new_ris)
