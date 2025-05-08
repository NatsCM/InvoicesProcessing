import os
import re
import pdfplumber

def process_receipt(pdf_path):
    with pdfplumber.open(pdf_path) as pdf:
        full_text = ""
        for page in pdf.pages:
            page_text = page.extract_text()
            if page_text:
                full_text += page_text + "\n"
    return full_text

def extract_client_line(lines):
    for line in lines:
        if "CLIENT" in line:
            return line[line.index("CLIENT"):].strip()
    return "CLIENT: Not found"

def extract_product_lines(lines):
    product_lines = []
    capture = False
    skip_next = False

    for i, line in enumerate(lines):
        stripped = line.strip()

        if stripped == "Item Quantity Net Amount Tax Rate Gross Amount Amount":
            capture = True
            continue

        if not capture:
            continue

        if stripped.startswith("NET"):
            break

        if re.match(r"\d{12,}\s*\(\d+\)", stripped):
            skip_next = False
            continue

        if skip_next:
            product_lines.append(stripped)
            skip_next = False
            continue

        if stripped:
            # Cortar antes del símbolo €
            if "€" in stripped:
                stripped = stripped.split("€")[0].strip()
            product_lines.append(stripped)

    return product_lines


def main():
    input_folder = "receipts"
    output_file = "mailText.txt"

    files = sorted([f for f in os.listdir(input_folder) if f.endswith(".pdf")])
    print(f"📄 Files found: {files}")

    with open(output_file, "w", encoding="utf-8") as output:
        for index, filename in enumerate(files, start=1):
            path = os.path.join(input_folder, filename)
            print(f"📂 Processing file: {filename}")

            text = process_receipt(path)
            lines = text.splitlines()
            client_info = extract_client_line(lines)
            product_lines = extract_product_lines(lines)

            output.write(f"\n--- {index} ---\n")
            output.write(client_info + "\n\n")

            for line in product_lines:
                output.write(line + "\n")

            output.write("\n" + "="*50 + "\n")

if __name__ == "__main__":
    main()


