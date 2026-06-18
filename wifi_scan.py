import subprocess

def scan_wifi():

    # Run WiFi scan command
    output = subprocess.check_output(
        "netsh wlan show networks mode=bssid",
        shell=True
    ).decode("utf-8", errors="ignore")

    lines = output.split("\n")

    current_ssid = ""

    wifi_data = {}

    for line in lines:

        line = line.strip()

        # Detect SSID
        if line.startswith("SSID") and "BSSID" not in line:

            parts = line.split(":")

            if len(parts) > 1:
                current_ssid = parts[1].strip()

        # Detect Signal
        elif line.startswith("Signal"):

            parts = line.split(":")

            if len(parts) > 1:

                signal = parts[1].replace("%", "").strip()

                if current_ssid != "":

                    # Store strongest signal
                    signal = int(signal)

                    if current_ssid not in wifi_data:
                        wifi_data[current_ssid] = signal

                    else:
                        wifi_data[current_ssid] = max(
                            wifi_data[current_ssid],
                            signal
                        )

    return wifi_data


# TEST
wifi = scan_wifi()

print(wifi)