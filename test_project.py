from project import is_valid, return_dates, save_pdf
from fpdf import FPDF
import filecmp
import pypdf

def test_is_valid():
    assert is_valid("Chicago") == True
    assert is_valid("Seattle") == True
    assert is_valid("New York City") == True
    assert is_valid("Albuquerque") == True
    assert is_valid("Los Angeles") == True

    assert is_valid("London") == False
    assert is_valid("Paris") == False
    assert is_valid("Tokyo") == False
    assert is_valid("Beijing") == False

def test_return_dates():

    assert return_dates(["03/04/1837", "13/11/1851", "27/08/1664", "23/04/1706", "09/04/1781"]) == "03/04/1837, 13/11/1851, 27/08/1664, 23/04/1706 and 09/04/1781"
    assert return_dates(["12/10/1492", "01/20/1778", "08/27/1664", "27/01/1820", "26/01/1788"]) == "12/10/1492, 01/20/1778, 08/27/1664, 27/01/1820 and 26/01/1788"
    assert return_dates(["03/04/1837", "11/13/1851", "08/27/1664", "04/23/1706", "09/04/1781"]) == "03/04/1837, 11/13/1851, 08/27/1664, 04/23/1706 and 09/04/1781"


def test_save_pdf(monkeypatch):
    file = FPDF()
    file.add_page()
    file.set_font("Times", "", 12)
    file.write(0, "Test_1 \n Test 1 \n Test 1")
    file.output("temporary.pdf")
    monkeypatch.setattr("builtins.input", lambda: "q")
    save_pdf()
    assert pypdf.PdfReader("temporary.pdf").pages[0].extract_text() == pypdf.PdfReader("user_requested_data.pdf").pages[0].extract_text()

    file = open("user_requested_data.pdf","w")
    file.close
    file = FPDF()
    file.add_page()
    file.set_font("Times", "", 12)
    file.write(0, "Mountains \n Skies \n Air")
    file.output("temporary.pdf")
    monkeypatch.setattr("builtins.input", lambda: "q")
    save_pdf()
    assert pypdf.PdfReader("temporary.pdf").pages[0].extract_text() == pypdf.PdfReader("user_requested_data.pdf").pages[0].extract_text()




