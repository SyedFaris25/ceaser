from scapy.all import sniff, IP, TCP, UDP, ICMP, Raw, get_if_list
from datetime import datetime

def process_packet(packet):
    print("[Debug] Packet received")  # Debug line to confirm packet capture

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    if IP in packet:
        ip_layer = packet[IP]
        src = ip_layer.src
        dst = ip_layer.dst
        proto = ip_layer.proto

        if proto == 6 and TCP in packet:
            protocol = "TCP"
        elif proto == 17 and UDP in packet:
            protocol = "UDP"
        elif proto == 1 and ICMP in packet:
            protocol = "ICMP"
        else:
            protocol = f"Other({proto})"

        length = len(packet)
        print(f"[{timestamp}] {protocol} | {src} -> {dst} | Length: {length} bytes")

        if Raw in packet:
            data = packet[Raw].load[:20]
            try:
                data_str = data.decode('utf-8', errors='replace')
            except Exception:
                data_str = str(data)
            print(f"Payload (truncated): {data_str}\n")

def start_sniffing(interface, packet_count=0):
    print(f"[*] Starting packet sniffing on interface: {interface}...\n")
    try:
        sniff(prn=process_packet, iface=interface, store=0, count=packet_count, filter="ip")
    except KeyboardInterrupt:
        print("\n[!] Sniffing stopped by user.")
    except Exception as e:
        print(f"[!] Error during sniffing: {e}")
        print("Make sure you are running the script as Administrator/root.")

if __name__ == "__main__":
    interfaces = get_if_list()
    print("Available network interfaces:")
    for i, iface in enumerate(interfaces):
        print(f"{i}: {iface}")

    try:
        choice = int(input("\nEnter the number of the interface you want to sniff: "))
        selected_iface = interfaces[choice]
    except (ValueError, IndexError):
        print("Invalid interface choice.")
        exit(1)


    start_sniffing(interface=selected_iface, packet_count=0)