import os  # import os library to lcear terminal
import platform  # import platform library to check os
import time  # import time library to wait inbetween text

# set the clear terminal command bassed on user's os
clear_command = 'cls'
if platform.system() == 'Linux' or platform.system() == 'Darwin':
    clear_command = 'clear'

# dict of brands as keys and its values are 2d arrays made which is just a list of lists
# Ex:
# [
# [1,1,1,1,1,1,1,1],
# [1,1,1,1,1,1,1,1],
# [1,1,1,1,1,1,1,1],
# [1,1,1,1,1,1,1,1],
# [1,1,1,1,1,1,1,1],
# [1,1,1,1,1,1,1,1],
# [1,1,1,1,1,1,1,1]
# ]
# rows are attributes, Name,CPU,GPU,Storage,Ram,Screen, Price
# The colums are different devices under that brand
Brands = {
    "Apple": [["MacBook Air", "MacBook Pro 13-inch", "MacBook Pro 16-inch", "MacBook", "MacBook Pro 14-inch", "MacBook Pro 15-inch", "MacBook Pro 17-inch", "MacBook Pro 13-inch M1", "MacBook Pro 16-inch M1", "MacBook Air M1"], ["Apple M1 chip", "Intel Core i5", "Intel Core i9", "Intel Core m3", "Apple M1 Pro chip", "Intel Core i7", "Intel Core i7", "Apple M1 chip", "Apple M1 Pro chip", "Apple M1 chip"], ["Apple M1 chip", "Intel Iris Plus Graphics 645", "AMD Radeon Pro 5300M", "Intel HD Graphics 615", "Apple M1 Pro chip", "AMD Radeon Pro 455", "NVIDIA GeForce GT 330M", "Apple M1 chip", "Apple M1 Pro chip", "Apple M1 chip"], ["256GB SSD", "512GB SSD", "512GB SSD", "256GB SSD", "512GB SSD", "512GB SSD", "512GB SSD", "256GB SSD", "512GB SSD", "512GB SSD"], ["8GB", "8GB", "16GB", "8GB", "16GB", "16GB", "4GB", "8GB", "16GB", "8GB"], ["13.3-inch Retina Display", "13.3-inch Retina Display", "16-inch Retina Display", "12-inch Retina Display", "14-inch Retina Display", "15.4-inch Retina Display", "17-inch LED-backlit Glossy Display", "13.3-inch Retina Display", "16-inch Retina Display", "13.3-inch Retina Display"], [999, 1299, 2399, 1299, 1799, 2399, 2499, 1299, 2399, 999]],
    "Dell": [["Dell XPS 13", "Dell XPS 15", "Dell G3 15", "Dell G5 15", "Dell Inspiron 14 5000", "Dell Inspiron 15 3000", "Dell Latitude 9410 2-in-1", "Dell Precision 7550", "Dell Vostro 14 5490", "Dell Alienware m15 R6"], ["Intel Core i5-1135G7", "Intel Core i7-11800H", "Intel Core i5-10200H", "AMD Ryzen 7 5800H", "Intel Core i5-11300H", "Intel Pentium Gold 7505", "Intel Core i7-1185G7", "Intel Xeon W-10885M", "Intel Core i5-1135G7", "Intel Core i9-11900H"], ["Intel Iris Xe Graphics", "NVIDIA GeForce RTX 3050 Ti", "NVIDIA GeForce GTX 1650", "NVIDIA GeForce RTX 3060", "Intel UHD Graphics", "Intel UHD Graphics 620", "Intel Iris Xe Graphics", "NVIDIA Quadro RTX 5000", "NVIDIA GeForce MX450", "NVIDIA GeForce RTX 3070"], ["256GB SSD", "512GB SSD", "256GB SSD + 1TB HDD", "512GB SSD + 1TB HDD", "256GB SSD", "256GB SSD", "512GB SSD", "1TB SSD", "512GB SSD", "512GB SSD"], ["8GB DDR4", "16GB DDR4", "8GB DDR4", "16GB DDR4", "8GB DDR4", "4GB DDR4", "16GB LPDDR4x", "64GB DDR4", "8GB DDR4", "16GB DDR4"], ["13.4-inch FHD+ (1920 x 1200)", "15.6-inch UHD+ (3840 x 2400)", "15.6-inch FHD (1920 x 1080)", "15.6-inch FHD (1920 x 1080)", "14-inch FHD (1920 x 1080)", "15.6-inch HD (1366 x 768)", "14-inch FHD+ (1920 x 1200)", "15.6-inch UHD+ (3840 x 2400)", "14-inch FHD (1920 x 1080)", "15.6-inch UHD (3840 x 2160)"], [999, 1099, 809, 949, 549, 399, 1749, 1319, 849, 1599]],
    "LG": [["LG Gram 17", "LG Gram 16", "LG Gram 14", "LG Ultra PC 17U70N", "LG Gram 2-in-1 16", "LG Gram 14 2-in-1", "LG Ultra PC 14U390"], ["Intel Core i7-1165G7", "Intel Core i5-1165G7", "Intel Core i5-1135G7", "Intel Core i7-1165G7", "Intel Core i5-1135G7", "Intel Core i7-1165G7", "Intel Core i5-10210U"], ["Intel Iris Xe Graphics", "Intel Iris Xe Graphics", "Intel Iris Xe Graphics", "NVIDIA GeForce GTX 1650 Ti Max-Q", "Intel Iris Xe Graphics", "Intel Iris Xe Graphics", "Intel UHD Graphics"], ["512GB SSD", "256GB SSD", "256GB SSD", "1TB SSD", "512GB SSD", "512GB SSD", "512GB SSD"], ["16GB DDR4", "8GB DDR4", "8GB DDR4", "16GB DDR4", "16GB DDR4", "16GB DDR4", "8GB DDR4"], ["17-inch WQXGA (2560 x 1600)", "16-inch WQXGA (2560 x 1600)", "14-inch WUXGA (1920 x 1200)", "17-inch WQXGA (2560 x 1600)", "16-inch WQXGA (2560 x 1600)", "14-inch FHD (1920 x 1080)", "14-inch FHD (1920 x 1080)"], [1499, 1299, 999, 1699, 1599, 1299, 1199]],
    "Microsoft": [["Surface Laptop 4", "Surface Book 3", "Surface Go 3", "Surface Laptop Studio", "Surface Pro 7", "Surface Pro X", "Surface Book 2", "Surface Laptop Go", "Surface Pro 8", "Surface Pro 6"], ["Intel Core i5-1135G7", "Intel Core i7-1065G7", "Intel Pentium Gold 6500Y", "Intel Core i7-11800H", "Intel Core i5-1035G4", "Microsoft SQ2", "Intel Core i5-7300U", "Intel Core i5-1035G1", "Intel Core i7-1185G7", "Intel Core i5-8250U"], ["Intel Iris Xe Graphics", "NVIDIA GeForce GTX 1660 Ti", "Intel UHD Graphics 615", "NVIDIA GeForce RTX 3050 Ti", "Intel Iris Plus Graphics", "Microsoft SQ2 Adreno 690 GPU", "NVIDIA GeForce GTX 1050", "Intel UHD Graphics", "Intel Iris Xe Graphics", "Intel UHD Graphics 620"], ["256GB SSD", "512GB SSD", "128GB eMMC", "1TB SSD", "128GB SSD", "256GB SSD", "256GB SSD", "128GB SSD", "512GB SSD", "128GB SSD"], ["8GB or 16GB LPDDR4x", "16GB or 32GB LPDDR4x", "4GB or 8GB LPDDR4x", "16GB or 32GB DDR4", "8GB or 16GB LPDDR4x", "8GB or 16GB LPDDR4x", "8GB or 16GB LPDDR3", "4GB or 8GB LPDDR4x", "8GB or 16GB LPDDR4x", "8GB or 16GB LPDDR3"], ["13.5-inch PixelSense (2256 x 1504)", "13.5-inch PixelSense (3000 x 2000)", "10.5-inch PixelSense (1920 x 1280)", "14.4-inch PixelSense (2400 x 1600)", "12.3-inch PixelSense (2736 x 1824)", "13-inch PixelSense (2880 x 1920)", "13.5-inch PixelSense (3000 x 2000)", "12.4-inch PixelSense (1536 x 1024)", "13-inch PixelSense (2880 x 1920)", "12.3-inch PixelSense (2736 x 1824)"], [999, 1599, 399, 1599, 749, 999, 1499, 549, 899, 899]],
    "HP": [["HP Spectre x360", "HP ENVY x360", "HP Pavilion x360", "HP Elite Dragonfly Max", "HP ProBook 440 G8", "HP ZBook Firefly 14 G8", "HP Chromebook 11", "HP Omen 15", "HP EliteBook 840 G8", "HP Spectre x2"], ["Intel Core i7-1165G7", "Intel Core i7-1165G7", "Intel Core i5-1135G7", "Intel Core i7-1185G7", "Intel Core i5-1135G7", "Intel Core i7-1185G7", "Intel Celeron N3350", "Intel Core i7-11800H", "Intel Core i7-1185G7", "Intel Core i7-1160G7"], ["Intel Iris Xe Graphics", "Intel Iris Xe Graphics", "Intel UHD Graphics", "Intel Iris Xe Graphics", "Intel Iris Xe Graphics", "NVIDIA T500", "Intel UHD Graphics 600", "NVIDIA GeForce RTX 3070", "Intel UHD Graphics", "Intel Iris Xe Graphics"], ["512GB SSD", "1TB SSD", "256GB SSD", "2TB SSD", "256GB SSD", "512GB SSD", "16GB eMMC", "1TB SSD", "512GB SSD", "1TB SSD"], ["16GB DDR4", "16GB DDR4", "8GB DDR4", "16GB LPDDR4X", "8GB DDR4", "16GB DDR4", "4GB LPDDR4", "16GB DDR4", "16GB DDR4", "16GB LPDDR4X"], ["13.3-inch FHD (1920 x 1080)", "15.6-inch FHD (1920 x 1080)", "14-inch FHD (1920 x 1080)", "13.3-inch FHD (1920 x 1080)", "14-inch FHD (1920 x 1080)", "14-inch FHD (1920 x 1080)", "11.6-inch HD (1366 x 768)", "15.6-inch FHD (1920 x 1080)", "14-inch FHD (1920 x 1080)", "13-inch FHD (1920 x 1080)"], [1099, 949, 549, 2199, 819, 1329, 219, 849, 1289, 1199]],
    "Lenovo": [["Lenovo ThinkPad X1 Carbon", "Lenovo ThinkPad X1 Yoga", "Lenovo Yoga 9i", "Lenovo Legion 5 Pro", "Lenovo IdeaPad 3", "Lenovo IdeaPad 5 Pro", "Lenovo ThinkPad X12 Detachable", "Lenovo ThinkPad P15", "Lenovo ThinkBook 14s Yoga", "Lenovo Legion 7i"], ["Intel Core i5-1135G7", "Intel Core i7-1185G7", "Intel Core i7-11800H", "AMD Ryzen 7 5800H", "Intel Core i5-10210U", "AMD Ryzen 7 5800U", "Intel Core i7-1180G7", "Intel Core i9-11950H", "Intel Core i7-1165G7", "Intel Core i9-11900H"], ["Intel Iris Xe Graphics", "Intel Iris Xe Graphics", "NVIDIA GeForce GTX 1650", "NVIDIA GeForce RTX 3070", "Integrated Intel UHD Graphics", "NVIDIA GeForce RTX 3050", "Intel Iris Xe Graphics", "NVIDIA Quadro RTX 4000", "Intel Iris Xe Graphics", "NVIDIA GeForce RTX 3070"], ["256GB SSD", "512GB SSD", "1TB SSD", "1TB SSD", "512GB SSD", "512GB SSD", "512GB SSD", "2TB SSD", "512GB SSD", "1TB SSD"], ["8GB LPDDR4x", "16GB LPDDR4x", "16GB LPDDR4x", "16GB DDR4", "8GB DDR4", "16GB DDR4", "16GB LPDDR4x", "128GB DDR4", "16GB LPDDR4x", "16GB DDR4"], ["14-inch FHD (1920 x 1080)", "14-inch FHD (1920 x 1080)", "14-inch UHD (3840 x 2160)", "16-inch QHD (2560 x 1600)", "14-inch FHD (1920 x 1080)", "16-inch QHD (2560 x 1600)", "12.3-inch FHD+ (1920 x 1280)", "15.6-inch UHD (3840 x 2160)", "14-inch FHD (1920 x 1080)", "16-inch QHD (2560 x 1600)"], [1329, 1569, 999, 1299, 319, 899, 1099, 1519, 999, 1399]],
    "Google": [["Google Pixelbook Go", "Google Pixelbook", "Google Pixel Slate", "Google Pixelbook 2-in-1"], ["Intel Core m3-8100Y", "Intel Core i5-10210U", "Intel Core m3-8100Y", "Intel Core i7-8500Y"], ["Intel UHD Graphics 615", "Intel UHD Graphics", "Intel UHD Graphics 615", "Intel UHD Graphics 615"], ["64GB eMMC", "128GB SSD", "64GB eMMC", "256GB SSD"], ["8GB RAM", "8GB RAM", "8GB RAM", "16GB RAM"], ["13.3-inch FHD (1920 x 1080)", "12.3-inch QHD (2400 x 1600)", "12.3-inch Molecular Display (3000 x 2000)", "12.3-inch 4K (3840 x 2400)"], [649, 999, 799, 999]],
    "Toshiba": [["Toshiba Tecra A50", "Toshiba Portege X30L-G", "Toshiba Dynabook Tecra A50", "Toshiba Dynabook Portege X30L-G"], ["Intel Core i7-1165G7", "Intel Core i5-1135G7", "Intel Core i7-1165G7", "Intel Core i5-1135G7"], ["Intel Iris Xe Graphics", "Intel Iris Xe Graphics", "Intel Iris Xe Graphics", "Intel Iris Xe Graphics"], ["512GB SSD", "256GB SSD", "512GB SSD", "256GB SSD"], ["16GB DDR4", "16GB LPDDR4x", "16GB DDR4", "16GB LPDDR4x"], ["15.6-inch FHD (1920 x 1080)", "13.3-inch FHD (1920 x 1080)", "15.6-inch FHD (1920 x 1080)", "13.3-inch FHD (1920 x 1080)"], [469, 179, 769, 179]],
    "Sony": [["Sony VAIO SX14", "Sony VAIO Z", "Sony VAIO S", "Sony VAIO F"], ["Intel Core i7-8565U", "Intel Core i7-9750H", "Intel Core i7-620M", "Intel Core i7-2630QM"], ["Intel UHD Graphics 620", "Intel UHD Graphics 630", "Intel HD Graphics", "NVIDIA GeForce GT 540M"], ["512GB SSD", "512GB SSD", "500GB HDD", "500GB HDD + 512GB SSD"], ["16GB DDR4", "16GB DDR4", "4GB DDR3", "6GB DDR3"], ["14-inch FHD (1920 x 1080)", "14-inch 4K (3840 x 2160)", "13.3-inch FHD (1920 x 1080)", "16.4-inch FHD (1920 x 1080)"], [1499, 2389, 1049, 1349]],
    "Acer": [["Acer Swift 3", "Acer Nitro 5", "Acer Aspire 5", "Acer Chromebook Spin 713"], ["AMD Ryzen 7 4700U", "AMD Ryzen 5 5600H", "AMD Ryzen 5 4500U", "Intel Core i5-10210U"], ["AMD Radeon Graphics", "NVIDIA GeForce GTX 1650", "AMD Radeon Graphics", "Intel UHD Graphics"], ["512GB SSD", "8GB DDR4", "512GB SSD", "128GB eMMC"], ["8GB LPDDR4x", "8GB DDR4", "8GB DDR4", "8GB LPDDR4x"], ["14-inch FHD (1920 x 1080)", "15.6-inch FHD (1920 x 1080)", "15.6-inch FHD (1920 x 1080)", "13.5-inch QHD (2256 x 1504)"], [679, 749, 419, 529]],
    "Asus": [["ASUS ZenBook 13", "ASUS ROG Zephyrus G14", "ASUS TUF A15", "ASUS Chromebook Flip C434"], ["Intel Core i7-1165G7", "AMD Ryzen 9 5900HS", "AMD Ryzen 5 4600H", "Intel Core m3-8100Y"], ["Intel Iris Xe Graphics", "NVIDIA GeForce RTX 3060", "NVIDIA GeForce GTX 1650", "Intel UHD Graphics 615"], ["1TB SSD", "1TB SSD", "512GB SSD", "128GB eMMC"], ["16GB LPDDR4x", "16GB DDR4", "8GB DDR4", "4GB LPDDR3"], ["13.3-inch FHD (1920 x 1080)", "14-inch QHD (2560 x 1440)", "15.6-inch FHD (1920 x 1080)", "14-inch FHD (1920 x 1080)"], [799, 1299, 799, 569]],
    "Alienware": [["Alienware m15 R4", "Alienware Area-51m R2", "Alienware m17 R4", "Alienware 17 R5"], ["Intel Core i7-10870H", "Intel Core i9-10900K", "Intel Core i7-10870H", "Intel Core i9-8950HK"], ["NVIDIA GeForce RTX 3060", "NVIDIA GeForce RTX 2080 Super", "NVIDIA GeForce RTX 3070", "NVIDIA GeForce GTX 1080"], ["512GB SSD", "2TB RAID0 (2x 1TB PCIe M.2 SSDs)", "512GB SSD", "256GB SSD + 1TB HDD"], ["16GB DDR4", "32GB DDR4", "16GB DDR4", "16GB DDR4"], ["15.6-inch FHD (1920 x 1080)", "17.3-inch FHD (1920 x 1080)", "17.3-inch FHD (1920 x 1080)", "17.3-inch FHD (1920 x 1080)"], [1793, 2283, 1873, 1499]],
    "Nokia": [["Nokia Purebook X14", "Nokia Purebook S14"], ["Intel Core i5-10210U", "Intel Core i5-1035G1"], ["Intel UHD Graphics 620", "Intel UHD Graphics"], ["512GB SSD", "512GB SSD"], ["8GB DDR4", "8GB DDR4"], ["14-inch FHD (1920 x 1080)", "14-inch FHD (1920 x 1080)"], [615, 499]],
    "Samsung": [["Samsung Galaxy Book Flex", "Samsung Notebook 9 Pro"], ["Intel Core i7-10510U", "Intel Core i7-8565U"], ["Intel UHD Graphics", "NVIDIA GeForce MX150"], ["512GB SSD", "256GB SSD"], ["16GB DDR4", "8GB DDR4"], ["13.3-inch QLED (1920 x 1080)", "13.3-inch FHD (1920 x 1080)"], [849, 1099]],
    "MSI": [["MSI GS66 Stealth", "MSI GE75 Raider", "MSI GL65 Leopard", "MSI Modern 14"], ["Intel Core i7-10870H", "Intel Core i7-10750H", "Intel Core i7-10750H", "Intel Core i5-10210U"], ["NVIDIA GeForce RTX 3070", "NVIDIA GeForce RTX 2070", "NVIDIA GeForce GTX 1660 Ti", "Intel UHD Graphics"], ["1TB SSD", "1TB HDD + 512GB SSD", "512GB NVMe SSD", "512GB NVMe SSD"], ["16GB DDR4", "16GB DDR4", "16GB DDR4", "8GB DDR4"], ["15.6-inch FHD (1920 x 1080)", "17.3-inch FHD (1920 x 1080)", "15.6-inch FHD (1920 x 1080)", "14-inch FHD (1920 x 1080)"], [1499, 1399, 699, 649]],
    "Razer": [["Razer Blade 15", "Razer Blade Pro 17", "Razer Blade Stealth 13"], ["Intel Core i7-10750H", "Intel Core i7-10875H", "Intel Core i7-1065G7"], ["NVIDIA GeForce RTX 3070", "NVIDIA GeForce RTX 2080 Super Max-Q", "Intel Iris Plus Graphics"], ["512GB SSD", "1TB SSD (PCIe NVMe)", "512GB SSD (PCIe M.2)"], ["16GB DDR4", "16GB DDR4", "16GB LPDDR4x"], ["15.6-inch FHD (1920 x 1080)", "17.3-inch FHD (1920 x 1080)", "13.3-inch FHD (1920 x 1080)"], [2199, 2145, 2399]],
    "ROG": [["ROG Zephyrus S GX701", "ROG Strix Scar 15", "ROG Zephyrus G15", "ROG Zephyrus Duo 15"], ["Intel Core i7-9750H", "AMD Ryzen 9 5900HX", "AMD Ryzen 7 5800HS", "Intel Core i9-10980HK"], ["NVIDIA GeForce RTX 2070", "NVIDIA GeForce RTX 3080", "NVIDIA GeForce RTX 3060", "NVIDIA GeForce RTX 2080 Super"], ["1TB SSD", "1TB SSD", "1TB SSD", "2TB RAID0 (2x 1TB PCIe NVMe M.2 SSDs)"], ["32GB DDR4", "16GB DDR4", "16GB DDR4", "32GB DDR4"], ["17.3-inch FHD (1920 x 1080)", "15.6-inch FHD (1920 x 1080)", "15.6-inch FHD (1920 x 1080)", "15.6-inch UHD (3840 x 2160)"], [1399, 1999, 1499, 4199]],
    "Gateway": [["Gateway Creator Series", "Gateway Ultra Slim Notebook"], ["AMD Ryzen 5 4600H", "Intel Core i5-10210U"], ["NVIDIA GeForce GTX 1650", "Intel UHD Graphics"], ["256GB SSD", "256GB SSD"], ["8GB DDR4", "16GB DDR4"], ["15.6-inch FHD (1920 x 1080)", "14.1-inch FHD (1920 x 1080)"], [259, 229]],
}

# default laptop class which will be the parent for the classes I create for each brand


class Laptop:
    # initialize attributes of object in class
    def __init__(self, Name, CPU, GPU, Storage, Ram, Screen, Price) -> None:
        self.Name = Name
        self.CPU = CPU
        self.GPU = GPU
        self.Storage = Storage
        self.Ram = Ram
        self.Screen = Screen
        self.Price = Price
    # print attributes of object

    def specs(self) -> None:
        print(f'Name: {self.Name}\nCPU: {self.CPU}\nGPU: {self.GPU}\nStorage: {self.Storage}\nRam: {self.Ram}\nScreen: {self.Screen}\nPrice: {self.Price}\n')


# iterate throught the keys in Brands
for brand in Brands.keys():
    # create each class that's identical to class Laptop using exec function
    exec("class "+brand+"(Laptop):\n    pass")
    # go through device names under brand
    for names in Brands[brand][0]:
        # create object for each device and grab their attributes from their column
        exec(names.replace(' ', '_').replace('-', '_') + "=" + brand + "(\"" + Brands[brand][0][Brands[brand][0].index(names)] + "\",\"" + Brands[brand][1][Brands[brand][0].index(names)] + "\",\"" + Brands[brand][2][Brands[brand][0].index(
            names)] + "\",\"" + Brands[brand][3][Brands[brand][0].index(names)] + "\",\"" + Brands[brand][4][Brands[brand][0].index(names)] + "\",\"" + Brands[brand][5][Brands[brand][0].index(names)] + "\"," + str(Brands[brand][6][Brands[brand][0].index(names)]) + ")")

# set total to 0
price = 0
# create cart which will hold device name and number of device
cart = dict()
# create a bool to check when player exits
shopping = True
# keep track of info in terminal with brands being the first
info_shown = "brands"
# keep track of the last text shown
prev_info = str()
# Keep track of user choices
chosen_brand = 0
chosen_device = 0
chosen_removal = 0

# while user is in program
while shopping:
    # show infor for brands
    if info_shown == "brands":
        # print every brand and highlight the chosen brand
        for brand_index, brand_name in enumerate(Brands):
            # check if brand is brand user is hovering over
            if brand_index == chosen_brand:
                print("\033[1m\033[4m" + brand_name)
            else:
                print("\033[0m" + brand_name)
        # ask for input
        user_input = input(
            "\n\033[0mPress W to move up, S to move down, Enter to select, E to view Cart, & Esc to exit: ")
        # check if w was pressed and go up in selection
        if user_input.lower() == "w" and chosen_brand - 1 > -1:
            chosen_brand -= 1
            os.system(clear_command)
        # check if s was pressed and go down in selection
        elif user_input.lower() == "s" and chosen_brand + 1 < len(Brands):
            chosen_brand += 1
            os.system(clear_command)
        # check if e was pressed and view cart
        elif user_input.lower() == "e":
            prev_info = "brands"
            info_shown = "cart"
            os.system(clear_command)
        # confirm selection by pressing Enter
        elif user_input == "":
            os.system(clear_command)
            if info_shown == "brands":
                info_shown = "devices"
        # type esc to exit shop
        elif user_input.lower() == "esc":
            os.system(clear_command)
            break
        # clear screen if anything else
        else:
            os.system(clear_command)
    # what to do if showing devices info
    elif info_shown == "devices":
        # go through the device names of user's chosen brand and highlight selected one
        for device_index, device_name in enumerate(Brands[list(Brands.keys())[chosen_brand]][0]):
            if device_index == chosen_device:
                print("\033[1m\033[4m" + device_name)
            else:
                print("\033[0m" + device_name)
        # ask for user input
        user_input = input(
            "\n\033[0mPress W to move up, S to move down, Enter to select, E to view Cart, Esc to exit & A to go back: ")
        # check if w was pressed and go up in selection
        if user_input.lower() == "w" and chosen_device - 1 > -1:
            chosen_device -= 1
            os.system(clear_command)
        # check if s was pressed and go down in selection
        elif user_input.lower() == "s" and chosen_device + 1 < len(Brands[list(Brands.keys())[chosen_brand]][0]):
            chosen_device += 1
            os.system(clear_command)
        # check if e was pressed and view cart
        elif user_input.lower() == "e":
            prev_info = "devices"
            info_shown = "cart"
            os.system(clear_command)
        # confirm selection by pressing Enter
        elif user_input == "":
            os.system(clear_command)
            info_shown = "specs"
        # press a to go back to the previous text which is always the brands menu
        elif user_input.lower() == "a":
            chosen_device = 0
            info_shown = "brands"
            os.system(clear_command)
        # type esc to exit shop
        elif user_input.lower() == "esc":
            os.system(clear_command)
            break
        else:
            os.system(clear_command)
    # if menu being shown is specs
    elif info_shown == "specs":
        # store the object name for the device the user chose
        device = Brands[list(Brands.keys())[chosen_brand]][0][chosen_device].replace(
            ' ', '_').replace('-', '_')
        # print specs of device
        exec(f"{device}.specs()")
        # get user input
        user_input = input(
            "\n\033[0mAdd this product to cart? y/n (Esc to exit, A to go back): ")
        # if user says y see how many they wanna add
        if user_input.lower() == 'y':
            os.system(clear_command)
            # store number of devices to add to cart
            num_of_device = 1
            while True:
                # Clear the terminal screen
                os.system(clear_command)
                # Print the current number of devices and their names
                exec(f'print({device}.Name + \'(x{num_of_device})\')')
                # Ask the user for input
                user_input = input(
                    "\n\033[0mPress W to add one, S to remove one, Enter to confirm, Esc to exit & A to go back: ")
                # If the user pressed 'W', add one to the number of devices
                if user_input.lower() == 'w':
                    num_of_device += 1
                # If the user pressed 'S', remove one from the number of devices (if there's more than one)
                elif user_input.lower() == 's' and num_of_device - 1 > 0:
                    num_of_device -= 1
                # If the user pressed 'S' but there's only one device, show an error message
                elif user_input.lower() == 's' and not num_of_device - 1 > 0:
                    print(
                        "\033[1m\033[4mSilly, One is the lowest you can go, If you'd like to go back press A")
                    time.sleep(0.3)
                # If the user pressed Enter, add the devices to the cart and exit the loop
                elif user_input == '':
                    cart[device] = num_of_device
                    os.system(clear_command)
                    print("Successfully added items to cart")
                    time.sleep(1.5)
                    os.system(clear_command)
                    info_shown = "devices"
                    break
                # If the user pressed 'A', go back to the previous screen
                elif user_input.lower() == 'a':
                    os.system(clear_command)
                    break
                # If the user pressed 'N', go back to the previous screen
                elif user_input.lower() == 'n':
                    os.system(clear_command)
                    info_shown = "devices"
                # If the user pressed 'Esc', exit the loop
                elif user_input.lower() == 'esc':
                    break
                # If the user entered any other input, clear the screen and ask for input again
                else:
                    os.system(clear_command)
    # check if current menu is cart
    elif info_shown == "cart":
        # If the cart is empty, display a message and prompt the user to exit or go back.
        if list(cart.keys()) == []:
                while True:
                    os.system(clear_command)
                    print("You have nothing in your Cart")
                    user_input = input("\n\033[0mEsc to exit & A to go back: ")
                    if user_input.lower() == 'esc':
                        break
                    elif user_input.lower() == 'a':
                        os.system(clear_command)
                        info_shown = prev_info
                        break
                    else:
                        os.system(clear_command)
                        shopping = False
                        break
        # If the cart has items in it, display the names and quantities of each item and prompt the user
        # to remove an item, exit, or go back.
        else:
            for i in list(cart.keys()):
                    exec(f'print({i}.Name + \'(x{cart[i]})\')')
            user_input = input("\n\033[0mRemove Product? y/n (Esc to exit, A to go back): ")
            # If the user chooses to remove an item, display the items in the cart and prompt the user to
            # choose an item to remove.
            if user_input.lower() == 'y':
                os.system(clear_command)
                while True:
                    # Loop through the list of products in the cart
                    for cart_index,cart_device in enumerate(list(cart.keys())):
                        # If the product at index chosen_removal, print with highlight
                        if chosen_removal == cart_index:
                            exec(f'print(\"\033[1m\033[4m\" + {cart_device}.Name + \"(x{cart[cart_device]})\")')
                        # Otherwise, print normally
                        else:
                            exec(f'print(\"\033[0m\" + {cart_device}.Name + \"(x{cart[cart_device]})\")')
                    # Get user input for moving up, down, selecting, or exiting
                    user_input = input("\n\033[0mPress W to move up, S to move down, Enter to select, Esc to exit & A to go back: ")
                    # If user selects to move up and there is an index above chosen_removal
                    if user_input.lower() == "w" and chosen_removal - 1 > -1:
                        chosen_removal -= 1
                        os.system(clear_command)
                    # If user selects to move down and there is an index below chosen_removal
                    elif user_input.lower() == "s" and chosen_removal + 1 < len(list(cart.keys())):
                        chosen_removal += 1
                        os.system(clear_command)
                    # If user selects to select the product at chosen_removal index
                    elif user_input == "":
                        os.system(clear_command)
                        device_in_cart = cart[list(cart.keys())[chosen_removal]]+1
                        # Loop until user confirms their changes or exits
                        while shopping:
                            num_of_device = cart[list(cart.keys())[chosen_removal]]
                            os.system(clear_command)
                            # Print the product and its quantity
                            exec(f'print({list(cart.keys())[chosen_removal]}.Name + \'(x{num_of_device})\')')
                            # Get user input for adding, removing, confirming, or exiting
                            user_input = input("\n\033[0mW to add one, S to remove one, Enter to confirm, Esc to exit & A to go back: ")
                            # If w add one unless it would result in more of the device than you started with
                            if user_input.lower() == 'w'and cart[list(cart.keys())[chosen_removal]] +1 < device_in_cart:
                                cart[list(cart.keys())[chosen_removal]]+=1
                            # if s decrease unless it will become less than zero
                            elif user_input.lower() == 's' and num_of_device -1 > -1:
                                cart[list(cart.keys())[chosen_removal]]-=1
                            # if it does become less than zero flash a message that you can't go lower
                            elif user_input.lower() == 's' and not num_of_device -1 > -1:
                                print("\033[1m\033[4mSilly, Zero is the lowest you can go, If you'd like to confirm, press Enter")
                                time.sleep(0.3)
                            #if enter is pressed to confirmn
                            elif user_input == '':
                                #remove device entirely from cart if num of device equals 0
                                if num_of_device == 0:
                                    del cart[list(cart.keys())[chosen_removal]]
                                os.system(clear_command)
                                #special case if nothing was removed
                                if cart[list(cart.keys())[chosen_removal]] +1 == device_in_cart:
                                    print("Successfully removed nothing from cart")
                                else:
                                    print("Successfully removed items from cart")
                                time.sleep(1.5)
                                os.system(clear_command)
                                #go back to cart
                                info_shown = "cart"
                                break
                            #if a just break loop
                            elif user_input.lower() == 'a':
                                os.system(clear_command)
                                break
                    #If a go back to previous menu
                    elif user_input.lower() == "a":
                        chosen_device = 0
                        info_shown = prev_info
                        os.system(clear_command)
                        break
                    #if esc exit shopping
                    elif user_input.lower() == "esc":
                        os.system(clear_command)
                        shopping = False
                        break
                    else:
                        os.system(clear_command)
            #If n go back to previous menu
            elif user_input.lower() == 'n':
                os.system(clear_command)
                info_shown = prev_info
            #if esc exit shopping
            elif user_input.lower() == 'esc':
                os.system(clear_command)
                shopping = False
                break
            #If a go back to previous menu
            elif user_input.lower() == 'a':
                os.system(clear_command)
                info_shown = prev_info
            else:
                os.system(clear_command)

if list(cart.keys()) == []:  # If cart is empty
    # Display message for no items in cart
    print("Your total is 0, Thank you for shopping.")

else:  # If cart is not empty
    for devices in list(cart.keys()):  # For each device in cart
        # Add the price of the device to the total price
        exec(f'price+={devices}.Price')
    # Display total price
    print(f'You owe {price} dollars, Thank you for shopping.')