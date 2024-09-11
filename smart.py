import subprocess
import time

class SmartTVControl:
    def __init__(self, ip_address, port=5555):
        self.ip_address = ip_address
        self.port = port
        self.device = f"{ip_address}:{port}"

    def connect(self):
        try:
            subprocess.run(["adb", "connect", self.device], check=True)
            print(f"Connected to {self.device}")
            return True
        except subprocess.CalledProcessError:
            print(f"Failed to connect to {self.device}")
            return False

    def disconnect(self):
        subprocess.run(["adb", "disconnect", self.device])
        print(f"Disconnected from {self.device}")

    def send_keyevent(self, keycode):
        try:
            subprocess.run(["adb", "-s", self.device, "shell", "input", "keyevent", str(keycode)], check=True)
            return True
        except subprocess.CalledProcessError:
            print(f"Failed to send keyevent {keycode}")
            return False

    def power(self):
        return self.send_keyevent(26)  #  power

    def volume_up(self):
        return self.send_keyevent(24)  #  + volume

    def volume_down(self):
        return self.send_keyevent(25)  #  - volume 

    def mute(self):
        return self.send_keyevent(164)  # mute

    def change_channel(self, number):
        for digit in str(number):
            self.send_keyevent(int(digit) + 7)  # rubah channel
            time.sleep(0.5)  # delay dikit

    def home(self):
        return self.send_keyevent(3)  # ke home

    def back(self):
        return self.send_keyevent(4)  # back

    def menu(self):
        return self.send_keyevent(82)  # list menu

    def enter(self):
        return self.send_keyevent(66)  # enter

    def dpad_up(self):
        return self.send_keyevent(19)  # up

    def dpad_down(self):
        return self.send_keyevent(20)  # down

    def dpad_left(self):
        return self.send_keyevent(21)  # left

    def dpad_right(self):
        return self.send_keyevent(22)  # right

def main():
    tv_ip = "192.168.1.5"  # IP address smart tv
    tv = SmartTVControl(tv_ip)

    if tv.connect():
        while True:
            print("\nSmart TV Control")
            print("1. Power On/Off")
            print("2. Volume Up")
            print("3. Volume Down")
            print("4. Mute")
            print("5. Rubah Channel")
            print("6. Home")
            print("7. Back")
            print("8. Menu")
            print("9. Navigasi (Up/Down/Left/Right/Enter)")
            print("0. Exit")

            choice = input("Enter your choice: ")

            if choice == '1':
                tv.power()
            elif choice == '2':
                tv.volume_up()
            elif choice == '3':
                tv.volume_down()
            elif choice == '4':
                tv.mute()
            elif choice == '5':
                channel = input("Masukkan nomor channel : ")
                tv.change_channel(channel)
            elif choice == '6':
                tv.home()
            elif choice == '7':
                tv.back()
            elif choice == '8':
                tv.menu()
            elif choice == '9':
                while True:
                    nav = input("Mau ngapain? (u/d/l/r/e) or 'q' untuk keluar: ").lower()
                    if nav == 'u':
                        tv.dpad_up()
                    elif nav == 'd':
                        tv.dpad_down()
                    elif nav == 'l':
                        tv.dpad_left()
                    elif nav == 'r':
                        tv.dpad_right()
                    elif nav == 'e':
                        tv.enter()
                    elif nav == 'q':
                        break
            elif choice == '0':
                break
            else:
                print("Gagal, coba lagi.")

        tv.disconnect()
    else:
        print("Gagal tekneksi dengan smart tv / android tv, pastikan 1 jaringan.")

if __name__ == "__main__":
    main() 