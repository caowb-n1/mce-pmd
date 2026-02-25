import os
import markdown
from weasyprint import HTML

def convert_markdown_to_pdf(input_markdown_files, output_pdf_file):
    """
    Convert Markdown files to a single PDF file, extracting Doxygen comments as needed.
    :param input_markdown_files: List of paths to Markdown files.
    :param output_pdf_file: Path to save the generated PDF file.
    """

    # Combine Markdown content
    combined_markdown = ""
    for md_file in input_markdown_files:
        with open(md_file, 'r') as file:
            combined_markdown += file.read() + '\n\n'

    # Convert combined Markdown to HTML
    html_content = markdown.markdown(combined_markdown)

    # Create PDF from HTML
    HTML(string=html_content).write_pdf(output_pdf_file)

if __name__ == '__main__':
    # Example usage
    input_files = ['file1.md', 'file2.md']  # Update with your Markdown file paths
    output_file = 'output.pdf'
    convert_markdown_to_pdf(input_files, output_file)