# roomallocationtechfest
The room allocation application is designed to streamline the process of allocating rooms in hostels based on group information and hostel capacity. The application ensures that members of the same group stay together as much as possible while adhering to gender-specific accommodations and room capacities.

Logic
Sorting Hostels: The hostels are sorted by their names and room numbers to ensure a predictable allocation order.
Group Allocation:
Each group is iterated over to find an appropriate room.
The application first tries to allocate the entire group to a single room.
If a single room cannot accommodate the group, the group is split across multiple rooms.
Gender and Capacity Constraints:
Rooms are allocated based on gender (boys or girls).
Room capacity is respected, and rooms are not overfilled.
# instructionbs to run the program
open in vs code
in folder create something like this

foldername

├── app.py

├── templates/
│   └── index.html

├── static/
│   └── style.css

├── uploads/

python -m venv venv

venv\Scripts\activate 

install flask and pandas

python app.py

