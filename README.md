# Parking-management-system
Parking management project which generates barcode parking ticket with user-friendly Tkinter program GUI


### How to run

Download the repo and pip install these libraries (if you have not installed them before)

- cv2
- PIL
- pyzbar
- tkinter 
- datetime 
- barcode 


### Known error:

Invalid Fee output: This occurs due when non standard plate number is entered, i.e. Less than 10 digits.


## Working:

 1. When a car arrives at entry gate, the user can enter the number plate and car brand and create a ticket and ticketId.
 2. The time of arrival is automatically stored in ticket
 3. When the car goes to exit gate, the user can verify the ticket by entering the Id (in turn scanning from local storage, will be using camera approach soon)
 4. If the strings match, then the exit_check.py will generate the parking fee. 
 5. Default Rate is INR 0.25 per min [changeable]

## Screenshots
 - Main GUI


![image](https://user-images.githubusercontent.com/81807980/152167557-46cb0cf6-ae4a-4c04-85bf-d98f49586085.png)
 - Create Ticket


![image](https://user-images.githubusercontent.com/81807980/152167869-5aceffaf-c7c1-483a-acad-02fc2ba47351.png)
 - Parking Ticket generated


![pid_4502](https://user-images.githubusercontent.com/81807980/152170432-029709fd-fdb0-45c5-afbb-f40bc2b6b970.png)
 - Checking Ticket on Exit


![image](https://user-images.githubusercontent.com/81807980/152168799-6bd53dd3-e647-45fd-9a84-a7b3db42a567.png)


