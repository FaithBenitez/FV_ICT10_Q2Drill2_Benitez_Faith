from pyscript import display, document

def add_member(e):
    #Member names
    Grade10 = {'Carlos David', 'Jadrien Godino', 'Zara Llaguno'}
    Grade9 = {'Gabrielle Ramos', 'Lorenzo Bulesco', 'Elise Adlawan'}
    Grade8 = {'Mari Mediarito', 'Abrigo Gagaza', 'Alexa Piattos'}
    Grade7 = {'Zach Toribio', 'Hope Papcorn', 'Wen Hsu'}

    document.getElementById('output1').innerHTML = ""

    input_fname = document.getElementById('fname').value.strip()
    input_lname = document.getElementById('lname').value.strip()
    full_name = (input_fname + " " + input_lname)
   
    
    #get all members
    all_members = Grade10 | Grade9 | Grade8 | Grade7
     #add inputted name to the list
    all_members.add(full_name)

    total_members = len(all_members)
    #arrange in alphabetical order
    allmember_list = "<br>".join(sorted(all_members))

    document.getElementById('output1').innerHTML = f'All members: <br> {allmember_list}'
    display(f'Total members: {total_members}', target="output1")

    #clear names
    document.getElementById('fname').value = ""
    document.getElementById('lname').value = ""
