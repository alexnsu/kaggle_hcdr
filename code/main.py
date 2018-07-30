import logging
import pandas as pd

def main():
    data = pd.read_csv("data/application_train.csv")
    print(data)

if __name__ == "__main__":
    logging.basicConfig(filename='logs.log', level=logging.DEBUG, format='%(asctime)s %(message)s', filemode='w')
    try:
        main()
    except Exception as e:
        logging.exception("Main crashed. Error:\n%s", e)
