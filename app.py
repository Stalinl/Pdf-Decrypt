import os
import glob
import PyPDF2


def decrypt_pdf(pdf_loc: str, password: str):
    pdf_files = glob.glob(pdf_loc)

    for fl in pdf_files:
        file_name = os.path.basename(fl)
        print(f"Reading file: {file_name}")

        with open(fl, 'rb') as file_object:
            input_pdf = PyPDF2.PdfFileReader(file_object)
            if input_pdf.decrypt(password) == 0:
                print('Failed to decrypt!')
                continue

            output_pdf = PyPDF2.PdfFileWriter()
            for pn in range(input_pdf.numPages):
                output_pdf.addPage(input_pdf.getPage(pn))

            # os.path.join(pdf_loc + "/__", file_name)
            with open('__' + file_name, 'wb') as output_file:
                output_pdf.write(output_file)
                output_file.close()
        file_object.close()


decrypt_pdf(r"C:\Users\*.pdf", "****")
