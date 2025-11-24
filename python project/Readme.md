Flight Ticket Booking Program
This Python program allows users to book flight tickets for either domestic or international travel. It interacts with the user through the console to gather necessary information, then generates and displays a ticket summary including random seat number and price.

Features
Supports booking for both domestic and international flights.

Lets the user select:

Starting point

Destination

Seat preference (Economy, Premium Economy, Business)

Trip type (One way, Round trip)

Travel date

Generates a random seat number and ticket price depending on the flight type.

Displays the complete ticket details for confirmation.

How It Works
The program first asks if the flight is domestic or international.

Based on the input:

If domestic, the user is prompted to enter starting point, destination, seat preference, trip type, and date.

If international, the same details are requested.

After collecting inputs, the program prints a ticket confirmation showing:

Route (From and To)

Date of travel

Seat number (randomly assigned)

Seat type

Ticket price (randomly generated within a range based on flight type)

Trip preference

Usage
Run the program. When prompted, enter the required information step-by-step:

Type domestic or international for the flight type.

Fill in the starting point and destination.

Choose a seat preference from the available options.

Specify whether the trip is one way or round trip.

Enter the travel date in any preferred format.

The program will display a formatted booking confirmation.

Code Structure
The program defines two functions: domestic() and international(), which handle the booking processes based on the flight type.

It uses Python's random module to assign seat numbers and prices dynamically.

Input validation is not implemented, so inputs must be entered carefully according to prompts.

You can use the above markdown content to create a README.md file or convert it into PDF format for documentation purposes. If you want, help with PDF conversion can also be provided.



