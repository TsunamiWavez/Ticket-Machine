# 🎟️ Ticket Machine Simulator

This is a **simple simulation of a ticket vending machine** for a drawing masterclass.  
It is a console-based Python program designed for learning purposes and small-scale ticket sale simulation.

---
## 📋 Features
- ✅ Sell up to **10 tickets**
- 🎓 Special **discounts for students**
- ⏳ Discounts for **early buyers** (90+ days before event)
- 🕒 Price increase for **late purchases** (7 days or less)
- 💾 Number of tickets are stored in a `tickets.json` file to make sure each ticket has a unique number
- ⚠️ The program takes into account all possible errors and displays a special message if the user has entered an incorrect input value

---
## 🖥️ How It Works
- The program checks how many tickets are already sold from `tickets.json`
- User can choose wheter to buy a ticket or exit the program
- Depending on the date and user status (student or not), the ticket price is calculated
- A ticket is printed in the terminal with:
  - Ticket number
  - Price
  - Purchase date
  - Event date and time
- The ticket number will be saved in `tickets.json`
---

## 📁 Files
- `main_program.py` — main Python script with simulation logic  
- `tickets.json` — stores sold ticket numbers (created automatically on first run)
---


## ▶️ Example Usage

```
----------------Drawing Masterclass Ticket System----------------

0 - Exit
1 - Buy a ticket

>>> 1

We have a special discount for students! Are you a student?
0 - no, 1 - yes.

>>> 0

We have a discount for tickets purchased in advance!

Your ticket is being printed...

----------------Ticket for a drawing masterclass-----------------
	Ticket price: 10.50$
	Ticket number: 3
	Date of purchase: 2025-04-30
	Event date and time: 01.08.25, 14:00
-----------------------------------------------------------------

0 - Exit
1 - Buy a ticket

>>> 1

We have a special discount for students! Are you a student?
0 - no, 1 - yes.

>>> 1

Your ticket is being printed...

----------------Ticket for a drawing masterclass-----------------
	Ticket price: 7.50$
	Ticket number: 2
	Date of purchase: 2025-04-30
	Event date and time: 01.08.25, 14:00
-----------------------------------------------------------------

0 - Exit
1 - Buy a ticket

>>> 0

The end of the program...
```

## Requirements
- Python 3.x

## License
This project is open-source and available under the MIT License.
