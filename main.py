import oo_resale_shop
import computer as cp

def main():
    
    # First, let's make a computer
    computer = cp.Computer(
        "Mac Pro (Late 2013)",
        "3.5 GHc 6-Core Intel Xeon E5",
        1024, 64,
        "macOS Big Sur", 2013, 1500)

    # Create an object "shop" in resale shop class
    shop = oo_resale_shop.ResaleShop()


    # Print a little banner
    print("-" * 21)
    print("COMPUTER RESALE STORE")
    print("-" * 21)


    # Add it to the resale store's inventory
    print("Buying", computer.description)
    print("Adding to inventory...")
    computer_id = shop.buy(computer)
    print("Done.\n")


    # Make sure it worked by checking inventory
    print("Checking inventory...")
    shop.print_inventory()
    print("Done.\n")

    # Now, let's refurbish it
    new_OS = "MacOS Monterey"
    print("Refurbishing Item ID:", computer_id, ", updating OS to", new_OS)
    print("Updating inventory...")
    shop.refurbish(computer_id, new_OS)
    print("Done.\n")

    # Make sure it worked by checking inventory
    print("Checking inventory...")
    shop.print_inventory()
    print("Done.\n")
    
    # Now, let's sell it!
    print("Selling Item ID:", computer_id)
    shop.sell(computer_id)
    
    # Make sure it worked by checking inventory
    print("Checking inventory...")
    shop.print_inventory()
    print("Done.\n")

    print("-" * 21)
    print("Testing code! Adding 2 computers to the inventory and sell one of them")
    print("-" * 21)

    # To further test the code, add 2 computers to the inventory
    computer1 = cp.Computer(
        "Test Computer1",
        "Random processor type 1",
        2048, 128,
        "Random operating system 1", 2002, 2000
    )
    computer2 = cp.Computer(
        "Test Computer2",
        "Random processor type 2",
        4096, 256,
        "Random operating system 2", 2021, 2500
    )
    # Testing...
    print("Buying", computer1.description)
    print("Adding to inventory...")
    computer_id1 = shop.buy(computer1)
    print("Done.\n")

    print("Buying", computer2.description)
    print("Adding to inventory...")
    computer_id2 = shop.buy(computer2)
    print("Done.\n")

    print("Checking inventory...")
    shop.print_inventory()
    print("Done.\n")

    new_OS = "New Operating System 1"
    print("Refurbishing Item ID:", computer_id1, ", updating OS to", new_OS)
    print("Updating inventory...")
    shop.refurbish(computer_id1, new_OS)
    print("Done.\n")

    new_OS = "New Operating System 2"
    print("Refurbishing Item ID:", computer_id2, ", updating OS to", new_OS)
    print("Updating inventory...")
    shop.refurbish(computer_id2, new_OS)
    print("Done.\n")

    print("Checking inventory...")
    shop.print_inventory()
    print("Done.\n")

    print("Selling Item ID:", computer_id2)
    shop.sell(computer_id2)

    print("Checking inventory...")
    shop.print_inventory()
    print("Done.\n")




# Calls the main() function when this file is run
if __name__ == "__main__": main()

