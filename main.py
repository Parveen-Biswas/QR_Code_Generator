import qrcode

data_entry = input("Enter Your Data : ")
version_entry = int(input("Enter Your Version (Complexity) : "))
box_size1 = int(input("Enter Your Box Size : "))
box_color = input("Enter Your Box Color : ")
background_color = input("Enter Your Background Color : ")
file_name = input("File Name : ")

generate_qrcode = qrcode.QRCode(
    version=version_entry,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=box_size1,
    border=4,
)


generate_qrcode.add_data(data_entry)
generate_qrcode.make(fit=True)

img = generate_qrcode.make_image(fill_color=box_color, back_color=background_color)
img.save(f"{file_name}.jpg")
print("QRCode has generated Succusfully") 
