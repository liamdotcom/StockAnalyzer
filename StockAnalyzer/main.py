import multiprocessing
import stockPlotter
import stockScraper
import time
import os

ticker= 'TSLA'

def print_menu():

    print("====================================\n"
          "MENU\n"
          "====================================\n"
          "1 - Set Ticker\n"
          "2 - Start Analysis\n"
          "3 - Exit\n"
          "====================================\n")


if __name__ == '__main__':
    print_menu()
    choice = 0
    while choice != 2 or choice != 3:
        print_menu()
        choice = int(input("Enter Selection: "))
        if choice == 1:
            ticker = input("Enter Ticker: ")
        if choice == 2:
            p1 = multiprocessing.Process(target=stockScraper.startScrape, args=[ticker])
            p2 = multiprocessing.Process(target=stockPlotter.startPlot)
            f = open('stock_data.csv', 'w')
            f.truncate()
            f.close()
            p1.start()
            time.sleep(10)
            p2.start()
            p1.join()
            p2.join()
        if choice == 3:
            print("Closing...")
            time.sleep(3)




    

