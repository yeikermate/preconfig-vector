import pexpect
import scapy.all as scapy
import time

def detect_vector_ip(target_mac):
    arp_request = scapy.ARP(pdst="192.168.0.0/24")  # Adjust the IP range according to your network
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_request_broadcast = broadcast / arp_request
    answered_list = scapy.srp(arp_request_broadcast, timeout=1, verbose=False)[0]

    for element in answered_list:
        if element[1].hwsrc == target_mac:
            return element[1].psrc

    return None

# Required data for the form
accept_terms = "y"
robot_name = "Vector-X1B2"
serial_number = "00XXXXXX"
target_mac = "00:00:00:00:00:00"  # Replace with your Vector's MAC
ip_wirepod = "192.168.0.XXX"

# Loop to keep trying until the IP is obtained and the configuration is successful
while True:
    ip_robot = detect_vector_ip(target_mac)
    if not ip_robot:
        print("Vector's IP not found on the network. Retrying in 5 seconds...")
        time.sleep(5)  # Wait 5 seconds before trying again
        continue  # Retry getting the IP

    print(f"Vector's IP found: {ip_robot}. Starting configuration...")

    # Run the configuration script
    child = pexpect.spawn('python3 -m anki_vector.configure')

    child.timeout = 120
    child.logfile = open("/app/configure_vector.log", "wb")

    try:
        # Automate the responses for the configuration script
        child.expect(r"Do you wish to proceed\? \(y/n\)")
        child.sendline(accept_terms)

        child.expect(r"Enter robot name:")
        child.sendline(robot_name)

        child.expect(r"Enter robot ip:")
        child.sendline(ip_robot)

        child.expect(r"Enter wire-pod ip:")
        child.sendline(ip_wirepod)

        child.expect(r"Enter robot serial number:")
        child.sendline(serial_number)

        child.expect(pexpect.EOF)
        print("Configuration completed successfully.")
        break  # Exit the loop since the configuration was successful

    except pexpect.exceptions.TIMEOUT as e:
        print("Timeout exceeded:", e)
        print("Buffer content:", child.before.decode())
    except Exception as e:
        print("An error occurred:", e)
    finally:
        child.logfile.close()

    print("Configuration error. Retrying in 5 seconds...")
    time.sleep(5)  # Wait 5 seconds before retrying
