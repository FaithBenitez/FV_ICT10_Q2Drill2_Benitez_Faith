from pyscript import display, document

def add_member(e):
    document.getElementById('output1').innerHTML= ""
    
    members={'Uniqlo', 'Bench', 'Zara'}

    input_fname=document.getElementById('fname').value
    input_lname=document.getElementById('lname').value
    #assign the valute to set variable 
    new_brand_set = {input_member}

    all_brands = brands | new_brand_set

    total_brands = len(brands | new_brand_set)

    brand_list = "<br>".join(sorted(all_brands))
    #display
    document.getElementById('output1').innerHTML = f'All brands: <br> {brand_list}'
    display(f'Total brands: {total_brands}', target="output1")

    new_student= input_lname+ "" +input_fname 