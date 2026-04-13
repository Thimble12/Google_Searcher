import random
global length
length = 44 # Length of UUID generated for links. Google Docs, Sheets, and Slides links have a 44 character UUID.
global base_doc_link
global base_spr_link
global base_sli_link
base_doc_link = "https://docs.google.com/document/d/"
base_spr_link = "https://docs.google.com/spreadsheets/d/"
base_sli_link = "https://docs.google.com/presentation/d/"

link_amount = 50 # Number of links to generate and append to the text file.

valid_amount = 0 # Counter for the number of valid links added in to the list.
valid_restricted_amount = 0 # Counter for the number of valid links with restricted access added to the list.
valid_full_amount = 0 # Counter for the number of valid links with full access added to the list.


def generate_google_link(type="doc"): # Creates a random UUID and appends it to the base link for the specified Google service (Docs, Sheets, or Slides) to create a random link.
    random.seed()
    randdoclink = ""
    randsprlink = ""
    randslilink = ""
    rand_letters = []
    for i in range(length):
        random.seed()
        randtemp = random.choice(["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","-","_","0","1","2","3","4","5","6","7","8","9"])
        rand_letters.append(randtemp)
        
    rand_ending = "".join(rand_letters)
    
    randdoclink = base_doc_link + rand_ending
    randsprlink = base_spr_link + rand_ending
    randslilink = base_sli_link + rand_ending

    if type == "doc":
        return {"link": randdoclink, "type": type}
    elif type == "spr":
        return {"link": randsprlink, "type": type}
    elif type == "sli":
        return {"link": randslilink, "type": type}
    else:
        print("Invalid type specified. Please choose 'doc', 'spr', or 'sli'.")
        return None, None



for i in range(link_amount): # Generates 'link_amount' amount of random links and appends them to a text file called "Link_List.txt".
    random.number = random.randint(0, link_amount)
    if random.number % 12 == 0:
        valid_amount += 1
        randnum = random.randint(0, 1)
        if randnum == 0:
            valid_restricted_amount += 1
            with open("Link_List.txt", "a") as file:
                file.write("https://docs.google.com/document/d/1-_Zn92xWh1v0O7q6dHS1tgk3ZMAqjik7MM1ZZBeRD5M/edit?" + "\n") # Example of a valid link with restricted access.
        elif randnum == 1:
            valid_full_amount += 1
            with open("Link_List.txt", "a") as file:
                file.write("https://docs.google.com/document/d/1dpkcL5cE2XbnjMAkU-WPRatnEXEcdR6t_t08ANWW98Y/edit" + "\n") # Example of a valid link with full access.
    else:
        with open("Link_List.txt", "a") as file:
            file.write(generate_google_link("doc")["link"] + "\n")

print(f"\n\nGenerated {link_amount} links, with {valid_amount} valid links, {valid_restricted_amount} valid links with restricted access, and {valid_full_amount} valid links with full access.")
print("\n\nInvalid to valid link ratio: " + str((link_amount - valid_amount) / valid_amount))
print("\n\nValid restricted access to valid full access ratio: " + str(valid_restricted_amount/valid_full_amount) + "\n\n")