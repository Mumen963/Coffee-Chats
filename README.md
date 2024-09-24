# Weekly Coffee Chats Scheduler

The Weekly Coffee Chats Scheduler is a Python application designed to facilitate scheduling weekly coffee chats for Aspiring Professionals on a platform. It intelligently matches Aspiring Professionals with Senior Executives based on industry, interests, availability, and other factors.


### Overview

The Weekly Coffee Chats Scheduler automates the process of scheduling weekly coffee chats between Aspiring Professionals and Senior Executives. It considers various parameters to ensure optimal matches and scheduling efficiency.

### Features

- **Automated Matching**: Matches Aspiring Professionals with Senior Executives based on industry and interest compatibility.
- **Flexible Scheduling**: Allows for customization of scheduling preferences, including frequency and preferred times.
- **User Interface**: Provides a user-friendly interface for easy management and interaction with scheduling functionalities.
- **Algorithm Integration**: Implements an intelligent algorithm that optimizes matches and schedules based on availability and preferences.
- **Comprehensive Reporting**: Generates reports and insights on scheduled coffee chats and participant interactions.
- **Customizable Profiles**: Allows users (Aspiring Professionals and Senior Executives) to create detailed profiles.
- **Flexibility**: Empowers users to initiate new bookings, modify existing booking times, or cancel scheduled appointments with ease.
- **Intuitive Booking Display**: Provides a clear and accessible view of all booking details.
- **Frequency Tracking**: Automatically tracks the frequency at which each professional has already been appearing on the roster.

### User Stories :
- *As a user, I want to be able to add a new senior executive.*
- *As a user, I want to be able to remove a senior executive.*
- *As a user, I want to be able to update details of a senior executive*
- *As a user, I want to be able to make a new booking.*
- *As a user, I want to be able to change the time of a booking.*
- *As a user, I want to be able to delete a booking.*
- *As a user, I want to be able to display all aspiring professionals.*
- *As a user, I want to be able to display all senior executives.*
- *As a user, I want to be able to display all bookings.*
- *As a user, I want to be able to see all events when the application closes*

### Future User Stories
- *As a user, I want to have the option to save/load the application data to/from a file* 

### Instructions for User
- Add a New Senior Executive: To add a new senior executive to the platform.
- Remove a Senior Executive: To remove an existing senior executive from the platform.
- Update Senior Executive Details: To update the details (such as name, industry, etc.) of a senior executive.
- Make a New Booking: To schedule a new coffee chat booking.
- Change Booking Time: To modify the time of an existing booking.
- Delete Booking: To cancel and remove an existing booking.
- Show All Aspiring Professionals: To view a list of all aspiring professionals registered on the platform.
- Show All Senior Executives: To view a list of all senior executives available for coffee chats.
- Show All Bookings: To display a list of all scheduled coffee chat bookings.
- Quit: To view all events and activities related to the platform, and quit.

### Automated Test Cases (note that all events will be displayed after the app quits, including the addition of the dummy data)
Platform Menu:
1. Add New Senior Executive
2. Remove Senior Executive
3. Update Senior Executive Details
4. Make New Booking
5. Change Booking Time
6. Delete Booking
7. Show All Aspiring Professionals
8. Show All Senior Executives
9. Show All Bookings
10. Exit

Enter your choice: 1
Enter the name of the Senior Executive: Mumen Asdo
Enter the industry of the Senior Executive: Health
Enter the company of the Senior Executive: Albasha
Enter the title of the Senior Executive: Manager
Enter the price for booking a coffee chat with the Senior Executive ($): 80
Enter the region of the Senior Executive: Vancouver
Enter interests of the Senior Executive (comma-separated): Education, CPSC, Math
Senior Executive Mumen Asdo added successfuly.

Platform Menu:
1. Add New Senior Executive
2. Remove Senior Executive
3. Update Senior Executive Details
4. Make New Booking
5. Change Booking Time
6. Delete Booking
7. Show All Aspiring Professionals
8. Show All Senior Executives
9. Show All Bookings
10. Exit

Enter your choice: 4
Welcome to the booking process.
Are you new to the platform? (yes/no): yes 
Welcome! Please provide the following details:
Name: Ahmad
Industry: Health
Interests (comma separated): Health

Thank you for joining us. Here are the available executives in your industry:
Available executives:
1. Name: Zara
Industry: Health
Company: Pioneer Solutions
Title: Chief Executive Officer
Price: 50
Region: Canada
Interests: ['Health']

2. Name: Mumen Asdo
Industry: Health
Company: Albasha
Title: Manager
Price: 80.0
Region: Vancouver
Interests: ['Education', ' CPSC', ' Math']

Choose an executive (enter number): 2
Choose a preferred day for the booking(Mon, Tue, Wed): Monday
Booking successfully made.

Platform Menu:
1. Add New Senior Executive
2. Remove Senior Executive
3. Update Senior Executive Details
4. Make New Booking
5. Change Booking Time
6. Delete Booking
7. Show All Aspiring Professionals
8. Show All Senior Executives
9. Show All Bookings
10. Exit

Enter your choice: 9
Senior Executive Mumen Asdo is booked by Aspiring Professional Ahmad on Monday


Platform Menu:
1. Add New Senior Executive
2. Remove Senior Executive
3. Update Senior Executive Details
4. Make New Booking
5. Change Booking Time
6. Delete Booking
7. Show All Aspiring Professionals
8. Show All Senior Executives
9. Show All Bookings
10. Exit

Enter your choice: 5
Enter the name of the Senior Executive booked with: Mumen Asdo
Enter the name of the Aspiring Professional: Ahmad
Enter the new day of the booking (e.g., Monday): Tuesday
Booking time changed.

Platform Menu:
1. Add New Senior Executive
2. Remove Senior Executive
3. Update Senior Executive Details
4. Make New Booking
5. Change Booking Time
6. Delete Booking
7. Show All Aspiring Professionals
8. Show All Senior Executives
9. Show All Bookings
10. Exit

Enter your choice: 9
Senior Executive Mumen Asdo is booked by Aspiring Professional Ahmad on Tuesday


Platform Menu:
1. Add New Senior Executive
2. Remove Senior Executive
3. Update Senior Executive Details
4. Make New Booking
5. Change Booking Time
6. Delete Booking
7. Show All Aspiring Professionals
8. Show All Senior Executives
9. Show All Bookings
10. Exit

Enter your choice: 6
Enter the name of the Senior Executive: Mumen Asdo
Enter the name of the Aspiring Professional: Ahmad
Booking deleted.

Platform Menu:
1. Add New Senior Executive
2. Remove Senior Executive
3. Update Senior Executive Details
4. Make New Booking
5. Change Booking Time
6. Delete Booking
7. Show All Aspiring Professionals
8. Show All Senior Executives
9. Show All Bookings
10. Exit

Enter your choice: 9
No bookings found.

Platform Menu:
1. Add New Senior Executive
2. Remove Senior Executive
3. Update Senior Executive Details
4. Make New Booking
5. Change Booking Time
6. Delete Booking
7. Show All Aspiring Professionals
8. Show All Senior Executives
9. Show All Bookings
10. Exit

Enter your choice: 2
Enter the name of the Senior Executive to remove: Mumen Asdo
Senior Executive Mumen Asdo removed successfuly.

Platform Menu:
1. Add New Senior Executive
2. Remove Senior Executive
3. Update Senior Executive Details
4. Make New Booking
5. Change Booking Time
6. Delete Booking
7. Show All Aspiring Professionals
8. Show All Senior Executives
9. Show All Bookings
10. Exit

Enter your choice: 10

--- Event Log ---
2024-07-01 23:54:32.973448
Senior Executive added: Mohammed
 
2024-07-01 23:54:32.973453
Senior Executive added: Ali
 
2024-07-01 23:54:32.973455
Senior Executive added: Fatima
 
2024-07-01 23:54:32.973456
Senior Executive added: Aisha
 
2024-07-01 23:54:32.973457
Senior Executive added: Omar
 
2024-07-01 23:54:32.973459
Senior Executive added: Yusuf
 
2024-07-01 23:54:32.973460
Senior Executive added: Sana
 
2024-07-01 23:54:32.973461
Senior Executive added: Imran
 
2024-07-01 23:54:32.973462
Senior Executive added: Layla
 
2024-07-01 23:54:32.973463
Senior Executive added: Zaynab
 
2024-07-01 23:54:32.973464
Senior Executive added: Ibrahim
 
2024-07-01 23:54:32.973465
Senior Executive added: Huda
 
2024-07-01 23:54:32.973466
Senior Executive added: Ahmad
 
2024-07-01 23:54:32.973467
Senior Executive added: Safiya
 
2024-07-01 23:54:32.973468
Senior Executive added: Salim
 
2024-07-01 23:54:32.973469
Senior Executive added: Jamal
 
2024-07-01 23:54:32.973471
Senior Executive added: Ayesha
 
2024-07-01 23:54:32.973472
Senior Executive added: Yasin
 
2024-07-01 23:54:32.973473
Senior Executive added: Nadia
 
2024-07-01 23:54:32.973474
Senior Executive added: Hamza
 
2024-07-01 23:54:32.973475
Senior Executive added: Zara
 
2024-07-01 23:54:32.973476
Senior Executive added: Amir
 
2024-07-01 23:54:32.973477
Senior Executive added: Hana
 
2024-07-01 23:54:32.973478
Senior Executive added: Khalid
 
2024-07-01 23:54:32.973479
Senior Executive added: Safia
 
2024-07-01 23:54:32.973480
Senior Executive added: Bilal
 
2024-07-01 23:54:32.973481
Senior Executive added: Mariam
 
2024-07-01 23:54:32.973483
Senior Executive added: Tariq
 
2024-07-01 23:54:32.973484
Senior Executive added: Saida
 
2024-07-01 23:54:32.973485
Senior Executive added: Jamil
 
2024-07-01 23:55:17.854891
Senior Executive added: Mumen Asdo
 
2024-07-01 23:55:54.377751
Aspiring Professional added: Ahmad
 
2024-07-01 23:56:08.046076
Booking added: Ahmad with Mumen Asdo
 
2024-07-01 23:56:53.287135
Booking time changed from Monday to Tuesday for Ahmad with Mumen Asdo
 
2024-07-01 23:57:21.146808
Booking removed: Ahmad with Mumen Asdo
 
2024-07-02 00:01:18.305135
Senior Executive removed: Mumen Asdo
 
Exiting platform.


### Future Goals and Enhancements:
**Data Management Optimization**: Future updates will focus on enhancing data management capabilities. This includes implementing robust features for saving and loading user data, ensuring seamless access to preferences, booking histories, and user settings. These improvements aim to streamline user interactions and provide a more personalized experience.

**Graphical User Interface (GUI) Development**: Plans are underway to develop an intuitive graphical user interface (GUI) that enhances user navigation and interaction. The GUI will feature user-friendly designs, intuitive controls, and visual enhancements to improve overall usability. This initiative aims to elevate user satisfaction by simplifying access to platform functionalities.
