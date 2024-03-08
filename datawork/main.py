from fpdf import FPDF as f
import pandas as pd


def createbasicfile():
    file = f(orientation='P', unit='mm', format='A4')

    file.add_page()

    file.set_font(family='Times', style='B', size=12)
    file.cell(w=10, h=12, txt='Hello', align='L', ln=1)

    file.set_font(family='Times', style='B', size=12)
    file.cell(w=10, h=12, txt='Hellohello', align='L', ln=1)


    file.add_page()

    file.set_font(family='Times', style='B', size=12)
    file.cell(w=10, h=12, txt='Hello', align='L', ln=1)

    file.output("output.pdf")




def createCSVfile():

    file = f(orientation='P', unit='mm', format='A4')


    file2 = pd.read_csv("topics.csv")

    for index, row in file2.iterrows():
        print(row["Topic"])
        print(row["Pages"])

        file.add_page()
        file.set_font(family='Times', style='B', size=24)
        file.cell(w=10, h=12, txt=row["Topic"], align='L', ln=1)
        file.line(x1=10, y1=19, x2=200, y2=19)

        for i in range(row["Pages"]-1):
            file.add_page()


    file.output("output.pdf")



createCSVfile()