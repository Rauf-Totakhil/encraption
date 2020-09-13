import text_to_image


def display_menu():
    print('----------------------------------')
    print('-------------proseccin--------------')
    print('-----------------------------------')
    print('1. Text to Image')
    print('2. Image To Text')
    print('3. Modify ')
    print('4. Delete ')



def text_to_Image():
    global encoded_image_path
    global inputt
    inputt=input("Enter text: ")
    encoded_image_path = text_to_image.encode(inputt, "test")
    print('This is a test print', encoded_image_path, inputt)
    print('file is opend!!!!!!!!!!')
    encoded_image_path = text_to_image.encode_file("../test/test.txt", "result.png")
    return text_to_Image

def image_To_text():
    #global decoded_text
    global decoded_file_path
    global inputFor
    inputFor=input("")
    #decoded_text = text_to_image.decode("encoded_image.png")
    decoded_file_path = text_to_image.decode_to_file(inputFor, "output_text_file.txt")
    return image_To_text
    

while True:
    display_menu()

    option = input("Enter your option  ")

    if option == '1':
        text_to_Image()
    elif option == '2':
        image_To_text()
    elif option == '3':
        """modify()
    elif option == '4':
        delete()
    else:
        break"""
