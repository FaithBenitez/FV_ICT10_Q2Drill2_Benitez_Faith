from pyscript import display, document


members = {'Zara Llaguno', 'Jadrien Godino', 'Carlos David'}

def add_member(e):

    document.getElementById('output1').innerHTML = ""

    input_fname = document.getElementById('fname').value.strip()
    input_lname = document.getElementById('lname').value.strip()

    new_student = {input_fname + " " + input_lname}

    members = members | new_student
    total_members = len(members)

    member_list = "<br>".join(sorted(members))

    document.getElementById('output1').innerHTML = f'All members: <br> {member_list}'
    display(f'Total members: {total_members}', target="output1")