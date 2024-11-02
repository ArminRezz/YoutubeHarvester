from fpdf import FPDF

def convert_txt_to_pdf(txt_file, pdf_file):
    # Create a PDF object
    pdf = FPDF()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.set_font("Arial", size=12)

    word_count = 0  # Initialize word count
    pdf_index = 1  # Initialize PDF index for naming
    current_pdf_file = f"{pdf_file.split('.')[0]}_{pdf_index}.pdf"  # Create initial PDF file name
    pdf.add_page()  # Add the first page

    # Read the text file and add it to the PDF
    with open(txt_file, 'r') as file:
        for line in file:
            words_in_line = len(line.split())
            word_count += words_in_line  # Update word count

            # Check if word count exceeds 4200
            if word_count > 1000:
                pdf.output(current_pdf_file)  # Save the current PDF
                pdf_index += 1  # Increment PDF index
                current_pdf_file = f"{pdf_file.split('.')[0]}_{pdf_index}.pdf"  # Create new PDF file name
                pdf = FPDF()  # Create a new PDF object
                pdf.set_auto_page_break(auto=True, margin=15)
                pdf.set_font("Arial", size=12)
                pdf.add_page()  # Add a new page for the new PDF
                word_count = words_in_line  # Reset word count for the new PDF

            pdf.cell(200, 10, txt=line.encode('latin-1', 'replace').decode('latin-1'), ln=True)

    # Save the last PDF to a file
    pdf.output(current_pdf_file)

# Example usage
if __name__ == "__main__":
    convert_txt_to_pdf("output_essay_unique.txt", "output.pdf")