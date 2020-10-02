username=("intanyasmina")
passwordku=("12344321")

def masuk(user,passw):
    if user != username and password != passwordku:
        stop = False
    else:
        stop = True
    return stop

x=3
for i in range(0,x):
    user_baru = input("username = ")
    password_baru = input("password = ")
    stop = (masuk(user_baru, password_baru))
    if stop == True:
        print("Anda telah berhenti masuk")
        break
    else:
        print("Username dan Password anda salah")
