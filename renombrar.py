import os
import re
import PyPDF2

def extract_info_from_pdf(pdf_path):
    with open(pdf_path, 'rb') as pdf_file:
        pdf_reader = PyPDF2.PdfReader(pdf_file)
        text = ''
        for page in pdf_reader.pages:
            text += page.extract_text()
        return text

def rename_pdf_files(folder_path):
    for filename in os.listdir(folder_path):
        if filename.lower().endswith('.pdf'):
            pdf_path = os.path.join(folder_path, filename)
            extracted_text = extract_info_from_pdf(pdf_path).split('\n', 1)[0]
            resultado = re.search(r"Fecha\s*:\s*([\d/]+)\s*-\s*Nro\. Entrada:\s*(\d+)\s*Medico\s*:\s*\w+\s*Paciente:\s*([\w\s]+)", extracted_text)

            if resultado:
                fecha = resultado.group(1).replace('/','-')
                orden = resultado.group(2)
                paciente = resultado.group(3)
                new_name = (f"{fecha}_{orden}_{paciente}.pdf")
                new_path = os.path.join(folder_path, new_name)
                os.rename(pdf_path, new_path)
                print(f"Cambio nombre {filename} a {new_name}")
            else:
                print("sin_coincidencia")            
                        
folder_path = './'
rename_pdf_files(folder_path)