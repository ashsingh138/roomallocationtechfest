from flask import Flask, render_template, request, send_file
import pandas as pd

app = Flask(__name__)

def allocate_rooms(groups, hostels):
    hostels = hostels.sort_values(by=['Hostel Name', 'Room Number'])
    allocation = []

    group_list = groups.to_dict(orient='records')
    hostel_list = hostels.to_dict(orient='records')

    for group in group_list:
        group_id = group['Group ID']
        members = group['Members']
        gender = group['Gender']

        allocated = False
        for hostel in hostel_list:
            if hostel['Gender'] == gender and hostel['Capacity'] >= members:
                allocation.append({
                    'Group ID': group_id,
                    'Hostel Name': hostel['Hostel Name'],
                    'Room Number': hostel['Room Number'],
                    'Members Allocated': members
                })
                hostel['Capacity'] -= members
                allocated = True
                break
        
        if not allocated:
            remaining_members = members
            for hostel in hostel_list:
                if hostel['Gender'] == gender and hostel['Capacity'] > 0:
                    allocate_members = min(remaining_members, hostel['Capacity'])
                    allocation.append({
                        'Group ID': group_id,
                        'Hostel Name': hostel['Hostel Name'],
                        'Room Number': hostel['Room Number'],
                        'Members Allocated': allocate_members
                    })
                    hostel['Capacity'] -= allocate_members
                    remaining_members -= allocate_members
                    if remaining_members == 0:
                        break

    allocation_df = pd.DataFrame(allocation)
    return allocation_df

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_files():
    groups_file = request.files['groups']
    hostels_file = request.files['hostels']

    if not groups_file or not hostels_file:
        return "No file uploaded", 400

    groups = pd.read_csv(groups_file)
    hostels = pd.read_csv(hostels_file)

    allocation = allocate_rooms(groups, hostels)
    allocation.to_csv('uploads/allocation.csv', index=False)

    return send_file('uploads/allocation.csv', as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)
