import argparse
import pandas as pd
parser = argparse.ArgumentParser()
parser.add_argument("input", help="Enter the path to the input file")
parser.add_argument("output", help="Enter the path to the output file")
args = parser.parse_args()
cvsDataframe = pd.read_csv(args.input)
resultExcelFile = pd.ExcelWriter(args.output)
cvsDataframe.to_excel(resultExcelFile, index=False)
resultExcelFile.save()


