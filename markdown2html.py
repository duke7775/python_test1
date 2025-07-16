#markdown转HTML
import markdown

def convert_markdown_to_html() -> None:
    with open('markdown2html.md', 'r', encoding='utf-8') as md_file:
        markdown_text = md_file.read()
    html_output = markdown.markdown(markdown_text)
    with open('markdown2html.html', 'w', encoding='utf-8') as html_file:
        html_file.write(html_output)
    print("Markdown has been converted to HTML and saved as 'markdown2html.html'.")

if __name__ == "__main__":
    convert_markdown_to_html() 



